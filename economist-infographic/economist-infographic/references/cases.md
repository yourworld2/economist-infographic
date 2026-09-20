# Real Cases and Hard Rules

> Real Graphic Detail / interactive cases observed on economist.com, plus hard rules distilled from third-party design analyses. Use this to validate the design choices in `tokens.md`, `moods.md`, and `chart-types.md` against what the masthead actually publishes.

## Confidence note

- **High confidence**: directly observed in the official Design System, the open-source data-team repos, or the live `/interactive/` pages whose SVG markup is inspectable.
- **Medium confidence**: observed in Graphic Detail PNGs (visible in the article body) but not extracted as inline SVG.
- **Inferred**: from the design-system principles + third-party analyses, not directly measured in a published chart.

---

## Real cases (12 total)

### A. Hard-data interactives (SVG-extractable, /interactive/)

#### Case A1 — EIU Democracy Index 2025
- **URL**: `https://www.economist.com/interactive/democracy-index-2025`
- **Topic**: 167 countries' democracy scores, 2006–2025
- **Charts**: line chart (global mean 5.0–5.6, 2006–2025), 5-country comparison line (Norway / US / Romania / Pakistan / Afghanistan), horizontal bar (7 regions 0–10)
- **Palette observed**:
  - Blue = Norway (best)
  - Red = Afghanistan (worst)
  - Orange = Romania / Pakistan
  - Green = regional bars (multi-step opacity)
  - Greyscale for grid + background
- **Style**: serious-newspaper, white background, near-invisible grid
- **Takeaway**: protagonist series in saturated hue + supporting series in low-saturation variants; never rainbow
- **Confidence**: high

#### Case A2 — Mapping the Iran war's trade disruption
- **URL**: `https://www.economist.com/interactive/graphic-detail/2026/05/11/mapping-the-iran-wars-trade-disruption`
- **Topic**: Strait of Hormuz trade disruption, scrollytelling
- **Charts**: line+area (tanker traffic, urea/aviation fuel/gasoline prices), horizontal bar (semiconductor market share, crude export destinations), stacked/grouped bar (LPG imports, aluminium premium), donut (54% Gulf / 46% other for naphtha imports), choropleth (countries >25% Gulf imports + EU fuel-tax-cut highlighted)
- **Palette observed**:
  - Deep navy `#003366` — primary
  - Red `#C7012E` — event marker ("US-Israeli air strikes on Iran begin")
  - Dark grey `#333333` — body text
  - Yellow highlight — map countries + EU fuel-tax cut
- **Axes**: Y ticks visible (0–300 tankers/week, 0/5/10/15 m bbl/day, 0–40 m tonnes, 0–80% share, prices $/t or $/bbl or $/gallon); pale grey hairlines as grid
- **Annotation**: red dashed vertical line for events + inline text callout
- **Source line**: `Sources: Kpler; EIA; Argus Media; Bloomberg; Vortexa; IEA` — **multi-source with semicolons**
- **Style**: serious-newspaper, scrollytelling-driven
- **Takeaway**: scrollytelling can pack 8+ chart types in one piece; the red dashed event marker is a recurring signature; multi-source credit is acceptable
- **Confidence**: high

#### Case A3 — US Inflation Tracker
- **URL**: `https://www.economist.com/interactive/inflation-tracker`
- **Topic**: Economist forecast model vs actual inflation
- **Charts**: line comparison (Economist 3.6% vs Headline 3.5%, 1960–2026), inflation concentration time series (65 years)
- **Palette**: light grey background, dark line + annotation
- **Special detail**: "Jan 1999" callout — tobacco prices rose 33.5% after 1998 lawsuit
- **Source line**: `Source: U.S. Bureau of Economic Analysis, The Economist` — **"The Economist" self-credited when using internal model**
- **Style**: serious-newspaper
- **Confidence**: high

### B. Graphic Detail articles (PNG, paywalled, but visible)

#### Case B1 — Computer-science degrees
- **URL**: `https://www.economist.com/graphic-detail/2026/06/01/do-you-really-want-that-computer-science-degree`
- **Topic**: US universities expanding CS degrees, but job market cooling
- **Chart type**: bar / dot-plot by university, 2022 vs 2024
- **Asset URL pattern**: `cdn-cgi/image/width=1424,quality=80,format=auto/content-assets/images/20260530_WOT565.png` (standard "WOT" weekly chart)
- **Style**: serious-newspaper
- **Confidence**: medium (paywall, asset URL only)

#### Case B2 — Why science is becoming less innovative
- **URL**: `https://www.economist.com/graphic-detail/2026/05/25/why-science-is-becoming-less-innovative`
- **Topic**: "disruption index" of papers / patents falls with researcher age
- **Chart type**: scatter + fitted curve (small multiples candidate)
- **Style**: serious-newspaper, data-heavy
- **Confidence**: medium

#### Case B3 — FIFA World Cup tickets
- **URL**: `https://www.economist.com/graphic-detail/2026/05/18/fifas-exorbitant-world-cup-tickets-could-backfire`
- **Topic**: Price elasticity of World Cup ticket demand
- **Chart type**: scatter + elasticity fit line
- **Style**: serious-newspaper, sports angle
- **Confidence**: medium

#### Case B4 — Russia–Ukraine territorial change
- **URL**: `https://www.economist.com/graphic-detail/2026/05/17/russia-is-starting-to-lose-ground-in-ukraine`
- **Topic**: Russian territorial gains/losses, satellite-detected fire intensity as proxy
- **Chart type**: area / region-fill time-series
- **Methodology note**: "satellite-detected fires" — common Economist pattern of using **indirect proxies** when direct data is unavailable
- **Style**: serious-newspaper
- **Confidence**: medium

#### Case B5 — Allied defence spending
- **URL**: `https://www.economist.com/graphic-detail/2026/05/11/by-one-measure-americas-allies-now-outspend-it-on-defence`
- **Topic**: European defence as % of GDP vs US
- **Chart type**: dual-axis line / stacked area (small multiples)
- **Style**: serious-newspaper
- **Confidence**: medium

#### Case B6 — UK local elections
- **URL**: `https://www.economist.com/graphic-detail/2026/05/01/labour-faces-a-drubbing-in-englands-local-elections`
- **Topic**: Labour seats at risk
- **Chart type**: horizontal bar + historical column comparison
- **Style**: serious-newspaper
- **Confidence**: medium

#### Case B7 — Why eldest siblings are brainier
- **URL**: `https://www.economist.com/graphic-detail/2026/04/16/why-eldest-siblings-are-brainier`
- **Topic**: Birth order vs education/income, infection-exposure hypothesis
- **Chart type**: box / dot-plot
- **Style**: serious-newspaper
- **Confidence**: medium

#### Case B8 — Hungary's skewed elections
- **URL**: `https://www.economist.com/graphic-detail/2026/04/09/even-hungarys-skewed-elections-might-not-save-viktor-orban`
- **Topic**: Gerrymandering effect on election outcome
- **Chart type**: choropleth (map) + deviation bar
- **Style**: serious-newspaper
- **Confidence**: medium

#### Case B9 — Trump approval rating
- **URL**: `https://www.economist.com/graphic-detail/2026/04/01/donald-trumps-approval-rating-has-sunk-to-joe-bidens-lowest-point`
- **Topic**: Polling tracker, Trump vs Biden's low
- **Chart type**: time-series line (YouGov data)
- **Data source**: YouGov polling tracker; "tracker of military budgets" is another recurring Economist tracker
- **Style**: serious-newspaper
- **Confidence**: medium

---

## Hard rules from third-party design analyses

### shadcn.io "The Economist Design System" reverse-engineer
- **URL**: `https://www.shadcn.io/design/economist`
- **Key claims**:
  1. **"Rationed brand red"** — `#E3120B` used only for text or 1px borders in the **web product**; chart editors are more lenient and do use red as series fill. **This is a known divergence between web-product and editorial-chart rules.**
  2. **"Navy CTA voltage"** — CTA buttons almost always `#1F2E7A` (Chicago Navy), 20px pill radius
  3. **"Two-family duet"** — EconomistSerif (titles) + EconomistSans (UI/chrome)
  4. **"Four-radius geometry"** — only 4 / 20 / 32 / 50% radii are used; no in-between
  5. **"London greyscale"** — London-5 → London-100 naming convention
- **Confidence**: medium (third-party reverse-engineer; consistent with our design-system tokens)

### AECharts "How to create charts like The Economist"
- **URL**: `https://aecharts.com/blog/posts/how-to-create-charts-like-the-economist/`
- **Key rules**:
  1. **"One chart, one message"** — the protagonist data gets the saturated red; everything else recedes to grey
  2. **"Headline title"** — title is a complete sentence stating the insight (e.g., *"Sales jumped 40% in Q4"*), not a topic
  3. **"Direct labelling > legends"** — numbers go directly on the bar/line
  4. **"Embrace white space"** — white space is a design element
  5. **"Supporting data at 30–50% opacity"** — historical baseline, peer comparison, etc. all at low alpha
  6. **Font**: "Proprietary Econ Sans"; free equivalent is Arial Bold / Helvetica Bold
- **Confidence**: high (specific, consistent with our tokens)

### Prezlab "What We Can Learn from The Economist"
- **URL**: `https://prezlab.com/what-we-can-learn-from-the-economist-about-data-visualization/`
- **Key rules**:
  1. **Simplicity-first** — use the most basic chart types (line, bar); titles are declarative sentences
  2. **Primary message rule** — the main message must be readable in seconds
  3. **Unified visual language** — print, web, social all use the same vocabulary
  4. **Strategic highlighting** — use opacity differences for emphasis, not new colours
  5. **Y-axis breaks** — **lines** may break the Y-axis (with clear labeling); **bars MUST NOT** break (distorts proportion)
- **Confidence**: high

### fountn.design visual style guide summary
- **URL**: `https://fountn.design/resource/the-economist-visual-style-guide/`
- **Original PDF** (referenced, not retrieved): `https://design-system.economist.com/documents/CHARTstyleguide_20170505.pdf`
- **Three pillars**: **Clarity / Accuracy / Visual consistency**
- **Coverage**: chart types, scaling & proportions, typography, colours, gridlines, data sourcing
- **Confidence**: medium (PDF not retrieved directly; summary consistent with data-team code)

### FlowingData indirect signal
- **URL**: `https://flowingdata.com/?s=economist`
- **What gets cited repeatedly** as "Economist-style" by other data-viz sites:
  - Dot plot (Elon Musk tweet time distribution)
  - Dot density map (elections)
  - Slope chart (GDP, innovation index)
- **Takeaway**: when the topic is **categorical × comparative** or **time × categorical** with many groups, dot plot / slope chart / small multiples are the canonical "Economist look"

---

## Palette conflict resolution (final)

The single most-asked question about Economist charts is "what red do they use?". The honest answer has three layers:

| Context | Red | Source |
|---|---|---|
| **Editorial chart, modern** | `#E3120B` | Design System + AECharts + shadcn + fountn all converge |
| **Editorial chart, archival** | `#E30010` | Data-team CSS (`econ_colours.js`) |
| **Editorial chart, very old** | `#e11b17` | Data-team JS brand |
| **Interactive event marker** | `#C7012E` (slightly cooler) | Observed in Iran war case |
| **Pantone** | `2347 C` (red) / `7436 C` (white) | brandcolorcode.com |

**Default to `#E3120B` in new work.** Document the variant when reproducing an archived chart verbatim.

## Type scale reconciliation

The Design System gives a precise 16-px-base modular scale (ratio ≈ 1.125). Third-party analyses say data labels are 9–11 px, tick labels 9–11 px, title 18–22 px. These reconcile as follows:

- **Data label / tick label** = scale level −3 (−2 is 13 px is too big for tick labels) — i.e., 11 px, the floor of the scale
- **Title** = scale levels 2–3 (20–23 px); could go to 4 (26 px) for feature charts
- **Subtitle / standfirst** = level 0–1 (16–18 px) but visually appears smaller because of greyer colour
- **Kicker** = −3 to −2 (11–13 px), uppercase + letter-spacing
- **Source line** = −2 to −1 (13–14 px) — slightly above tick labels so it remains findable

> **Conclusion**: the design-system's modular scale and the third-party "9–11 px" claims are consistent — the 9–11 px figure is the floor of the scale, and titles are 2× the subtitle per AECharts.

## Three style variants (observed vs prescribed)

The 4-mood scheme in `moods.md` (newspaper-serious / classic-crimson / colorful-explainer / monochrome-spare) is more granular than what the masthead itself names. The 3-variant summary that emerged from observing 12 cases is:

| Variant | When it appears in the wild | Masthead name (if any) |
|---|---|---|
| **Serious newspaper** | Macro, policy, elections, finance, geopolitics, inflation, war | The default (≈ newspaper-serious + classic-crimson) |
| **Bright explainer** | Tech, consumer, lifestyle, science explainers, election maps, sports | ≈ colorful-explainer |
| **Monochrome spare** | Op-eds, research notes, methodology charts | ≈ monochrome-spare |

The skill's 4-mood system is correct and more granular; this 3-variant summary is just a way to remember the elasticity range.
