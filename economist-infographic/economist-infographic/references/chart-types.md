# Chart Type Rules

The masthead's chart style guide establishes a default for each chart type, including which colour ramp to use, when to drop the gridlines, and what to do with the tick marks. This file is the per-type rule book.

## Bar / column (side-by-side)

**Use when**: comparing discrete categories at one point in time, or comparing peer groups.

- Sort by value, **descending**, longest bar at the top (horizontal) or left (vertical). Never sort alphabetically.
- Gap between bars: 20 px (in the data-team D3 source: `gutter = 20`). Or 50–80% of the bar width, whichever is smaller.
- Bar fill: solid colour, no gradient, no border. 1 px border in the series colour is acceptable on small multiples for definition.
- Y-axis: tick labels on the left, no axis line beyond the ticks, no horizontal gridlines.
- X-axis: category labels under the bars, 0/45/90° rotation as needed. No axis line.
- **Time-series side-by-side** (e.g. one bar per year for the same metric): use the **same hue, light → dark** as years progress. 2015 = `--grey-3`, 2016 = `--grey-2`, 2017 = `--london-10`.
- **Category side-by-side** (e.g. one bar per company for the same metric): use **contrasting hues**, ideally from different accent families (Chicago + Singapore, for example).

**Anti-patterns**: 3D bars, exploded bars, gradient fills, sorted alphabetically, "creative" tilted bars.

## Bar / column (stacked)

**Use when**: showing composition over time, or showing part-to-whole across many categories.

- **If there are few segments** (≤ 4): **delete the tick marks entirely** and label each segment's value directly inside the bar segment in white (if the bar is dark) or in the bar's colour (if the bar is light). This is the explicit style-guide instruction.
- **If there are many segments** (> 4): keep the y-axis, but reduce the tick density; show every other or every fifth label.
- Stack order: largest segment at the bottom, smallest at the top, in all bars (consistent ordering).
- Colour ramp: light → dark, single hue if the segments represent time slices. Multi-hue if the segments represent distinct categories (use the categorical palette from your chosen mood).
- 100% stacked bar is a special case: use it for normalised comparisons when absolute magnitude is not the point.

**Anti-patterns**: 3D stacked, exploded segments, more than 6 segments, rainbow stacking.

## Line (side-by-side)

**Use when**: showing trends over time, ≤ 4 series.

- One series = one line. If you have 5+ series, switch to small multiples.
- Line stroke: **2 px** for the protagonist, 1.25 px for context. **Never** set `stroke-width` smaller than 1 px in print.
- Use `<line>` segments (data-team style) or a single `<path>`, not a mix.
- Data points: `<circle r="3">` on the protagonist series; **omit points** on context series to reduce ink. Highlighted/hovered point: `<circle r="6">` with fill at `rgba(series, 0.5)`.
- Inactive/non-highlighted points: `fill: rgba(series, 0.25); stroke: series`.
- Use **Voronoi cells** as invisible hover targets (data-team pattern) when the chart is interactive; not needed for static SVGs.
- X-axis: years or months at the bottom, no axis line, only the tick marks (1 px).
- Y-axis: numerical labels at the left, no axis line, 1 px ticks.
- Highlight the last data point with a label and a small dot — this is the "current state" callout and is the standard Economist ending.

**Anti-patterns**: smoothed/spline interpolation (use straight lines), multi-line plots with > 4 series, dual y-axes (use small multiples or normalised values), gradient fills under the line unless it's an area chart.

## Line (stacked) / area (stacked)

**Use when**: showing how parts-of-whole evolve over time, or showing a cumulative trend.

- Stack order: largest at the bottom, consistent across all x-positions.
- Colour ramp: light → dark, single hue family. Bottom (largest) = `--chicago-30` or similar, top (smallest) = `--chicago-90`.
- For pure area (single series): use the colour at 30% opacity, with a 2 px solid stroke on top. This reads as "filled area with a defined edge".
- X-axis ticks: every year or quarter, no axis line.
- Y-axis: drop if the parts are absolute numbers and the total is well-known; show the total as a label inside the topmost segment.

**Anti-patterns**: stacked area with > 5 series, area charts where the categories don't sum meaningfully, area + line combos unless explicitly justified.

## Thermometer / bullet chart

**Use when**: showing a single metric against a target or scale, or ranking items on a single dimension.

- The data-team style: a horizontal bar with a target tick.
- **Max 4 series**, else switch to a small-multiples layout. Explicit style-guide rule.
- Background "track" in `--london-95` (lightest grey).
- Foreground "value" in the protagonist hue.
- Target tick: 2 px vertical line in `--london-10` with a label above it.
- Labels: value at the right end of the bar, target above the tick.

**Anti-patterns**: more than 4 series in a single thermometer, gradient fills on the track, multiple target ticks without legend.

## Scatter plot

**Use when**: showing the relationship between two continuous variables, or a distribution in two dimensions.

- Dot size: 4–6 px diameter, semi-transparent (alpha 0.6) so overlaps are visible. Do not increase to 12+ px; the data density is more important than the individual data point.
- Dot fill: protagonist series in its hue, **outlined** in `--london-10` at 0.5 px for definition.
- Highlighted/important points: 8 px, full opacity, with a 1 px white halo to lift them off the page.
- Axes: numeric on both, no gridlines beyond light reference lines at quartile values.
- Annotation: a 1-sentence label at one or two notable points, with a hairline lead line.

**Anti-patterns**: bubble charts where bubble area encodes a third variable (use a small multiples or a different encoding), rainbow-coloured points, regression lines without a confidence band.

## Pie / doughnut

**Use sparingly.** The masthead avoids pie charts. Use them only when:

- The composition is the point and the parts are mutually exclusive
- There are **at most 4 slices** (explicit style-guide rule)
- The largest slice is at the top (12 o'clock) and the slices go clockwise

If you need pie, **prefer horizontal bar** instead — it sorts better, labels better, and is more accessible.

- Colour ramp: protagonist slice in the lead hue, supporting slices in greys or a single-hue family.
- Labels: outside the pie with a short lead line, never on the slice.
- **Doughnut** is acceptable if you have 2–3 slices and need the centre for a total label.

**Anti-patterns**: 3D pie, exploded pie, > 4 slices, rainbow slices, percentage-only labels (show the absolute number too).

## Double-scale / dual-axis

**Use when**: two metrics that share an x-axis but have very different scales, and the relationship between them is the story.

- The masthead uses this **sparingly** and only when the alternative (small multiples) would lose the cross-axis relationship.
- Each axis in the colour of its series. Y-axis labels and ticks coloured to match the line.
- Series 1 = left axis, Series 2 = right axis. **Never** a third axis.
- A short annotation explaining the scales: "Left: USD billions, inflation-adjusted. Right: % change year-on-year."

**Anti-patterns**: more than two axes, two axes that share a unit (use a single normalised axis), diverging colour palettes that make the two series feel unrelated.

## Timeline / horizontal event chart

**Use when**: showing events or milestones along a time axis, with annotations.

- Single horizontal rule (1 px) as the spine, with year/month labels below.
- Events: small filled circles (5 px) on the spine, alternating above and below to avoid label collisions.
- Event labels: 1-line, Econ Sans 12–13 px, `--london-10`.
- Highlight the most important event with a 10×30 red flag dropped from above the spine (or a red circle on the spine).
- **Mobile timeline**: a vertical spine with events stacked top to bottom; the same flag treatment.

**Anti-patterns**: spaghetti timelines with > 12 events without grouping, double-spine timelines, "ribbon" timelines that span a full chart area without information density.

## Choropleth (map)

**Use when**: showing geographic variation in a single metric.

- Single-hue sequential palette: lightest = `--chicago-90` (or `--red-90` in crimson mood), darkest = `--chicago-30`. Never rainbow, never diverging without a clear midpoint.
- Stroke between regions: 0.5 px `--london-10`.
- Labels for major regions only. Smaller regions: 1-letter abbreviation, 9 px, `--london-35`.
- Legend: horizontal, single-hue gradient bar, with min/max values labelled.
- No 3D extrusion, no rotation, no globe.

**Anti-patterns**: rainbow palettes, double-encoding (size + colour), Mercator projection without acknowledgment of distortion.

## Small multiples

**Use when**: a chart with too many series, or comparing the same metric across many categories.

- One mini-chart per panel, all sharing the same x and y scales.
- 2 × 2 or 2 × 3 grid; **avoid** 3 × 4+ grids (labels collide).
- Panel titles: 12–13 px Econ Sans, `--london-10`, one or two words.
- No individual source lines per panel — one source line at the bottom of the grid.
- Sort panels in a meaningful order (alphabetical, by magnitude, by chronology), not random.

**Anti-patterns**: free-form positioning, mismatched scales between panels, individual legends per panel.

## Common mistakes (any chart type)

1. **3D anything.** Always wrong. Use 2D.
2. **Gridlines beyond the axis ticks.** The masthead drops them. If you must keep them, use `--london-95` (lightest grey) at 0.5 px.
3. **Two serifs at once.** Pick one (Milo TE for serif-heavy moods, Econ Sans for sans-heavy).
4. **Old-style figures in data labels.** Use lining figures for numbers on the chart; reserve old-style for running body text.
5. **Decorative icons, emoji, or illustrations** inside the chart area. Pictograms are OK only in the headline section (e.g. a coffee bean icon next to a "Coffee" kicker), not inside the data.
6. **Two saturated hues on adjacent series.** Always use the protagonist/context split; if you have two saturated series, they're competing for attention and the reader can't tell which is the story.
7. **Missing source line.** A chart without a source is not a Economist chart. Always include one.
