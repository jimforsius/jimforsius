# Fastest drag-and-drop colour pipeline in Final Cut Pro 12.3 for Sony a6700 S-Log3 on an M4 MacBook Air (free and built-in tools only)

> **Scope note (user constraint added mid-research):** NO purchases of any kind. The pipeline below uses only Final Cut Pro 12.3, Motion and Compressor (all included in Apple Creator Studio), Adobe 2026 apps he already owns, and free downloads such as Sony's own LUTs. Paid plugins appear only as one-line footnotes.
>
> Research date: 2026-10-12. Unless marked otherwise, **verified facts** come from Apple, Sony or vendor documentation. **User/opinion** marks forum posts, third-party blogs or reviewer opinion. **Inferences** are my own reasoning and are untested.

---

## Q1. Log conversion stage: Camera LUT, library and project colour, matching the in-camera LUT, levels, double LUTs, Custom LUT options, Sony "Embed LUT File"

### Takeaway
FCP's built-in "Sony S-Log3/S-Gamut3.Cine" Camera LUT is a **709(800%)** transform. It is not Sony's **s709** look, and that is the most likely reason the post grade did not match what he saw in camera (if his camera was monitoring with s709). The free fix: download Sony's official "Slog3-S-Gamut3.Cine To s709 V200.cube" (or 709(800%) if that is what he monitored with), add it once as a **Custom Camera LUT** in the Info inspector, and batch-assign it to every clip. It then sits at the media level, before every clip effect. Use exactly one log-to-709 conversion per clip, never two.

### Cited Findings
- **Automatic detection (verified):** "On import, Final Cut Pro reads metadata that identifies the log format and automatically applies the matching built-in camera LUT." Apple also warns that some cameras do not embed this metadata, and that it can be lost on transcode, so the LUT may have to be set by hand. — [Apple: Apply LUTs in FCP for Mac](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac)
- **Manual or batch assignment (verified):** Select one or more clips, open the inspector (Cmd-4), click Info, set Metadata View to General, Extended or Settings, then choose from the **Camera LUT** pop-up. The setting applies to every selected clip at once. — [Apple guide](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac)
- **Built-in Sony entries (verified):** Sony S-Log2/S-Gamut, S-Log3/S-Gamut3 and S-Log3/S-Gamut3.Cine. Apple's description of each: "Applies the appropriate linearization and **709(800%) MLUT tone mapping** for footage shot with the S-Log3/S-Gamut3.Cine setting on Sony cameras such as the F5 and F55." — [Apple guide (en-ca)](https://support.apple.com/en-ca/guide/final-cut-pro/ver24f966423/mac)
- **Add Custom Camera LUT (verified):** In the Info inspector's Camera LUT pop-up, choose "Add Custom Camera LUT". Select a .cube or .mga file. You can pick one file, several, or a whole folder, and a folder becomes a submenu. Choose the **Output Color Space** the LUT converts to ("usually indicated in the custom camera LUT name"), then click Open. The LUT appears in the "Custom Camera" section of the menu. Apple says custom camera LUTs can come from "camera manufacturers or from a DP, DIT, or colorist". — [Apple guide (en-ca)](https://support.apple.com/en-ca/guide/final-cut-pro/ver24f966423/mac)
- **Order of processing (verified):** "Camera LUTs apply at the media level, before any clip effects", while Custom LUT effects "are clip effects and can be placed at any point in the effect order." — [Apple guide](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac)
- **Library colour processing (verified):** "If the library is set to Wide Gamut HDR, camera LUTs preserve the full dynamic range of the log media… If the library is set to either Standard or Wide Gamut (Deprecated) when you apply a camera LUT, the media is tone mapped (downgraded) to the narrower standard dynamic range (SDR)." — [Apple guide (en-ca)](https://support.apple.com/en-ca/guide/final-cut-pro/ver24f966423/mac)
- **Wide Gamut HDR working space (verified):** linear RGB with Rec. 2020 primaries. Built-in camera LUTs preserve the full dynamic range of log media when converting into the working space. — [Apple: Use wide-gamut HDR color processing](https://support.apple.com/guide/final-cut-pro/ver1cd9629a5/mac); Apple's white paper says FCP can convert log "for viewing in Rec. 709 or wider color gamuts, and in either SDR or HDR." — [Apple WCG/HDR white paper (PDF)](https://www.apple.com/euro/final-cut-pro/f/generic/docs/Working_with_Wide_Color_Gamut_and_High_Dynamic_Range_in_Final_Cut_Pro_X.pdf)
- **SDR delivery (user):** Apple Community advice is to use an SDR (Rec. 709) timeline when there is no HDR monitor or HDR deliverable. — [Apple Community thread](https://discussions.apple.com/thread/254900312)
- **Official free Sony conversion LUTs (verified it exists, download is behind a form):** Sony's cinematography site lists "Slog3-S-Gamut3.Cine To s709 V200.cube" (Rec. 709), plus sP3DCI and sP3D65 versions, described as "LUTs to process Sony S-LOG 3 to standard color spaces". There is no 709(800%) file on that page. A form must be filled in to download, and no price is shown. — [sony-cinematography.com/resources/luts](https://sony-cinematography.com/resources/luts/)
- **s709 vs 709(800%) (verified on another Sony body):** Sony's BURANO page says the camera has "the established s709 and 709 (800) looks", which shows they are two different Sony looks. — [Sony Pro BURANO LUTs](https://pro.sony/ue_US/technology/cinealta-burano-luts)
- **Free alternative (third-party, free, no redistribution):** Alister Chapman's free S-Log3/SGamut3.Cine LUTs. He describes one as "similar to Sony's s709 but a bit less yellow/green". — [xdcam-user.com](https://www.xdcam-user.com/picture-settings-and-luts/alisters-free-luts/)
- **Sony Embed LUT File (verified):** With [Embed LUT File] on, the LUT is embedded in the movie file **and** saved to the card as a separate file. Tools that support the **Catalyst Prepare Plugin** import the embedded LUT automatically. Other tools can import the LUT file from the card manually. — [Sony helpguide: Using metadata in post-production](https://helpguide.sony.net/di/pp/v1/en/contents/TP1000756722.html). On the a6700 the setting is On/Off and is **locked to Off with SD/SDHC cards**, so an SDXC or CFexpress A card is needed. — [Sony ILCE-6700 helpguide: Log Shooting Setting](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_log_shoot_setting.html)
- **Washed-out or wrong Sony LUT results (user):** An FX3 user said footage "doesn't look correct in FCP even with Sony's own LUT… still washed out" (no resolution posted). — [Apple Community: Sony FX3 LUT problem](https://discussions.apple.com/thread/255318022). Another user fixed misinterpreted colour by setting the colour space to Rec. 709 by hand. — [Apple Community](https://discussions.apple.com/thread/252301147)
- **Custom LUT effect options (verified):** Effects browser > Color > Custom LUT. In the Video inspector choose "Choose Custom LUT…", then set **Input** (the colour space the LUT converts from, "determined when the custom LUT was created"), **Output** (the colour space it converts to) and **Mix** ("the amount of the original image to be blended with the adjusted image"). Apple's page does not describe a separate "Convert" control. — [Apple guide (en-ca)](https://support.apple.com/en-ca/guide/final-cut-pro/ver24f966423/mac)
- **Fixed bug (verified):** In 12.3, Apple "Fixes an issue that caused proxies generated from Canon Log and other log-encoded formats to have a noticeable color tint." Before 12.3, log proxies could look different from the originals. — [FCP release notes](https://support.apple.com/en-us/102825); [Larry Jordan](https://larryjordan.com/articles/new-features-in-apple-final-cut-pro-12-3/)
- **Vendor opinion:** Gamut.io says FCP's built-in log LUTs "are not entirely color accurate". This is a commercial vendor's opinion. — [gamut.io](https://gamut.io/hdr-video-in-final-cut-pro/)

### Inferences
- **Why the camera preview and FCP differ:** FCP's Sony entry is 709(800%) (verified). If the a6700's Display Assist was set to s709, which I believe is Sony's default "look" on current bodies (unverified for the a6700, see Gaps), the two transforms differ in contrast and hue. Loading Sony's s709 .cube as a Custom Camera LUT should make FCP match the monitor almost exactly. Test it on one clip next to a still frame grabbed from the camera.
- **Double-LUT pitfall:** If FCP auto-applied the built-in Sony Camera LUT and he also drops a Sony S-Log3→709 .cube in as a Custom LUT effect, the conversion happens twice and the image looks crushed and oversaturated. Use **either** the Camera LUT slot **or** a Custom LUT effect with Camera LUT = None, never both. The Camera LUT slot is the faster route because it is batchable and applied before effects.
- **Library and project settings for YouTube SDR:** A Wide Gamut HDR library with a project colour space of Rec. 709 (SDR) is the documented way to keep log range for grading while delivering SDR. Apple's text says a Standard library also works but tone maps at the Camera LUT stage. With a 709-target LUT the visible difference is small, but Wide Gamut HDR keeps more highlight headroom for Super Highlights recovery.
- **Data vs video levels:** I found no source that covers full vs legal range handling in FCP's Custom LUT import. Sony's download page also does not say whether the s709 V200 LUT is full or legal range. If the image looks lifted or crushed after applying it, compare the result against the built-in Sony entry. FCP's Custom LUT effect has no exposed range toggle (Apple's page lists only Input, Output and Mix).
- **Embed LUT File:** I found no Apple statement that FCP reads Sony's embedded LUT. FCP documents only its metadata-driven log detection. The practical route is to load the .cube that the camera also writes to the card (or Sony's download) as a Custom Camera LUT.

### Gaps
- I did not verify which Display Assist/Base Look LUTs the a6700 offers (s709 vs 709(800%)) or which one is the default. The Sony Log Shooting page links "Select LUT" but does not list the options. Check the camera menu.
- No source documents the full vs legal range of Sony's s709 V200 .cube in FCP.
- No Apple statement says whether FCP reads Sony's embedded LUT metadata.
- Whether Sony's LUT download form is free could not be confirmed (no price shown; historically free).
- No current Apple page describes a "Convert" option in the Custom LUT effect. The task brief's mention of it may refer to older versions.

---

## Q2. Creative look stage: Custom LUT on Rec. 709, ordering, Mix, adjustment clips (native since 11.1), effect presets, Paste Effects

### Takeaway
FCP has had **native Adjustment Clips since 11.1 (March 2025)**, so the title-based adjustment-layer workaround is obsolete. The fastest one-click route is a saved **Video Effects Preset** holding [Noise Reduction → Color Adjustments → Custom LUT (look, Mix ~50–80%) → mist/bloom]. Drag it onto clips or Paste Effects (Opt-Cmd-V) across a selection. An alternative is one Adjustment Clip spanning the whole timeline for the look, with only per-clip exposure trims on the clips themselves.

### Cited Findings
- **Adjustment clips (verified):** FCP 11.1 added "Adjustment clips for applying color and effects to a range of clips". — [FCP release notes](https://support.apple.com/en-us/102825). Create one with Edit > Add Adjustment Clip. It is a transparent connected clip with the magenta Adjustment Clips role, and "effects applied to an adjustment clip are applied to all clips below it in the timeline". It accepts colour corrections, blurs, masks and built-in transforms. — [Apple: Add adjustment clips](https://support.apple.com/guide/final-cut-pro/add-adjustment-clips-verfda63436e/mac). Default length is 10 seconds at the playhead. — [Larry Jordan 11.1](https://larryjordan.com/?p=167097); [No Film School](https://nofilmschool.com/final-cut-pro-11-1-update)
- **12.0 bug fix (verified):** Fixed an adjustment clip disappearing when using Overwrite to Primary Storyline. — [FCP release notes](https://support.apple.com/en-us/102825)
- **Save a video effects preset (verified):** Select the clip, then choose File > Save Video Effects Preset or click Save Effects Preset in the Video inspector. The preset appears in the Effects browser and "functions like any other video effect". — [Apple: Save video effects presets](https://support.apple.com/guide/final-cut-pro/save-video-effects-presets-ver462c2078f/mac). Colour correction presets can also be saved and applied by dragging or double-clicking. — [Apple: Save color correction presets](https://support.apple.com/guide/final-cut-pro/save-color-correction-presets-verbbd35f70/mac)
- **Paste Effects / Paste Attributes (verified):** Edit > Paste Effects (Opt-Cmd-V) copies all of a clip's effects to a group of clips and is "the fastest way". Paste Attributes (Shift-Cmd-V) lets you choose individual effects. — [Apple: Copy effects between clips](https://support.apple.com/guide/final-cut-pro/copy-effects-between-clips-ver3029fc422/mac)
- **Custom LUT Mix slider (verified):** It blends the original image with the LUT result, which acts as LUT intensity. — [Apple guide](https://support.apple.com/en-ca/guide/final-cut-pro/ver24f966423/mac)
- **Blogger workflow (opinion):** One blogger places Sony's S-Log3→709 LUT *after* other adjustments in the stack. That is a workflow choice. — [Roman Fox](https://www.snapsbyfox.com/blog/how-to-grade-sony-s-log3-in-final-cut-pro)

### Inferences
- **Recommended per-clip stack** (top to bottom in the Video inspector; FCP processes top-down):
  1. Camera LUT (Info inspector, media level): Sony s709 custom.
  2. Noise Reduction (only on high-ISO clips; Apple says put it first).
  3. Color Adjustments: exposure/WB trim, Super Highlights pulled down, Shadows slightly crushed for the "dark" look.
  4. Custom LUT (creative look, Input/Output = Rec. 709, Mix 50–80%). Without paid LUT packs, he can export his own look LUT, or skip this and rely on Color Adjustments/Color Board/Color Wheels saved as a colour preset.
  5. Auto Mask (skin) correction or blur (Q5).
  6. Mist/bloom effect (Q4).
- **Two-preset strategy:** "DD Base" (Color Adjustments + look + mist) for every clip, and "DD Night NR" (the same plus Noise Reduction first) for ISO 3200+ clips. Then: select all clips, drag the preset once. Or grade one clip, Cmd-C, select the rest, Opt-Cmd-V.
- **Adjustment clip vs per-clip:** An adjustment clip makes the look and mist a single object (one place to tweak), but Noise Reduction should stay per-clip because temporal analysis is per source. Also check that mist on an adjustment clip affects titles placed under it.
- **Free creative look LUT:** He can build the look once in FCP or DaVinci Resolve (free) and export a .cube, or use Alister Chapman's free LUTs or Sony's free LUT-gallery looks ([Sony Alpha Universe LUT gallery](https://www.sony.co.uk/alphauniverse/lut-gallery)). FCP itself cannot export a .cube (not verified, but no such feature is documented).

### Gaps
- No current Apple doc confirms whether effect presets can include Auto Mask definitions that re-detect per clip. One reviewer says auto masks can be copied to the next clip, where they find the same subject again ([FCP Academy](https://fcpacademy.com/tutorial-fcp-12-3)).
- No benchmark compares adjustment clip vs per-clip render cost.

---

## Q3. New in FCP 12.x: Auto Mask (skin), Match Color, Super Highlights, HEVC proxies, background rendering off

### Takeaway
12.3 (30 June 2026) is the key release for this workflow. **Auto Mask** isolates skin, hair, sky and more with no tracking. **Match Color** now creates an adjustable correction from a reference frame, which is a free way to match every clip to one hero "look" frame. **Super Highlights** gives highlight roll-off control above about 70 IRE. Proxies are now **HEVC**, and **background rendering is off by default**.

### Cited Findings
- **12.3 release notes (verified):** Match Color tool "to match color across cameras, lighting, and cinematic styles"; Auto Mask "isolates recognized objects so you can color correct or enhance them without manual tracking"; Edit Detection; Generate Captions; proxies now HEVC instead of H.264 "for better compression and HDR support"; background rendering now off by default; fix for log-proxy tint. — [FCP release notes](https://support.apple.com/en-us/102825)
- **12.0 (Jan 28 2026):** Transcript and Visual Search, Beat Detection. **12.2 (Apr 9 2026):** minor fixes. No 12.1 entry exists on Apple's page. — [FCP release notes](https://support.apple.com/en-us/102825)
- **Auto Mask categories (Iain Anderson, verified hands-on):** people, hair, clothing, **skin**, lips, mouth, teeth, eyes, eyebrows, foreground/background, sky, foliage, cats/dogs. Choose it from a new icon in the header of a colour correction or effect. Masks can be blurred, shrunk or expanded, applied inside or outside, and combined. Detection runs per frame, and playback is "more or less" real time. Small or distant subjects can flicker, and an eyes mask can drop out for a frame when someone blinks. Anderson calls it the "hero feature". — [ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/)
- **Auto Mask is on-device AI** and works alongside the existing Magnetic Mask. — [RedShark News](https://www.redsharknews.com/apple-creator-studio-update-includes-final-cut-pro-12.3-and-more); [PetaPixel](https://petapixel.com/2026/07/01/apple-brings-new-masking-tools-to-final-cut-pro-amid-creator-studio-update/); [MacMost how-to](https://macmost.com/how-to-use-final-cut-pro-auto-mask.html)
- **Match Color (verified hands-on):** Now adds an adjustable correction module whose sliders (the same as Color Adjustments, including Super Highlights) are preset to match a chosen reference frame. A button picks a new source. Anderson: "Previously, the Match Color feature didn't have enough flexibility to be truly useful." — [ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/)
- **Super Highlights:** In Color Adjustments and Match Color. Normal Highlights starts affecting values around 20 IRE, while Super Highlights leaves anything below about 70 IRE untouched. — [ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/)
- **Background rendering:** Off by default because modern Macs live-render most corrections. — [ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/). Neat Video's FCP known-issues page also recommends disabling background rendering and skimming when heavy filters are applied. — [Neat Video known issues](https://www.neatvideo.com/support/known-issues/finalcut)
- **Regression report (user):** One reader on Larry Jordan's site said 4K drone footage that played fine on 11.1.1 "has major issues with 12.3" and he reverted. This is anecdotal. — [Larry Jordan 12.3](https://larryjordan.com/articles/new-features-in-apple-final-cut-pro-12-3/)
- **Other reviews:** [Ripple Training](https://www.rippletraining.com/whats-new-in-final-cut-pro-12-3/); [FCP Academy](https://fcpacademy.com/tutorial-fcp-12-3); [fcpxfullaccess](https://fcpxfullaccess.com/blogs/blog/final-cut-pro-12-3-auto-mask-match-color-whats-new)

### Inferences
- **Match Color as a free "look matcher":** Grade one hero clip by hand. For every other clip, apply Match Color with the hero frame as reference, then trim. Because the result is an adjustable module, it can be refined, unlike the old one-shot version.
- **Super Highlights** gives the soft highlight roll-off typical of the Dalen-style dark/filmic look without curves work.
- **Leave background rendering off** on the Air. Render manually (Ctrl-R) only heavy sections such as Noise Reduction clips, which avoids constant heat and SSD writes on a fanless machine.
- **Auto Mask "Sky"** plus a darker exposure gives a moody, darker sky in one click. **"Skin"** inside a warm Color Adjustments correction protects skin tones under a teal/dark grade.

### Gaps
- No official Apple user guide page for Auto Mask settings and categories was retrieved; the list comes from Anderson's review.
- No measured fps or performance for Auto Mask on a base M4 Air.

---

## Q4. Noise reduction: built-in vs alternatives (free only), settings, order, render strategy

### Takeaway
Use FCP's built-in **Noise Reduction** effect, first in the stack and only on high-ISO clips. Its controls are Amount and Sharpness pop-ups, it needs a one-time analysis, and Apple says it should go first for performance. It is weaker than Neat Video on heavy noise. It is still free and is far faster than After Effects Remove Grain, which took 14 s/frame. Adobe-owned alternatives exist (Premiere/AE), but the user found AE too slow.

### Cited Findings
- **Built-in effect (verified):** Search "noise reduction" in the Effects browser. "The first time the effect is applied, Final Cut Pro analyzes the clip for noise. This analysis must be complete before you can see the result." Controls are an **Amount** pop-up and a **Sharpness** pop-up. Apple recommends placing Noise Reduction **first** in the effects list for best performance and results. — [Apple FCP user guide: reduce video noise](https://support.apple.com/en-my/guide/final-cut-pro/ver7d031487b/mac)
- **Third-party tips:** Start with Amount High, Sharpness Medium. — [Motion Array](https://motionarray.com/learn/final-cut-pro/reduce-video-noise-in-final-cut-pro/). Use the least sharpness to avoid "vibrating" edges. — [Boris FX blog](https://borisfx.com/blog/how-to-use-final-cut-pro-noise-reduction-remove/)
- **Quality opinions:** A 2018 test found Apple's filter did a "solid job" but with less control than Neat. — [Larry Jordan](https://larryjordan.com/articles/final-cut-pro-x-new-remove-video-noise/). An Apple Community user said it worked poorly on pro-camera footage. — [Apple Community](https://discussions.apple.com/thread/256071768). Neat Video's own blog says it handles moderate grain but struggles with severe noise; this is a competitor's view. — [Neat Video blog](https://www.neatvideo.com/blog/post/reduce-noise-fc)
- **A reader asked Apple for "pro-level denoise"** in the 12.3 comments, implying no upgrade in 12.3. — [Larry Jordan 12.3](https://larryjordan.com/articles/new-features-in-apple-final-cut-pro-12-3/). The 12.x release notes list no noise reduction changes. — [FCP release notes](https://support.apple.com/en-us/102825)
- **General speed principle (Neat docs, applies to any heavy filter):** Applying denoise to smaller frames is always faster than to larger frames. Neat suggests using an HD compound clip instead of a 4K clip. — [Neat Video FC guide](https://www.neatvideo.com/support/quick-start-guide-fc); [Neat: smooth editing in FCP](https://www.neatvideo.com/blog/post/fc-smooth-play)

### Inferences
- **Best free night strategy:** Expose S-Log3 brighter at capture (+1 to +2 stops over meter, within highlight limits) to reduce visible noise. I did not research this; it belongs to the camera-side researcher. In FCP, apply Noise Reduction (Amount Medium/High, Sharpness Low/Medium) only to ISO 3200–6400 clips, then **render just those clips** (select, Ctrl-R) before playback, rather than leaving background rendering on.
- **Mist/grain helps:** A mist plus light grain look hides residual noise. That is a stylistic opinion consistent with the Dalen aesthetic.
- **Export at 4K but NR only where needed.** Applying NR to every clip would multiply export time.

### Gaps
- No measured fps for FCP's Noise Reduction on M4. No Apple doc lists the exact Amount options (believed to be Low/Medium/High/Max; unverified).
- Whether the built-in effect is spatial-only or temporal is not documented.

*Paid footnote: Neat Video 6 (v6.1 supports FCP 12; Home edition limited to 1920×1080; Pro unlimited; v5 prices were $79.90/$144.90, current v6 price unverified) — [Neat compatibility](https://www.neatvideo.com/features/compatibility/nv6fc), [digitalproduction](https://digitalproduction.com/2026/04/13/neat-video-6-1-2-adds-vegas-2026-and-nuke-17/), [videohelp](https://www.videohelp.com/tools/Neat-Video).*

---

## Q5. Pro Mist / bloom / halation with built-in tools, including a one-click Motion-published "Pro Mist" effect

### Takeaway
There are two free routes. (a) **In FCP:** duplicate the clip above itself (Option-drag), add Gaussian Blur, and set the top clip's blend mode to Screen (white Pro Mist) or Soft Light (Black Pro Mist) at low opacity. This works but doubles decode and is not one click. (b) **Better:** build a **Final Cut Effect template in Motion** (included in Creator Studio) using Motion's built-in **Bloom** filter, or a blur + blend stack, and **publish** Amount, Threshold, Blur and Mix as sliders. It then sits in the FCP Effects browser as a single drag-on effect and can be part of the saved preset.

### Cited Findings
- **Motion is included (verified):** Apple Creator Studio includes Final Cut Pro, Logic Pro, Pixelmator Pro, **Motion**, **Compressor** and MainStage, at US$12.99/month or $129/year. — [Yahoo Tech](https://tech.yahoo.com/ai/apple-intelligence/articles/apple-creator-studio-bundles-six-221403816.html); [heise](https://heise.de/-11139924); [RedShark pricing](https://www.redsharknews.com/apple-creator-studio-features-pricing-analysis)
- **Motion Bloom filter (verified):** "Simulates the effect of extremely overexposed highlights on film. Highlights above a specific threshold are blurred, brightened, and recomposited with the original." Parameters: **Amount**, **Brightness**, **Threshold** (the luminance where bloom starts), Horizontal/Vertical distance, Clip to White, Crop, Mix. — [Apple Motion guide: Bloom filter](https://support.apple.com/guide/motion/bloom-filter-motn169fae47/mac) (parameter text from the [Motion 5.2 help](https://help.apple.com/motion/mac/5.2/en.lproj/motn169fae47.html))
- **Effect template workflow (verified):** Open a **Final Cut Effect** project in Motion, add filters to the **Effect Source** layer, and choose **Publish** from each parameter's Animation menu, or Control-click the parameter name, to expose it in the FCP Inspector. Publishing the filter's top row exposes only the on/off checkbox. **Rigs** can combine parameters into one slider and limit their range. Some parameters cannot be published. — [Apple: Create an effect template](https://support.apple.com/kb/PH16040?locale=en_US); [Motion: Publishing filter parameters](https://help.apple.com/motion/mac/5.0/help/English/en/motion/usermanual/chapter_19_section_7.html); [Larry Jordan: Use Motion to create effects for FCP](https://larryjordan.com/articles/use-apple-motion-to-create-effects-for-final-cut-pro-x/); [fcp.cafe Motion templates](https://fcp.cafe/ecosystem/motiontemplates/)
- **DIY blend-mode recipe (user, old forums):** Duplicate the clip above, add Gaussian Blur to the upper copy, and set its composite mode to **Screen** for Pro Mist or **Soft Light** for Black Pro Mist. Suggested blur is 10–15. Another poster used blur 75 + Screen at 100% opacity for a "very nice glow". — [Creative COW: Pro Mist filter](https://creativecow.net/forums/thread/pro-mist-filter-plugin/); [Creative COW: Pro Mist look in AE](https://creativecow.net/forums/thread/pro-mist-look-in-ae/)
- **FCP mechanics (verified):** Option-drag a clip above the primary storyline to duplicate it as a connected clip. — [Apple FCP guide](https://support.apple.com/en-hk/guide/final-cut-pro/ver1b0945a01/mac). Blend modes are listed in [Apple: Types of blend modes](https://support.apple.com/guide/final-cut-pro/types-of-blend-modes-ver007271c06/mac).

### Inferences: one-click "Pro Mist" in Motion (built-in only; exact values are starting points, not sourced)
1. Motion > New > **Final Cut Effect**. Set the resolution to 3840×2160 at 23.98 to match the footage.
2. **Variant A (simplest): Bloom filter.** Select the Effect Source layer > Filters > Light (or Glow) > **Bloom**. Start values: Threshold about 70–80% (only highlights bloom), Amount low, Brightness ~1.0–1.2, H and V distance equal (about 20–40 px at 4K) for round, mist-like spread, Mix 30–50%. Publish Amount, Threshold, Brightness, Horizontal, Vertical and Mix.
3. **Variant B (closer to a real Black Pro Mist, softer halo plus lowered contrast):** Group > add a **Clone Layer** of the Effect Source above it. On the clone, add Blur > **Gaussian Blur** (about 30–60 at 4K) and set Blend Mode **Screen** (white mist) or **Soft Light** / **Lighten** (black mist), Opacity 15–35%. Optional: add a **Levels** or Luma Keyer to the clone so only highlights glow, which mimics a real mist filter that affects bright sources most. Publish Blur Amount and Opacity, and rig one "Strength" slider driving both opacity and blur.
4. **Optional halation (free):** Duplicate the clone, tint it red/orange with Colorize, and use a smaller blur and Add/Screen at low opacity.
5. Save (Publish): choose a Category (e.g. "My Looks"), a Theme, and a name ("Pro Mist DIY"). It then appears in FCP's Effects browser under that category.
6. In FCP, drag it last in the stack, or include it in the saved Video Effects Preset or on an Adjustment Clip.
- **Render cost:** A Motion effect runs inside the effect pipeline on the GPU, which avoids the second decode stream of the duplicate-clip method. It should therefore be cheaper than stacking duplicate clips (inference). Large blur radii at 4K are the main cost; a smaller blur radius at lower Opacity is cheaper.
- **FCP built-in alternatives:** FCP's Effects browser may also have Bloom/Glow-type effects (the Apple search did not return a definitive FCP list; FCP 11 added a 360° Bloom transition). Search "Bloom" or "Glow" in the Effects browser to check.

### Gaps
- I did not retrieve the exact category name or path of Motion's Bloom/Glow filters in the current Motion version, or Apple's step-by-step "Create an effect template" text (the page returned only its TOC).
- No benchmark of a Motion-built bloom effect's render cost on M4.
- No source verifies a list of FCP-native Bloom or Glow effects in 12.3.

*Paid footnote (not to buy): Dehancer (bloom/halation, ~$399–699 perpetual per third parties), FilmConvert Nitrate (from $119) + Halation add-on, FilmConvert Hazy ($99), Pixel Film Studios Glow Lab, Gamut Halation ($47) — [FilmConvert](https://www.filmconvert.com/nitrate), [Newsshooter Hazy](https://www.newsshooter.com/2024/11/24/filmconvert-hazy-diffusion-plugin/), [Dehancer FCP](https://dehancer.com/shop/final_cut/halation), [Glow Lab](https://pixelfilmstudios.com/plugins/glow-lab/).*

---

## Q6. Skin softening with built-in tools

### Takeaway
Use **Auto Mask → Skin** on a soft blur, or on a Color Adjustments correction that lowers contrast and texture, all inside FCP 12.3. Feather (blur) the mask, keep the effect subtle, and watch for flicker on small or distant faces.

### Cited Findings
- **Auto Mask can be applied from the header of any colour correction *or effect*.** Masks can be blurred, shrunk or expanded and inverted (inside/outside). It works on skin, lips, eyes and teeth as separate categories, and masks can be combined. — [ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/)
- **Known artefacts:** Flicker on small or distant subjects, and the eyes mask drops out on blinks. — [ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/)
- **How-to:** [MacMost: How to use FCP Auto Mask](https://macmost.com/how-to-use-final-cut-pro-auto-mask.html)

### Inferences
- **Recipe:**
  1. Add **Gaussian Blur** (small amount, about 2–6 at 4K) and use Auto Mask → Skin.
  2. **Subtract Eyes, Eyebrows and Lips** (combine masks) so features stay sharp.
  3. Expand or feather the mask slightly, and lower the effect's Mix/opacity (if exposed) to about 30–50%.
  4. Optionally add a Color Adjustments correction with Auto Mask → Skin: slightly lower Contrast and Shadows, warm it up, and pull Super Highlights down to remove shine.
- Save it as a "Skin Soft" effects preset. On close-ups only, this is one click per clip.
- Because detection runs per frame, this is likely heavier than a plain blur. Render talking-head close-ups before playback on the Air.

### Gaps
- No measured cost of Auto Mask on base M4. It is unconfirmed whether Gaussian Blur itself offers an Auto Mask button (Anderson says "any colour correction or effect").

*Paid footnote: Digital Anarchy Beauty Box Video 6 ($199, FCP + Apple silicon, AI masks) — [Digital Anarchy](https://digitalanarchy.com/beauty-box-video/), [Digital Production](https://digitalproduction.com/2026/07/31/beauty-box-gets-premiere-ai-prompts/).*

---

## Q7. Performance on the M4 MacBook Air: H.264 4:2:2 10-bit decode, playback, proxies, export, throttling, YouTube export

### Takeaway
**There is no definitive Apple statement** on hardware decode of H.264 10-bit 4:2:2 for the media engine. The best evidence is joema's tests in the Apple Community, which were run on an M4 MacBook Air. They describe an undocumented limitation **only above 4K** (where the M4 fails outright and shows black frames). That implies 4K UHD 4:2:2 10-bit XAVC S, which is what the a6700 records, decodes normally on M4. Even so, long-GOP 4:2:2 H.264 scrubs less smoothly than intra or ProRes. On a 16 GB-or-smaller fanless Air with NR, Auto Mask and mist stacked, create **HEVC proxies (new in 12.3)** for editing and switch back to Original/Optimized for the grade and export.

### Cited Findings
- **joema (Apple Community, user, but detailed testing):** Apple Silicon's decoder "does not accelerate 10-bit 4:2:2 H.264 if over 4k resolution". The M1–M3 decoder (AVD-1) falls back to software. The M4 (AVD-2) "returns fail", which produces black frames in FCP. This was reproduced on an **M4 MacBook Air** and an M4 Pro Mac mini (Sequoia 15.5, FCP 11.1.1), with 6K footage from a DJI Mavic 4 Pro. — [Apple Community thread 256067122](https://discussions.apple.com/thread/256067122)
- **Conflicting anecdotes (user):** A base M1 user said H.264 10-bit 4:2:2 seemed to go through the CPU and was "very laggy", while H.265 4:2:2 was smooth. An M1 Pro user said playback was "absolutely fine" but scrubbing showed long-GOP sluggishness. Another user on the same thread said Apple's decoders "work well for 10-bit H.264 4:2:2" but better on HEVC. — [Blackmagic Forum](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=143682&start=0)
- **Sony A7S III 10-bit 4:2:2 choppy in FCP (older, user):** Advice was to transcode to proxy. — [FCP.co forum](https://fcp.co/forum/4-final-cut-pro-x-fcpx/34349-a7s-iii-10-bit-422-footage-choppy-playback)
- **Compressor release notes:** Compressor lists support for decoding H.264 10-bit 4:2:2 files (not stated to be hardware). — [Compressor release notes](https://support.apple.com/en-gu/102745)
- **NVIDIA comparison:** Only Blackwell (RTX 50) GPUs hardware-decode H.264 10-bit 4:2:2 on Windows. — [Adobe community](https://community.adobe.com/bug-reports-505/media-encoder-fails-to-hardware-decode-sony-xavc-s-h-264-4-2-2-10-bit-on-rtx-5070-ti-blackwell-architecture-1631045); [Puget Systems](https://www.pugetsystems.com/labs/articles/what-h-264-and-h-265-hardware-decoding-is-supported-in-premiere-pro-2120/)
- **Proxies (verified):** 12.3 generates proxies in HEVC ("accelerated on all modern Macs", according to Anderson). ProRes Proxy remains an option. — [FCP release notes](https://support.apple.com/en-us/102825); [ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/)
- **Thermal throttling:** I found no rigorous M4 Air FCP sustained-export test. One guide says a fanless Air "can settle at a lower sustained frequency" in long renders, and suggests that if a fanless Air takes about 4× clip duration on a job, sustained thermals are the bottleneck. These are rule-of-thumb sources with commercial bias. — [Kryozon (cooling vendor)](https://www.kryozon.com/blogs/cooling-hub/laptop-cooler-for-macbook-final-cut-pro-guide); [primetechsupport](https://primetechsupport.com/blogs/mac-repairs/macbook-thermal-throttling). NexraGear's "minimal throttling" claims are unsourced. — [NexraGear](https://nexragear.com/m4-thermal-performance-review/)
- **Heavy filters and responsiveness:** With skimming and background rendering on, FCP may respond slowly after a heavy filter is applied. Disable those or toggle the filter off while editing. — [Neat Video FCP known issues](https://www.neatvideo.com/support/known-issues/finalcut)

### Inferences
- **The a6700's 4K is 3840×2160, which is not above 4K**, so joema's failure case should not apply. Most likely the M4 media engine handles it, but this is unconfirmed by Apple. **Test:** play a clip in FCP with Activity Monitor open. Low CPU means hardware decode. If CPU is at 400%+, it is software decode, so use proxies.
- **Proxy workflow:** Import with "Create proxy media" (HEVC). Set the viewer to Proxy Preferred while cutting and to Optimized/Original while grading the hero frame and exporting. Optimized (ProRes 422) media is about 5–6× larger, so only use it if scrubbing original H.264 is laggy and disk space allows.
- **Export for YouTube SDR (built-in):** File > Share > Master File (or YouTube & Facebook destination) with HEVC 10-bit or H.264 at 3840×2160 and the project in Rec. 709. HEVC export uses the media engine and is fast. Exact presets and bitrates were not researched in depth, and no source verified M4 Air export times.
- **Thermal strategy:** Render NR clips in short batches. Export on a hard surface, with the lid open, plugged in. Expect long exports to slow after several minutes (fanless design; unquantified). Leave background rendering off (12.3 default).

### Gaps
- **No authoritative Apple or VideoToolbox documentation** confirms or denies hardware decode of 4K H.264 4:2:2 10-bit on M4. The evidence is user tests only.
- No measured M4 Air export times or throttling curves for FCP 12.3.
- YouTube upload settings were not researched in this pass (HEVC vs H.264, bitrate). See Apple's Share destination docs.

---

### Suggested one-click pipeline summary (inference, built from the cited facts above)
1. **Library** Wide Gamut HDR. **Project** 3840×2160, 23.98, Rec. 709 SDR.
2. **Import** with HEVC proxies. Select all clips > Info inspector > Camera LUT = **Sony s709 (custom, from Sony's free download)**. FCP auto-applies its built-in 709(800%) LUT otherwise.
3. **Grade a hero clip:** Color Adjustments (exposure, darker shadows, Super Highlights down, cool/teal mids), optional free look LUT via Custom LUT at Mix ~60%, Auto Mask Skin warm-protect, and the Motion-built "Pro Mist DIY" effect last. Save it as the "DD Base" Video Effects Preset, plus "DD Night NR" with Noise Reduction first.
4. **Select all other clips:** Paste Effects (Opt-Cmd-V) or drag the preset. For shots that drift, use Match Color with the hero frame, then trim.
5. **Render** only the NR and Auto Mask clips (Ctrl-R). Export with HEVC/H.264 Rec. 709.
