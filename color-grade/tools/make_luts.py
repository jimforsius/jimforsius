"""Generoi S-Log3 / S-Gamut3.Cine -> Rec.709 (gamma 2.4) look-LUTit.

Ajo:  python3 make_luts.py   (tarvitsee numpy)
Tulos: ../luts/*.cube (33^3, data levels 0-1)
"""
import numpy as np
from pathlib import Path

N = 33
OUT = Path(__file__).resolve().parent.parent / "luts"


# --- S-Log3 -> scene linear (Sony tech summary) -----------------------------
def slog3_to_lin(x):
    cv = x * 1023.0
    hi = 10.0 ** ((cv - 420.0) / 261.5) * (0.18 + 0.01) - 0.01
    lo = (cv - 95.0) * 0.01125 / (171.2102946929 - 95.0)
    return np.where(cv >= 171.2102946929, hi, lo)


def lin_to_slog3(y):
    hi = (420.0 + np.log10((y + 0.01) / (0.18 + 0.01)) * 261.5) / 1023.0
    lo = (y * (171.2102946929 - 95.0) / 0.01125 + 95.0) / 1023.0
    return np.where(y >= 0.01125, hi, lo)


# --- gamut: S-Gamut3.Cine -> Rec.709, both D65 ------------------------------
def npm(prim, white=(0.3127, 0.3290)):
    xyz = lambda x, y: np.array([x / y, 1.0, (1 - x - y) / y])
    P = np.stack([xyz(*p) for p in prim], axis=1)
    S = np.linalg.solve(P, xyz(*white))
    return P * S


SG3C = npm([(0.766, 0.275), (0.225, 0.800), (0.089, -0.087)])
R709 = npm([(0.64, 0.33), (0.30, 0.60), (0.15, 0.06)])
SG3C_TO_709 = np.linalg.inv(R709) @ SG3C
LUMA = np.array([0.2126, 0.7152, 0.0722])


def gamut_compress(rgb):
    """Vedä gamutin ulkopuoliset (negatiiviset) arvot luminanssia kohti."""
    Y = np.maximum(rgb @ LUMA, 0.0)[..., None]
    m = rgb.min(-1, keepdims=True)
    t = np.where(m < 0, Y / np.maximum(Y - m, 1e-9), 1.0)
    return Y + (rgb - Y) * np.clip(t, 0, 1)


# --- tonescale: Hill-käyrä + toe (mustien crush) ----------------------------
def tonescale(x, mid_in, mid_out, contrast, peak, toe):
    x = np.maximum(x, 0.0)
    # f(x) = peak * x^p / (x^p + k), f(mid_in) = mid_out (ennen toea)
    k = mid_in ** contrast * (peak / mid_out - 1.0)
    f = peak * x ** contrast / (x ** contrast + k)
    g = f * f / (f + toe)           # toe: painaa varjot alas, keskisävyt säilyvät
    return g * (peak + toe) / peak  # skaalaa niin että peak pysyy peakina


# --- OkLab --------------------------------------------------------------------
M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929],
               [0.2119034982, 0.6806995451, 0.1073969566],
               [0.0883024619, 0.2817188376, 0.6299787005]])
M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468],
               [1.9779984951, -2.4285922050, 0.4505937099],
               [0.0259040371, 0.7827717662, -0.8086757660]])


def to_oklab(rgb):
    return np.cbrt(np.maximum(rgb, 0) @ M1.T) @ M2.T


def from_oklab(lab):
    return (lab @ np.linalg.inv(M2).T) ** 3 @ np.linalg.inv(M1).T


def bump(h, center, width):
    """Pehmeä paino 0..1 sävykulman ympärille (asteina)."""
    d = np.abs((h - center + 180.0) % 360.0 - 180.0)
    return np.where(d < width, 0.5 + 0.5 * np.cos(np.pi * d / width), 0.0)


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


def look(rgb_disp, p):
    lab = to_oklab(rgb_disp)
    L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.hypot(a, b)
    h = np.degrees(np.arctan2(b, a)) % 360.0

    # 1) hue-rotaatiot (esim. vihreä -> teal)
    for center, width, shift in p["hue_shift"]:
        h = h + shift * bump(h, center, width)

    # 2) subtraktiivinen saturaatio: globaali * sävykohtainen
    sat = np.full_like(C, p["sat"])
    for center, width, gain in p["hue_sat"]:
        w = bump(h, center, width)
        sat = sat * (1 - w) + sat * gain * w
    # 3) Lum vs Sat: varjot ja highlightit vähemmän saturoituja
    sat *= 1 - p["shadow_desat"] * (1 - smoothstep(0.08, p["shadow_desat_end"], L))
    sat *= 1 - p["high_desat"] * smoothstep(p["high_desat_start"], 0.98, L)
    C = C * sat

    a = C * np.cos(np.radians(h))
    b = C * np.sin(np.radians(h))

    # 4) split tone (OkLab a/b -offsetit, painotettu luminanssilla)
    ws = 1 - smoothstep(0.05, 0.45, L)           # varjot
    ws *= smoothstep(0.0, 0.10, L)               # syvä musta pysyy neutraalina
    wh = smoothstep(0.45, 0.90, L)               # keskisävyt-highlightit
    a = a + ws * p["shadow_ab"][0] + wh * p["high_ab"][0]
    b = b + ws * p["shadow_ab"][1] + wh * p["high_ab"][1]
    return from_oklab(np.stack([L, a, b], -1))


LOOKS = {
    # A/B/C: low-key yö, crushed neutral black, lämpimät practicalit, yksi aksentti
    "Night_QuietLuxury": dict(
        exposure=-0.9, mid_out=0.10, contrast=1.30, peak=0.97, toe=0.020,
        sat=0.82,
        hue_shift=[],
        hue_sat=[(30, 35, 1.20),    # punaiset (takavalot)
                 (65, 30, 1.10),    # oranssi/amber (lyhdyt, natrium)
                 (140, 45, 0.55),   # vihreät pois
                 (230, 50, 0.70),   # syaani/sininen hillitty
                 (330, 35, 1.05)],  # magenta (LED-ambient) säilyy
        shadow_desat=0.45, shadow_desat_end=0.40,
        high_desat=0.55, high_desat_start=0.80,
        shadow_ab=(-0.003, -0.006),  # hento viileys varjoihin
        high_ab=(0.001, 0.012),      # lämmin/kermainen yläpää
        lift=0.0, white=1.0,
    ),
    # D: sateinen moody, matte black, teal-vihreä, punainen aksentti
    "Rain_MoodyMatte": dict(
        exposure=-0.35, mid_out=0.13, contrast=1.10, peak=0.90, toe=0.006,
        sat=0.78,
        hue_shift=[(135, 45, 22.0)],  # vihreä -> teal
        hue_sat=[(30, 35, 1.35),      # punaiset vanteet/takavalot esiin
                 (70, 30, 0.80),      # keltaiset ja oranssit hillitty
                 (150, 45, 0.70),     # teal-vihreä mutta muted
                 (250, 50, 0.80)],
        shadow_desat=0.35, shadow_desat_end=0.35,
        high_desat=0.60, high_desat_start=0.70,
        shadow_ab=(-0.010, -0.010),   # sinivihreä varjo
        high_ab=(-0.004, 0.000),
        lift=0.030, white=0.93,       # matte black + ei puhdasta valkoista
    ),
}


def render(slog3_rgb, p):
    lin = slog3_to_lin(slog3_rgb) @ SG3C_TO_709.T
    lin = gamut_compress(lin) * 2.0 ** p["exposure"]
    disp = tonescale(lin, 0.18, p["mid_out"], p["contrast"], p["peak"], p["toe"])
    disp = np.clip(look(np.clip(disp, 0, 1), p), 0, 1)
    code = disp ** (1 / 2.4)
    return np.clip(p["lift"] + code * (p["white"] - p["lift"]), 0, 1)


def write_cube(name, p):
    g = np.linspace(0, 1, N)
    b, gg, r = np.meshgrid(g, g, g, indexing="ij")  # .cube: R muuttuu nopeimmin
    grid = np.stack([r, gg, b], -1).reshape(-1, 3)
    out = render(grid, p)
    path = OUT / f"SLog3_SG3C_to_709_{name}.cube"
    with open(path, "w") as f:
        f.write(f'TITLE "SLog3 SGamut3.Cine -> Rec709 g2.4 | {name}"\n')
        f.write("# Input: S-Log3 / S-Gamut3.Cine, data levels. Output: Rec.709 gamma 2.4\n")
        f.write(f"LUT_3D_SIZE {N}\nDOMAIN_MIN 0.0 0.0 0.0\nDOMAIN_MAX 1.0 1.0 1.0\n")
        for v in out:
            f.write(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
    return path


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, p in LOOKS.items():
        print("wrote", write_cube(name, p))
