---
name: CommsAlign
description: A facilitator’s worksheet for workplace communication
colors:
  navy: "#17365d"
  teal: "#216b68"
  mark-teal: "#216b68"
  navy-hover: "#244d7a"
  ink: "#172d45"
  muted: "#4b6171"
  paper: "#f7f6f0"
  sheet: "#fffefa"
  wash: "#e8efea"
  review: "#edf2ec"
  rule: "#c9d2ca"
  field-border: "#83958a"
  focus: "#007975"
  white: "#ffffff"
  warning: "#6f3e17"
  warning-paper: "#f9edda"
  warning-border: "#dbc09f"
typography:
  display:
    fontFamily: "Georgia, serif"
    fontSize: "clamp(2.65rem, 5.5vw, 5rem)"
    fontWeight: 500
    lineHeight: 1.04
    letterSpacing: "-.035em"
  tool-display:
    fontFamily: "Georgia, serif"
    fontSize: "clamp(2.5rem, 5vw, 4rem)"
    fontWeight: 500
    lineHeight: 1.04
    letterSpacing: "-.035em"
  headline:
    fontFamily: "Georgia, serif"
    fontSize: "clamp(1.6rem, 2.6vw, 2.1rem)"
    fontWeight: 500
    lineHeight: 1.18
  title:
    fontFamily: "Segoe UI, sans-serif"
    fontSize: "1.1rem"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: "Segoe UI, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Segoe UI, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 700
    lineHeight: 1.55
rounded:
  control: ".35rem"
  sheet: ".8rem"
spacing:
  worksheet-gap: "1.2rem"
  gutter: "1.5rem"
  compact-gutter: "1rem"
components:
  button-primary:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.white}"
    rounded: "{rounded.control}"
    padding: ".55rem 1rem"
  button-primary-hover:
    backgroundColor: "{colors.navy-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.navy}"
    rounded: "{rounded.control}"
    padding: ".55rem 1rem"
  button-secondary-hover:
    backgroundColor: "{colors.wash}"
  field:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: ".55rem .7rem"
  sheet:
    backgroundColor: "{colors.sheet}"
    rounded: "{rounded.sheet}"
    padding: "clamp(1.1rem, 3vw, 2rem)"
  review-sheet:
    backgroundColor: "{colors.review}"
    rounded: "{rounded.sheet}"
    padding: "clamp(1.1rem, 3vw, 2rem)"
  signal-current:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.white}"
    rounded: "{rounded.control}"
    padding: ".35rem .6rem"
---

# CommsAlign Design System

## Overview

**Creative North Star**
The facilitator’s worksheet

CommsAlign takes its cues from a facilitator’s worksheet. Warm paper, navy ink, and ruled sections make the tools feel like material someone could bring to a discussion. Teal guides attention to evidence, links, and current selections.

The layout keeps related material close. Drafts sit beside reviews, and survey findings sit beside discussion prompts. Serif headings mark the sections while the sans-serif body supports longer reading, labeling, and data entry.

- Warm paper surfaces and a navy and teal CA monogram.
- Related inputs and evidence in adjacent sheets.
- Ruled rows for tools, findings, and survey profiles.

## Colors

### Primary

- Identity navy anchors the CA mark, wordmark, and primary buttons. A lighter navy indicates primary-button hover.

### Secondary

- Worksheet teal marks the A in the monogram, links, labels, current navigation, selected signals, and meter fills.
- Focus teal provides the shared keyboard outline.

### Tertiary

- The warm warning palette gives warning text a separate background and border.

### Neutral

- Reading ink and muted ink separate primary copy from supporting text. Page paper frames the brighter worksheet paper.
- Sample and evidence washes mark examples and review material. Worksheet rules organize sections and a stronger border defines fields.

## Typography

- Georgia sets display and section headings at medium weight. The tool headings have a lower size ceiling than the overview heading.
- Segoe UI sets body text, form labels, and controls. Paragraphs and lists use a 70ch measure and lead copy uses 56ch.
- Use tabular numerals for tool numbers, review scores, and the diagnostic profile. Consolas serves preformatted review content.

## Layout

The shell caps the content at 75rem with 1.5rem side gutters. Worksheet panels use two equal, top-aligned columns with a 1.2rem gap. The overview places its introduction and sample above a ruled tool index, with a number, description, and action in each row.

At 760px and below, use 1rem side gutters and stack the overview, worksheet panels, and tool row contents. The header and navigation can wrap. At 420px and below, filters fill the available width and findings headings can wrap to accommodate scores.

## Elevation & Depth

Use flat paper tones to separate surfaces. Worksheet panels have a fine border. The sample sheet uses a wash and teal rules at the top and bottom. Repeated rows within a surface are separated by horizontal rules.

## Shapes

Controls and notices have softly squared corners (.35rem). Bordered worksheet panels use a slightly broader curve (.8rem). The sample sheet and ruled index use square edges.

## Components

- **Buttons.** Use a navy fill and white text for the primary action. Secondary actions use navy text and border on a transparent surface that takes a wash on hover. Both share a 2.75rem minimum height and a consistent footprint. A disabled button reduces opacity and shows a wait cursor.
- **Fields.** Keep labels above full-width inputs with worksheet-paper fills and defined borders. Checkboxes sit beside their labels. Textareas resize vertically.
- **Navigation.** Keep the CA mark and wordmark together. Current and hovered links use teal text with a matching underline. Keyboard focus uses a 3px outline with a 4px offset across controls and links.
- **Worksheet panels.** Use worksheet paper for source material and the evidence wash for reviews or discussion guides. Use ruled findings and native disclosure controls for supporting details.
- **Diagnostic signals.** The signal links wrap in an outlined row. A teal fill and white text identify the current signal. Pair profile meters with a visible numerical score.

## Do's and Don'ts

- Do keep the CA monogram alongside the CommsAlign wordmark.
- Do keep Message Coach ahead of Team Diagnostic in navigation and the tool index.
- Do keep evidence beside its source on wide screens and directly after it in stacked reading order.
- Do keep scores readable as text alongside their meters and label withheld results in words.
- Do preserve the visible keyboard focus treatment and the skip link.
