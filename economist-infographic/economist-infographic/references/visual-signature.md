# Visual Signature

The handful of structural marks that make a chart read as "Economist" at a glance, even before you parse the data. Get these right and you've captured 80% of the look.

## The red flag (10×30 px)

A small filled rectangle, exactly **10 px wide and 30 px tall**, in `#E3120B`, placed flush against the top-left corner of the chart block, overlapping the 2 px red top border.

- Width: 10 px
- Height: 30 px
- Fill: `#E3120B` (never any other red)
- Position: `top: 0; left: 16px` (matching the chart block's 16 px padding)
- Z-order: above the 2 px top border, so the border runs *behind* the flag

This is the most copied single element of the Economist visual identity. It is a registered trademark of the publication — do not use the exact shape in commercial work that could be confused for an Economist publication.

**Substitution rules** (when the mood is monochrome-spare or when brand safety matters):
- monochrome-spare mood: replace the flag with a **1 px `#E3120B` horizontal rule** above the title; no rectangle.
- non-editorial work: use a different accent rectangle (e.g. 10×30 in Chicago-30) to avoid mimicking the masthead.

## The 2 px red top border

A horizontal rule, **2 px tall**, in `#E3120B`, spanning the full width of the chart block, sitting at the top edge.

- Stroke: 2 px
- Colour: `#E3120B`
- Position: top of the chart block, behind the flag
- In CSS: `border-top: 2px solid #E3120B;` on the chart block
- In SVG: `<line>` at the top of the chart area

The combination of flag + top border is the structural signature. Either alone reads as something else; both together is unmistakably Economist.

## The kicker

The all-caps category label, sitting 16 px to the right of the flag, baseline-aligned with the bottom of the flag.

- Font: Econ Sans, **700 weight**
- Size: 11–13 px
- Colour: `#E3120B` (same as the flag)
- Transform: uppercase
- Letter-spacing: 0.06–0.10 em
- Examples: `WORLD THIS WEEK`, `GRAPHIC DETAIL`, `FINANCE & ECONOMICS`, `COFFEE`, `DAILY CHART`

The kicker is **not** optional. It establishes the section/context. Even a one-word kicker (`COFFEE`) is better than no kicker.

## The title

A single sentence with a verb that states the finding.

- Font: Milo TE (newspaper-serious, monochrome-spare) **or** Econ Sans (classic-crimson, colorful-explainer)
- Size: 20–24 px
- Weight: 700
- Line-height: 1.2 (or the type-scale 1.2 multiplier for sizes ≥ 23 px)
- Colour: `#1A1719` (no red on the title, except for the single word you want to emphasise, if any)
- Max width: matches the chart block width minus 28 px left padding

**Good titles** (verb-led, finding-led):
- "Coffee briefly got cheaper, then caught up with inflation"
- "Germany's export machine has finally hit the buffers"
- "Even America's allies are now outspending America"

**Bad titles** (topic-led, no finding):
- "Coffee prices 2019–2024" ❌
- "German exports" ❌
- "Defence spending, 2018–2024" ❌

## The standfirst (optional)

A second sentence, smaller, usually italic, that gives the context the title assumes. Often the units or the time range.

- Font: Milo TE Italic (serif moods) or Econ Sans Regular (sans moods)
- Size: 14–16 px
- Colour: `#525254` (London 35, or close to it)
- Line-height: 1.4
- Margin: 0 0 16 px 28 px (16 px below to separate from the chart area)

If the title already states the units, the standfirst is omitted. If the title is funny or provocative, the standfirst is the place to anchor it with hard data ("% of adults who drink coffee daily, 2019–2023").

## The chart area

Inside the chart block, padded by 16 px all sides plus the title block height.

- Internal padding: 40 px L/R (for the left axis labels), 24 px T/B
- Background: `#FFFFFF` (the chart block is the same colour as the page, no inset)
- Axes: 1 px black ticks, no axis line beyond the ticks (in newspaper-serious, classic-crimson, monochrome-spare moods)
- Gridlines: none, or `#F2F2F2` (London 95) at 0.5 px (in colorful-explainer mood only)

## The source line

The closing signature. Always present, always at the bottom.

- Font: Econ Sans, 400 weight
- Size: 12–13 px
- Colour: `#696A6C` (London 35) or `#5E5E60` (London 3)
- Position: 16 px below the chart area, 28 px from the block left edge
- Format: `Source: <name>` — for Economist work, append ` | The Economist` or similar attribution
- Examples:
  - `Source: ICE Futures U.S.`
  - `Source: Eurostat | The Economist`
  - `Source: Bloomberg, author's calculations`

**The source line is non-negotiable.** A chart without a source is not a Economist chart, regardless of how good the visual style is.

## The note (optional)

A second line below the source, for definitions, methodology, or asterisks.

- Font: Econ Sans Italic, 12 px
- Colour: `#696A6C`
- Examples:
  - `*Inflation-adjusted to 2023 USD.`
  - `Includes only countries with > 1m population.`

## Total composition checklist

- [ ] Chart block has 16 px padding on all sides
- [ ] 2 px red top border on the chart block
- [ ] 10×30 red flag in the top-left, overlapping the border
- [ ] Kicker 16 px right of the flag, 11–13 px, all caps, red, bold sans
- [ ] Title 28 px right of the flag, 20–24 px bold (serif or sans by mood), `#1A1719`
- [ ] Standfirst 28 px right of the flag, 14–16 px, `#525254`, optional
- [ ] Chart area 28 px from the block left edge (to clear the flag), full available width
- [ ] Axes 1 px black ticks, no gridlines
- [ ] Source line 16 px below the chart, 28 px from the block left, 12 px, `#696A6C`
- [ ] Optional note line below the source
- [ ] Total width matches the target (595 / 640 / 800 / 1280 px)

## Width conventions

| Context | Width | Rationale |
|---|---|---|
| Print column | 595 px | The canonical daily-chart print width |
| Web inline | 640 px | Retina-density minimum; preserves hierarchy |
| Feature chart | 800 px | For top-of-article lead charts |
| Full-bleed interactive | 1280 px | Maximum readable width; beyond this the reader's eye loses the data on the left |
| PPT (16:9) | See `ppt-adaptation.md` | Different aspect ratio, scaled-up typography |

## The "leader block" proportions

A "leader block" is the small daily chart that appears at the top of *The Economist*'s print edition, summarising the lead story. The rules for leader block charts are stricter than the web rules:

- **Width**: 595 px (print column)
- **Aspect ratio**: roughly 1:0.5 to 1:0.6 (wider than tall)
- **Minimalism**: "as simple as possible, with as few gridlines and tick marks as possible. The chart's purpose is to show the overall information, not to identify the specific value of each data point."
- **Maximum 2 data series**
- **No annotations** on the data area beyond a single callout for the latest data point
- **Source line mandatory**

When in doubt, follow the leader block rules. The leader block is the strictest form of the style, and anything that works there will work in any other context.
