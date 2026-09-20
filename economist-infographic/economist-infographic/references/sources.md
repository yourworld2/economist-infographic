# Sources and Confidence

Where every rule in this skill came from, with a confidence rating. When in doubt, defer to the higher-confidence source.

## Primary sources (high confidence)

### The Economist Design System (production)

- **URL**: `https://design-system.economist.com/`
- **Pages consulted**:
  - `/` (top-level nav)
  - `/foundations/colour/palettes` — full design-system colour palette with hex values
  - `/foundations/typography/typefaces` — font family declarations, **the explicit "Econ Sans Condensed — For charts and interactive graphics" instruction**
  - `/foundations/typography/modular-scale` — full type scale 11–74 px
  - `/foundations/typography/line-height` — the 1.4 / 1.2 line-height switchover rule
  - `/foundations/grid/grid-spacing` and `/grid-layout` — 8 px base, 1/6/12 column grid, 12/16/24/32 px gap/gutter tokens
  - `/foundations/rules` — 8 rule variants
  - `/foundations/principles/design-principles` — 6 design principles: Less is more, Deliberate typography, Visual harmony, Clear wayfinding, Intelligence and wit, Recognisable consistency
- **Confidence**: high. This is the production design system for the current masthead.

### economist-data-team (open-source, 2016 archive)

- **Org**: `https://github.com/economist-data-team`
- **Repos consulted**:
  - `component-dti-generic-d3` — the React + D3 base component
  - `euromap` — the React + D3 + Redux Euro map
  - `fed_projections` — Federal Reserve dot-plot interactive
  - `GermanyInteractive`, `migration-totals`, `unanimity`, `crony`, `syrianaid` — other 2016-era interactives
- **Files extracted**:
  - `econ_colours.js` and `colours.css` — complete chart palette
  - `euromap/css/typography.css` — Officina font stack
  - `euromap/css/index.css` — chart container, flag, and rule CSS
  - `fed_projections/js/time_ind_line_chart.js` — line chart engine source
  - `euromap/js/bar-chart.js` — bar chart engine source
  - `euromap/js/colour-legend.js` and `line-legend.js` — legend markup
- **Confidence**: high on the palette and font stack; **medium on chart code patterns** (only three projects sampled, 2016 vintage, current production stack may have moved on but the brand tokens have not).

### Chart style guide (referenced, not retrieved)

- **URL**: `https://design-system.economist.com/documents/CHARTstyleguide_20170505.pdf`
- **Status**: referenced by external sources (Tencent Cloud article), but the PDF itself was not retrievable in this research session (the host timed out on direct download, the file was not served by `web_fetch`). The rules inferred from the Tencent Cloud article and the Pengpai summary are consistent with the data-team code and the masthead's general style.
- **Confidence**: medium. Use the rules but verify against a specific case if you have access to the PDF.

## Secondary sources (medium confidence)

### 经济学人视觉风格指南 (中文整理)

- **URLs**:
  - `https://www.thepaper.cn/newsDetail_forward_21827913` (Pengpai / 澎湃新闻, 2023-02-07, author 丑丑姐姐)
  - `https://cloud.tencent.com/developer/article/2138472` (Tencent Cloud)
- **Content**: Both are Chinese-language summaries of the same official PDF. They confirm the chart-type taxonomy (Bar/column side-by-side, Bar/column stacked, Lines side-by-side, Lines stacked, Thermometer, Scatter, Pie/doughnut, Double-scale, Blob heads, Timeline) and the colour-ramp-by-series-type rule (light → dark for time series, contrasting hues for categories). They do not provide specific hex values.
- **Confidence**: medium. The taxonomy matches the data-team code; the colour-ramp rule is a reasonable inference.

### Office of Communications / typography practice (general)

- **URL**: `https://cloud.tencent.com/developer/article/2138472` and similar Chinese-language typography guides
- **Content**: General PPT font-size guidance (演讲型 PPT 18–28 pt; 阅读型 PPT 12–16 pt minimum 10 pt)
- **Confidence**: medium. These are general best-practice rules, not Economist-specific.

## Tertiary sources (low confidence, used for context only)

- `https://infographics.economist.com/` — listed as "The Economist Infographics server"; unreachable in this session. Possibly retired, possibly IP-restricted.
- `https://economist.com/graphic-detail` article pages — paywalled, all chart graphics are PNG exports rather than inline SVG; only confirms the page chrome (kicker, title, byline, source).

## Conflicts and resolutions

| Topic | Source A | Source B | Resolution |
|---|---|---|---|
| Brand red | Design System: `#E3120B` | Data-team CSS: `#E30010`; Data-team JS: `#e11b17` | Use `#E3120B` (Design System is newer). The other two are legacy aliases; use them only if reproducing archived assets. |
| Chart font | Design System: "Econ Sans Condensed — For charts" | Data-team CSS: `Officina` (with `Calibri` fallback) | Use the Design System token. The data-team CSS predates the Condensed variant being broadly available. |
| Greys | Design System: `--london-35 = #595959` | Data-team: `--grey-3 = #5E5E60` | These are very close (off by one digit). Use the Design System value; the data-team value reflects a slightly different grey ramp. |
| Bar gutter | Data-team: `gutter = 20` | Various style guides: "50–80% of bar width" | Either is fine; in the templates we use 20 px absolute, which works for the 595/640 px column widths. |

## What this skill does NOT cover

- The current production interactive stack (post-2017): the data-team org has been dormant since 2016, and the live interactives on `interactive.economist.com` may use a different framework. The skill assumes the **brand tokens are stable** (true) and the **chart aesthetic is stable** (very likely true but unverified for 2024+ work).
- Print pre-press (CMYK conversions, bleed, crop marks): out of scope. The skill delivers RGB.
- Multi-slide decks: the skill produces a **single slide** with a single chart. For a full Economist-style deck, repeat the recipe per slide, with consistent title/source formatting.
- Animated / interactive SVGs: the skill delivers **static** SVGs. For interactive charts (with hover, transitions), use D3 or React and follow the same design tokens.

## Maintenance

If the design system is updated, re-check:
- `/foundations/colour/palettes` — confirm `#E3120B` is still the brand red
- `/foundations/typography/typefaces` — confirm the chart font recommendation

If the masthead publishes a new chart style guide PDF, re-read the bar/line/stacked sections and update `references/chart-types.md`.
