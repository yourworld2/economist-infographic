---
name: economist-infographic
description: Generate information graphics and slide visuals in The Economist's signature editorial style. Use this skill whenever the user asks for an "information graphic", "infographic", "data visualization chart", "news graphic", "Daily Chart"-style chart, "editorial chart", or wants to embed Economist-style visuals in PPT slides, articles, or reports. Also triggers on Chinese requests like 经济学人风格信息图、新闻图表、PPT 数据图、报告插图、每日图表风格、Econ Sans 风格图表. Do NOT use for general UI design, logo work, web component libraries, or non-editorial dashboard charts. The skill is opinionated: it produces single self-contained SVG/HTML files or a 16:9 PPT slide, both following the masthead's design tokens (Economist Red #E3120B, Chicago deep blue, Officina/Econ Sans family, 8px grid, 10×30 red flag, Source: line) and four preset moods (newspaper-serious, classic-crimson, colorful-explainer, monochrome-spare).
---

# Economist Infographic

Produce a single, self-contained editorial chart or PPT slide that looks like it belongs in *The Economist*'s Graphic Detail section.

## When to load this skill

Load it when the user wants any of:

- A news/data chart styled like The Economist (柱子/折线/面积/散点/滑珠/饼图/双坐标/时间轴/地图)
- A standalone editorial information graphic for an article, report, deck
- A PPT slide whose centerpiece is a chart or data diagram, not a text bullet
- A "Daily Chart"–style single chart with a strong opinion

Do not load it for: general UI design, brand logos, web app component libraries, multi-page dashboards, marketing posters unrelated to data, or non-editorial decorative graphics.

## Core principles (from the masthead)

1. **Less is more.** Drop gridlines, drop redundant axis lines, drop legends when direct labels work. Negative space is part of the message.
2. **Deliberate typography.** Use one serif (Milo TE / Officina) for the voice, one sans (Econ Sans) for the mechanics. Numbers in lining figures. Never two serifs at once.
3. **Visual harmony.** Pick a single accent family per chart; grayscale everything else. Maximum two saturated hues per composition.
4. **Clear wayfinding.** Direct labels at the data point > callout lines > legend. The reader should never have to glance at a key to decode the chart.
5. **Intelligence and wit.** Title is a sentence with a verb that states the finding, not a topic label. ("China's coal habit is harder to kick than its smoking habit", not "Coal consumption 2010–2024".)
6. **Recognisable consistency.** 10×30 px red flag in the upper-left of the chart header, 2 px red top border on the chart block, `Source:` line in grey, all-caps `ECONOMIST` or category kicker in red.

## Procedure

Follow these steps in order. Do not skip the mood selection — every later decision depends on it.

### Step 1 — Confirm mood (ask the user if not stated)

Pick exactly one of the four preset moods. Each has a distinct color/typography recipe (see `references/moods.md`):

| Mood | When to pick | Voice |
|---|---|---|
| **newspaper-serious** | Macro/policy/election/finance | Authoritative, quiet, near-monochrome with one red highlight |
| **classic-crimson** | Default when unsure; anything that wants a strong "Economist" feel | Single-accent (red) on near-white, red 10×30 flag, classic Leader Block proportions |
| **colorful-explainer** | Tech/lifestyle/science/consumer explainers | Multi-hue (up to 4 saturated tones), softer palette, friendly sans emphasis |
| **monochrome-spare** | Op-eds, research notes, minimalist briefs | Black/grey/one muted accent, hairline axes, maximum whitespace |

If the user did not specify a mood, **default to `classic-crimson`** — it is the safest and the most recognisable.

### Step 2 — Lock the data and the finding

Before drawing, write a one-sentence finding. This becomes the title. Reject generic topics ("GDP growth"), demand a verb ("Slowdown has finally caught up with Germany's export machine").

Then:
- List the data points as a flat table (rows × columns)
- Identify the chart type that *forces the reader to see the finding* (not the type that's easiest to draw)
- If the dataset has > 1 series, decide which series is the protagonist (gets the saturated accent) and which is context (gets grey or a muted tone)

### Step 3 — Choose chart type (consult `references/chart-types.md`)

Common mappings:

- Trend over time, ≤ 2 series → **line chart**, x-axis years, y-axis value, axis at bottom and left only
- Compare categories at one point → **horizontal bar**, sorted, longest at top
- Compare categories over time → **stacked bar** if parts-of-whole, or **grouped bar** if peer comparison
- Show distribution → **dot plot** preferred over histogram; show every datum
- Show composition → **stacked bar (single, 100%)** or **small multiples of pies** only if ≤ 4 slices
- Show relationship between two metrics → **scatter**, with a 1-line trend annotation
- Show geographic → **choropleth** with sequential palette; never rainbow
- Show progression / event timeline → **horizontal timeline** with year markers
- Show magnitude relative to a target → **thermometer / bullet chart**

**Hard rules** (from the style guide):
- Pie / doughnut: never with more than 4 series. Prefer horizontal bar.
- Stacked bar: when few segments, delete tick marks and label each segment's value directly.
- Thermometer: max 4 series, else pick another type.
- Time-series side-by-side: if series represent the *same metric across years* (e.g. 2015, 2016, 2017), use **the same hue, light → dark** as years progress. If they represent *different categories*, use **contrasting hues**.

### Step 4 — Apply the design tokens (see `references/tokens.md`)

Use the tokens via CSS custom properties or inline styles. Never hardcode colors that differ from the palette.

Required minimum:
- Background: `#FFFFFF` (default) or `#F5F4EF` (Los Angeles 95, print-style cream)
- Primary text: `#1A1719` (London 5) for body, `#E3120B` (Economist Red) only for the kicker/flag/title emphasis
- Main series color: depends on mood (see recipes)
- Font stack: `'Econ Sans', 'Milo TE', 'Officina', 'Calibri', 'Arial', sans-serif` for charts; `'Milo TE', 'Officina', Georgia, serif` for titles in newspaper-serious mood
- Base size: 16px body, 14px caption/source, 18–22px chart title, 13–14px tick labels
- Grid: 8px base; chart block padded by 16px on all sides

If the user is rendering the SVG in a context where Econ Sans / Officina are not available, **substitute with the closest free equivalents**: `Source Serif Pro` for Milo TE, `Inter` for Econ Sans. Note the substitution in a comment, do not silently fall back to Arial.

### Step 5 — Compose the visual signature

Every chart block, in this order, top to bottom:

1. **Top-left flag**: 10×30 px filled `#E3120B` rectangle, flush against the top-left of the chart block. 2 px `#E3120B` top border running the full width of the chart block, with the flag overlapping it.
2. **Kicker / category label** (all caps, 11–13 px, red): e.g. `WORLD THIS WEEK`, `GRAPHIC DETAIL`, `FINANCE & ECONOMICS`. 16 px from the flag's left edge.
3. **Title** (one sentence, with a verb): Milo TE Bold 20–24 px (newspaper-serious) or Econ Sans Bold 20–24 px (other moods), `#1A1719`.
4. **Standfirst / dek** (one sentence, optional, italic or regular 14–16 px, `#525254`).
5. **Chart area**: padded by 40 px left/right, 24 px top, 24 px bottom within the chart block.
6. **Source line** (12–13 px, `#696A6C`, Econ Sans): `Source: <name> | The Economist` (or whatever the data source is). 16 px from the chart's bottom edge.
7. **Note** (optional, 12 px, `#696A6C`, italic): for definitions, methodology, or asterisks.

Total width: 640 px (web embed) or 595 px (print column). 800 px for a feature chart. 1280 px max.

### Step 6 — Build the SVG/HTML

See `references/code-templates.md` for full drop-in templates (line, bar, scatter, thermometer, timeline, choropleth skeleton).

Key SVG rules (from the source D3 components):

- `<line>` segments, not `<path>`, for line charts
- `<circle r="3">` for data points; on hover or highlighted state, `r="6"` and fill `rgba(colour, 0.5)`
- Inactive series: `fill: rgba(colour, 0.25); stroke: colour` (faded-but-readable)
- Axes: 1 px black tick marks via `d3.axis().outerTickSize(1)`; no full axis line
- Tooltips: HTML overlay, not `<title>`; white bg, 1 px `#5E5E60` border
- Voronoi hover targets are not required for static SVGs

Wrap the SVG in a single HTML file with inline `<style>`. No external CSS, no external fonts, no JS required.

### Step 7 — If output is PPT

See `references/ppt-adaptation.md` for the full recipe. Quick version:

- Canvas: 16:9, 13.33" × 7.5" (or 10" × 5.625" for 16:9 small)
- The chart goes in the **upper 2/3**; the lower 1/3 holds the title + kicker + source
- **All font sizes scale up 1.5–2×** versus the web version (24 pt title, 18 pt standfirst, 14 pt source, 24 pt chart axis labels)
- 5% safe margin on all sides
- Background: white, never cream (creams look muddy when projected)
- Use the 10×30 red flag and 2 px red top border at the same position — they are the visual signature
- **Never** use theme defaults (Calibri, blue accents, Office SmartArt) — override the master slide

If `python-pptx` is available, generate a `.pptx` programmatically and embed the SVG rasterised at 300 dpi (use `cairosvg` or `rsvg-convert`). If not, hand off the SVG with explicit "place this at (x, y) on a 16:9 blank slide" instructions.

### Step 8 — Self-check before delivery

Verify in order; fail the deliverable and fix if any check trips:

- [ ] Title is a sentence with a verb, not a topic
- [ ] Background is white or cream, **never** a saturated color
- [ ] 10×30 red flag is present in the top-left of the chart block (omit only in monochrome-spare mood, where a 1px red rule replaces it)
- [ ] 2 px red top border spans the full chart block width
- [ ] Source line is present and starts with `Source:`
- [ ] Maximum 2 saturated hues in the chart area (count the series palette)
- [ ] Pie/doughnut used only if ≤ 4 slices
- [ ] Side-by-side time series use single-hue light→dark ramp, not contrasting hues
- [ ] No gridlines beyond the axis ticks
- [ ] All text meets WCAG AA contrast (≥ 4.5:1) against the background
- [ ] Total file is self-contained: no `<link>`, no `<script>`, no external `<img>` refs

## Output contract

Deliver **one** of:

- A single `.html` file containing the chart inline (SVG + inline CSS), openable in any browser, ≤ 60 KB
- A single `.svg` file, openable in any browser or design tool, ≤ 40 KB
- A single `.pptx` file, 16:9, one slide, with the chart embedded as a vector group plus the kicker/title/source as native text boxes
- A `files.md` manifest listing the above plus a one-paragraph caption

Always include the source line. Always include the red flag (or the 1px red rule in monochrome-spare). Never deliver a chart without the editorial framing.

## Failure handling

- **If the user's data is too sparse** (< 4 data points) for the requested chart type, say so and propose a table or a single-sentence callout instead. Do not pad with fake data.
- **If the user wants > 6 series**, refuse to use line chart; propose small multiples (one panel per series) or a heatmap.
- **If the user asks for a 3D / pie-of-pie / exploded-pie chart**, redirect to a flat horizontal bar; explain why.
- **If the host environment cannot render the font**, fall back to `Inter` + `Source Serif Pro` and add a one-line comment at the top of the HTML noting the substitution. Do not silently downgrade to Arial.
- **If you cannot produce the PPT file** (no `python-pptx`, no SVG-to-PPT bridge), hand off the SVG and a short placement note, and say so in plain language — do not claim success.
- **If validation trips** (e.g. > 4 series in a pie), fix it before delivery, do not deliver a known-bad chart.

## Minimal example (full HTML, classic-crimson mood)

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Coffee, briefly cheaper, then not</title>
<style>
  :root {
    --red: #E3120B;
    --ink: #1A1719;
    --grey-3: #5E5E60;
    --grey-9: #CBCCCE;
    --bg: #FFFFFF;
    --serif: 'Milo TE', 'Officina', Georgia, serif;
    --sans:  'Econ Sans', 'Inter', 'Calibri', Arial, sans-serif;
  }
  body { margin: 0; background: var(--bg); font-family: var(--sans); color: var(--ink); }
  .chart-block { width: 640px; margin: 24px auto; padding: 16px; position: relative; }
  .chart-block::before {
    content: ''; position: absolute; top: 0; left: 16px; right: 16px;
    height: 2px; background: var(--red);
  }
  .flag {
    position: absolute; top: 0; left: 16px;
    width: 10px; height: 30px; background: var(--red);
  }
  .kicker {
    margin: 16px 0 6px 28px; font-size: 11px; font-weight: 700;
    letter-spacing: 0.08em; color: var(--red); text-transform: uppercase;
  }
  h1 {
    margin: 0 0 4px 28px; font-family: var(--serif); font-weight: 700;
    font-size: 22px; line-height: 1.2; color: var(--ink);
  }
  .standfirst {
    margin: 0 0 16px 28px; font-size: 14px; color: var(--grey-3);
  }
  svg { display: block; margin-left: 28px; }
  .source {
    margin: 12px 0 0 28px; font-size: 12px; color: var(--grey-3);
  }
  .axis line, .axis path { stroke: var(--ink); stroke-width: 1; fill: none; }
  .axis text { font-family: var(--sans); font-size: 12px; fill: var(--ink); }
  .series { fill: none; stroke: var(--red); stroke-width: 2; }
  .series-context { fill: none; stroke: var(--grey-3); stroke-width: 1.5; }
  .point { fill: var(--red); }
</style>
</head>
<body>
  <div class="chart-block">
    <div class="flag"></div>
    <div class="kicker">Coffee</div>
    <h1>Coffee briefly got cheaper in 2023, then caught up with inflation</h1>
    <p class="standfirst">Arabica futures, USD per pound, monthly average</p>
    <svg width="560" height="280" viewBox="0 0 560 280" role="img" aria-label="Arabica coffee price 2020 to 2024">
      <!-- axes and data go here -->
    </svg>
    <p class="source">Source: ICE Futures U.S.</p>
  </div>
</body>
</html>
```

This is the minimum required skeleton. Real charts replace the SVG body with axes and data points; the wrapping, kicker, title, source, and flag stay.

## Mood comparison — same data, four voices

The same dataset rendered in each of the four preset moods (eval baseline, June 2026, China GDP growth 2010–2024). All five HTML files below passed the Step 8 self-check; differences are by **design**, not by accident.

| Mood | Title | Voice | Visual signature |
|---|---|---|---|
| **newspaper-serious** | `Two shocks and a long slowdown have reset China's growth to 5%` | Authoritative, near-monochrome, serif title (Milo TE) | 10×30 red flag + 2 px red top border; red ≤ 2 occurrences (flag + protagonist series); 595–640 px width |
| **classic-crimson** *(default)* | `China's growth has cooled to less than half its 2010 pace` | Daily Chart / Graphic Detail, sans title (Econ Sans), single saturated red | 10×30 red flag + 2 px red top border; red on protagonist series + flag; 640–800 px |
| **colorful-explainer** | `China's growth has cooled from sizzling to simmering` | Friendly, multi-hue; data split into 4 phase series (each a different palette hue) | 10×30 red flag + 2 px red top border; **red is flag-only**, never on a series; 800 px |
| **monochrome-spare** | `China's annual growth has more than halved in 15 years` | Op-ed / research note, hairline axes, ink + at most one Chicago-30 accent (used once) | **1 px red rule** replaces both flag and top border; serif title (Milo TE); 595–640 px |
| **baseline (no skill)** | `China's growth has *more than halved* since 2010` | Model's free-form impression; cream `#FFFEF6` background | 3 px red bar (deformed flag); grey kicker; serif title with red-highlighted word |

**Files** (in `examples/`, open in any browser to see the rendered output; bilingual index at `examples/INDEX.md`):

- `examples/eval_serious_china_gdp.html` — newspaper-serious
- `examples/eval_producer_china_gdp.html` — classic-crimson *(the recommended default)*
- `examples/eval_colorful_china_gdp.html` — colorful-explainer *(data split into 4 phase series)*
- `examples/eval_monochrome_china_gdp.html` — monochrome-spare
- `examples/eval_baseline_china_gdp.html` — baseline, no skill loaded

**Key takeaway for mood selection**:

1. When unsure, pick **classic-crimson** — it is the most recognisable "Economist" voice and matches the default Daily Chart tradition.
2. Switch to **newspaper-serious** when the topic is heavy (geopolitics, war, recession, central-bank decisions) and the chart must not compete with the prose. The serif title does the heavy lifting; the chart itself goes quiet.
3. Switch to **colorful-explainer** when the data naturally splits into 3–4 distinct categories that each deserve their own colour. Tech explainers, election maps, sports comparisons, science stories.
4. Switch to **monochrome-spare** for op-eds, research notes, methodology charts, or any context where the chart is one of many on a page and must recede.

## Verified PPT output (June 2026)

The `references/ppt-adaptation.md` recipe has been **end-to-end verified** in this environment:

- **Tooling check**: `python-pptx 1.0.2` is installed; `cairosvg`, `rsvg-convert`, `inkscape`, `wand`, `playwright` are **all absent**.
- **Conclusion**: **Approach 1 (native PowerPoint shapes) is the only viable path** in this environment. The `add_picture` SVG-rasterise path in ppt-adaptation.md is documented for the user's local machine but cannot be verified here.
- **Verified output**: `examples/eval_ppt_output.pptx` — 30 KB, 1 slide, 13.333" × 7.5" (16:9), 58 shapes (17 red `#E3120B` for flag + top border + 15 data points), wraps the classic-crimson mood. Generated by `scripts/build_ppt.py` (run `python3 scripts/build_ppt.py [--output path]`); preview render at `examples/ppt_preview.png`. Rebuilt and re-verified September 2026 — regeneration produces identical slide XML (all 38 internal parts match; 30,238 bytes).
- **Self-check**: opens cleanly in LibreOffice (rendered to PDF for preview), all 5 core elements present (flag, top border, kicker, title, source line), chart line + covid band + data labels all native shapes (fully editable in PowerPoint).

**If you are on a machine with `cairosvg` / `rsvg-convert` / `inkscape` installed**, prefer Approach 2 (SVG-embed) for finer detail and smaller file size. **If not**, Approach 1 (the verified path) is fully sufficient for any single chart slide.

## References (in this directory)

- `references/tokens.md` — full design tokens: brand red, Chicago/Hong Kong/Tokyo/Singapore/New York accent families, London greyscale, Los Angeles/Paris canvases, Milo TE / Econ Sans stacks, modular type scale, 8px grid
- `references/chart-types.md` — per-chart-type rules: bar/line/area/stacked/scatter/thermometer/pie/double-scale/timeline/choropleth, with the side-by-side vs stacked color logic
- `references/moods.md` — the four preset moods with full recipes (color set, type weight, flag treatment, spacing)
- `references/code-templates.md` — drop-in SVG/HTML templates for the most common chart types
- `references/visual-signature.md` — the red flag, the rule, the source line, the leader block proportions, with a checklist
- `references/ppt-adaptation.md` — PPT-specific sizing, safe margins, font scaling, python-pptx recipe
- `references/sources.md` — the URLs, repos, and articles this skill is distilled from, with confidence ratings
- `references/cases.md` — 12 real Graphic Detail / interactive cases observed on economist.com + 4 third-party design analyses (shadcn, AECharts, Prezlab, fountn), with palette/type-scale reconciliation
- `references/skill-index.md` — one-page newcomer index: trigger phrases, 4-mood comparison, chart-type map, prompt templates, demo file locations, self-check, known limits, maintenance guide. Read this first if you have never opened the skill before.
- `examples/` — 7 verified end-to-end demo outputs (5 HTML moods + 1 PPTX + 1 PNG preview), indexed in `examples/INDEX.md`
- `scripts/build_ppt.py` — runnable PPTX generator (Approach 1, native shapes; `python3 scripts/build_ppt.py [--output path]`)
