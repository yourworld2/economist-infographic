# Moods — Four Preset Recipes

Each mood is a complete, opinionated design choice across colour, typography, flag treatment, and spacing. Pick one per chart. Never blend two moods in a single chart.

## 1. newspaper-serious

**Voice**: authoritative, quiet, near-monochrome with one red highlight.
**Use for**: macro, policy, geopolitics, elections, finance, central-bank charts, anything where the chart's job is to deliver a hard fact without theatrics.

| Aspect | Choice |
|---|---|
| Background | `#FFFFFF` (no cream — cream reads as "old") |
| Series 1 (protagonist) | `#E3120B` (Economist Red) — single saturated line/bar |
| Series 2 (context) | `#5E5E60` (London grey-3) — hairline at 1.25 px |
| Series 3+ (rare) | `#1F2E7A` (Chicago 30) and `#595959` (London 35) — no warm tones |
| Title font | Milo TE / Officina Bold 22 px |
| Title colour | `#1A1719` (no red) |
| Standfirst | Milo TE Italic 14 px, `#525254` |
| Flag | 10×30 red, **plus** 2 px red top border, full width |
| Source line | 12 px Econ Sans, `#696A6C` |
| Axis ticks | 1 px black; no axis line beyond ticks |
| Gridlines | **None** |
| Default chart type | line, then bar; avoid multi-colour |
| Recommended width | 595 px (print column feel) or 640 px (web) |

**Composition rule**: at most one red element on the page outside the flag (typically the protagonist series line, or the title verb, never both).

## 2. classic-crimson  *(default if user has no preference)*

**Voice**: the canonical "Daily Chart" / Graphic Detail look. Single-accent crimson, near-white, strong typographic hierarchy.
**Use for**: any time you want the chart to be unmistakably Economist.

| Aspect | Choice |
|---|---|
| Background | `#FFFFFF` |
| Series 1 | `#E3120B` (Economist Red) |
| Series 2 | `#1F2E7A` (Chicago 30) |
| Series 3+ | `#1DC9A4` (Hong Kong 45), `#C91D42` (Tokyo 45) — desaturated by 50% via alpha if they become too prominent |
| Title font | Econ Sans Bold 22 px (sans, not serif — this is the data-blog voice) |
| Title colour | `#1A1719` |
| Standfirst | Econ Sans 14 px regular, `#525254` |
| Flag | 10×30 red, **plus** 2 px red top border, full width |
| Source line | 12 px Econ Sans, `#696A6C` |
| Axis ticks | 1 px `#1A1719` |
| Data labels | Econ Sans Condensed 12–14 px, 700, colour-matched to series |
| Default chart type | line, then bar, then small multiples |
| Recommended width | 640 px web, 800 px feature |

**Composition rule**: protagonist series is red. Everything else is supporting cast.

## 3. colorful-explainer

**Voice**: friendly, modern, more hues, but still disciplined.
**Use for**: technology, consumer, lifestyle, science explainers, anything where the reader is learning rather than deciding.

| Aspect | Choice |
|---|---|
| Background | `#FFFFFF` |
| Series palette | Up to 4 saturated tones: `#2E45B8` (Chicago 45), `#1DC9A4` (Hong Kong 45), `#F9C31F` (New York 55), `#F97A1F` (Singapore 55). **The Economist Red is reserved for the flag only** — do not use it as a series in this mood, it loses its signalling power. |
| Title font | Econ Sans Bold 24 px |
| Title colour | `#1A1719` |
| Standfirst | Econ Sans 16 px, `#525254` |
| Flag | 10×30 red, plus 2 px red top border |
| Source line | 13 px Econ Sans, `#696A6C` |
| Axis ticks | 1 px `#1A1719`; light grey background gridlines OK if they aid reading |
| Default chart type | grouped bar, stacked bar, small multiples, area; lines only if time series |
| Recommended width | 800 px |

**Composition rule**: pick a "lead hue" (usually the most saturated of your four) and a "support hue"; the other two are used sparingly, often only for the smallest or contextual series.

## 4. monochrome-spare

**Voice**: op-ed, research note, minimalist brief. Hairlines, max whitespace, no theatrics.
**Use for**: thinkpieces, methodology charts, supporting visuals in long-form articles where the chart is one of many on the page.

| Aspect | Choice |
|---|---|
| Background | `#FFFFFF` |
| Series 1 | `#1A1719` (London 10) — solid black ink |
| Series 2 | `#1F2E7A` (Chicago 30) — the only chromatic accent |
| Series 3+ | Greys only: `#595959`, `#909294`, `#CBCCCE` |
| Title font | Milo TE Bold 22 px |
| Title colour | `#1A1719` |
| Standfirst | Milo TE Italic 14 px, `#525254` |
| Flag | **Replaced** by a 1 px `#E3120B` horizontal rule above the title. The 10×30 box is omitted because it would be too loud. |
| Source line | 11 px Econ Sans, `#696A6C` |
| Axis ticks | 0.5 px `#1A1719` (hairline) |
| Gridlines | None |
| Default chart type | line, dot plot, scatter, small multiples |
| Recommended width | 595 px or 640 px |

**Composition rule**: total ink in the chart area is ≤ 30% of the canvas. The white must dominate. The single Chicago-30 accent is used at most once.

## Mood comparison at a glance

|  | newspaper-serious | classic-crimson | colorful-explainer | monochrome-spare |
|---|---|---|---|---|
| Protagonist colour | Red | Red | Chicago/HK/NY/SG | Black |
| Red allowed as series? | Yes (1) | Yes | No (flag only) | No (rule only) |
| Title font | Serif | Sans | Sans | Serif |
| Flag (10×30) | Yes | Yes | Yes | No (replaced by 1px rule) |
| Multi-hue OK? | No | Up to 4 | Yes (4 max) | No |
| Cream background OK? | No | No | No | No |
| Print-style 595 px | Yes | OK | No | Yes |
| Projected to PPT? | Yes | Yes | Yes (sparingly) | Yes |
