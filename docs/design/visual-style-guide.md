# Visual Style Guide for LibreOffice Impress Templates

**Purpose:** This document translates the design constitution into practical visual rules that can be applied when modernizing or creating templates in this repository.

**Scope:** Use this guide when editing `styles.xml`, `content.xml`, master pages, presentation layouts, placeholders, footers, and thumbnails.

---

# 1. Design Goal

Every template should look:

- clear;
- professional;
- modern without being trendy;
- visually intentional;
- easy to use for real presentations.

A template is successful when the user can insert content immediately and the slide already feels composed.

---

# 2. Recommended Typography System

Use the font catalog documented here:

[free-alternative-to-microsoft-fonts.md](free-alternative-to-microsoft-fonts.md)

## 2.1 General rule

Do not use many font families in a single template.

Prefer:

- one main family;
- one optional supporting family;
- one optional monospaced family only for technical layouts.

## 2.2 Good default choices

### Neutral sans-serif templates

- Source Sans Pro
- Noto Sans
- Carlito
- Liberation Sans
- IBM Plex Sans

### Editorial or formal serif templates

- Source Serif 4
- IBM Plex Serif
- Liberation Serif
- Caladea
- Gelasio

### Technical or developer-oriented templates

- JetBrains Mono
- DejaVu Sans Mono
- Hack
- Iosevka
- Fragment Mono

## 2.3 Typical usage

- Title: bold or semibold
- Subtitle: regular or medium
- Body text: regular
- Captions and footer: regular and discreet

## 2.4 Typography rules

- Avoid mixing two different expressive fonts in one template.
- Avoid decorative fonts for body text.
- Avoid very light weights for projected presentations.
- Prioritize readability over personality.

---

# 3. Color System

Each template should normally define:

- one neutral background color;
- one primary color;
- one accent color;
- one optional secondary accent.

## 3.1 Background

Preferred backgrounds:

- white;
- off-white;
- very light gray;
- very soft warm neutral;
- very soft cool neutral.

Avoid loud gradients and heavily textured backgrounds unless the template concept depends on them.

## 3.2 Text colors

Preferred body text:

- dark navy;
- charcoal;
- deep gray;
- very dark desaturated brown when justified by the theme.

Avoid medium gray body text on light backgrounds.

## 3.3 Accent colors

Accent colors should:

- direct attention;
- define sections;
- emphasize hierarchy;
- remain readable beside text.

Use saturated colors in small amounts.

---

# 4. Layout Families

Every serious template should provide clear layout roles.

At minimum, a template should have:

- cover;
- title + content;
- section divider.

If the template supports more layouts, preferred additions are:

- two columns;
- comparison;
- quote;
- closing slide;
- image-focused layout;
- timeline or process layout.

## 4.1 Cover

The cover should establish the visual identity immediately.

It may include:

- a strong title block;
- a subtitle or descriptor;
- one clear accent shape or band;
- more visual drama than inner slides.

## 4.2 Title + content

This is the most important layout in the template.

It must:

- leave enough room for real text;
- support moderate title length;
- remain visually stable with bullet lists.

## 4.3 Section divider

This layout should behave like a separator, not like a normal content slide.

Use:

- larger text;
- stronger accent color;
- fewer elements;
- generous whitespace.

---

# 5. Spacing and Composition

Use spacing deliberately.

## 5.1 Practical spacing rule

Choose a base spacing unit and repeat it consistently.

Possible systems:

- 0.3 cm
- 0.4 cm
- 0.5 cm
- Fibonacci-inspired intervals when useful

## 5.2 Margin behavior

Margins should feel stable across all layouts.

Do not let each slide invent its own left, right, top, or bottom rhythm.

## 5.3 Whitespace

When a slide feels amateur, the problem is often lack of whitespace rather than lack of decoration.

If something feels crowded:

- reduce the size of nonessential elements;
- remove unnecessary shapes;
- increase empty space before adding more styling.

---

# 6. Titles and Text Blocks

## 6.1 Titles

Titles should be:

- visually dominant;
- easy to scan;
- short enough to fit naturally;
- resilient to somewhat longer user text.

Avoid title boxes that only work with perfect demo text.

## 6.2 Body text

Body text should:

- remain comfortably readable;
- fit realistic bullet lists;
- align with the visual grid;
- avoid colliding with decorative blocks.

## 6.3 Shrink and overflow behavior

When appropriate, placeholders may use shrink-to-fit behavior.

But do not depend on aggressive shrinking to rescue poor layout decisions.

The box itself must already be well sized.

---

# 7. Placeholder Rules

Placeholders are part of the design system, not an implementation detail.

## 7.1 Required behavior

When the user:

- creates a new slide;
- duplicates a slide;
- changes the layout;
- types a long title;
- types real body content;

the template should still behave correctly.

## 7.2 Rules

- Keep placeholders aligned with the master-page definitions.
- Do not replace working placeholders with decorative text boxes.
- Do not let title, subtitle, or outline frames drift away from their intended zones.
- If a layout is centered, the placeholder behavior must also remain centered.

## 7.3 Intelligent template rule

If a template has more than one layout, every new slide created from those layouts must place text in the correct region without manual repair.

---

# 8. Decorative Elements

Decorative elements are allowed only when they improve composition.

Good examples:

- vertical accent bars;
- subtle header or footer bands;
- section panels;
- soft geometric blocks;
- thin separators.

Bad examples:

- random floating shapes;
- gradients with no structural purpose;
- shadows added only to look modern;
- busy ornaments that reduce usable content area.

## 8.1 Visibility rule

The template should not look empty.

At least one clear visual identity element should be visible:

- accent bar;
- side panel;
- title block;
- section band;
- image frame language;
- strong footer structure.

---

# 9. Footer, Date, and Slide Number

Footer elements must be present only if they improve usability.

They should be:

- discreet;
- consistent;
- aligned;
- lower contrast than the main title and content.

Avoid footers that visually compete with the slide body.

---

# 10. Thumbnail Rule

`Thumbnails/thumbnail.png` must represent the current design truthfully.

If the design changes significantly:

- regenerate the thumbnail;
- make sure the gallery preview matches the actual template.

---

# 11. ODF and Implementation Constraints

The visual style guide does not override technical constraints.

When improving a template:

- preserve master pages;
- preserve valid presentation layouts;
- preserve placeholder behavior;
- preserve ODF structure;
- preserve usability inside LibreOffice Impress.

Design quality is not valid if the template breaks when opened or used.

---

# 12. Practical Review Checklist

Before considering a template visually ready, verify:

- the cover looks intentional;
- the main content slide is readable;
- the section slide is visually distinct;
- the palette is restrained;
- typography is consistent;
- decorative elements support hierarchy;
- footers are discreet;
- new slides created from each layout still work;
- long titles still fit reasonably;
- the template thumbnail matches the final visual style.

---

# 13. What to Avoid

- overdesigned gradient-heavy backgrounds;
- fake modernity based only on shadows and glow;
- decorative fonts for core text;
- gray-on-gray low contrast text;
- layouts that only work with placeholder demo text;
- inconsistent margins between slides;
- section slides that behave like content slides;
- visual changes that break Impress placeholders.
