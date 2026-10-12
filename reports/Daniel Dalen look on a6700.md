# Shoot bright, grade dark: Dalen's look on a6700

Daniel Dalen's look comes from simple choices you can copy. He uses two Sony cameras with fixed jobs, keeps the lens near a natural wide angle, sometimes uses a mist filter, publishes at 24 frames per second, and adds a bought-in colour look in the edit. He does not have a hidden colourist. You can get most of the way there with what you own. Shoot your normal S-Log3 settings with one change: brighten the picture at night with the exposure dial, because the dark mood gets added later on the Mac. Then use two things that get built once on the Mac: a grade preset you drag onto clips, and a "Pro Mist" glow effect made in Motion. Your C0051 clip went wrong for two reasons, and both are now fixed. It was recorded about 2 stops too dark because Auto ISO stopped at about 2500. On top of that, Final Cut Pro turned the flat footage into colour with Sony's harsh "709(800)" recipe rather than the softer "s709" recipe your camera may show on its screen. Two other corrections to the brief: Dalen is Dutch, not Norwegian, and he lives in Hong Kong, not Thailand.

**How to read the labels:** **V** means verified from a source. **I** means our best judgement, not tested. Plain-word meanings for each term are given the first time it appears.

## What to do: one camera card, one Mac setup, one drag routine

### Camera settings card (set once, then leave it)

S-Log3 is the flat, grey-looking recording mode. It keeps the most detail, and the colour gets added on the Mac.

| Setting | Set to | Why, in plain words | |
|---|---|---|---|
| Recording | XAVC S 4K, 24p, 100M 4:2:2 10-bit | Keep. Dalen mostly publishes at 24 frames per second | V |
| Log mode | Log Shooting Setting: On (Flexible ISO), S-Gamut3.Cine | Keep. This is the a6700's proper S-Log3 mode | V |
| Aperture | f/2.8 | Keep. This lets in the most light | V |
| Shutter | 1/50 | Keep. It stops flicker from Egypt's mains lights. Only exception: on a tripod with nobody moving fast, 1/25 gives double the light | I |
| ISO | Auto, min 800, max 6400 | Keep. ISO is the camera's brightness boost. 2500 to 6400 is the clean high range on this sensor | V |
| Exposure dial (+/- comp) | **Night and indoors: +0.7. Daylight: 0** | This nudges the picture brighter. A brighter recording means less grain once it's darkened on the Mac | I |
| White balance | Fixed, not auto. Daylight 5600K. Warm indoor lamps 3200K. Night streets 4300K | Auto white balance shifts colour mid-shot under mixed street lights | I |
| Screen view | Display LUT: On. Select LUT: **s709** | The screen then shows the same colour recipe the Mac will use | V/I |
| Zebras (warning stripes) | On, level 100+ | Stripes on lamps and signs are fine. Stripes on faces are not | I |
| Filters | ND in daylight only. **Take every filter off at night** | ND works like sunglasses for the lens. At night, extra glass makes green and orange ghost blobs from lamps | V/I |
| Zoom | Stay near 18mm | This is close to Dalen's "natural" 24mm look | I |
| SteadyShot | Standard when handheld. Off on a tripod | Standard keeps the full wide view | V |
| Heat | Auto Power OFF Temp: High. Flip the screen out. Wi-Fi and Bluetooth off | This keeps the camera running in Cairo heat | V |
| Focus | Face/Eye AF on | The camera follows faces | I |

**One rule to remember:** if the ISO number blinks, the camera has run out of range. In daylight, add ND. At night, move the person closer to a light, or turn their face toward it. Never darken the shot in camera to make it "moody". The mood is added on the Mac.

### One-time Mac setup (for the assistant, about 90 minutes)

This builds three items in Final Cut Pro's Effects list: **DD Grade Day**, **DD Grade Night** and **Pro Mist**. After that, Jim only drags.

**A. Get the free colour files**

1. Go to [sony-cinematography.com/resources/luts](https://sony-cinematography.com/resources/luts/), fill in the form, and download **"Slog3-S-Gamut3.Cine To s709 V200.cube"**. A LUT is a colour recipe file that turns flat footage into normal colour. Put it in a folder called Documents/Jim LUTs. (V: the file exists. The download sits behind a form, and we could not confirm it is free.)
2. Optional film look: copy **"Kodak 5218 Kodak 2383 (by Adobe).cube"** out of the Premiere Pro app into the same folder. It usually sits inside the app: right-click Premiere Pro > Show Package Contents > Contents > Lumetri > LUTs > Creative. If it isn't there, run `find /Applications -name "*2383*.cube"` in Terminal. (I: the location and the input format are not confirmed.)

**B. Library and project**

3. Create a new library. In the library inspector, set Color Processing to **Wide Gamut HDR**. Create a new project with custom settings: **3840x2160, 23.98p, Rec. 709**. When importing, tick **Create proxy media**. A proxy is a lighter copy of the clip that keeps editing smooth on the Air, and FCP 12.3 makes these as HEVC. Leave background rendering off, which is already the 12.3 default ([Apple release notes](https://support.apple.com/en-us/102825)).

**C. Load the s709 file**

4. Import any a6700 clip and select it. Press Cmd-4 and open the **Info** tab. Set the metadata view to Settings. Open the **Camera LUT** pop-up and choose **Add Custom Camera LUT**. Pick the s709 .cube, set Output Color Space to **Rec. 709**, then click Open. "s709" now appears under Custom Camera in that pop-up ([Apple: Apply LUTs](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac)).

**D. Build "DD Grade Day"**

5. Choose a normal daylight clip with a face. Set its Camera LUT to s709.
6. In the Effects browser, go to Color and drag **Color Adjustments** onto the clip. Enter these starting values. They come from our reading of Dalen's footage and are not tested (I):

| Slider | Value | What it does |
|---|---|---|
| Exposure | 0 | Leave it. Change it only on a clip that is clearly too dark |
| Contrast | +10 | A little more punch |
| Black Point | -3 | Deep blacks that aren't crushed flat |
| Shadows | -10 | A darker, moodier lower half |
| Highlights | -10 | Calmer bright areas |
| Super Highlights | -25 | Soft, film-like fade on the brightest parts |
| Saturation | +5 | Slightly richer colour |
| Shadows Warmth | -15 | Cool, teal-leaning shadows |
| Mids Warmth | -5 | Slight cool in the middle. Set to 0 if skin looks grey |
| Highlights Warmth | +15 | Warm lamps and bright areas |

7. Optional: drag on **Custom LUT** (Effects > Color). Choose the Adobe 2383 file and set Input to Rec. 709, Output to Rec. 709, Mix to **30%**. Mix is the strength. If faces turn green or the picture goes very dark, delete this step.
8. Search the Effects browser for **Vignette** and drag it on. Use a large, soft shape at low strength. The target is corners about 20% darker than the middle, which is what Dalen's footage measured. A starting Amount of about 0.3 is a guess (I).
9. Put a screenshot from Dalen's video next to the viewer. If the overall brightness is far off, change only Exposure.
10. In the Video inspector, click **Save Effects Preset**. Name it **DD Grade Day**, set the category to **Jim Looks**, include all effects, and save. It now sits in the Effects browser like any built-in effect ([Apple: Save video effects presets](https://support.apple.com/guide/final-cut-pro/save-video-effects-presets-ver462c2078f/mac)).

**E. Build "DD Grade Night"**

11. Choose a night clip. Double-click DD Grade Day to apply it. Then drag on **Noise Reduction**, which reduces grainy speckles. In the Video inspector, drag Noise Reduction to the **top** of the effects list, because Apple says it works best first. Set Amount to **Medium** and Sharpness to **Low** ([Apple: reduce video noise](https://support.apple.com/en-my/guide/final-cut-pro/ver7d031487b/mac)). Save it as a preset called **DD Grade Night** in Jim Looks.

**F. Build "Pro Mist" in Motion**

A Pro Mist filter makes lamps and bright areas glow softly. This builds a free version of it.

12. Open Motion. In the Project Browser, choose **Final Cut Effect**. Set the size to 3840x2160 and the frame rate to 23.98, then click Open.
13. In the Layers list, select **Effect Source**. Add a filter: Filters > Glow (or Light) > **Bloom**. Bloom blurs and brightens only the parts above a brightness level, then lays them back over the picture ([Apple Motion: Bloom](https://support.apple.com/guide/motion/bloom-filter-motn169fae47/mac)).
14. Enter these starting values (I): Threshold **75%** (only bright things glow), Brightness **1.1**, Horizontal **30**, Vertical **30** (the same number gives a round glow), Amount **10**, Mix **40%**.
15. Click the small arrow next to **Mix** and choose **Publish**. Do the same for **Threshold**. Publishing puts the slider into Final Cut Pro, so the assistant can adjust it later. In the project's Publishing list, rename Mix to "Strength" ([Apple: Create an effect template](https://support.apple.com/kb/PH16040?locale=en_US)).
16. Use File > Save. Name it **Pro Mist**, set the category to **Jim Looks**, and save. Quit Motion.
17. Check it in Final Cut Pro on a night street clip. Lamps should get a soft halo and faces should stay sharp. If lamps turn into big white blobs, reopen the effect in Motion, set Mix to 25%, and save again. Jim never touches it after that.

### The drag routine (Jim, every day, about 5 minutes)

1. Import the card, with proxies on.
2. In the browser, press Cmd-A, then Cmd-4, open the Info tab, and set Camera LUT to **s709**. This puts the correct colour recipe on every clip at once.
3. Edit as normal.
4. In the timeline, select the day clips and double-click **DD Grade Day**. Select the night clips and double-click **DD Grade Night**. Dragging works too ([Apple: Save color correction presets](https://support.apple.com/guide/final-cut-pro/save-color-correction-presets-verbbd35f70/mac)).
5. Select the clips you want to glow and double-click **Pro Mist**.
6. Select the night clips and press Ctrl-R to render them before playback. Noise Reduction is heavy work for the Air.
7. Export with File > Share > YouTube & Facebook (or Master File), 4K, Rec. 709.

Never put two log-to-colour recipes on one clip. If someone adds an S-Log3 .cube as an effect **and** leaves the Camera LUT on, the picture goes crushed and over-coloured (I).

## Dalen is a Dutch, Hong Kong-based founder who films with two Sonys

**Who he is (V).** Dalen was born in the Netherlands and grew up in Europe and China. He is based in **Hong Kong** and works a lot in mainland China and Dubai. He runs the fulfilment company Ecomflow and the eyewear brand LENSE ([The Chow](https://www.thechow.net/p/post-manosphere-daniel-dalen-art-of-mondays); [301 Podcast](https://the301podcast.podbean.com/e/daniel-dalen-every-mentor-has-a-mentor/); [danieldalen.com](https://www.danieldalen.com/)). In his September 2026 live podcast he describes growing up in "a small Dutch to[wn]" ([YouTube](https://www.youtube.com/watch?v=FfeAr4pgGmM)). No source ties him to Norway or Thailand.

**Cameras and lenses (V).** Both of his gear videos name the same two-camera Sony system. For wide "talking to you" shots he uses a **Sony FX30 with a Sony E 11mm f/1.8**. For "documentation" shots he uses a full-frame Sony with the **FE 24-70mm f/2.8 GM**. That was an **A7S III** in 2024, owned by his crew member Wojtek, and an **FX3** by 2026 ([2024 gear video](https://www.youtube.com/watch?v=CTkma5c0qCo); [2026 gear video](https://www.youtube.com/watch?v=bK6283rQ7c0)). He says the 24mm end "creates the most natural real-life look". He also mixes in VHS camcorder clips, a DJI Osmo Pocket 3 and iPhone shots. His Instagram's vintage stills come from 35mm film point-and-shoots, not from video.

| Dalen's job for each camera | His gear | Your nearest match | |
|---|---|---|---|
| Documentation (main look) | FX3 + 24-70 GM at about 24mm | a6700 + Sigma at 18mm (about 27mm full-frame view) | I |
| Wide talking head | FX30 + 11mm (about 16.5mm full-frame view) | Sigma at 18mm, standing further back. You can't go as wide without buying a lens | I |
| Static "same spot, different time" shots | Camera clamped to furniture or a car | a6700 on a tripod, SteadyShot off | V/I |

**Filters (V).** In 2024 he showed a **mist filter**, recommended by a friend, which "adds a super soft kind of glare to the light". The brand and strength were never stated. The crew uses **ND filters** in sun so they can keep the lens wide open. In 2026 he mentions buying "some ND filters" ([2024 video](https://www.youtube.com/watch?v=CTkma5c0qCo); [2026 video](https://www.youtube.com/watch?v=bK6283rQ7c0)). Your Motion "Pro Mist" stands in for the mist filter. Your ND filters do the same job as his.

**Crew (V).** Dalen says, "I've always edited my own videos", and that he filmed many shots himself ([Amsterdam podcast](https://www.youtube.com/watch?v=FfeAr4pgGmM)). His camera operators have changed over time: an unnamed American early on, **Wojtek** (also his Head of Growth) in 2024, and **Valentine**, a new creative director from the Netherlands, in 2026. None of the roughly 37 video descriptions checked credits an editor or colourist.

**Grading and LUTs (V, with limits).** Dalen has never named his editing software or his recording profile. His one statement on colour is a testimonial for **Cinegrams**, a pack of ready-made LUTs, grain and film burns. He says it made his videos "look very professional, especially when it comes to color grading" ([Cinegrams Academy](https://cinegrams.com/pages/academy)). Cinegrams later sold "Vlogger Signature" LUTs "inspired by creators like Daniel Dalen". These are a house look, not Dalen's own ([Cinegrams](https://cinegrams.com/products/vlogger-luts)). A free fan pack, "Daniel Dalen Colorgrade", exists for Premiere and describes the look as soft highlights, orange and teal, plus a Pro Mist effect. It is not endorsed by him ([Eleven Percent](https://elevenpercent.net/products/daniel-dalen-colorgrade-lut-presets-for-premiere-pro)). The fair reading (I) is that he drops a bought look onto Sony footage and does not grade by hand much. In his own words, "I just use what feels good."

**Frame rate (I, from YouTube's file data).** Of 10 uploads checked, **7 are 24 fps**, 2 are 25 fps and 1 is 30 fps. All were 4K ([example](https://www.youtube.com/watch?v=Iyp3Vff1VNw)). No source states his shutter speed. Your 24p at 1/50 matches.

**What the look measures as (Jim's own earlier measurement of "Two Really Chaotic Weeks", minutes 7 to 12).** Blacks sit at about 1.8% (deep but not crushed). The middle of the picture sits low, at about 22% brightness, which is moody. Highlights stop at about 81%, so there are no harsh whites. Corners are about 20% darker than the centre. Shadows lean teal and highlights lean warm, with no added grain. The preset values above aim at exactly this. One outside writer calls his look "grainy", but the clip we measured had none ([The Chow](https://www.thechow.net/p/post-manosphere-daniel-dalen-art-of-mondays)).

## C0051 failed twice: too dark in camera, wrong recipe on the Mac

**Problem 1: the camera ran out of ISO.** With Auto ISO capped near 2500 in a dim room, the camera hit its limit and recorded about **2 stops too dark**. One stop means half the light, so 2 stops is a quarter. On the a6700, about 3 stops too dark is where grain starts to show after brightening ([CineD lab test](https://cined.com/sony-a6700-lab-test-rolling-shutter-dynamic-range-and-latitude/)). The sensor has two clean starting points, ISO 800 and ISO 2500, with almost the same quality at each (11.2 vs 11.1 stops of range, per CineD). Reviewers saw a "sudden drop in noise" going from ISO 2000 to 2500, and call the image "very clean" up to about 6400 ([Pro Moviemaker](https://online.bright-publishing.com/view/639798169/56/)). Your new 6400 cap lets the camera reach a proper exposure. A bright recording at ISO 6400 beats a dark recording at ISO 2500 that gets brightened later (I). Sony itself says S-Log3 noise "may be improved by shooting with a brighter setting" ([Sony a6700 Help Guide](https://helpguide.sony.net/ilc/2320/v1/en/contents/0412D_picture_profile.html)).

**Why +0.7 on the dial.** The exposure dial works in your mode (manual, with Auto ISO) and goes from -2 to +2 ([Sony Help Guide](https://helpguide.sony.net/ilc/2320/v1/en/contents/0406B_exposure_compensation.html)). At night the camera averages a frame full of black street and sky, and it gets fooled. Sony's own exposure guide says it is "generally better to be a little bit brighter rather than a bit too dark" with S-Log3 faces ([Sony Cinematography](https://sony-cinematography.com/articles/how-correctly-expose-s-log3-a7s-iii-fx3-fx6-fx9/)). Keep it at +1.0 or below, or street lamps will blow out sooner (I).

**Problem 2: the Mac used a different colour recipe.** Final Cut Pro sees Sony S-Log3 and automatically applies its built-in Sony recipe. Apple states that this is **"709(800%)"** tone mapping ([Apple](https://support.apple.com/guide/final-cut-pro/apply-luts-ver24f966423/mac)). Sony calls 709(800) high contrast with "vivid colors", while **s709** is "a softer low-contrast tone curve" that is "close to the characteristics of film" ([Sony Cinematography](https://sony-cinematography.com/articles/sony-s709-lut-overview-and-breakdown/)). The a6700 can show s709, 709(800%) or user LUTs on its screen ([Sony Help Guide: Select LUT](https://helpguide.sony.net/ilc/2320/v1/en/contents/211h_select_lut.html)). If your screen was on s709, the Mac was always going to look harsher than what you saw. Setting both the camera screen and the Mac to s709 makes them match (I: the reasoning is solid, but we have not compared them side by side).

## Night in Cairo: light the face, let the lamps burn

**Faces first.** Put people where a shop window, café light, lamp or phone lights their face from the side. Let the background fall into darkness. Turning someone 45 degrees toward a light can be worth more than a full stop of ISO (I). This gives Dalen's "dark room, lit face" contrast without grain, because the light is real.

**Let lamps clip.** Bare bulbs, neon and headlights will turn pure white at any setting that's right for faces. That's normal and looks cinematic, and the Pro Mist glow softens it. What must not go white is skin or a big lit wall (I).

**Flicker.** Egypt runs on 50 Hz mains power, which is general knowledge and not from our sources. For 50 Hz lights, 1/50 and 1/25 avoid flicker, while 1/30 and 1/60 do not ([Nikon manual](https://onlinemanual.nikonimglib.com/z9/en/vrm_video_flicker_reduction_148.html)). Some cheap LED signs flicker at any shutter speed ([Playtech](https://playtech.ro/2025/cum-eviti-efectele-de-rolling-shutter-si-flicker-atunci-cand-filmezi-in-lumina-led-sau-neon/)). If a sign stripes on screen, reframe.

**1/25 for still shots only.** 1/25 doubles the light but smears anything that moves. Use it only on a tripod for interviews or empty rooms. Go back to 1/50 for walking shots (I; [EOSHD forum](https://www.eoshd.com/comments/topic/45201-i-really-like-the-look-of-360-degree-shutter-anyone-else/)). We could not confirm that the a6700 offers exactly 1/25 at 24p. If it doesn't, skip this.

**Heat.** At 4K 24p the a6700 ran 2 hours 10 minutes at about 23°C in a controlled test ([4K Shooters](https://www.4kshooters.net/2023/11/14/how-to-fix-overheating-on-the-sony-a6700-and-zv-e1/)). Sony's harder 4K 60p test gives about 30 minutes at 25°C and about 10 minutes at 40°C, with the heat limit set to High ([Sony Help Guide](https://helpguide.sony.net/ilc/2320/v1/en/contents/0601L_auto_power_off_temperature.html)). Keep the camera in shade between takes. Sony warns that with High set, the body can get hot enough to burn a hand, so hold it by the grip or strap.

## Mac details the assistant should know

**Speed on the M4 Air.** The a6700's 4K files are not above 4K, so the known M4 failure with 6K files of this type should not apply ([Apple Community test](https://discussions.apple.com/thread/256067122)). This is inferred and not confirmed by Apple. Proxies keep scrubbing smooth either way. Render only the night clips, because Noise Reduction is the heavy part.

**If a clip still drifts.** FCP 12.3's improved **Match Color** creates an adjustable correction that copies a reference frame. The assistant can match a stray clip to a good one in two clicks ([ProVideo Coalition](https://www.provideocoalition.com/surprise-its-final-cut-pro-12-3/)). For old underexposed clips like C0051, raise Exposure on that clip only.

**Mist fallback.** If Bloom looks too much like a glow and not enough like a mist, rebuild Pro Mist this way. Add a clone of Effect Source, give it Gaussian Blur at about 40, set its blend mode to Screen at 20% opacity, and publish Opacity (I; recipe from [Creative COW](https://creativecow.net/forums/thread/pro-mist-filter-plugin/)).

**Alternative free base.** Sony's free Picture Shop "Look 1" LUT is more film-like than s709, with reds and highlights pulled down ([TV Technology](https://tvtechnology.com/news/sony-picture-shop-team-up-on-new-luts)). It would not match the camera screen, though, so s709 stays the default.

**Skip:** S-Cinetone, double LUTs, auto white balance, and darkening the shot in camera.

## Conclusion

The surprise is how little of Dalen's look is secret. It isn't a special camera or a colourist. It comes from fixed lens habits, real light on faces, a 24p timeline, a soft glow, and a ready-made colour pack. That means the gap between him and you is mostly about process, not gear. Your one real weakness was night exposure, and it came from the camera settings, not the camera. Recording brighter and darkening on the Mac fixes it. Matching the camera screen and the Mac with s709 means what you see in Cairo is what you get in the edit.

The biggest risk now is the untested starting values in the preset and the Motion glow. Have the assistant tune them once on your existing clips, C0051 included, before you fly. Once that's done, you only drag.

*Footnote, paid options, not needed: a physical Black Pro-Mist 1/8 filter, Cinegrams Vlogger LUTs ($19.99), Neat Video noise reduction, and a Sony E 11mm f/1.8 for Dalen's ultra-wide view.*
