---
name: book-cover-prompt-generator
description: >-
  Generates strategic, market-ready book cover prompts for AI image generators
  (Midjourney, DALL-E, Imagen, etc.), delivered as a ready-to-copy-and-paste
  markdown file. Use this skill whenever the user mentions creating a book cover,
  designing a cover, generating a cover image prompt, or needs cover art for a
  novel — even if they don't explicitly ask for a "prompt." Reads genre,
  sub-genre, summary, and character details from the pipeline files. Applies the
  Type/Object/Profile/Landscape framework, picks a "forward" element
  strategically, layers in genre conventions, and produces a ready-to-paste
  prompt the user can drop into any AI image generator.
---

# Book Cover Prompt Generator

## Before You Begin

Read the following files from the active book's working directory:

- `story-config.md` — sub-genre and stacked plot archetypes
- `story-seed.md` — characters, world, conflict, and tone
- `3-act-outline.md` — themes, arc, and story scope

If any are missing, ask the user to provide the relevant story details directly before proceeding.

---

## What This Skill Is For and How to Think About It

This skill exists to turn the story that has been written — the characters, the world, the conflict, the magic system, the technology, the tone — into a detailed prompt that can be pasted into an AI image generator like Midjourney, DALL-E, Adobe Firefly, or Imagen, and get back a book cover that looks like it was designed by a professional who has spent years studying what sells in that specific corner (sub-genre) of the sci-fi and fantasy market.

The key word in that sentence is **sell**. This is not about making a cover that you personally think looks beautiful. It is not about making a cover that your writing group thinks is cool. It is about making a cover that causes a complete stranger — someone who has never heard of this book, someone who is scrolling through hundreds of book thumbnails on Amazon at 11pm — to stop, feel something in their chest, and click.

That stranger did not read the blurb first, they do not read the reviews and they just see the book cover for approximately one second, often at thumbnail size, often on a phone screen. In that one second, the book cover has to answer three questions for them without using a single word of explanation. Those three questions are:

**Question One: What genre is this?** The stranger needs to be able to look at the book cover and know immediately whether this is the kind of story they are already in the mood for. A fantasy reader knows what a fantasy cover looks like. A science fiction reader knows what a science fiction cover looks like. If the cover does not hit that recognition signal, the reader does not stop scrolling — because their brain did not file it in the right category fast enough to trigger interest.

**Question Two: What kind of story is this within that genre?** Genre is broad. "Fantasy" contains cozy fantasy about witches baking bread and grimdark fantasy about cities drowning in blood and they are completely different products sold to completely different people. The book cover needs to communicate not just the genre but the sub-genre — the specific flavor, tone, and emotional promise that the reader is looking for. A cozy fantasy reader browsing Amazon will skip past a cover that looks grimdark even if the blurb is perfect for them, because the cover told them the wrong thing.

**Question Three: Is this for me specifically?** Beyond genre and sub-genre, the best covers communicate something about the emotional experience of the book — the feeling the reader is going to have while reading it. Hopeful or devastating? Epic or intimate? Funny or terrifying? Romantic or cold? This is the hardest signal to plant and the most powerful one when it works.

If the book cover answers all three questions correctly in under one second, it is a book cover that sells.

This skill is the process for building that book cover — from the strategic decisions all the way down to the word-for-word prompt to paste into an image generator.

---

## A Critical Rule Before You Begin: Never Invent, Always Extract

This skill is designed to run after the pipeline has produced its core files. Everything this skill does — every decision it makes about color and composition and typography and mood — must be grounded in the actual story already written, not in what an AI thinks a generic fantasy novel looks like.

Before generating a single word of the prompt, gather the following from the pipeline files:

1. The **title** and the **author name** exactly as they will appear on the cover.
2. The **story summary** — not a pitch, not a tagline, but a clear description of what happens in the story: who the protagonist is, what they want, what stands in their way, and what the stakes are if they fail.
3. The **sub-genre** exactly as the user already labeled it in `story-config.md`. If the story says "epic fantasy," the sub-genre is "epic fantasy." Do not upgrade it to "dark high fantasy with political intrigue and dragon-rider elements."
4. The **tone and mood** — how does the story feel to read? Dark and brutal? Warm and whimsical? Tense and paranoid? Lyrical and melancholic?
5. The **key visual details** — any objects, settings, characters, or imagery described in the manuscript or notes as visually important to the story.
6. The **magic system or technology system** — what does power look like in the story world? What does it do to the air, the light, the bodies of people who use it? What color, texture, or behavior does it have?

Only ask the user for information that is genuinely absent from the pipeline files. Do not ask them to repeat themselves.

---

## Step #1: Competitive Shelf Analysis (Do This Before Everything Else)

This is the step that most cover design advice skips, and it is the most important step of all.

Before making a single decision about the cover — before choosing a color palette, before deciding which element goes forward, before thinking about typography — you need to know what the shelf looks like. The shelf is the collection of covers that the book will sit next to on Amazon. It is the visual competition the cover has to win against or deliberately stand apart from.

Here is how to think about it. Imagine a reader who loves epic fantasy. They open Amazon and type "epic fantasy" into the search bar. They scroll through the results. Their eyes move fast. Their brain is doing something remarkable: it is scanning all those covers simultaneously and sorting them into categories. "Seen this style before — yes." "Seen this style before — no." "This one is different — maybe." "This one looks cheap — skip." "This one looks exactly like the last five books I loved — click."

That reader's brain has been trained by hundreds of covers. It has built up a visual vocabulary for what epic fantasy looks like. When the cover appears in those results, it either speaks that vocabulary or it does not. If it does not, the reader does not know what to do with it, and so they skip it.

The competitive shelf analysis gives you that vocabulary.

**How to conduct the competitive shelf analysis:**

Ask the user to go to Amazon.com and search for their exact sub-genre label. If their book is a grimdark fantasy, they search "grimdark fantasy." If it is a LitRPG, they search "LitRPG." If it is a romantasy, they search "romantasy." They should do this search and look at the first two pages of results — the books that Amazon's algorithm considers the most relevant and successful for that search term.

Ask the user to identify five covers from those results that they feel represent the genre well — not necessarily covers they personally love, but covers that clearly look like they belong in that genre. These are the comp covers.

For each of the five comp covers, extract the following information:

**The dominant color family.** What is the single most prominent color on this cover? Is it warm (reds, oranges, golds) or cool (blues, purples, silvers)? Is it saturated or desaturated? Is it dark and heavy or light and airy?

**Which element is forward.** Is the cover leading with a character (profile-forward)? Is it leading with a landscape or world (landscape-forward)? Is it leading with a symbolic object (object-forward)? Is it leading with the typography (type-forward)?

**The render style.** Does this cover look like a painting? A photograph? A digital illustration? Does it have a realistic, painterly quality (like traditional fantasy art) or a cleaner, more graphic quality (like illustrated cozy fantasy) or a high-contrast digital render quality (like LitRPG)?

**The typography treatment.** Is the title font a serif (with small horizontal lines at the ends of the letters) or a sans-serif (clean, without those lines)? Is it tall and condensed or wide and bold? Does it have any special effects — embossing, gold foil, distressing, glowing edges? How big is the author name relative to the title?

**Any recurring motifs.** Are there specific visual elements that appear on multiple covers? In romantasy, filigree patterns and roses appear constantly. In grimdark, chains and broken weapons appear constantly. In space opera, ships and nebulae appear constantly. These recurring elements are genre signals — the visual shorthand that tells the reader what kind of story this is.

After analyzing all five comp covers, look for patterns. What do three or more of them have in common? Those common elements are the genre conventions — the things the cover must include (or must deliberately and strategically exclude) to communicate the right genre signal.

Write down:

- What is consistent across the majority of comp covers. (These are the conventions to almost certainly follow.)
- What varies across comp covers. (These are areas where there is room to differentiate.)
- What is absent from all comp covers. (These are potential white space opportunities — visual approaches that no one else on the shelf is using yet, which means they could make the cover stand out if executed well. But be careful: something absent from all comp covers might be absent for a good reason.)

This competitive shelf analysis becomes the foundation for every decision in the steps that follow.

---

## Step #2: Understanding the Four Cover Elements and What Each One Sells

Every book cover in the history of publishing is built from some combination of four fundamental elements. Understanding what each element communicates is the foundation of everything else in this skill.

### The Type Element

The type element is everything on the cover that is text: the title, the author name, any series name or tagline, and the sub-genre tag at the top of the cover. Type is technically present on every single cover, so when a cover is **Type-Forward** it means the typography itself is doing the primary visual work — that the title treatment (the size, style, color, and design of the letters) is the most visually dominant thing on the cover.

Type-Forward covers are most common in literary fiction, where the author's reputation and the cleverness of the title are the primary selling points. They are rare in sci-fi and fantasy because readers of those genres expect visual world-building from their covers — they want to see the world, the character, or the object before they commit to reading the title.

### The Object Element

The object element is a symbolic item — a single thing that represents the story's core conflict, its central power, its most important stakes, or its most iconic image. In fantasy this might be a sword, a crown, a magic artifact, a grimoire, a compass, a key. In science fiction it might be a spaceship, a weapon, a piece of alien technology, a data chip.

The object is powerful when it carries meaning all by itself. A reader who has never heard of the book should be able to look at the object on the cover and feel something — a sense of danger, of mystery, of power, of beauty.

### The Profile Element

The profile element is a character — a person, a humanoid, a creature — rendered in enough detail that the reader forms an emotional connection with them on first glance. It can be a full portrait, a three-quarter view, a silhouette, a partial face cut by the edge of the frame, or even just a pair of eyes.

**Profile-Forward** covers sell character above all else. They work best when the protagonist is genuinely the biggest hook of the story — when readers are going to fall in love with this character and follow them through however many books in the series.

One important sub-decision: how much of the face to show? A fully rendered, clearly visible face is the most intimate choice — it defines the character completely and invites the reader to bond with a specific person. A silhouette or a back-turned figure is more mysterious — it allows readers to project themselves into the character.

### The Landscape Element

The landscape element is the world — the setting, the environment, the sky, the architecture, the terrain, the atmosphere of the story's world.

There are two distinct modes of landscape-forward and they communicate completely different things:

**Landscape as World** — the setting dominates the cover and the character is either absent entirely or so abstracted (reduced to a silhouette, obscured by elements of the environment) that the world is what the reader sees. The world is the subject. The world is the promise.

**Landscape as Scale** — a character is present and visible, but deliberately tiny in relation to their environment. This composition communicates something very specific: the protagonist is a small human being facing something overwhelmingly large. The reader instantly understands that this story is about someone small trying to do something huge.

Confusing them produces covers that feel muddled — where the character is too big to read as "small" but too small to read as "present." The decision must be made explicitly and early: **Landscape-forward as Scale** or **Landscape-forward as World**.

---

## Step #3: Choose the Forward Element — The Most Important Decision

The forward element is the element that dominates the cover. It is the element that gets the most visual real estate, the most contrast, the most detail, the most light. It is the first thing the reader's eye lands on. Everything else on the cover is either supporting the forward element or staying out of its way.

Choosing the wrong forward element is the most common mistake writers make when designing their own covers. A cover that tries to show everything equally ends up communicating nothing clearly.

The forward element is chosen by answering one question: **what is the single biggest reason someone who has never heard of this book would want to read it?**

**Decision guidance by sub-genre:**

**Epic Fantasy** — landscape-forward (scale mode) or profile-forward depending on whether the story's primary hook is the scope of the world or the arc of the protagonist.

**Grimdark Fantasy** — almost always profile-forward or object-forward. A grimdark cover that leads with a beautiful landscape says "epic fantasy" to the reader, not "grimdark."

**Romantasy** — always profile-forward, no exceptions in the current market. Romantasy is selling a relationship between specific people, and the cover must communicate that specific people exist and that they are compelling to look at.

**Cozy Fantasy** — profile-forward or object-forward with a specific illustrated quality. The forward element must immediately communicate warmth and safety.

**LitRPG** — profile-forward or landscape-forward with a digital-render or anime-adjacent quality that signals the sub-genre immediately.

**Space Opera** — splits between landscape-forward (scale mode, ships or fleet in a vast cosmic environment) and profile-forward depending on whether the story's hook is the scale of the universe or the characters navigating it.

**Hard Science Fiction** — often object-forward or landscape-forward (world mode, not scale mode). Hard sci-fi that goes profile-forward risks looking like a thriller.

**Dark Fantasy (Horror-Adjacent)** — object-forward or profile-forward with heavy shadow treatment.

**Solarpunk** — landscape-forward (world mode) because the genre is fundamentally about imagining a better world, and that world is the entire point.

---

## Step #4: The Sub-Genre Visual Convention Table

Every decision about the cover — color palette, typography, render style, motifs, composition — should be checked against these conventions. If the cover departs from these conventions, that departure needs to be intentional and strategic.

---

### Epic Fantasy

**Color Palette:** Deep jewel tones — emerald, sapphire, deep violet, and burgundy — combined with aged gold, warm amber, and desaturated stone-grey for contrast. The palette should feel rich and heavy, like something valuable and old.

**Render Style:** Painterly and oil-like. Visible brush texture (or the illusion of it), soft atmospheric depth, warm luminous light sources that feel like fire, candlelight, or magic glow.

**Typography:** Tall serif fonts with slightly sharp or pointed terminals. Condensed serif typefaces are extremely common because they allow a long title to fit without crowding the art.

**Most Common Motifs:** Maps, dragons (in silhouette or partial view — a wing cutting across the composition, a claw gripping the edge), ancient crowns and swords, glowing runes or ancient script, fire and torchlight, stone architecture, cloaked figures.

**Composition:** Rule of thirds used almost universally. For profile-forward epic fantasy, the character typically faces slightly away from the reader — a three-quarter view or back view — rather than looking directly at the camera. For landscape-forward (scale mode), the character is placed at the bottom third of the composition, with the environment rising above.

---

### Grimdark Fantasy

**Color Palette:** Desaturated and heavy. Dominant colors are grey-green, charcoal, muddy brown, and deep black, broken by a single saturated accent — typically blood red, sickly yellow-green, or bone white. Even gold, if used, should look tarnished rather than gleaming.

**Render Style:** Gritty and textured, often photorealistic or photo-composite. Harder edges, more visible shadow, and texture that communicates physical reality — rust, blood, torn fabric, scarred skin, worn leather.

**Typography:** Distressed, damaged, or extremely severe. Either fonts that look worn and broken, or extremely clean, sharp, geometric fonts that read as cold and unfeeling.

**Most Common Motifs:** Broken or damaged weapons and armor, chains, skulls, wounds and scars, rain and mud, burning cities in the background, crows and ravens, impaled objects, maps that have been burned or torn.

**Composition:** Asymmetric compositions with heavy shadow in the corners and edges (vignetting). Profiles often shown from the side or three-quarter view with heavy shadow cutting across the face.

---

### Romantasy

**Color Palette:** Two dominant palettes. **Dark romantasy:** deep jewel-tone backgrounds (midnight blue, deep plum, forest black-green) combined with warm rose gold, champagne, and blush. **Soft romantasy:** blush, ivory, soft sage, and gold. Which palette depends on the tone of the romance: enemies-to-lovers with significant tension → dark palette; fated mates or slow burn → soft palette.

**Render Style:** Photo-composite (looks like models in costume composited onto a fantasy background) dominates the dark romantasy space. Illustrated romantasy (detailed digital painting, slightly stylized) is increasingly popular for softer romantasy.

**Typography:** Almost always a combination of two typefaces — a script or calligraphic font for one element of the title, and a bold display serif or small-caps for the main noun. Filigree elements are frequently incorporated. Gold or rose-gold lettering with a slight embossed or foil effect is the current standard.

**Most Common Motifs:** Flowers (particularly roses), filigree and decorative metalwork, glowing magical effects (soft warm light from hands, eyes, or objects), feathers, water and reflections, full moons, stars, candles.

**Composition:** Built around the characters. Two common two-character compositions: the "facing each other" composition (profiles facing inward, the moment just before something happens) and the "over the shoulder" composition (one character foreground facing partially away, second character visible in background or reflected light).

---

### Cozy Fantasy

**Color Palette:** Warm and earthy, with a softness that makes every color feel slightly muted. Dominant palette: amber, cream, soft terracotta, sage green, and dusty rose. Avoid cool colors and very dark shadows — they signal danger, which is the opposite of the cozy promise.

**Render Style:** Illustrated, with a hand-drawn or watercolor quality. Soft watercolor, warm digital illustration (the visual vocabulary of picture books for adults), or gouache-style illustration.

**Typography:** Rounded and friendly. Script fonts or clean rounded sans-serifs. Avoid condensed or tall serif fonts (they read as epic fantasy) and anything distressed or aggressive.

**Most Common Motifs:** Small magical creatures (foxes, cats, rabbits, birds, hedgehogs), herbs and plants, tea and food and comfort objects, books, small cozy interiors (windowsills with plants, shelves of jars and candles), lanterns and candlelight, cottage and village architecture.

**Composition:** Often centered and symmetrical, or with a strong central focal point that feels stable and grounded rather than dynamic and tense. "Frame within a frame" is common — a character viewed through a doorway or window, a scene contained within a decorative border.

---

### LitRPG

**Color Palette:** High contrast and saturated. Deep blue-black backgrounds with vivid neon accents (electric blue, bright green, glowing yellow, vivid purple). The palette communicates a digital, screen-based world.

**Render Style:** Digital render with a tendency toward anime or game-art aesthetics. The protagonist is rendered with the visual vocabulary of action RPG character design — dynamic pose, visible gear, glowing skill effects, clean and polished.

**Typography:** Bold and geometric, often with a slight technological or digital quality. All-caps titles are common.

**Most Common Motifs:** Status bars and experience point indicators, skill icons (geometric symbols for abilities, rendered in glowing light), dungeon environments, weapons and equipment rendered with visible magical enhancement, the protagonist mid-action against a monster, notification windows and floating text referencing the game system.

**Composition:** Dynamic and energetic. The protagonist is rarely standing still — they are in motion, mid-combat, or in a power stance.

---

### Space Opera

**Color Palette:** Deep cosmic: the dark black-blue-purple of deep space, punctuated by vivid stellar phenomena — nebulae in pink and gold and violet, the hot white-blue of stars, the warm glow of inhabited worlds seen from orbit.

**Render Style:** Photorealistic digital render, or high-quality concept art in the style of science fiction film production design. Cinematic scope, cinematic light, photorealistic detail.

**Typography:** Clean, geometric, and futuristic. Wide-tracking (increased spaces between letters, making the title feel expansive and cosmic). Metal and chrome effects on title type are common.

**Most Common Motifs:** Ships (the silhouette of a distinctive ship is as recognizable a genre signal as a sword in fantasy), nebulae and stellar phenomena, planets, space battles, alien architecture, figures in space suits against a vast cosmic backdrop.

**Composition:** Wide-format composition sensibility. Landscape-forward (scale mode) is common: a ship enormous against the cosmos, or a small figure at the edge of a vast alien landscape.

---

### Hard Science Fiction

**Color Palette:** Cool, restrained, and precise. Greys and whites of spacecraft interiors, cold blues of cryogenic systems or deep ocean environments, muted earth tones of a Mars surface or near-future Earth.

**Render Style:** Technical and photorealistic, referencing documentary photography, scientific illustration, or the visual language of aerospace and engineering.

**Typography:** Clean and geometric, or in the tradition of classic science fiction cover design — blocky, strong, utilitarian.

**Most Common Motifs:** Spacecraft rendered with engineering detail, space stations and orbital structures, close-up details of technology, near-future Earth environments (flooded cities, vast solar arrays, underground habitats), scientific data visualizations.

**Composition:** Centered and precise, with clean negative space that allows the primary element to be read with clarity.

---

### Dark Fantasy (Horror-Adjacent)

**Color Palette:** Black dominates. Beside black: deep blood red, sickly poisonous yellow-green, bone white, and the specific brown of old dried blood. These colors are used sparingly — the cover should be mostly black, with accent colors appearing only where they need to create maximum unease.

**Render Style:** Painterly and textured, with a quality that borders on grotesque. The detail level should be high enough that the reader can see things they would rather not have seen.

**Typography:** Either classically ornate (a beautiful, heavily-decorated serif that has been corrupted — stained, cracked, overgrown with something organic) or brutally simple (a plain, stark font that refuses decoration). The middle ground does not work for dark fantasy.

**Most Common Motifs:** Tentacles and wrong geometry, eyes appearing in places where eyes should not be, mouths and teeth as architectural or environmental elements, decay and rot, burning and smoke, fungi and organisms that imply death-as-process, figures that are wrong in some way the reader cannot immediately identify.

**Composition:** Asymmetric, with compositions that deliberately create visual unease. Heavy vignette is standard.

---

### Solarpunk

**Color Palette:** Warm, saturated greens combined with warm gold and amber. Teal and cyan appear as secondary colors representing clean water and clear sky. Solarpunk green feels alive and growing, not dark and threatening.

**Render Style:** Illustrated, referencing poster art, Art Nouveau, and contemporary environmental graphic design.

**Typography:** Art Nouveau-influenced organic type, or clean, sturdy sans-serifs in the tradition of environmental and activist communication design.

**Most Common Motifs:** Living architecture (buildings covered in growing plants, solar panels integrated with gardens, rooftop farming), community and collective action, clean energy technology shown as beautiful, animals and humans in proximity, water that is clean and flowing.

---

## Step #5: The Magic System and Technology Visual Signature

The magic system or technology system in the story has a visual signature — a specific appearance that exists only in this world. That visual signature, if incorporated into the book cover, does something nothing else can: it tells the reader not just what genre this is, but what this story's specific power system looks and feels like.

Before writing the prompt, answer these questions about the magic or technology system:

**What color is the power?** Magic almost always has a color association. What is the primary color of magic as it appears in this world?

**What does the power do to the air around it?** Does it glow? Does it distort? Does it create smoke or steam or sparks? Does it absorb light or emit it? Does it create geometric patterns (runes, lattices) or organic patterns (smoke, water, vine-growth)?

**What does the power do to the body of someone using it?** Does it mark their skin? Change their eyes? Create visible heat? Make their veins visible? Change their physical form? Leave lasting damage?

**What is the emotional quality of the power?** Is it beautiful and aspirational? Terrifying and consuming? Precise and clinical? Wild and uncontrolled?

**For technology systems:** What era of technology? Near-future? Far-future? Retro-futurism? Post-collapse (advanced but degraded, repaired, jury-rigged)?

---

## Step #6: Assemble the Specifications

Before writing a single word of the final prompt, every specification must be decided and written down. Writing the prompt while still making decisions produces muddled, contradictory prompts.

Go through this checklist and write a specific answer for every field:

**Sub-genre tag text and styling:**
- What text will appear in the sub-genre tag at the top of the cover? This text should match the exact sub-genre text from `story-config.md`. Examples: "A LITRPG ADVENTURE," "AN EPIC FANTASY," "A GRIMDARK FANTASY NOVEL," "A COZY MYSTERY," "A SPACE OPERA EPIC."
- Position: top and center aligned
- Color: pulled from the accent palette
- Size: approximately one-third the height of the title letterforms; must be visible at Amazon thumbnail scale

**Primary element description:** A precise description of exactly what the forward element is, how it sits in the composition, what it is doing, what it is wearing or made of, what emotional quality it communicates, and how it is lit. Not "a woman with long silver hair in a dark cloak." A sufficient description says: where on the cover she is positioned (which third, which side), how much of her is visible (full body, waist up, face only), what direction she faces, what her physical posture communicates, what specific details of her appearance carry the magic system's visual signature, and how the light hits her.

**Secondary element description:** Same level of precision. How large relative to the primary? Where does it sit? How does it support the primary without competing (softer focus, lower contrast, less detailed, darker)?

**Color palette:** Specific named colors, not generic descriptions. Not "blue and gold" — "deep cobalt fading to near-black at the edges, with warm amber-gold concentrated at the center where the light source is, and a single saturated turquoise accent for the magic effect."

**Mood and atmosphere:** Three to five specific phrases capturing the exact emotional quality the cover should produce. Not "dark and mysterious" — "the feeling of discovering something that was not meant to be found."

**Typography specification:** The exact style of the title font, the style of the author name font, relative sizes, colors, and any effects (gold foil, embossing, glow, distress).

**Render style:** A precise description cross-referenced against the sub-genre convention table from Step Four.

**Composition map:** A description of where everything is. Think of the cover divided into thirds both horizontally and vertically — nine zones. Which zone(s) does the primary element occupy? The secondary element? The title? The author name?

**Texture and finish:** What is the physical quality of the surface? Paper grain? Matte or glossy? Embossed elements? Hand-painted texture?

---

## Step #7: Write the Final Prompt

Every decision from Steps #1 through #6 is assembled into the final prompt. The prompt is written for the image generator, not for a human reader — it needs to be specific, visual, and unambiguous. Use exactly this format:

---

```markdown
**Create a book cover that is [PRIMARY ELEMENT]-Forward, with secondary emphasis on [SECONDARY ELEMENT]. The cover must communicate [THE CORE INTUITIVE READ — one sentence describing what the reader feels in the first second] within one second of being seen at thumbnail scale.**

[STRATEGIC PARAGRAPH: Three sentences maximum. Sentence one explains why the forward element was chosen and what it communicates about the story. Sentence two explains how the secondary element supports the forward element without competing with it. Sentence three states the genre signal the cover must hit and the emotional register it must land in.]

---

**Sub-Genre Tag — Top of Cover Banner:**

Exact text: "[SUBGENRE LABEL IN ALL CAPS]"
Position: Top of cover, horizontally centered.
Size: Approximately one-third the cap height of the title typeface. Must be fully legible at Amazon thumbnail size (~160px wide).
Typeface treatment: [SPECIFIC FONT STYLE]
Color: [SPECIFIC COLOR pulled from the cover's accent palette]
Tone: [HOW IT SHOULD FEEL]

---

**Primary Element — [TYPE/OBJECT/PROFILE/LANDSCAPE] (~[PERCENTAGE]%):**

[COMPLETE PRECISE DESCRIPTION. What it is. Exactly where it sits in the composition (use thirds: upper left, center right, lower center, etc.). How large it is relative to the total cover area. What physical state it is in. What direction it faces. What it is doing. How it is lit — where the light comes from, what color the light is, how it falls on the element. What specific details communicate the story's magic system or technology aesthetic. What emotional quality the element communicates.]

---

**Secondary Element — [TYPE/OBJECT/PROFILE/LANDSCAPE] (~[PERCENTAGE]%):**

[COMPLETE PRECISE DESCRIPTION. What it is. Where it sits relative to the primary element. How it is visually subordinated — softer in focus, lower in contrast, darker in tone, smaller in scale, more atmospheric. What details are visible and what details are deliberately softened or obscured.]

---

**Magic System / Technology Visual Signature:**

[DESCRIPTION OF HOW THE STORY'S SPECIFIC POWER SYSTEM APPEARS VISUALLY ON THE COVER. What color is the power. What physical behavior does it have — does it glow, flow, crystallize, distort, consume, ignite? Where on the cover is it visible? What texture does it have at close range? What emotional quality should its visual appearance communicate?]

---

**Color Palette:**

Primary color family: [SPECIFIC NAME AND HEX OR DESCRIPTIVE EQUIVALENT]
Secondary color family: [SPECIFIC NAME AND HEX OR DESCRIPTIVE EQUIVALENT]
Accent color: [SPECIFIC NAME AND HEX — the single most saturated, concentrated color on the cover]
Tonal direction: [Predominantly warm or cool? Where is the lightest point? Where is the darkest point? Does it transition from warm to cool?]
Colors to explicitly avoid: [Any specific colors that would signal the wrong sub-genre, wrong tone, or wrong era]

---

**Mood and Atmosphere:**

[FIVE SPECIFIC PHRASES describing the exact emotional experience the cover should produce. Each phrase should be specific enough that it could not apply to any other book — not "dark and atmospheric" but "the specific dread of knowing what is about to happen and being unable to stop it."]

---

**Typography:**

Title typeface: [EXACT STYLE DESCRIPTION — serif or sans-serif, condensed or expanded, traditional or modern, any special treatment]
Title size: [Dominant — occupying approximately what percentage of the cover width?]
Title color and finish: [Specific color, any effects such as foil simulation, embossing, glow, distress]
Title position: [Upper third / lower third / centered / aligned to the left]
Author name typeface: [Same as title or complementary secondary font]
Author name size: [Relative to title — debut author typically at 1/3 to 1/4 the title size]
Author name position: [Below the title / above the title / at the bottom of the cover]
Author name color: [Typically same as the title or in the accent color]
Series name (if applicable): [Position, size relative to title, typeface, color]

---

**Genre Cues:**

[A DETAILED LIST OF SPECIFIC MOTIFS that will communicate the sub-genre signal to a reader scanning at thumbnail scale. Each motif described precisely enough that it could be illustrated: not "fantasy elements" but "the faint outline of a dragon's wing cutting across the upper right corner, visible only in silhouette against the sky." Include at least four to six specific motifs from the sub-genre convention table in Step Four.]

---

**Composition:**

[A PRECISE SPATIAL DESCRIPTION of where every element lives on the cover. Use the nine-zone grid (upper left / upper center / upper right / middle left / center / middle right / lower left / lower center / lower right) to specify every major element's location. Describe the sight lines — where does the eye enter the cover and where does it travel? Where is negative space used deliberately? Is the composition balanced and stable, or dynamic and slightly unstable?]

---

**Texture and Finish:**

[SPECIFIC MATERIAL QUALITY. What does this cover feel like if you could touch it? Is there visible paper grain, brush texture, painted surface, photographic sharpness, digital precision, or hand-drawn line quality? How does the texture affect the reading of the primary element versus the secondary element?]

---

**Output Specifications:**

Dimensions: 1,600 px (width) × 2,500 px (height)
Format: JPG
Quality: 4K high quality, minimal compression — optimized for Amazon KDP
```

---

## Self-Check Gate — Run Every Question Before Delivering the Prompt

Do not deliver the prompt until every question in this gate can be answered with a confident yes. If any question produces a no or an "I'm not sure," revise the relevant section before delivering.

- Did the competitive shelf analysis happen, and are the cover's decisions visibly grounded in what the comp covers said about genre conventions? If no, go back to Step One.
- Were the genre label, sub-genre label, story summary, character descriptions, and world details pulled from the pipeline files rather than invented? If any detail was invented — any character physical attribute, any world-building element, any magic system description — remove it and replace it with a question to the user.
- Is the sub-genre tag present at the very top of the cover, specified with exact text, exact position, exact size relative to the title, exact color pulled from the cover palette, and a clear tonal description? If not, add it.
- Does the primary element specification contain enough precision that an AI image generator could render it without ambiguity? "A woman in a cloak" is not precise enough. A precise description says where on the cover she is positioned (which third, which side), how much of her is visible, what direction she faces, what her posture communicates, what details carry the magic system's visual signature, and how the light hits her.
- Is the secondary element visually subordinated to the primary in the prompt language?
- Is the magic system or technology visual signature explicitly present in the prompt, appearing on at least one of the specified elements?
- Does the color palette include specific named colors with enough precision that an AI could interpret them — not "blue" but "deep cobalt fading to near-black at the edges"?
- Does the typography specification match the sub-genre convention table from Step Four?
- Does the render style match the sub-genre convention table from Step Four?
- If the title and author name were removed from the cover, would the visual elements alone still communicate the correct sub-genre to a genre-fluent reader? If no, the primary element, secondary element, motifs, and palette are not doing their job and need revision.

---

## Output

Write the completed prompt to: `[title-folder]/book-cover-prompt.md`.

**Finding the title folder:** Read `book-title.md` at the book root, extract the `Final Title:` value, sanitize it (replace `:` with ` -`, remove `< > " / \ | ? *`). The title folder was created by Step 6.

The file should contain only the final formatted prompt — no planning notes, no skill commentary, no intermediate decisions. The user should be able to open the file and paste the prompt directly into their image generator of choice.

The next step is to paste the prompt into Midjourney, DALL-E, Adobe Firefly, Imagen, or any preferred AI image generation tool.

---

## Agentic Handoff

When invoked by the orchestrator (`/ai-publishing-house`) in auto-chain mode, after the cover prompt file is written end with the exact line:

> **Step 11 complete. Output: `[book-folder]/[sanitized-title]/book-cover-prompt.md`**

The orchestrator will then run `pipeline_validator.py --step 11` and report that the pipeline is complete. This is the terminal step — no further skills follow. When invoked manually by the user, end as described above.
