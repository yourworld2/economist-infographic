# Design Tokens

All values distilled from the official Economist Design System (`design-system.economist.com/foundations/*`) and the open-source `economist-data-team` GitHub organization. When a token differs between the two sources, the **Design System value wins** for production, the **data-team value wins** for legacy interactive compatibility.

## Colour

### Brand

| Token | Hex | RGB | Notes |
|---|---|---|---|
| `--red` (Economist Red) | `#E3120B` | `rgb(227, 18, 11)` | **Canonical brand red.** Use for flag, kicker, title emphasis, and the protagonist series in classic-crimson mood. |
| `--red-60` | `#F6423C` | `rgb(246, 66, 60)` | Hover/active state for red elements. |

Legacy aliases (use only if matching a specific archived asset):

- `#E30010` — data-team CSS canonical (`--red-1`); visually indistinguishable from `#E3120B`; keep if you are reproducing an old chart verbatim.
- `#e11b17` — older data-team JS brand; do not introduce into new work.

### Accent — Chicago (deep blue)

| Token | Hex | Role |
|---|---|---|
| `--chicago-20` | `#141F52` | Title ink on white in monochrome-spare mood |
| `--chicago-30` | `#1F2E7A` | Primary secondary series |
| `--chicago-45` | `#2E45B8` | Highlighted secondary series |
| `--chicago-55` | `#475ED1` | Active state |
| `--chicago-90` | `#D6DBF5` | Pale backdrop |
| `--chicago-95` | `#EBEDFA` | Pale backdrop, lighter |

### Accent — Hong Kong (aquamarine)

| Token | Hex |
|---|---|
| `--hk-45` | `#1DC9A4` |
| `--hk-55` | `#36E2BD` |
| `--hk-90` | `#D2F9F0` |
| `--hk-95` | `#E9FCF8` |

### Accent — Tokyo (crimson-pink)

| Token | Hex |
|---|---|
| `--tokyo-45` | `#C91D42` |
| `--tokyo-55` | `#E2365B` |
| `--tokyo-90` | `#F9D2DB` |
| `--tokyo-95` | `#FCE9ED` |

### Accent — Singapore (orange)

| Token | Hex |
|---|---|
| `--sg-55` | `#F97A1F` |
| `--sg-65` | `#FB9851` |
| `--sg-75` | `#FCB583` |
| `--sg-90` | `#FEE1CD` |

### Accent — New York (gold)

| Token | Hex |
|---|---|
| `--ny-55` | `#F9C31F` |
| `--ny-65` | `#FBD051` |
| `--ny-75` | `#FCDE83` |
| `--ny-90` | `#FEF2CD` |

### Greyscale — London

| Token | Hex | Role |
|---|---|---|
| `--london-5`  | `#0D0D0D` | (rarely used) |
| `--london-10` | `#1A1719` | **Primary text ink** on light backgrounds |
| `--london-20` | `#333333` | Body text alternative |
| `--london-35` | `#595959` | Secondary text |
| `--london-70` | `#B3B3B3` | Disabled / light axis ticks |
| `--london-85` | `#D9D9D9` | Pale dividers |
| `--london-95` | `#F2F2F2` | Pale background |
| `--london-100`| `#FFFFFF` | Pure white |

### Canvas

| Token | Hex | Use |
|---|---|---|
| `--la-85`  | `#E1DFD0` | Warm cream (print) |
| `--la-90`  | `#EBE9E0` | Warm cream (lighter) |
| `--la-95`  | `#F5F4EF` | Warm cream (lightest, default print background) |
| `--paris-85` | `#D0E1E1` | Cool cream |
| `--paris-90` | `#E0EBEB` | Cool cream (lighter) |
| `--paris-95` | `#EFF5F5` | Cool cream (lightest) |

**Default chart background: white `#FFFFFF`.** Cream is for print simulation only.

## Typography

### Font families (priority order)

| Token | Stack | Role |
|---|---|---|
| `--ds-type-system-serif` | `Milo TE`, `Milo TE W01 Regular`, `Officina`, `Source Serif Pro`, `Georgia`, serif | Body, descriptions, headlines in newspaper-serious mood |
| `--ds-type-system-serif-smallcaps` | `Milo SC TE`, `Milo TE W01 SC`, `Officina SC`, `Source Serif Pro`, serif | Small caps in Milo TE flow |
| `--ds-type-system-serif-lining` | `Milo LN TE`, `Milo TE W01 Lining`, `Officina Lining`, serif | Lining figures in serif flow |
| `--ds-type-system-sans` | `Econ Sans OS`, `Econ Sans W01`, `Inter`, `Calibri`, `Arial`, sans-serif | Navigation, fly titles, captions, datelines, metadata. **Old style figures.** |
| `--ds-type-system-sans-lining` | `Econ Sans` (lining), `Inter`, `Calibri`, `Arial`, sans-serif | Pagination, form labels, table numbers, **numerical data in tables and inputs**. Lining figures. |
| `--ds-type-system-sans-condensed` | `Econ Sans Condensed`, `Inter Tight`, `Inter`, `Arial Narrow`, sans-serif | **Charts and interactive graphics. Lining figures.** ← explicit design-system instruction |
| `--ds-type-system-eco-pict` | `EcoPict`, icon-font fallback | Pictograms (12 chart glyphs + 8 arrows) |

The Design System says literally: "Econ Sans Condensed — For charts and interactive graphics. Uses lining figures." That is the single most explicit chart-specific instruction in the entire design system.

### Modular type scale (16 px base, ratio ≈ 1.125)

| Level | px | rem | line-height multiplier | line-height (px) |
|---|---|---|---|---|
| −3 | 11 | 0.689 | 1.4 | 15 |
| −2 | 13 | 0.826 | 1.4 | 18 |
| −1 | 14 | 0.889 | 1.4 | 20 |
| **0 (base)** | **16** | **1.000** | **1.4** | **22** |
| 1 | 18 | 1.125 | 1.4 | 25 |
| 2 | 20 | 1.266 | 1.4 | 28 |
| 3 | 23 | 1.424 | 1.2 | 28 |
| 4 | 26 | 1.602 | 1.2 | 31 |
| 5 | 29 | 1.802 | 1.2 | 35 |
| 6 | 32 | 2.027 | 1.2 | 38 |
| 7 | 36 | 2.281 | 1.2 | 43 |

**Switchover rule**: line-height = **1.4** for body sizes ≤ 23 px, **1.2** for sizes ≥ 23 px. 23 px is the boundary.

### Recommended font roles for a chart

| Element | Token | px | Weight | Colour |
|---|---|---|---|---|
| Kicker (all-caps category) | `--ds-type-system-sans` | 11–13 | 700 | `--red` |
| Title | `--ds-type-system-serif` (newspaper-serious) **or** `--ds-type-system-sans` (other moods) | 20–24 | 700 | `--london-10` |
| Standfirst / dek | `--ds-type-system-serif` italic **or** `--ds-type-system-sans` | 14–16 | 400 | `--london-35` |
| Axis labels | `--ds-type-system-sans-condensed` | 13–14 | 400 | `--london-10` |
| Tick numbers | `--ds-type-system-sans-lining` | 12–14 | 400 | `--london-10` |
| Data labels (on the chart) | `--ds-type-system-sans-condensed` | 12–14 | 700 | matches series colour or `--london-10` |
| Source line | `--ds-type-system-sans` | 12–13 | 400 | `--london-35` |
| Note | `--ds-type-system-sans` italic | 12 | 400 | `--london-35` |

## Grid and spacing

- **Base unit**: 8 px (`--ds-grid-base`)
- **Layout grid**: 1 col (< 600 px) / 6 col (≥ 600 px) / 12 col (≥ 960 px)
- **Grid gap (intra-column)**: 12 px @ ≤ 600 px, 16 px @ > 600 px
- **Grid gutter (inter-column)**: 24 px @ ≤ 600 px, 32 px @ > 600 px
- **Max content width**: 1432 px (89.5 rem)
- **Chart block paddings**: 16 px on all sides; chart-area inside the block: 40 px L/R, 24 px T/B
- **Source line offset**: 16 px from chart bottom edge, 28 px from block left edge (to clear the flag)

**For chart sizing** (from the daily-chart tradition):
- Print column: **595 px** wide (the canonical print column width)
- Web embed: **640 px** (minimum to retain the flag/title hierarchy at retina density)
- Feature chart: **800 px** wide
- Max: 1280 px

## Rules (dividers)

CSS tokens for lines and borders:

- `--ds-border-rule` (default, 1 px subtle)
- `--ds-border-rule--emphasised` (1 px prominent)
- `--ds-border-rule--heavy` (2 px, used for the chart-block top border in red)
- `--ds-border-rule--accent` (1 px in `--red`)

The 2 px red top border on the chart block is the most distinctive structural rule in the system.

## Legacy interactive palette (data-team, 2016)

For reproducing archived interactives, the open-source repo uses a different palette. Do not mix with the Design System values.

```js
// econ_colours.js
{
  brand: '#e11b17',           // → use #E3120B in new work
  green:    ['#44674C', '#6E8F75', '#96B19B', '#B9CDBC', '#DBE8DC'],
  brown:    ['#632514', '#762B1A', '#9D8278', '#DEC3AB', '#EAD6BF'],
  red:      ['#E30010', '#E84932', '#E88B6F', '#EBA289'],
  aquamarine:['#00857C', '#74BCBF'],
  blue:     ['#004C64', '#009FD7', '#528EA5', '#6895A7', '#75D0F4', '#C1D5DF', '#D5E3EA', '#F4FBFE'],
  grey:     ['#1A1719', '#525254', '#5E5E60', '#696A6C', '#808184', '#909294', '#ACADB0', '#909294', '#CBCCCE', '#E6E7E8']
}
```

Note: in this legacy palette, `red[0] = #E30010` is the canonical CSS "Economist red". `grey[6]` and `grey[8]` are duplicates (`#909294`) — a copy-paste bug, harmless.

## Sub-palettes for choropleths (data-team)

Hard-coded in the euromap project's `init.js`, used for the Euro/Schengen map. Available if you need a geographic palette that the masthead historically approved:

```
--euro-schengen     #0082C3
--euro-nonschengen  #00A67C
--eu-schengen       #40A1D2
--eu-nonschengen    #8CD7C4
--schengen-area     #BFE0F0
--none              #E2E3E4
--andorra           #00A67C
--text-light        #FFFFFF
--text-dark         #231F20
```

## Accessibility

- All text on white: must meet WCAG AA (≥ 4.5:1 for body, ≥ 3:1 for large text ≥ 18 px bold)
- Verified pairs: `--london-10` on white = 17.4:1 ✅; `--london-35` on white = 7.2:1 ✅; `--red #E3120B` on white = 5.4:1 ✅ (passes for body but not large text 3:1 — fine for body, push to chicago-30 for headlines if you need more pop)
- Never use `--london-70` for body text on white
