# Color grade -analyysi + S-Log3-kaava

Analysoitu 5 näyttötallennetta (Instagram/Reels), 339 framea (5 fps). Mittasin jokaisesta framesta
luminanssijakauman, mustan ja valkoisen tason, värisävyn eri sävyalueilla (Lab a*/b*),
saturaation suhteessa kirkkauteen, mitkä värisävyt ovat kuvassa jäljellä sekä keskustan ja
reunojen kirkkauseron. UI-elementit (sydämet, tekstit) ja letterbox-palkit on rajattu pois.

> Huom: lähde on Instagram-pakattu ruudunkaappaus, joten luvut ovat suuntaa antavia
> (noin ±2–3 %). Suhteet ja suunnat pitävät paikkansa, desimaalit eivät ole absoluuttisia.

| Klippi | Sisältö |
|---|---|
| **A** | Yömontaasi: Rolls-Roycet, F1, lyhtypuu, The Dorchester, viini |
| **B** | Maybachin sisätila, ambient-LEDit (pystykuva) |
| **C** | Abu Dhabi / F1 -yö, autotalli, konsertti, auringonlasku |
| **D** | GT3 RS sateessa, 2.39:1-crop |
| **E** | "Dream Big": Hollywood Hills -villa yöllä → sisätila → päivä, uima-allas, Maybach |

---

> Koko estetiikan analyysi (miksi tämä näyttää niin hyvältä): [`AESTHETIC.md`](AESTHETIC.md)

## 1. Mikä se fiilis on

**A, B, C: "Quiet luxury after dark".** Kuva on hiljainen, kallis ja salaperäinen. Siitä tulee tunne,
että olet päässyt paikkaan, jonne muut eivät pääse. Kuva **ei näytä kaikkea**, vaan
pimeys tekee siitä yksityisen. Valo tulee vain siitä, mikä on arvokasta: ajovaloista,
lyhdyistä, takavaloista ja LED-nauhoista. Lämmin valo tuo intiimiyttä, ja yksi kirkas väri
pimeyden keskellä tuo halun ja statuksen (punainen Ferrari, takavalo, magenta-ambient).

**D: "Rain noir / moody matte".** Sama hillintä, mutta melankolinen, viileä ja eristetty.
Kuvassa on sumua, märkää asfalttia ja teal-vihreää. Mustat ovat mattaiset eikä missään ole
puhdasta valkoista. Kokonaisuus muistuttaa elokuvaa (2.39:1), ja punainen on ainoa lämmin asia.

**Yhteinen nimittäjä: hillintä.** Grade piilottaa enemmän kuin näyttää.

---

## 2. Isoin juttu: se on VALOTUS ja TIHEYS, ei väri

Ihmiset luulevat, että lookki on värisävy (teal & orange tms.). Se ei ole. Isoin juttu on,
**miten vähän kuvassa on valoa** ja **missä se valo on**.

| Mittari | A | B | C | D | "Normaali" Rec.709 |
|---|---|---|---|---|---|
| Mediaani-luma | **4 %** | **4 %** | **3 %** | 15 % | ~35–45 % |
| Pikselit alle 5 % | **56 %** | **66 %** | **65 %** | 16 % | ~5 % |
| Pikselit alle 10 % | 74 % | 85 % | 79 % | 37 % | ~10–15 % |
| Mustan taso (p0.5) | 0 % | 0 % | 0 % | **3 % (sininen)** | 0–2 % |
| Kirkkain kohta (p99.9) | 95 % | 67 % | 92 % | **88 %** | 100 % |
| Klippaa >98 % | 0 % | 0 % | 0,01 % | 0 % | usein |

Mitä tämä tarkoittaa:
- **Yli puolet kuvasta on käytännössä mustaa.** Yö-klipeissä tyypillinen pikseli on 3–4 % kirkkaudella.
  Tämä on ylivoimaisesti tärkein yksittäinen asia. Jos teet vain tämän, olet 60 % perillä.
- **Mustat ovat oikeasti mustia** (0 %) ja **neutraaleja** (syvän mustan kroma C\* ≈ 1–2, eli ei sävyä).
  Ei haalistettu "film-look" -nostettua mustaa (paitsi D).
- **Mikään ei klippaa valkoiseksi.** Highlightit pyöristyvät pehmeästi kermaiseksi.
- **Valo on paikallista** (practicalit). C-klipissä keskusta on 1,8× ja A:ssa 1,3× kirkkaampi kuin
  reunat, joten katse ohjautuu valoon kuin vinjetillä, mutta se tulee valaistuksesta.

## 3. Toiseksi isoin: subtraktiivinen väri + YKSI aksentti

| | A | B | C | D |
|---|---|---|---|---|
| Keskim. kroma C\* | 6,3 | 7,1 | 6,1 | 8,2 |
| Kroma p99 (aksentit) | 48 | 58 | 66 | 36 |
| Hallitseva sävy (väripikseleistä) | oranssi 47 % + kelt. 29 % | magenta 54 % + pun. 27 % | **oranssi 86 %** | vihreä→teal 68 % + sin. 21 % |
| Vihreä + syaani | 4 % | 0 % | 2 % | (teal-hallittu) |

- **Kokonaissaturaatio on matala** (keskiarvo C\* noin 6–8), mutta **aksentit ovat todella saturoituja**
  (p99 jopa 66). Suurin osa kuvasta on lähes harmaata/mustaa, ja yksi väri hehkuu.
- Jokaisessa klipissä on **1–2 sävyn paletti**. Vihreät ja syaanit on käytännössä poistettu yö-klipeistä
  (lähes 0 %). Tämä on tärkeää, koska kaupunkiyön vihreät loisteputket ja LEDit tappaisivat lookin.
- **Saturaatio vs. kirkkaus** -käyrä on kellon muotoinen: väri on vahvimmillaan keskisävyissä
  (noin 50–70 %) ja putoaa sekä varjoissa että highlighteissa. Highlightit desaturoituvat noin
  50 %, joten lyhdyt ja ajovalot palavat **kermanvalkoisina**, eivät keltaisina tai sinisinä.

## 4. Sävykartta (split) sävyalueittain

**Yö (A/C):** syvä musta neutraali → varjot hennosti lämpimät → low-mid/mid **amber/oranssi**
(hue 53–77°) → highlightit kermankeltaiset (b\* +7…+14) → huippu lähes neutraali.
Taustan "tyhjät" pinnat (seinät, katu) liukuvat hennosti viileään. Tästä tulee lämmin/kylmä-erotus
**ilman** räikeää teal & orangea.

**B (Maybach):** varjot magentat (hue 336°), mid hennosti punertava. Väri tulee ambient-LEDeistä,
eikä gradessa ole vihreää lainkaan (G−(R+B)/2 = −0,047, eli selvä magenta-kallistus).

**D (sade):** musta sinertävä ja nostettu (3 %), varjot ja mid **teal/syaani** (hue 180–216°),
highlightit lähes neutraalit. Vihreät on käännetty tealiin ja desaturoitu. Punainen (vanteet,
takavalo) on ainoa lämmin ja jätetty täyteen saturaatioon.

## 5. Pienemmät mausteet

- **Halation/glow** practicalien ympärillä (lyhdyt, takavalot): pieni, lämmin ja punertava hehku.
- **Pehmeä highlight roll-off**: ei kovaa klippausta, filmimäinen olkapää.
- **Kevyt grain** (näkyy erityisesti D:ssä ja tummissa kohdissa).
- **2.39:1-crop** (D) ja ~2:1 (C): elokuvallisuus.
- **Motion blur** (180° shutter), matala syväterävyys ja practical-bokeh.
- **Kuvaus**: aiheet on valaistu *vain* practicaleilla. Grade ei pysty luomaan tätä tyhjästä,
  koska se vahvistaa sitä, mitä kuvaushetkellä oli.

---

## 6. KAAVA S-Log3:lle (tärkeysjärjestyksessä)

### Prioriteetit, jos teet vain osan
1. **Tiheys alas** (−0,7…−1,2 stoppia) + **mustat nollaan**: suurin vaikutus.
2. **Vihreä ja syaani pois, yksi aksentti jää** (subtraktiivinen saturaatio).
3. **Highlightit pehmeästi kermaiseksi**, ei klippausta, highlightien desaturaatio.
4. Lämmin mid / neutraali musta (yö) **tai** teal + matte black (sade).
5. Halation, grain, vinjetti, crop.

### Kuvatessa (S-Log3 / S-Gamut3.Cine)
- **Base ISO** (FX3/A7S III: 640 tai 12800, FX30: 800 tai 2500). S-Log3 kohisee alivalotettuna,
  joten **älä alivalota kamerassa**. Valota normaalisti/hiukan yli ja tummenna postissa. Silloin
  varjot ovat puhtaat, ja kun ne painetaan mustaksi, kohina katoaa samalla.
- **Suojaa practicalit**: zebra noin 90–94 %. Ajovalot ja lyhdyt saavat olla lähellä, mutta eivät klipata.
- **Kiinteä Kelvin, ei AWB.** Yöllä noin 4300–5000 K: natrium/volframi pysyvät amberina ja taivas sekä
  ympäristö menevät hennosti viileiksi. Sateessa noin 5600 K.
- **Valaise vain practicaleilla**, ja anna muun pudota pimeään. Etsi kuvakulma, jossa tausta on tumma.
- 180° shutter, iso aukko, ND päivällä.

### DaVinci Resolve -nodepuu (DaVinci YRGB, ei color managediä)

| # | Node | Yö (A/B/C) | Sade (D) |
|---|---|---|---|
| 01 | **CST IN** | S-Gamut3.Cine / S-Log3 → DaVinci Wide Gamut / DaVinci Intermediate, tone mapping: None | sama |
| 02 | **Balance** | Offset/Temp/Tint: harmaa ja musta neutraaliksi, valotus normaaliksi (harmaa noin 0,336 DI:ssä) | sama |
| 03 | **Density ★** | HDR Global Exposure **−0,8…−1,2** · Contrast **1,20–1,30**, pivot **0,30** | Exposure **−0,3** · Contrast **1,05–1,10**, pivot 0,336 |
| 04 | **Mustat ★** | Lift/HDR Black Offset niin, että waveformin pohja **koskettaa 0:aa**. Syvä musta neutraali | Black Offset **ylös**: pohja noin **3 %**, hiukan sininen |
| 05 | **Subtraktiivinen väri ★** | Sat **41/50** (≈ 0,82) · Color Slice / Hue vs Sat: **vihreä −45 %**, syaani/sin. −30 %, **punainen +20 %**, oranssi +10 %, magenta 0 | Sat **39/50** · Hue vs Hue: **vihreä → teal +20°** · vihreä −30 % · **punainen +35 %** · keltainen −20 % |
| 06 | **Lum vs Sat** | varjot **−45 %**, highlightit (yli 80 %) **−55 %** | varjot −35 %, highlightit (yli 70 %) −60 % |
| 07 | **Split tone** | Varjot: hyvin hento viileä (sininen). Highlights/Gain: **kerma-amber** (lämmin, ei punainen) | Varjot: **teal/syaani**. Highlightit neutraalit, hiukan viileät |
| 08 | **Vinjetti/relight** | Power window, reunat **−0,3…−0,5 st**, pehmeä | −0,2 st |
| 09 | **Halation/Glow** | Glow/Halation OFX: threshold noin 0,8, lämmin punaoranssi, pieni säde | sama, punainen takavalo |
| 10 | **Grain** | Film Grain 35 mm, hienojakoinen, heikko | hiukan vahvempi |
| 11 | **CST OUT** | DWG / DI → Rec.709 / Gamma 2.4, tone mapping **DaVinci**, max 100 nits | sama + **White** max noin **88 %** (Gain alas tai soft clip) |
| – | Timeline | – | Output blanking **2.39:1** |

★ = ne kolme nodea, joissa itse lookki on.

### Scope-tavoitteet (Rec.709-waveform, valmis kuva)

| | Yö | Sade |
|---|---|---|
| Mustan pohja | 0 % | 3 % |
| Suurin osa kuvasta | 0–10 % | 5–30 % |
| Mediaani | 3–5 % | ~15 % |
| Aiheen/practicalin valo | 30–70 % | 30–55 % |
| Kirkkain | ≤ 95 %, ei klippiä | ≤ 88 % |
| Vectorscope | lyhyt, yksi piikki kohti punaista/oranssia (tai magentaa) | lyhyt, teal-akseli + punainen piikki |

---

## 7. Valmiit LUTit

Lataa: [`luts/`](luts/). Kolme 33³ .cube-LUTia, joiden **input on S-Log3 / S-Gamut3.Cine**
ja **output Rec.709 Gamma 2.4**. Ne tekevät koko ketjun (CST + tonemappaus + look) yhdellä kertaa:

- `SLog3_SG3C_to_709_Night_QuietLuxury.cube`: A/B/C/E-yölook
- `SLog3_SG3C_to_709_Rain_Moody.cube`: D-sadelook, **mustat 0 %** (referenssin 3 %:n matte
  saadaan takaisin asettamalla `lift=0.03`)
- `SLog3_SG3C_to_709_Day_DreamBig.cube`: E-päivälook (musta 0, ei klippausta, muted vihreä,
  lämmin iho vs. syaani vesi)

**Kaikissa kolmessa S-Log3-musta (CV 95) → 0 % ulos.** Jos kuva näyttää harmaalta, LUT ei ole
päällä tai syöte ei ole S-Log3:a (esim. Resolve Color Managed muuntaa ennen LUTia, tai kamera
oli S-Cinetonella).

**Input-tasot:** LUTit olettavat Resolven/Premieren normaalin käsittelyn, eli Sonyn video-level
-tiedosto (64–940) skaalattuna 0–1:ksi. 18 % harmaa = CV 420 = 41 IRE.

**Käyttö Resolvessa:** projekti DaVinci YRGB (ei Color Managed). Node 1 = valotus + WB
(log-kuvalle, Offset), node 2 = LUT. Älä laita CST:tä ennen LUTia. Jos kuva on liian tumma,
nosta valotusta **ennen** LUTia (Offset), älä sen jälkeen. Hienosäätö (vinjetti, glow, grain)
tehdään LUTin jälkeen. **Premiere:** Lumetri → Basic Correction → Input LUT = tämä .cube.

Mitattu harmaaskaala (oikein valotettu 18 % harmaa = stoppi 0):

| stoppia | −6 | −4 | −2 | −1 | **0** | +1 | +2 | +4 | +6 |
|---|---|---|---|---|---|---|---|---|---|
| Night | 0,4 % | 1,8 % | 7,3 % | 14 % | **24 %** | 37 % | 53 % | 84 % | 97 % |
| Rain | 1,0 % | 3,4 % | 14 % | 23 % | **33 %** | 45 % | 58 % | 77 % | 86 % |
| Day | 1,2 % | 4,7 % | 14 % | 22 % | **33 %** | 47 % | 62 % | 86 % | 96 % |

(Normaali Rec.709-LUT laittaa harmaan noin 41 %:iin. Nämä ovat tarkoituksella tummempia.)

`testikartta.png`: vasemmalta S-Log3-syöte (ColorChecker −2/0/+2 st, harmaa-ramppi, sävy-ramppi),
Night, Rain, Day.

LUTit generoidaan skriptillä `tools/make_luts.py` (numpy). Kaikki parametrit (valotus,
kontrasti, toe, sävykohtainen saturaatio, split tone, lift/white) ovat `LOOKS`-sanakirjassa,
joten voit säätää ja ajaa uudelleen.
