# Sony a6700 + Sigma 18-50mm f/2.8: low-light / night S-Log3 settings and habits (Cairo documentary)

User's kit: a6700, Sigma 18-50mm F2.8 DC DN Contemporary, ND filters. Hard constraint from the user: no purchases. Diffusion filters appear only as a footnote.
Current setup: XAVC S 4K 24p 100M 4:2:2 10-bit, S-Log3/S-Gamut3.Cine, f/2.8, 1/50, Auto ISO (up to 6400), three user LUTs in camera.

Source-quality note: Sony's a6700 Help Guide (helpguide.sony.net/ilc/2320) is the primary source for menu behaviour. CineD's lab test is the only controlled measurement of a6700 sensor performance I found. Pro Moviemaker gives the only review comment on the ISO 2000→2500 noise drop. Thermal data comes from one semi-controlled test (4K Shooters), Sony's own table and forum reports. No Gerald Undone a6700 S-Log3 review turned up in search. No Daniel Dalen-specific settings were found.

---

## 1. a6700 S-Log3 ISO behaviour: minimum ISO, second base (~2500), noise by ISO, and the Auto ISO range

### Takeaway
The a6700 sensor has two native gain stages, ISO 800 and ISO 2500. CineD measured almost identical dynamic range at both (11.2 vs 11.1 stops at SNR 2). Pro Moviemaker saw a "sudden drop in noise" going from ISO 2000 to 2500. That makes ISO 2500 to 6400 the clean high-gain range, and ISO 1000 to 2000 the worst place to be at night. Auto ISO 800 to 6400 is sensible. Raise the max to 12800 only as an emergency ceiling, because 12800 is "usable in a pinch", not clean.

### Cited Findings
- CineD lab test: "the sensor has two native ISO modes: ISO 800 and ISO 2500". It used 4K 25p XAVC S-I 4:2:2 10-bit. — [CineD a6700 lab test](https://cined.com/sony-a6700-lab-test-rolling-shutter-dynamic-range-and-latitude/)
- CineD dynamic range at ISO 800: about 12 stops visible above the noise floor. IMATEST gives 11.2 stops at SNR 2 and 12.4 stops at SNR 1. At ISO 2500: 11.1 / 12.3 stops, "only 0.1 stops less", and the waveform looks almost identical. CineD calls this "solid, but in the middle ground". — [CineD](https://cined.com/sony-a6700-lab-test-rolling-shutter-dynamic-range-and-latitude/)
- CineD exposure latitude: 8 stops in total. 4 stops over before the red channel clips on skin. At 3 stops under, "pushed-back noise starts to creep into the image". At 4 under it is "borderline" but the noise is "finely dispersed" so NR can save it to an extent. At 5 under it is "Game Over", with "horizontal (static) lines". The base exposure was 60% luma on the forehead. CineD calls this on par with the Sony A1 and one stop better than the Panasonic S5II / Canon R5 C. — [CineD](https://cined.com/sony-a6700-lab-test-rolling-shutter-dynamic-range-and-latitude/)
  - Caveat: my page extraction placed the latitude section next to the 120p results. I could not confirm whether the latitude test was shot in 25p or 120p.
- CineD 4K 120p (1.58x/1.6x crop) is noisier, at 9.51 / 10.9 stops (ISO 800) and 9.44 / 10.8 (ISO 2500). Avoid 120p at night. — [CineD](https://cined.com/sony-a6700-lab-test-rolling-shutter-dynamic-range-and-latitude/)
- Pro Moviemaker (Sept/Oct 2023) lists "base ISO settings – 800 and 2500". It notes Sony does not officially claim dual base ISO, but the reviewers "found a sudden drop in noise when going from ISO 2000 to 2500", which they liken to the FX30's EI mode. The image is "very clean" up to around 6400 and "usable at 12,800 in a pinch". Noise is more visible in the cropped 4K/120p and HD/240p modes. — [Pro Moviemaker Sept/Oct 2023, p.56](https://online.bright-publishing.com/view/639798169/56/)
- Engadget: noise is "well controlled up to ISO 6400", and images are usable up to ISO 12800. This was stills-oriented. Ephotozine (stills) calls 6400 and 12800 "quite noisy". — [Engadget](https://www.engadget.com/cameras/sony-a6700-review-the-companys-best-aps-c-camera-yet-164540597.html); [Ephotozine](https://www.ephotozine.com/article/sony-alpha-a6700-camera-review-36574/performance)
- DPReview forum ISO-invariance test (stills): "from 800 onward the noise [is] almost indistinguishable" once exposure is matched in post, while 100 to 400 is not ISO invariant. This was a single user test. — [DPReview forum](https://www.dpreview.com/forums/thread/4740029)
- Video ISO range is ISO 100 to 32000. "The available ISO range also depends on the [Gamma] setting". — [Sony Help Guide a6700: ISO](https://helpguide.sony.net/ilc/2320/v1/en/contents/0408C_iso.html); [Sony Help Guide: Picture Profile](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412D_picture_profile.html)
- Sony support (S-Log FAQ): the camera's minimum available ISO is higher with S-Log2/S-Log3 "because the camera controls the exposure differently than usual to achieve this wide dynamic range". If noise is significant at high ISO, "record with a brighter setting and perform grading after recording", with a corresponding decrease in dynamic range. Seen via search snippet; the page itself returned 403. — [Sony support article 00146206](https://www.sony.co.in/electronics/support/articles/00146206)
- Sony a6700 Help Guide (Picture Profile): "When using the S-Log3 gamma, noise becomes more noticeable compared to when using other gammas". Noise "may be improved by shooting with a brighter setting", with a narrower DR as the trade-off. — [Sony Help Guide: Picture Profile](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412D_picture_profile.html)
- Third-party sources consistently give the a6700's S-Log3 minimum/base as ISO 800 (CineD figure as quoted by Have Camera Will Travel; LUT maker listing 800/2500, plus an 800/3200 variant claiming "a cleaner image at 3,200 ISO"). The Sony Help Guide pages I fetched do not state the S-Log3 minimum number. — [Have Camera Will Travel (search snippet)](https://havecamerawilltravel.com/sony-a6700-auto-iso/); [gamut.io](https://gamut.io/camera/a7rv/)
- FX30 extrapolation (same 26MP APS-C sensor family; label as FX30, not a6700): Sony specifies FX30 S-Log3 base ISOs of 800 and 2500. Alister Chapman confirms 2500 as the FX30 high base. He says FX30-type dual-base cameras show "near identical performance at either the low or high base ISO". The high-base noise is "significantly lower than you would have by adding gain to get to the same level". — [XDCAM-User: Chart of Sony Dual ISO Base Levels](https://www.xdcam-user.com/2022/10/chart-of-sony-dual-iso-base-levels)
- FX30 (DPReview): Flexible ISO with custom ISOs such as 3200/6400/12800 switches base automatically. The FX30 is "a dual conversion gain design". — [DPReview FX30 review](https://www.dpreview.com/reviews/sony-fx30-initial-review)
- FX6 vs FX30 (Chapman, via search snippet): there is "more noise at 2500 than there is at 800, but not significantly more". The FX30 at high base is "clearly not as good as the FX6" at 12,800, but the fine grain from 6K-to-4K oversampling keeps it usable. — [XDCAM-User tag: ISO](https://www.xdcam-user.com/tag/iso)
- Low-light S-Log3 vs other gammas (Chapman): noise mostly "comes from the sensor". Switching gamma only changes the curve. At the same ISO and light, noise is "broadly similar". S-Cinetone looks cleaner mainly because its lower base ISO (320 vs 800) leads you to open up and give the sensor more light. — [XDCAM-User: Low light S-Log3 or S-Cinetone](https://www.xdcam-user.com/2022/11/low-light-shooting-s-log3-or-s-cinetone)
- A Sony community thread on a7S III low light found one test where "at ISO 8,000 the S-Log3 shot is so noisy that it's unusable" (different camera; anecdotal). — [Sony Cine community](https://community.sonycine.com/forums/topic/10-s-log3-better-or-worse-for-low-light-a7siii/)

### Inferences
- The user's old cap of about 2500 was not the problem in itself. With the cap at 2500 in a dim room, Auto ISO hit the ceiling, and the camera recorded about 2 stops under the S-Log3 target. Per CineD's latitude test, 2 to 3 stops under is where pushed-back noise starts to appear. Raising the cap to 6400 lets the camera reach the target exposure. A brighter exposure at ISO 6400 is cleaner after grading than an underexposed image at ISO 2500 that is pushed in post, because the sensor receives the same light and the high-gain stage adds less read noise than a digital push.
- The noise curve is not monotonic. ISO 1000 to 2000 is low-gain plus amplification, while 2500 switches to high gain. The Pro Moviemaker observation implies ISO 2000 can be noisier than 2500. For a "set and forget" night setup, the best fixed choice is Auto ISO min 800, max 6400. Where the user wants manual control at night, ISO 2500 or 3200 is a natural default.
- Auto ISO max 12800: keep 6400 as the normal cap. Reviewers call 12800 "in a pinch", and 1/25 shutter buys the same stop with no extra noise on static shots (see section 5). If the user truly will not touch the camera, 12800 as a cap is defensible because underexposure is worse than ISO 12800. The recommendation is still 6400, plus the habit of watching for the flashing ISO warning.
- "Dark, cinematic" is a grading outcome, not an exposure choice. Expose S-Log3 normally or slightly bright and darken in post. Underexposing in-camera for a "dark" look is what produces the noise and the lines CineD saw at 5 stops under.

### Gaps
- I found no measured a6700 S-Log3 noise comparison at 2500/3200/5000/6400/12800 in video, such as a SNR chart per ISO. Reviews give qualitative verdicts only. No Gerald Undone a6700 video turned up.
- Sony does not publish the a6700's high-gain switch point. The 2500 figure comes from CineD/Pro Moviemaker and the FX30 analogy. Whether Auto ISO in Flexible ISO picks the high-gain stage at exactly 2500 is unverified.
- The exact S-Log3 minimum ISO on the a6700 is not stated on the Sony Help Guide pages fetched; third parties say 800.

---

## 2. Auto ISO + auto exposure metering in S-Log3; exposure compensation

### Takeaway
In Manual mode with ISO AUTO, the a6700 does apply exposure compensation. The movie range is −2.0 to +2.0 EV. The meter is a scene-average meter aiming at standard S-Log3 levels (18% grey ≈ 41%), and it is easily fooled by night scenes with dark backgrounds and bright points. Use +0.7 to +1.0 EV for night/interiors. Sony's own guidance supports brighter exposure in S-Log3 to reduce noise. Sony-ecosystem guidance warns against auto exposure for consistency, but for this user Auto ISO plus comp is the pragmatic choice.

### Cited Findings
- a6700 Help Guide: exposure compensation for movies is −2.0 to +2.0 EV. "When using [Manual Exposure], you can perform the exposure compensation only when [ISO] is set to [ISO AUTO]". The screen only previews brightness changes within ±3.0 EV. — [Sony Help Guide a6700: Exposure Compensation](https://helpguide.sony.net/ilc/2320/v1/en/contents/0406B_exposure_compensation.html)
- a6700 Help Guide: ISO AUTO adjusts "within the set range". The min/max are set by pressing right on the control wheel on ISO AUTO. — [Sony Help Guide: ISO](https://helpguide.sony.net/ilc/2320/v1/en/contents/0408C_iso.html)
- a6700 Help Guide: Log Shooting On (Flexible ISO) lets you "record S-Log material with the exposure set by adjusting the ISO according to the shooting scene". — [Sony Help Guide: Log Shooting Setting](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_log_shoot_setting.html)
- Sony describes Flexible ISO (FX30) as a mode where ISO is "automatically adjusted on the fly, to compensate for changing lighting". — [Sony FX30 Cine EI video transcript](https://www.sony.com.tw/en/interchangeable-lens-cameras/products/ilme-fx30/ILME-FX30_Cine_EI_mode_video_transcript)
- S-Log3 reference levels: 18% grey ≈ 41%, 90% white ≈ 61%, skin ≈ 52% (FX6/FX9: 48 to 52%). The built-in metered-manual meter "is very easily confused" in S-Log3. Chapman doesn't recommend auto exposure because changes mid-shot "can make post production grading difficult". If you use auto exposure, he advises adding a +0.5 EV offset to avoid underexposure. He states that for low-noise cameras there is "no need to expose these cameras any brighter than the Sony recommended levels for most normal scenes". The article covers the a7S III/FX3/FX6/FX9, not the a6700. — [Sony Cinematography (Alister Chapman): How to correctly expose S-Log3](https://sony-cinematography.com/articles/how-correctly-expose-s-log3-a7s-iii-fx3-fx6-fx9/)
- Chapman also says the default zebra window (about ±10%) spans over a stop in S-Log3. Narrow it to about ±2% for grey/white cards and about ±6% for skin. — [XDCAM-User: zebras tag](https://www.xdcam-user.com/tag/zebras); [Wolfcrow / gamut.io via search](https://gamut.io/stop-overexposing-s-log3/)
- Gerald Undone's method, as reported by a blog: C1 Std+Range 55% for grey, C2 lower limit 94+ for clipping, which gives about +1.66 stops ETTR. Secondhand. — [daejeonchronicles (search snippet)](https://daejeonchronicles.com/tag/exposure-settings)
- Gamut.io argues against heavy overexposure of S-Log3 and puts S-Log3 highlights clipping near the high-80s/90s IRE (secondhand via search). — [gamut.io: Stop overexposing S-Log3](https://gamut.io/stop-overexposing-s-log3/)
- XDCAM-User (Chapman): on older/high-base cameras, 41% can be too noisy, so he advised exposing 1 to 2 stops brighter. He also says this is much less of an issue on newer sensors. — [XDCAM-User tag: S-Log3](https://xdcam-user.com/tag/s-log3)
- An a6700 user (DPReview forum) says that when the camera can't hold exposure within the Auto ISO range, the meter keeps showing the manual setting and the only warning is a flashing ISO value. — [DPReview forum](https://www.dpreview.com/forums/thread/4744065)

### Inferences
- Exposure compensation works in the user's mode, M with ISO AUTO, so it is the single dial that controls brightness. Recommended: +0.7 EV as a general night/interior default, and +1.0 EV where faces are lit by practicals against dark surroundings. Set 0 to +0.3 in daylight. Keep it at or below +1.0 at night. Above that, street lamps, signs and windows in frame will clip sooner. S-Log3 has a fixed ceiling, so each stop of comp moves one stop of highlight headroom into the shadows.
- Why comp is needed at night: average metering sees large black areas such as sky, streets and dark rooms, and raises ISO to lift them to grey. That makes ISO hunting and noisy, lifted blacks likely. Bright point sources pull the other way. Comp does not fix this; it biases it. A dark scene with a small bright face can still meter wrongly. A good habit: before a key take, fill the frame with the face or point at a mid-tone, half-press or note the ISO, and if the scene is static, switch ISO to that manual value (an AEL-style trick).
- Auto ISO ramps are visible in S-Log3 because the gamma is flat and the grade amplifies changes. For sit-down interviews and static shots, lock ISO manually (2500 or 3200 at night). Leave Auto ISO for walking/street shots where light changes.
- Watch for the flashing ISO value. It means the camera has hit 6400 and is underexposing. At that point, open up (already f/2.8), go to 1/25, find more light, or accept it.

### Gaps
- I found no Sony document stating the a6700 meter's exact target in Flexible ISO, such as metering S-Log3 grey to 41% vs a different internal target. The 41% figure is Sony's S-Log3 standard, not a confirmed a6700 meter behaviour.
- I found no a6700-specific test of exposure comp values in S-Log3 at night; the +0.7 to +1.0 recommendation is an inference from Sony/Chapman guidance and CineD's latitude data.

---

## 3. a6700 menu specifics

### Takeaway
Use Log Shooting Setting: On (Flexible ISO) with S-Gamut3.Cine. That route locks Gamma Display Assist to Off, so monitor with Display LUT On, using one of the user LUTs or s709. Set zebras to read exposure, Auto Slow Shutter off (it does nothing in M anyway), SteadyShot Standard for handheld (Active crops 1.13x), and fixed Kelvin WB. XAVC S 100M 4:2:2 10-bit is fine. XAVC S-I 240M is the best-quality option if card space allows.

### Cited Findings
**Log route**
- Log Shooting Setting (MENU → Shooting → Image Quality/Rec): options are Off and On (Flexible ISO). It also contains Color Gamut and Embed LUT File (On/Off). Embed LUT File is locked Off with SD/SDHC cards, so SDXC is needed. Custom WB setup may fail when Log Shooting is On; turn it off, do the custom WB, then turn it back on. — [Sony Help Guide: Log Shooting Setting](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_log_shoot_setting.html)
- Newer Sony bodies (a7 V / FX-series help guides) add Cine EI and Cine EI Quick in this menu. The a6700 page lists only Off / On (Flexible ISO). — [Sony Help Guide 2530 Log shooting](https://helpguide.sony.net/ilc/2530/v1/en/contents/211h_log_shoot_setting.html); [a6700 page](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_log_shoot_setting.html)
- Picture Profile gamma options include S-Log3. S-Gamut3.Cine and S-Gamut3 are colour modes. Detail is Level −7 to +7, with Mode, V/H, B/W, Limit, Crispening and Hi-Light Detail adjustments. Black Level is −15 to +15. The a6700 PP page lists PP1 to PP6, PP10 and PP11 (S-Cinetone) in its description. PP8/PP9 are not described on that page; on other Sony bodies they are S-Log3/S-Gamut3 and S-Log3/S-Gamut3.Cine. — [Sony Help Guide: Picture Profile](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412D_picture_profile.html)

**Monitoring**
- Gamma Display Assist is locked to Off when Log Shooting is On (Flexible ISO). It only affects the camera's screen, not HDMI. — [Sony Help Guide: Gamma Display Assist](https://helpguide.sony.net/ilc/2320/v1/en/contents/0601I_gamma_disp_assist.html)
- Display LUT (MENU → Setup → Display Option) shows the LUT during shooting and playback, as "a preview of the image after color grading". It can be assigned to a custom key (Display LUT Switch). — [Sony Help Guide: Display LUT](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_display_lut.html)
- Select LUT (MENU → Exposure/Color → Color/Tone) offers presets S-Log3, s709 and 709(800%), plus User1 to User16. — [Sony Help Guide: Select LUT](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_select_lut.html)
- DPReview: LUTs can be applied directly or used for preview only. When used for preview, they can be embedded in the file for post. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)

**Zebras**
- a6700 Zebra Level options are 70, 75, 80, 85, 90, 95, 100 and 100+, plus Custom 1 (standard value ± range, for correct exposure) and Custom 2 (lower limit, for overexposure). Zebras do not show on HDMI devices. — [Sony Help Guide: Zebra Display](https://helpguide.sony.net/ilc/2320/v1/en/contents/0406M_zebra_display.html)
- FX3/FX30 (Chapman): when a LUT is on, "the zebras measure the LUT, not the S-Log3". With s709, skin reads about 60% and a white card about 81%. Peak LUT output is typically 100%, so a zebra just below 100 works as a (conservative) clip warning. FX30 extrapolation; not verified on the a6700. — [XDCAM-User: What do FX3/FX30 zebras measure](https://www.xdcam-user.com/2023/04/what-do-the-fx3-and-fx30-zebras-zebras-measure-when-using-the-cine-ei-modes)
- On FX6/FX9, with no monitor LUT the zebras read S-Log3 levels; with a LUT on, they read LUT levels. — [Sony Cinematography](https://sony-cinematography.com/articles/how-correctly-expose-s-log3-a7s-iii-fx3-fx6-fx9/)

**Auto Slow Shutter / SteadyShot**
- Auto Slow Shutter slows the shutter automatically in dark scenes. It does not work in Shutter Priority, Manual, or when ISO is not ISO AUTO. — [Sony Help Guide: Auto Slow Shutter](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412_auto_slow_shutter.html)
- SteadyShot (movie): Active / Standard / Off. Active narrows the angle of view. Turn it off on a tripod. Active is unavailable at 100/120p. — [Sony Help Guide: SteadyShot (movie)](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412B_movie_steadyshot.html)
- DPReview: Active mode "applies a 1.13x crop". Gyro data is saved for Catalyst. The camera lacks Dynamic Active. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)
- Pro Moviemaker: IBIS is "very good" but not as strong as rival APS-C/M43 systems. — [Pro Moviemaker](https://online.bright-publishing.com/view/639798169/56/)
- Camera Labs: the Sigma 18-50 has no optical stabilisation, so the camera's IBIS does all the work. — [Camera Labs Sigma 18-50 review](https://www.cameralabs.com/sigma-18-50mm-f2-8-dc-dn-review/)

**Autofocus**
- DPReview: "Autofocus performance during video capture is top-notch". Face/eye and subject detection work in video "extremely well", and AF transition speed and responsiveness are adjustable. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)

**Codec / file format**
- a6700 4K 24p options:
  - XAVC HS 4K: 100M 4:2:2 10-bit, 100M 4:2:0 10-bit, 50M 4:2:2 10-bit, 50M 4:2:0 10-bit, 30M 4:2:0 10-bit
  - XAVC S 4K: 100M 4:2:2 10-bit, 100M 4:2:0 8-bit, 60M 4:2:0 8-bit
  - XAVC S-I 4K: 240M 4:2:2 10-bit
  - 24p means 23.98 fps and requires the NTSC setting. There is no 140M option at 24p.
  - [Sony Help Guide: Movie Settings](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412B_movie_setting.html)
- DPReview: All-I modes go up to 600 Mbps at high frame rates and "demand the use of an SD card with the fastest V90 rating". — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)
- Sony and third parties say XAVC S-I (intra) is easier to edit than Long GOP. HEVC (XAVC HS) saves card space but is heavier to decode. Pro Moviemaker says HS "is more intensive on your computer when editing". — [Freewell codec guide](https://freewellgear.com/blogs/news/sony-camera-codecs-guide-best-for-4k-compression); [Pro Moviemaker](https://online.bright-publishing.com/view/450984/45/)
- 2023 Apple Silicon bug: macOS 13.4 broke export/playback of Sony XAVC S 10-bit 4:2:2 at 100/120 fps in FCP 10.6.5/Resolve, while XAVC HS worked. Only high-frame-rate clips were affected, and I found no confirmation of a fix. — [Blackmagic forum](https://forum.blackmagicdesign.com/viewtopic.php?p=951009)
- An Infuse developer forum claims Macs have hardware-decoded H.264 Hi10P/Hi422P since M1. Unverified, with no Apple documentation. — [Firecore community](https://community.firecore.com/t/add-h-264-hi10p-hardware-decoding-support-on-macos/58028)

**White balance**
- Custom WB may fail with Log Shooting On (see above). — [Sony Help Guide: Log Shooting Setting](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_log_shoot_setting.html)

### Inferences
- **Route.** Keep Log Shooting On (Flexible ISO), with Color Gamut S-Gamut3.Cine. This is the a6700's dedicated log mode. The PP8/PP9 route records the same S-Log3 curve but leaves Gamma Display Assist available. Since the user has user LUTs, Display LUT is better than Gamma Display Assist anyway, because it shows something close to the final look and makes dark grading decisions visible on set. Use Embed LUT File On if using SDXC; it is metadata only and harmless.
- **LUT for monitoring vs exposure.** Many creator LUTs are built for "+1 exposed" footage and make normally exposed log look dark. If a user LUT looks right on screen, the exposure is whatever that LUT was designed for. For Cairo night work, monitor with whichever LUT the user grades with, but sanity-check against Sony's s709 occasionally. Assign Display LUT Switch to a custom button.
- **Zebras.**
  - Clip warning: set Custom 2 = 100+ while monitoring through the LUT. Per Chapman's FX30 note, zebras read the LUT output when Display LUT is on, so this is conservative, and the S-Log3 file has more headroom than the LUT shows.
  - Face exposure, if checking without LUT: Custom 1 = 52 ± 5 for skin in S-Log3 (Sony's 52% skin level), or 60 ± 5 on s709.
  - Simplest no-test habit: Display LUT on, zebra 100+ on, and accept zebras only on light sources themselves, never on faces.
- **White balance.** Use fixed Kelvin, not AWB. AWB in log shifts mid-shot under mixed Cairo street light (sodium, LED, neon), and those shifts are hard to grade out of a flat image. Suggested presets: about 3200K for tungsten/warm interiors and about 4300K for mixed night streets. A night street at 4300K renders sodium lamps warm/orange and LEDs neutral-cool, which suits a dark, warm-cool cinematic look. Keep one Kelvin per scene for continuity.
- **SteadyShot.** Use Standard for handheld walking/street; it keeps the full 18mm field of view, which matters indoors. Active adds a 1.13x crop and more stabilisation for walking shots. Use Off on a tripod, per Sony.
- **Auto Slow Shutter.** Turn it Off. It is irrelevant in M mode, but Off guarantees nothing changes if a mode dial gets knocked to P/A.
- **AF.** Face/Eye priority on, subject = Human, AF Transition Speed around 3 to 4 and AF Subject Shift Sensitivity around 4 to 5 for a slower, cinematic rack. These are typical vlog/documentary values and are inferences. At f/2.8 on APS-C there is moderate depth of field. AF hunting in very dark scenes is likely, so focus on lit faces or practicals. Note the inference only: contrast/phase AF loses confidence in very low light. Sources only say a6700 video AF is excellent; I found no low-light AF limit for video.
- **Detail/sharpening.** In Picture Profile, Detail −7 is common practice in log to avoid in-camera sharpening halos that noise reduction then amplifies. Not verified from a source for the a6700 Flexible-ISO route, and it is unclear whether PP Detail applies when Log Shooting is On. This is a gap.
- **Codec.**
  - XAVC S 4K 100M 4:2:2 10-bit is a good, safe choice and grades fine.
  - XAVC S-I 240M 4:2:2 10-bit is all-intra and the most robust for grading noisy night footage. It edits most smoothly in FCP but needs a V90 card and much more storage (about 2.4x).
  - XAVC HS 100M 4:2:2 10-bit (HEVC) gives the most quality per bit. That is useful for noisy night footage, since noise eats Long-GOP bitrate, but it is heavier to decode.
  - On an M4 Mac, all three should play in FCP (inference). If the user is happy with XAVC S 100M performance now, keep it. If storage allows and he has V90 cards, S-I 240M is the quality upgrade for night shots.

### Gaps
- Whether Picture Profile Detail/Black Level apply when Log Shooting is On (Flexible ISO) on the a6700 was not confirmed.
- Whether a6700 zebras read the Display LUT output or the S-Log3 signal was not confirmed by Sony docs. The evidence is the FX3/FX30 analogy from Chapman.
- I found no M4-specific FCP benchmark comparing XAVC S / S-I / HS 4:2:2 10-bit.
- I found no sourced a6700 low-light AF limits or recommended AF settings for documentary.

---

## 4. Sigma 18-50mm f/2.8 DC DN Contemporary: filter size, wide-open sharpness, low-light considerations (diffusion: footnote only)

### Takeaway
The filter thread is 55mm (confirmed by Sigma). Wide open at f/2.8, the lens is good but softest at 18mm wide open and at the 50mm end. One third of a stop down (f/3.2) noticeably sharpens it. At night the extra stop of light matters more than corner sharpness, so f/2.8 stays the default. The lens has no OIS, so the camera's IBIS does all the stabilisation.

### Cited Findings
- Filter size φ55mm (Sigma official spec; retailers agree). 290 g (L-mount). — [Sigma official](https://www.sigma-global.com/en/lenses/c021_18_50_28/feature.html); [Imaging Resource specs](https://imaging-resource.com/lenses/sigma/18-50mm-f2.8-dc-dn-contemporary/specifications)
- PetaPixel: at 18mm, centre sharpness peaks at f/6.3. "Wide-open at f/2.8 the performance was fine but does take a good positive leap in sharpness after just one-third stop down to f/3.2". 50mm wide open is sharper than 18mm wide open. — [PetaPixel review](https://petapixel.com/2021/10/19/sigma-18-50mm-f-2-8-dc-dn-contemporary-review-a-perfect-fit)
- Photography Blog (tested on A6000): at 50mm the centre is "a little soft at f/2.8, but outstanding between f/4 and f/11". At 24mm the centre is strong from f/2.8. Edges are a little soft wide open, with obvious vignetting and barrel distortion at the wide end. — [Photography Blog sharpness](https://www.photographyblog.com/reviews/sigma_18_50mm_f2_8_dc_dn_review/sharpness_2); [conclusion](https://www.photographyblog.com/reviews/sigma_18_50mm_f2_8_dc_dn_review/conclusion)
- Camera Labs: the downside is "a lack of optical stabilisation". — [Camera Labs](https://www.cameralabs.com/sigma-18-50mm-f2-8-dc-dn-review/)
- Footnote, diffusion (user owns none; no purchases): reviewers suggest Black Pro-Mist 1/8 for night city light and Glimmerglass 1/4 as the balanced night option. CineBloom 10% washes blacks at night. — [Alik Griffin comparison](https://alikgriffin.com/black-pro-mist-vs-glimmerglass-vs-cinebloom)

### Inferences
- At night, keep f/2.8. The softness at 18mm f/2.8 is a minor issue next to the extra 1/3 stop of light (f/3.2 = 1/3 stop more ISO). Video at 4K is about 8MP, so it is less demanding than 26MP stills; mild wide-open softness is largely invisible at 4K delivery. This is an inference.
- Remove any ND or UV/protective filter at night. Every extra flat glass surface in front of the lens increases ghosting and flare from street lamps, which show up as green/orange "orbs" opposite bright point sources. Alik Griffin notes coating matters for night city work. The user already owns ND filters; they should only be used in daylight to keep 1/50 at f/2.8, not at night.
- Vignetting at 18mm wide open darkens corners. That suits a dark look but adds corner noise when lifted; a vignette is usually added in grading anyway.
- The variable focal length does not change aperture (constant f/2.8), so zooming during a night shot does not change exposure.

### Gaps
- I found no video-specific review of this lens's focus breathing or its AF behaviour in very low light on the a6700.
- Per the coordinator, no further filter research was done.

---

## 5. Night-specific shooting habits: practicals, faces, highlight clipping, 1/25 shutter, flicker

### Takeaway
Expose for faces, not for the scene: brighter faces, darker environment, then darken in the grade. Use practical light (shop fronts, lamps, screens, street lamps) as key light by moving the subject, not the camera settings. Let point sources clip; protect faces. 1/25 at 24p is a legitimate +1 stop for static or slow shots. It costs motion blur and handheld stability, so avoid it for walking or panning shots. Egypt runs on 50 Hz mains, and 1/50 and 1/25 are both flicker-safe for 50 Hz lighting.

### Cited Findings
- S-Log3 skin target is about 52%, and "it is generally better to be a little bit brighter rather than a bit too dark" when exposing S-Log3 faces. — [Sony Cinematography (Chapman)](https://sony-cinematography.com/articles/how-correctly-expose-s-log3-a7s-iii-fx3-fx6-fx9/)
- Sony a6700 Help Guide: in S-Log3, noise "may be improved by shooting with a brighter setting"; Sony recommends test shooting. — [Sony Help Guide: Picture Profile](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412D_picture_profile.html)
- CineD a6700: 4 stops over before skin clips (from 60% luma base), while 3+ stops under starts showing noise. Latitude is asymmetric, favouring brighter exposure. — [CineD](https://cined.com/sony-a6700-lab-test-rolling-shutter-dynamic-range-and-latitude/)
- 360° shutter (1/25 at 24/25p) gains "a full stop of light" for more motion blur. Users report the blur is "massive" on movement and pans, and that slow shutter makes handheld shake more visible. Forum sources. — [EOSHD forum](https://www.eoshd.com/comments/topic/45201-i-really-like-the-look-of-360-degree-shutter-anyone-else/); [DVInfo forum](https://www.dvinfo.net/forum/archive/index.php/t-98587.html)
- For 50 Hz mains, shutter speeds of 1/100, 1/50 and 1/25 avoid flicker. — [Nikon Z9 manual: video flicker reduction](https://onlinemanual.nikonimglib.com/z9/en/vrm_video_flicker_reduction_148.html)
- Some LED luminaires are not tied to mains frequency (PWM), so a mains-matched shutter may not cure their flicker. — [Patent US11758281](https://patents.google.com/patent/US11758281); [Playtech.ro (Romanian)](https://playtech.ro/2025/cum-eviti-efectele-de-rolling-shutter-si-flicker-atunci-cand-filmezi-in-lumina-led-sau-neon/)
- The a6700's rolling shutter is about 15.8 to 15.9 ms in full-width 4K, which is "good but average" for APS-C. It is relevant to fast pans past street lights and to flash/LED banding. — [CineD](https://cined.com/sony-a6700-lab-test-rolling-shutter-dynamic-range-and-latitude/); [DPReview](https://www.dpreview.com/reviews/sony-a6700-review)
- XDCAM-User: S-Log3 vs S-Cinetone low-light noise is "broadly similar" at the same exposure. Noise depends on the light reaching the sensor, so getting light onto faces is the main noise lever. — [XDCAM-User](https://www.xdcam-user.com/2022/11/low-light-shooting-s-log3-or-s-cinetone)

### Inferences
- **Highlight clipping.** S-Log3 has a fixed clip point. Bare street lamps, neon tubes and car headlights will clip at any normal exposure for faces at night, and that is fine; real cinema footage has clipped practicals. Clipped point sources look most "cinematic" when small, warm and surrounded by soft roll-off, and S-Log3 gives a gentle roll-off before clipping. What must not clip is skin or large areas such as a lit wall or sky. Do not lower exposure to save a bulb.
- **Faces first.** Position people so a practical (shop window, café light, phone, lamp) lights the face from the side, ideally three-quarter, and let the background fall off. This gives the Daniel Dalen-style "dark with lit subject" contrast without lifting noise. Turning the subject 45° toward the light can be worth more than a full stop of ISO.
- **Metering trap at night.** In wide street shots with big dark areas, Auto ISO plus average metering will try to lift the darkness. The +0.7 to +1 EV comp in section 2 is for face-dominant shots. For wide, dark establishing shots, 0 to +0.3 EV may be enough, because the darkness is meant to be dark. Consider locking ISO (2500/3200) for wides.
- **1/25 shutter.** At 23.98p, 1/25 is about a 345° shutter, one stop brighter than 1/50. Use it for static interviews, locked-off or slow shots in dark rooms, and wides where nothing moves fast. Return to 1/50 for walking, handheld, crowds or traffic. 1/25 is flicker-safe in 50 Hz Egypt; 1/30 or 1/60 are not. It is better than going from ISO 6400 to 12800 for static scenes, because blur costs nothing when nothing moves. Avoid it with the 18mm wide handheld at walking pace.
- **Flicker in Cairo.** Egypt's grid is 50 Hz (common knowledge; not sourced above, see Gaps). Keep shutter at 1/50 or 1/25, never 1/48, 1/60 or 1/30, under fluorescent, sodium or cheap LED light. 23.98p with 1/50 is generally safe for mains flicker. Some PWM LED signage may still flicker or band; if it shows on the screen, try 1/25 or reframe.
- **Noise vs the "dark" look.** Exposing correctly and then darkening in the grade pushes noise down into the blacks, where it is less visible. Light noise reduction in FCP (or Resolve) plus a slightly crushed black point gives the clean, dark look. Underexposing in camera does the opposite.

### Gaps
- I did not find a source stating Egypt's mains frequency (50 Hz); it should be confirmed if needed for the report.
- I found no a6700-specific source on the slowest available movie shutter at 24p. I believe it is 1/25 on Sony cameras at 24p, but this is not confirmed from the Help Guide.
- I found no Daniel Dalen-specific settings or interviews about his exposure or grading.

---

## 6. Thermal / overheating in Cairo heat (28 to 32°C)

### Takeaway
At 4K 24p 100M with Auto Power OFF Temp set to High, the a6700 is likely to manage long continuous takes at 28 to 32°C in shade or at night. Sony's own worst-case table (4K 60p 150M, High) gives about 30 minutes at 25°C and about 10 minutes at 40°C. 4K 24p is much easier on the camera. The real risks are direct sun, hand-holding a hot body, and an enclosed rig or a closed screen.

### Cited Findings
- Sony a6700 Help Guide, Auto Power OFF Temp (MENU → Setup → Power Setting Option): Standard vs High. High lets the camera keep shooting when hotter. Sony's movie times with High:
  - 4K (XAVC S 4K 60p/50p 150M 4:2:0 8-bit): about 30 minutes at 25°C and about 10 minutes at 40°C.
  - HD 60p 50M: about 120 minutes at both temperatures.
  - Conditions: no Wi-Fi, monitor open.
  - Sony warns: "Do not shoot while holding the camera in your hand" with High, because of the risk of low-temperature burns.
  - [Sony Help Guide: Auto Power OFF Temp.](https://helpguide.sony.net/ilc/2320/v1/en/contents/0601L_auto_power_off_temperature.html)
- 4K Shooters test (73°F / about 23°C studio, tripod, screen open, external monitor, USB-C power, temp warning High): a6700 4K 24p 100 Mb/s ran 2 hours 10 minutes without a fan. 4K 60p ran 40 minutes (1h28 with a fan), and 4K 120p 20 minutes. Tips: set High, open the screen, keep the back unobstructed, avoid an external monitor. — [4K Shooters](https://www.4kshooters.net/2023/11/14/how-to-fix-overheating-on-the-sony-a6700-and-zv-e1/)
- Pro Moviemaker: 4K/60p at 25°C ran until the battery died (about 2 h). 4K/120p lasted about half an hour before overheating. — [Pro Moviemaker](https://online.bright-publishing.com/view/639798169/56/)
- DPReview forum (firmware 1.03, Standard, about 21°C): under 2 minutes at 4K 60p (an outlier); XAVC HS 4K 24p 30M with SteadyShot Standard ran 16 minutes. A reply suggests switching to High. — [DPReview forum: a6700 overheating?](https://www.dpreview.com/forums/threads/a6700-overheating.4795197/)
- Videomaker: overheat warnings can appear "after even 10 minutes of 4K/24p", and High delays them. — [Videomaker review](https://www.videomaker.com/reviews/cameras/sony-a6700-review-a-hybrid-mirrorless-camera-that-packs-a-punch/)
- DPReview review: "the a6700 can overheat, especially if you use its higher resolution and frame rate modes for longer periods". It did not overheat in their short-clip use. — [DPReview a6700 review](https://www.dpreview.com/reviews/sony-a6700-review)
- Anecdotes: a Florida beach shoot overheated at 4K 24p after 18 minutes; a 30p wedding overheated (user report). Neither had a controlled ambient temperature. — [thenewcamera.com](https://thenewcamera.com/does-sony-a6700-camera-overheat/)

### Inferences
- **Settings to set now.** Auto Power OFF Temp: High; flip the screen out, away from the body; turn off Wi-Fi/Bluetooth/smartphone connection; keep 24p rather than 60p/120p. Possibly prefer XAVC S/HS at 100M over S-I 240M; whether a higher bitrate meaningfully increases heat is not established.
- **Habits for Cairo.** Keep the camera out of direct sun between takes (shade, bag, or a white cloth over it). Do not leave it in a car. Stop recording between takes rather than rolling continuously. Power down in long pauses. Evenings and night shoots at 28 to 30°C are far kinder than midday sun.
- **Handheld with High.** Sony warns about low-temperature burns. Use a grip or strap, or hold by the lens and grip with short holds.
- **Battery heat.** Charging the camera internally via USB-C while recording adds heat. Using fresh, swapped batteries is cooler (inference). The 4K Shooters 2h10 result used USB-C power at about 23°C. At 30°C+ ambient, expect shorter times than that, but well beyond typical documentary take lengths.

### Gaps
- I found no controlled a6700 test at 30°C+ ambient for 4K 24p. Sony's table gives only 25°C/40°C, and only for 4K 60p 150M 8-bit with High.
- Whether XAVC S-I 240M runs hotter than XAVC S 100M on the a6700 was not found.
- Whether Standard vs High changes 4K 24p times on the a6700 at Cairo temperatures was not found.
