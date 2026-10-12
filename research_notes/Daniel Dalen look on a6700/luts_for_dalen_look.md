# LUTs for a Daniel-Dalen-like cinematic look from Sony a6700 S-Log3/S-Gamut3.Cine (Final Cut Pro 12.3)

Reference target, measured earlier from Dalen's "Two Really Chaotic Weeks", min 7-12: luma p1 about 0.018 (deep blacks, not crushed), mids about 0.22, highlights about 0.81, teal shadows and mids, warm highlights, about 53% cyan / 23% orange hues, light vignette (edge/centre about 0.80), no grain, soft and creamy. The user's footage is mostly dark (night and interiors in Cairo).

Research note: about 27 search/fetch calls. Many results were SEO aggregator pages or LUT-shop listings, which I excluded or flagged. Statements marked "unverified" come from general knowledge and could not be sourced in this pass.

---

## Q1. Sony's official LUTs (s709, LC-709, LC-709TypeA, Cine+709, 709(800), Sony "S-Log3 to 709" .cube files, Picture Shop LUTs): what each looks like, which is closest to a soft Dalen-style contrast, data vs video levels

### Takeaway
Among Sony's own transforms, **s709** (soft, film-like, subtle colour, highlight-preserving) and **LC-709TypeA** (Alexa-like, low contrast, slightly lifted blacks, desaturated) are the closest bases for a soft, creamy Dalen-style image. **Cine+709** and **709(800)/R709** are too contrasty and crush shadows, which is bad for dark Cairo night footage. Sony's free **Picture Shop "Josh Pines" Lo Con Base / Look 1 / Look 2** LUTs (S-Log3/S-Gamut3.Cine in, Rec.709 out) are an underused, high-quality free option made by a Hollywood post house. Final Cut Pro's built-in Sony S-Log3 camera LUT uses the contrasty 709(800) mapping.

### Cited Findings
**s709**
- Sony describes s709 as "a softer low-contrast tone curve" that "renders imagery in subtle colors, with smooth color gradation" with "subtle and well-rendered skin tones", and says "The s709 look is close to the characteristics of film." It is recommended for cinema and TV drama. — [Sony Cinematography: s709 LUT overview](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/)
- Sony's s709 white paper says s709 has a lower-contrast curve than 709(800) and preserves highlights. — [Sony S709 white paper (sony.jp, 2018)](https://www.sony.jp/ls-camera/knowledge/pdf/S709-white-paper-180524.pdf) (summarised via search result)
- Sony provides an s709 cube file (s709.cube) matching the VENICE built-in s709 output. — [Sony Cinematography](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/)
- In-camera, recent Sony bodies with "Base Look" offer the presets [s709], [709(800%)] and [S-Log3] in log mode, plus user LUT slots, with input S-Gamut3.Cine/SLog3 and output BT.709 or HLG. — [Sony Help Guide: Base Look (BRC-AM7)](https://helpguide.sony.net/rc/brc-am7/v1/en/contents/cm_base_look.html); [Sony Help Guide: Changing a LUT](https://helpguide.sony.net/ilc/2240/v1/en/contents/TP1000669630.html). Note: these pages are for other Sony models, not confirmed to be the a6700.

**LC-709 and LC-709TypeA**
- "LC709 stands for low contrast gamma with 709 color primaries, it is not 709 gamma!" LC-709 is darker and flatter than conventional TV levels. — [Alister Chapman, XDCAM-User (2017)](https://www.xdcam-user.com/2017/12/using-luts-for-exposure-choosing-the-right-lut)
- LC-709TypeA is a "Look", not an exposure LUT. It "mimics the way an Arri Alexa might look". With correct exposure, middle grey is about 41% and white about 70-72%, with skin about 55%. A 1-stop exposure change moves brightness only about 10%, so "you could easily be a full stop out". — [XDCAM-User](https://www.xdcam-user.com/2017/12/using-luts-for-exposure-choosing-the-right-lut)
- Sony describes LC-709 and LC-709TypeA as "low contrast with broadcast color". — [Sony Cinematography](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/)
- Community summaries say TypeA lifts blacks slightly and is less saturated than LC-709, and the difference is modest. — [Bilibili: Resolve's four Sony LUTs explained](https://www.bilibili.com/opus/366606644477573054); [Sohu (same content)](https://www.sohu.com/a/217125309_286786) (secondary, community)

**Cine+709**
- Sony: "Subtle colors, with high contrast and a tone curve close to film characteristics". It is intended as an easier grading starting point for TV workflows. — [Sony Cinematography](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/)
- A commentator calls it a negative-to-print emulation, "an aggressive look that really crushes highlights and shadows". — [XDCAM-User tag archive](https://www.xdcam-user.com/tag/s-log3/page/2) (via search snippet)

**709(800) / R709**
- High contrast tone curve, "high saturated, vivid colors". Renamed "R709" with VENICE. — [Sony Cinematography](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/)
- Middle grey goes in at 41% and comes out at 43%. A 61% white card maps to just over 85%. Everything above 61% is compressed into 85-109%, which gives "flat looking highlights". It is the best LUT for judging exposure because 1 stop changes brightness about 20%. — [XDCAM-User](https://www.xdcam-user.com/2017/12/using-luts-for-exposure-choosing-the-right-lut)

**Sony .cube file names**
- An older Sony set of S-Gamut3.Cine/S-Log3 cubes includes `SLog3SGamut3.CineToLC-709.cube` and `SLog3SGamut3.CineToLC-709TypeA.cube` (plus Cine+709 and 709(800) variants), posted on the Sony community forum. — [Adobe Community thread](https://community.adobe.com/t5/premiere-pro/sony-slog3-to-rec709-which-preset-lut/m-p/6797836)
- A second naming scheme exists, for example `1_SGamut3CineSLog3_To_LC-709` and `4_SGamut3CineSLog3_To_Cine+709`. TechSmith recommends these two for general use and says they come from Sony's website. — [TechSmith support](https://support.techsmith.com/hc/en-us/articles/41595058015117-My-Sony-Camera-Footage-appears-washed-out)
- A forum user reports that when recording S-Log3, the a6700 writes a default LUT to the SD card. The a6700 also has user LUT slots (PPLUT1-4) that can bake a LUT into movie recordings. — [Alpha Shooters forum](https://www.alphashooters.com/community/threads/a6700-picture-profiles-for-movies.7362/post-44207) (unofficial user report)

**Final Cut Pro built-in Sony LUT**
- FCP's built-in Sony S-Log3 camera LUT "Applies the appropriate linearization and 709(800%) MLUT tone mapping for footage shot with the S-Log3/S-Gamut3 setting". Camera LUTs are applied at the media level, before any clip effects. — [Apple FCP User Guide: Apply LUTs](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac)

**Sony x Picture Shop free LUTs (Nov 2022)**
- These are free LUTs on sonycine.com, designed for VENICE 2 but usable "with any Sony camera that supports S-Log3/S-Gamut3.Cine". — [TV Technology](https://tvtechnology.com/news/sony-picture-shop-team-up-on-new-luts); [Newsshooter](https://www.newsshooter.com/2022/11/11/sony-releases-new-custom-luts-for-the-venice-2/)
- Josh Pines family (Rec.709 and HDR):
  - **Lo Con Base**: low contrast with a built-in S-curve.
  - **Hi Con**
  - **50-50**: the "Goldilocks" option, with more contrast and saturation.
  - **Look 1** (Jason Fabbro): a bit more contrast and saturation, with reds and highlights pulled down to look less digital.
  - **Look 2**: warmer skin, more contrast and saturation, and the same red/highlight reduction.

  — [TV Technology](https://tvtechnology.com/news/sony-picture-shop-team-up-on-new-luts)
- D'Amore family (Rec.709 only): a daylight LUT, a tungsten LUT and a stylised look LUT. — [Newsshooter](https://www.newsshooter.com/2022/11/11/sony-releases-new-custom-luts-for-the-venice-2/); [Sony Cinematography announcement](https://sony-cinematography.com/articles/sony-and-picture-shop-announce-new-luts-designed-exclusively-with-the-venice-2/)

### Inferences
- **Closest Sony base to Dalen:** s709 or LC-709TypeA.
  - Dalen's mids are about 0.22, which is darker than a standard 709 render. His blacks are deep but not crushed, his highlights roll off at about 0.81, and the image is soft.
  - Both s709 and TypeA have soft contrast and protect highlights.
  - TypeA's lifted black (about 5%) is close to his p1 of about 0.018 once you pull the black slightly down.
  - Cine+709 and 709(800) crush shadows. On dark Cairo night footage that would push blacks below Dalen's level and clip the warm highlights.
- **Best free one-step option to test first:** Picture Shop "Look 1" or "Lo Con Base". Both start from a filmic low-contrast curve and tame reds and highlights. Look 2 adds warm skin, which matches Dalen's warm highlights. Teal in the shadows would still need a creative LUT or a colour-board shift.
- **Avoid the automatic FCP Sony LUT for this look.** It is the contrasty 709(800). Set Camera LUT to None, then apply a Custom LUT with your chosen Sony or third-party conversion. Alternatively, leave it on and use only a light creative layer, accepting the harder contrast.
- **Data vs video levels (unverified, general knowledge):** Sony's official cube downloads have historically shipped in two variants, typically marked "Data" (full-range, 0-1023) and "Video" (legal-range, 64-940) or "_Full"/"_Legal". In FCP and Premiere, which handle legal-range video internally, the standard (video/legal) LUTs are the usual choice. I could not confirm current Sony file naming in this pass.

### Gaps
- I could not reach a live pro.sony or sonycine.com download page. The exact current a6700 / alpha cube file names and data/video variants are therefore unconfirmed.
- No measured luma values for s709 output (only qualitative descriptions).
- I could not confirm in Sony documentation which preset LUTs the a6700 itself has (s709 vs 709(800)) or which LUTs the user already has in the camera's three user slots.
- The D'Amore stylised look is not described in any source found.

---

## Q2. Free creative film LUTs already on a Mac (Adobe "Kodak 5218 Kodak 2383 (by Adobe)", "Fuji ETERNA 250D Kodak 2395 (by Adobe)", SL CLEAN/SL BIG) and with Final Cut: expected input, look, usability in FCP

### Takeaway
I could not confirm the expected input of Adobe's bundled film LUTs from Adobe documentation. Print-film emulation LUTs in general often expect Cineon-log input, and feeding them other log or Rec.709 gives wrong (usually dark, contrasty) results. Test them only after a conversion LUT, at reduced strength. The "SL" presets are LookLabs SpeedLooks shipped inside Lumetri. Their input is undocumented here.

### Cited Findings
- Many film-emulation LUTs "are expecting files that have a Cineon input curve". Feeding them standard camera log gives very dark results because the black point sits differently (code value 95 in Cineon vs about 2.5 in other logs). — [DVinfo.net forum (camera maker post)](https://www.dvinfo.net/forum/silicon-imaging-si-2k/120686-film-out.html)
- The film LUTs shipped with DaVinci Resolve require Cineon input. A Blackmagic moderator noted this is undocumented. — [Blackmagic forum](https://forum.blackmagicdesign.com/viewtopic.php?p=768548)
- "Log scene exposure is not identical with balanced log Cineon CV input." The wrong encoding shifts colours. — [Lowepost forum](https://lowepost.com/forums/topic/842-green-color-on-kodak-5219/)
- 2383 print-emulation LUTs tend to shift greenery toward yellow. — [Lowepost / Resolve forum discussion, via search](https://lowepost.com/tags/kodak%20vision/)
- Most 2383 emulation LUTs derive from the same Light Illusion data and differ mainly in curves. — [Lowepost: Koji vs other film LUTs](https://wwwa.lowepost.com/forums/topic/773-koji-vs-other-film-luts)
- In one comparison, none of the film LUTs (FilmConvert, Magic Bullet, Juan Melara) preserved skin hues, so skin needed correcting. — [Wolfcrow comparison](https://wolfcrow.com/comparison-of-film-emulation-luts-filmconvert-vs-magic-bullet-film-vs-juan-maleras-free-luts-2/)
- SpeedLooks (LookLabs) presets appear in Premiere's Lumetri Presets list with "SL" names (for example "SL Blue Steel", "Clean Punch"). One user suspected a preset applies two LUTs, and a version difference made one look dark and desaturated. — [ToolFarm SpeedLooks tutorial](https://www.toolfarm.com/tutorial/using-speedlooks-and-dfs-in-premiere/); [Adobe Community](https://community.adobe.com/t5/premiere-pro-discussions/lumetri-grey-after-each-version-update/m-p/10143353/highlight/true)
- Adobe Community advice: let Premiere's colour management normalise log, then add look LUTs on top. Auto-detect log does a full transform to Rec.709. — [Adobe Community](https://community.adobe.com/questions-729/premiere-pro-treats-my-s-log3-footage-as-rec-709-what-am-i-doing-wrong-1621689)
- Juan Melara's free print-film LUTs (Fuji 3510, 3513, Kodak 2383, 2393; each in ConstLclip, ConstLmap and CUSPclip variants) expect log/Cineon-like input. Non-log footage needs his Video2Log LUT first. — [Tuts+ tutorial](https://photography.tutsplus.com/es/tutorials/how-to-create-the-film-look-with-your-footage-for-free--cms-27004); [Digital Production](https://digitalproduction.com/2014/01/13/print-film-emulation-luts/)

### Inferences
- **What the Adobe LUTs are (unverified, from general knowledge):**
  - The "(by Adobe)" .cube files ("Kodak 5218 Kodak 2383", "Fuji ETERNA 250D Kodak 2395", "Kodak 5205 Fuji 3510", etc.) live in Lumetri's *Creative* looks folder (inside the Premiere / After Effects app bundle, under Lumetri/LUTs/Creative). In Premiere they are offered as Creative-tab looks applied after Basic Correction, which suggests Adobe designed them for normalised Rec.709 input.
  - Names like "5218 to 2383" mean negative stock plus print stock. Their internals (Cineon vs 709 input) were not verified.
  - **Practical test:** in FCP, apply Sony conversion → Custom LUT (Adobe 5218/2383) and compare against applying it directly on S-Log3. Use whichever looks plausible, and expect it to be strong, so reduce its strength.
- **Using them in FCP:** .cube files can be loaded in FCP's Custom LUT effect (FCP accepts .cube and .mga, per general knowledge; not confirmed by the Apple page fetched). .itx/.look SpeedLooks files are not Custom LUT formats in FCP (unverified).
- **Look:** 2383 print emulations give dense blacks, warm/yellow-green bias and cyan shadows. That is close to Dalen's teal-shadow / warm-highlight split, but usually heavier contrast and saturation than his soft look. Use it at about 30-60% strength.

### Gaps
- No Adobe documentation was found specifying the input colour space of the "(by Adobe)" film LUTs or the SL presets.
- Not confirmed what LUTs ship with Final Cut Pro 12.3 itself (beyond camera LUTs).

---

## Q3. Paid and free LUT packs for a teal-warm cinematic vlog look from Sony S-Log3: products, prices, reputation

### Takeaway
The most credible conversion bases are:
- **Gamut BaseLUT** for FX30/A6700/A7RV ($35; S-Log3/S-Gamut3.Cine to Rec.709 or DWG)
- **Leeming LUT Pro, Sony Picture Profiles pack** ($39.99; S-Log3 corrective), with optional **Quickie Creatives** ($39.99)
- the free **Sony Picture Shop** LUTs

I found no legitimate "Daniel Dalen LUT" product. I could not verify 2026 pricing or reputations for Cinema Tools, Ground Control, CINECOLOR, Tom Antos or Joel Famularo in this pass.

### Cited Findings
- **Gamut:** the BaseLUT pack for Sony FX30, A6700 and A7RV costs $35. It provides precision conversion LUTs for Rec.709 and DaVinci Wide Gamut, with S-Log3/S-Gamut3.Cine input. Gamut also sells a BaseLUT Membership at $129/yr (2 BaseLUTs + 1 Creative LUT + 20% off). — [Gamut Sony cameras](https://gamut.io/camera/sony/); [Gamut A7RV page](https://gamut.io/camera/a7rv/); [Gamut LUTs for FCP](https://gamut.io/product/luts-for-final-cut-pro/)
- **Leeming LUT Pro:**
  - The Sony Picture Profiles pack is USD 39.99 and covers "S-Log3, S-Log2, HLG3, Cine2 Pro, S-Cinetone".
  - Its corrective LUT is designed to give "an accurate Rec709 image with zero effort".
  - Creative looks are sold separately as Quickie Creatives (USD 39.99), described as "professional film looks designed to work in perfect harmony with the corrective LUT baseline".
  - Leeming recommends ETTR after white balance, with zebras set per the setup guide. Final Cut Pro X is supported.
  - The site does not list the a6700 by name; check the setup guide.

  — [leeminglutpro.com](https://leeminglutpro.com/); [Leeming LUT Pro 4 Sony setup guide (PDF)](https://leeminglutpro.com/downloads/Leeming_LUT_Pro_4_Sony_Picture_Profiles_Setup_Guide.pdf)
- **Sony x Picture Shop:** free, S-Log3/S-Gamut3.Cine input, Rec.709 output (see Q1). — [TV Technology](https://tvtechnology.com/news/sony-picture-shop-team-up-on-new-luts)
- **Prolost:** Stu Maschwitz's free S-Log3 looks for Magic Bullet Looks 3.1 are matched to Sony's own LUTs and stay editable ("unlike a LUT, these are completely editable"). They need Magic Bullet Looks, not a plain LUT. — [Prolost](https://prolost.com/blog/slog3looks)
- **Juan Melara:** free 2383/2393/3510/3513 print-film LUTs (Resolve-oriented, log input). — [Digital Production](https://digitalproduction.com/2014/01/13/print-film-emulation-luts/)
- **Small-seller S-Log3 packs** seen in search; all are vendor claims with no independent reviews found:
  - Jordan Alsadi S-Log3 conversion/cinematic packs advise exposing +1.7 stops "for best results with that LUT". — [Sellfy](https://jordanalsadi.sellfy.store/p/s-log3-conversion-lut/)
  - Kondor Blue A7S3 creative LUT. — [Kondor Blue](https://kondorblue.com/products/sony-a7s3-creative-lut)
  - Henbu A7SIII LUTs, from $59.99. — [Henbu](https://henbu.sellfy.store/p/sony-a7siii-luts-for-slog3/)
  - Payhip 8-LUT pack, $25. — [Payhip](https://payhip.com/b/8Plm9)
  - Fstoppers Sony S-Log3 LUT pack. — [Fstoppers](https://fstoppers.com/product/sony-s-log3-luts-best-sony-luts-s-log3-video)
  - Etsy S-Log3 packs. — [Etsy](https://www.etsy.com/listing/4481092342)
  - A Kodak 2383 pack by Logflow ships Rec.709, DWG and S-Log3/S-Gamut3.Cine versions. — [Logflow Tools](https://logflowtools.gumroad.com/l/stockfusion)
- **"Daniel Dalen LUT":** a search found no LUT pack from or attributed to Daniel Dalen. The only near-match was an unrelated "Cinematic Color Grading LUT" by "Daniel Hook". — [Gumroad (unrelated)](https://captainhook.gumroad.com/l/OOPW)

### Inferences
- **Lowest effort that still gets close:**
  1. Gamut BaseLUT for A6700 ($35), or the free Sony s709 / Picture Shop Lo Con Base, as the conversion.
  2. A teal/orange or 2383-style creative LUT at partial strength.

  Leeming is the most "zero-thought" option because the corrective and creative LUTs are designed as a matched pair.
- **Treat any "Dalen LUT" sold on Etsy, Gumroad or TikTok shops as unofficial and unverified.** None was found.

### Gaps
- 2026 pricing and Reddit/forum reputations for Cinema Tools, Ground Control Color, CINECOLOR, Tom Antos, Joel Famularo and Kodachrome emulations: searches returned nothing usable.
- No Reddit threads surfaced via search (search tool returned none for r/SonyAlpha, r/colorists or r/videography queries).
- Not verified whether Leeming's current Sony pack explicitly lists the a6700.

---

## Q4. Stacking order (conversion → exposure/WB → creative LUT at partial strength → vignette) and partial LUT strength in FCP

### Takeaway
The accepted order is: correct exposure and white balance on the log (or immediately after the conversion), then the creative look on top, then finishing touches such as the vignette. FCP applies camera LUTs before all clip effects, so effects order in the inspector controls the rest.

### Cited Findings
- FCP camera LUTs "are applied at the media level (across the library) and are applied before any clip effects". Custom LUT effects are clip effects applied from the Effects browser, and can tone-map to the project's output colour space. — [Apple FCP: Apply LUTs](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac)
- A commercial S-Log3 to Rec.709 pack recommends adding its LUTs after exposure and white-balance adjustments. — [carlosq00 Gumroad](https://carlosq00.gumroad.com/l/lOJdb)
- Leeming: white balance, then ETTR, then corrective LUT, then Quickie Creative on top ("designed to work in perfect harmony with the corrective LUT baseline"). — [leeminglutpro.com](https://leeminglutpro.com/)
- Adobe advice: normalise log first, then apply look LUTs. — [Adobe Community](https://community.adobe.com/questions-729/premiere-pro-treats-my-s-log3-footage-as-rec-709-what-am-i-doing-wrong-1621689)
- An FCP adjustment layer spanning the project can act as a timeline-wide correction. — [Alpha Shooters forum](https://www.alphashooters.com/community/threads/a6700-picture-profiles-for-movies.7362/latest)

### Inferences
- **Recommended FCP 12.3 stack:**
  1. Clip Info inspector: set Camera LUT to None. Alternatively keep FCP's Sony S-Log3 LUT, but it is the contrasty 709(800).
  2. Color Board / Color Wheels on the S-Log3: exposure offset and white balance. Small moves in log are gentler than after the 709 conversion.
  3. Custom LUT: conversion (Sony s709, LC-709TypeA, Picture Shop, Gamut or Leeming), with input set to the LUT's expected space.
  4. Custom LUT: creative (2383-style / teal-orange), at partial strength.
  5. Color Wheels: slight teal push in shadows, warm in highlights, black point about 0.02.
  6. Vignette (FCP Vignette effect, subtle, for about a 0.80 edge/centre ratio).
- **Getting partial strength in FCP (unverified, test it):**
  - Option A: put the creative Custom LUT on an Adjustment Layer (a free FCP title template) and lower its Opacity. The layer's Video Inspector Compositing opacity blends the effected result with the clip below.
  - Option B: newer FCP versions may expose a "Mix" amount in the Custom LUT effect. I could not confirm this from the Apple pages fetched.
- **Apply the creative LUT once globally** (adjustment layer) and do exposure/WB per clip. This is the lowest-effort way to keep a consistent look.

### Gaps
- Apple's Custom LUT effect page could not be fetched in full. I did not confirm the existence of a Mix slider, the exact Input/Output colour-space options in FCP 12.3, or supported formats.

---

## Q5. Why LUTs look bad on underexposed log, and how much exposure headroom a drop-in LUT workflow tolerates

### Takeaway
A conversion LUT assumes Sony's reference exposure: middle grey about 41% S-Log3 in, about 43% out in 709(800). Underexposed S-Log3 puts the image in the noisy bottom of the curve. Brightening it afterwards lifts noise and colour errors, and a LUT that looks fine at correct exposure turns muddy or noisy. The traditional +1.7-stop overexposure rule comes from older, noisier sensors. Newer sensors need less, but you should not underexpose or shoot below base ISO.

### Cited Findings
- 709(800) expects middle grey at 41% in and outputs 43%. 1 stop equals about a 20% brightness change, so it is the best LUT for judging exposure. LC-709TypeA changes only about 10% per stop, so on it you "could easily be a full stop out". — [XDCAM-User](https://www.xdcam-user.com/2017/12/using-luts-for-exposure-choosing-the-right-lut)
- Chapman: when building or using custom LUTs, test shots must be exposed accurately. Either expose to Sony's levels and use EI offsets, or offset exposure in camera, but "never add an EI offset to a LUT that already has an offset". — [XDCAM-User](https://www.xdcam-user.com/2017/12/using-luts-for-exposure-choosing-the-right-lut)
- People often quote overexposing S-Log3 by "almost 2 stops, with 1.7 stops often quoted". Chapman argues this "was just a way to get around the noise in the previous cameras", and that on newer low-base-ISO sensors (A7S3, FX6, FX3) extra-bright exposure is not necessary. — [XDCAM-User: you don't always need to over expose S-Log3 (2023)](https://xdcam-user.com/2023/03/you-dont-always-need-to-over-expose-s-log3)
- Gamut: newer sensors handle noise much better. "always film at the Native ISO or slightly higher", and "Do not film under BaseISO!" — [Gamut: Stop overexposing S-Log3](https://gamut.io/stop-overexposing-s-log3/) (via search snippet; direct fetch was 403)
- Exposing S-Log3 at the reference level gives about 1.66 more stops of highlight detail at the cost of noisier shadows. — [Fstoppers](https://fstoppers.com/product/sony-s-log3-luts-best-sony-luts-s-log3-video)
- Some vendor LUTs are built around a specific overexposure (for example Jordan Alsadi: "expose your footage to 1.7 stops over for best results with that LUT"). — [Jordan Alsadi Sellfy](https://jordanalsadi.sellfy.store/p/s-log3-conversion-lut/)
- Leeming recommends ETTR after white balance, using zebras from its setup guide. — [leeminglutpro.com](https://leeminglutpro.com/)

### Inferences
- **For dark Cairo night and interior scenes:**
  - Expose for faces and practicals rather than the scene average. Aim for roughly +0.5 to +1 stop over Sony's reference on faces, keep ISO at or above base, and pull exposure down after the conversion. This keeps shadow noise low and still lets you land Dalen's dark mids (about 0.22).
  - Underexposing 1-2 stops then lifting gives blotchy teal/magenta shadow noise. That noise fights the "soft/creamy, no grain" quality.
- **a6700 base ISO (unverified, general knowledge):** in S-Log3 the a6700 has a minimum/base of ISO 800, with a second (higher) native ISO reportedly at 2500. Confirm in the a6700 manual or spec sheet.
- **Exposure tolerance of a drop-in LUT:**
  - Expect about ±1/2 stop before the look visibly shifts.
  - About +1 to +2 stops over is recoverable with an exposure pull before the LUT.
  - Underexposure beyond about -1 stop degrades quickly.
  - This is a practitioner rule of thumb, not sourced here.
- **Dalen-specific:** his p1 of about 0.018 (deep, not crushed) means the black should not be clamped. Lower blacks after the LUT, not before, and avoid Cine+709 or 2383 at full strength on dark scenes.

### Gaps
- No source quantifies the exact a6700 noise floor or a specific exposure tolerance for a drop-in LUT.
- The Gamut article could not be fetched in full (HTTP 403).

---

## Consolidated ranked shortlist: free / already-owned only (user constraint: NO purchases)
Everything below is free or already on the user's Mac or camera. The ranking is synthesised from the citations above.

1. **Sony Picture Shop "Josh Pines" LUTs: try "Look 1" first, then "Lo Con Base" or "Look 2".**
   - Free download from sonycine.com (Resources).
   - Input is S-Log3/S-Gamut3.Cine; output is Rec.709.
   - Use one Custom LUT in FCP, with Camera LUT set to None.
   - Why it fits: a low-contrast filmic S-curve with reds and highlights pulled down to look less digital, which matches Dalen's soft, creamy look and his highlights at about 0.81. Look 2 adds warm skin.
   - Then add a teal shadow / warm highlight nudge with FCP Color Wheels and a light FCP Vignette.
   - Sources: [TV Technology](https://tvtechnology.com/news/sony-picture-shop-team-up-on-new-luts); [Newsshooter](https://www.newsshooter.com/2022/11/11/sony-releases-new-custom-luts-for-the-venice-2/)
2. **Sony s709.**
   - Available as the s709 cube from Sony, possibly also as the in-camera Base Look or the default LUT the a6700 writes to the card (to be verified).
   - Input is S-Log3/S-Gamut3.Cine.
   - Why it fits: Sony calls it soft, low contrast, film-like, with subtle colour and highlight-preserving.
   - Use it alone, or with a creative LUT from #4 at partial strength on an adjustment layer.
   - Sources: [Sony Cinematography](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/); [Sony s709 white paper](https://www.sony.jp/ls-camera/knowledge/pdf/S709-white-paper-180524.pdf)
3. **Sony `SLog3SGamut3.CineToLC-709TypeA.cube`.**
   - Free Sony download; input is S-Log3/S-Gamut3.Cine.
   - Why it fits: Alexa-like, low contrast, slightly lifted blacks, less saturated. Lower the black point slightly to about 0.02 to reach Dalen's depth.
   - Sources: [XDCAM-User](https://www.xdcam-user.com/2017/12/using-luts-for-exposure-choosing-the-right-lut); [Adobe Community file list](https://community.adobe.com/t5/premiere-pro/sony-slog3-to-rec709-which-preset-lut/m-p/6797836)
4. **Creative layer on top of #2 or #3: "Kodak 5218 Kodak 2383 (by Adobe).cube"** (or "Fuji ETERNA 250D Kodak 2395 (by Adobe).cube" for a softer, cooler print).
   - Already on the user's Mac in the Adobe app bundle's Lumetri Creative LUTs folder. Copy the .cube out and load it via FCP Custom LUT.
   - Expected input is unverified. Try it after the Sony conversion; print-film LUTs may instead expect Cineon log.
   - Use it at about 30-60% (adjustment layer opacity) to get 2383-style cyan shadows and warm highlights without crushing Dalen's soft blacks.
   - Sources: [DVinfo on Cineon-input film LUTs](https://www.dvinfo.net/forum/silicon-imaging-si-2k/120686-film-out.html); [Lowepost on 2383 hue shifts](https://wwwa.lowepost.com/forums/topic/773-koji-vs-other-film-luts)
5. **Free film-print alternative: Juan Melara free 2383/2393/3513 print LUTs** (log input, more fiddly).
   - Source: [Digital Production](https://digitalproduction.com/2014/01/13/print-film-emulation-luts/)
6. **Built-in FCP Sony S-Log3 camera LUT.**
   - Zero effort, but it uses the contrasty 709(800). OK as a fallback with a creative layer kept light. Avoid Sony Cine+709 as the final look on dark Cairo footage because it crushes shadows and highlights.
   - Sources: [Apple FCP](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac); [Sony Cinematography](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/)
- **SL presets ("SL CLEAN", "SL BIG" .itx, LookLabs SpeedLooks in Lumetri):** probably not loadable in FCP's Custom LUT (not .cube; unverified). Input is undocumented. Low priority.

Footnote (excluded per no-purchase constraint): paid options would be Gamut BaseLUT A6700 ($35), Leeming LUT Pro Sony ($39.99) plus Quickie Creatives ($39.99), and assorted Sellfy/Etsy packs. None is needed.
