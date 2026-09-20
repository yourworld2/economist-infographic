# Code Templates

Drop-in HTML + SVG templates for the most common chart types. All templates use the **classic-crimson** mood by default. Switch the variables at the top to switch moods.

The wrapper (kicker, title, standfirst, flag, source line) is identical across all chart types — only the SVG body changes.

## Common wrapper

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>CHART TITLE</title>
<style>
  :root {
    --red: #E3120B;
    --ink: #1A1719;
    --grey-3: #5E5E60;
    --grey-7: #ACADB0;
    --grey-9: #CBCCCE;
    --bg: #FFFFFF;
    --serif: 'Milo TE', 'Officina', Georgia, serif;
    --sans:  'Econ Sans', 'Inter', 'Calibri', Arial, sans-serif;
    --cond:  'Econ Sans Condensed', 'Inter Tight', 'Arial Narrow', sans-serif;
  }
  body { margin: 0; background: var(--bg); font-family: var(--sans); color: var(--ink); }
  .chart-block {
    width: 640px; margin: 24px auto; padding: 16px;
    position: relative; box-sizing: border-box;
  }
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
    font-family: var(--sans);
  }
  h1 {
    margin: 0 0 4px 28px; font-family: var(--sans); font-weight: 700;
    font-size: 22px; line-height: 1.2; color: var(--ink);
  }
  .standfirst {
    margin: 0 0 16px 28px; font-size: 14px; color: var(--grey-3);
  }
  svg { display: block; margin-left: 28px; }
  .source {
    margin: 12px 0 0 28px; font-size: 12px; color: var(--grey-3);
  }
</style>
</head>
<body>
  <div class="chart-block">
    <div class="flag"></div>
    <div class="kicker">CATEGORY</div>
    <h1>One-sentence title with a verb</h1>
    <p class="standfirst">Optional one-sentence dek.</p>
    <!-- SVG GOES HERE -->
    <p class="source">Source: <name></p>
  </div>
</body>
</html>
```

## Line chart (single protagonist series)

```html
<svg width="560" height="280" viewBox="0 0 560 280" role="img" aria-label="Description">
  <!-- y axis ticks and labels -->
  <g class="axis" font-family="var(--cond)" font-size="12" fill="#1A1719">
    <line x1="40"  y1="40"  x2="40"  y2="220" stroke="#1A1719" stroke-width="1"/>
    <line x1="40"  y1="220" x2="540" y2="220" stroke="#1A1719" stroke-width="1"/>
    <text x="36" y="44"  text-anchor="end">300</text>
    <text x="36" y="104" text-anchor="end">200</text>
    <text x="36" y="164" text-anchor="end">100</text>
    <text x="36" y="224" text-anchor="end">0</text>
    <!-- x axis labels -->
    <text x="40"  y="240" text-anchor="middle">2019</text>
    <text x="165" y="240" text-anchor="middle">2020</text>
    <text x="290" y="240" text-anchor="middle">2021</text>
    <text x="415" y="240" text-anchor="middle">2022</text>
    <text x="540" y="240" text-anchor="middle">2023</text>
  </g>
  <!-- data line -->
  <polyline
    points="40,200 165,140 290,170 415,90 540,60"
    fill="none" stroke="#E3120B" stroke-width="2"
  />
  <!-- data points -->
  <g fill="#E3120B">
    <circle cx="40"  cy="200" r="3"/>
    <circle cx="165" cy="140" r="3"/>
    <circle cx="290" cy="170" r="3"/>
    <circle cx="415" cy="90"  r="3"/>
    <circle cx="540" cy="60"  r="3"/>
  </g>
  <!-- last-point callout -->
  <g font-family="var(--sans)" font-size="12" fill="#1A1719">
    <line x1="540" y1="60" x2="540" y2="40" stroke="#1A1719" stroke-width="0.5"/>
    <text x="540" y="34" text-anchor="end" font-weight="700">$2.40/lb</text>
  </g>
</svg>
```

## Bar chart (horizontal, sorted descending)

```html
<svg width="560" height="280" viewBox="0 0 560 280" role="img" aria-label="Description">
  <g font-family="var(--cond)" font-size="13" fill="#1A1719">
    <!-- category labels (left) -->
    <text x="0"   y="56">Germany</text>
    <text x="0"   y="96">France</text>
    <text x="0"   y="136">Italy</text>
    <text x="0"   y="176">Spain</text>
    <text x="0"   y="216">Netherlands</text>
    <!-- x axis (bottom) -->
    <line x1="100" y1="240" x2="540" y2="240" stroke="#1A1719" stroke-width="1"/>
    <text x="100" y="258" text-anchor="middle">0</text>
    <text x="210" y="258" text-anchor="middle">20</text>
    <text x="320" y="258" text-anchor="middle">40</text>
    <text x="430" y="258" text-anchor="middle">60</text>
    <text x="540" y="258" text-anchor="middle">80</text>
  </g>
  <!-- bars -->
  <g fill="#E3120B">
    <rect x="100" y="44"  width="380" height="24"/>
    <rect x="100" y="84"  width="290" height="24"/>
    <rect x="100" y="124" width="220" height="24"/>
    <rect x="100" y="164" width="160" height="24"/>
    <rect x="100" y="204" width="120" height="24"/>
  </g>
  <!-- data labels at end of each bar -->
  <g font-family="var(--cond)" font-size="13" font-weight="700" fill="#1A1719">
    <text x="488" y="61">76</text>
    <text x="398" y="101">58</text>
    <text x="328" y="141">44</text>
    <text x="268" y="181">32</text>
    <text x="228" y="221">24</text>
  </g>
</svg>
```

## Stacked bar with direct labelling (no tick marks)

```html
<svg width="560" height="280" viewBox="0 0 560 280" role="img" aria-label="Description">
  <g font-family="var(--cond)" font-size="12" fill="#1A1719">
    <text x="40"  y="60" text-anchor="middle">2019</text>
    <text x="180" y="60" text-anchor="middle">2020</text>
    <text x="320" y="60" text-anchor="middle">2021</text>
    <text x="460" y="60" text-anchor="middle">2022</text>
  </g>
  <g>
    <!-- Bar 1: stacked 4 segments -->
    <rect x="20"  y="80"  width="40" height="60"  fill="#1F2E7A"/>
    <rect x="20"  y="140" width="40" height="50"  fill="#475ED1"/>
    <rect x="20"  y="190" width="40" height="30"  fill="#D6DBF5"/>
    <text x="40"  y="118" text-anchor="middle" font-family="var(--cond)" font-size="11" font-weight="700" fill="#FFFFFF">35</text>
    <text x="40"  y="170" text-anchor="middle" font-family="var(--cond)" font-size="11" font-weight="700" fill="#FFFFFF">28</text>
    <!-- repeat for bar 2, 3, 4 -->
  </g>
  <!-- source is rendered in HTML, not SVG -->
</svg>
```

## Scatter plot

```html
<svg width="560" height="320" viewBox="0 0 560 320" role="img" aria-label="Description">
  <g font-family="var(--cond)" font-size="12" fill="#1A1719">
    <line x1="60" y1="40" x2="60" y2="260" stroke="#1A1719" stroke-width="1"/>
    <line x1="60" y1="260" x2="540" y2="260" stroke="#1A1719" stroke-width="1"/>
    <text x="54" y="44"  text-anchor="end">100</text>
    <text x="54" y="154" text-anchor="end">50</text>
    <text x="54" y="264" text-anchor="end">0</text>
    <text x="60"  y="280" text-anchor="middle">0</text>
    <text x="300" y="280" text-anchor="middle">50</text>
    <text x="540" y="280" text-anchor="middle">100</text>
  </g>
  <g fill="#E3120B" fill-opacity="0.6" stroke="#1A1719" stroke-width="0.5">
    <!-- replace with real data -->
    <circle cx="120" cy="200" r="5"/>
    <circle cx="180" cy="180" r="5"/>
    <circle cx="240" cy="140" r="5"/>
    <circle cx="320" cy="100" r="5"/>
    <circle cx="400" cy="80"  r="5"/>
  </g>
  <!-- highlight a notable point -->
  <g>
    <circle cx="320" cy="100" r="8" fill="#E3120B" stroke="#FFFFFF" stroke-width="1.5"/>
    <line x1="320" y1="92" x2="320" y2="60" stroke="#1A1719" stroke-width="0.5"/>
    <text x="320" y="54" text-anchor="middle" font-family="var(--sans)" font-size="12" font-weight="700" fill="#1A1719">The notable one</text>
  </g>
</svg>
```

## Thermometer / bullet

```html
<svg width="560" height="200" viewBox="0 0 560 200" role="img" aria-label="Description">
  <g font-family="var(--cond)" font-size="12" fill="#1A1719">
    <text x="0" y="60">Metric A</text>
    <text x="0" y="120">Metric B</text>
    <text x="0" y="180">Metric C</text>
  </g>
  <g>
    <!-- track backgrounds -->
    <rect x="120" y="44"  width="380" height="20" fill="#F2F2F2"/>
    <rect x="120" y="104" width="380" height="20" fill="#F2F2F2"/>
    <rect x="120" y="164" width="380" height="20" fill="#F2F2F2"/>
    <!-- value bars -->
    <rect x="120" y="44"  width="240" height="20" fill="#E3120B"/>
    <rect x="120" y="104" width="180" height="20" fill="#E3120B"/>
    <rect x="120" y="164" width="320" height="20" fill="#E3120B"/>
    <!-- target ticks -->
    <line x1="420" y1="40" x2="420" y2="68"  stroke="#1A1719" stroke-width="2"/>
    <line x1="360" y1="100" x2="360" y2="128" stroke="#1A1719" stroke-width="2"/>
    <line x1="480" y1="160" x2="480" y2="188" stroke="#1A1719" stroke-width="2"/>
    <!-- target labels -->
    <text x="420" y="36" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="#1A1719">target</text>
    <text x="360" y="96" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="#1A1719">target</text>
    <text x="480" y="156" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="#1A1719">target</text>
    <!-- value labels at end -->
    <text x="368" y="58" font-family="var(--cond)" font-size="13" font-weight="700" fill="#1A1719">63%</text>
    <text x="308" y="118" font-family="var(--cond)" font-size="13" font-weight="700" fill="#1A1719">47%</text>
    <text x="448" y="178" font-family="var(--cond)" font-size="13" font-weight="700" fill="#1A1719">84%</text>
  </g>
</svg>
```

## Horizontal timeline

```html
<svg width="560" height="120" viewBox="0 0 560 120" role="img" aria-label="Description">
  <line x1="40" y1="60" x2="520" y2="60" stroke="#1A1719" stroke-width="1"/>
  <g font-family="var(--sans)" font-size="12" fill="#1A1719">
    <text x="40"  y="80" text-anchor="middle">2018</text>
    <text x="160" y="80" text-anchor="middle">2019</text>
    <text x="280" y="80" text-anchor="middle">2020</text>
    <text x="400" y="80" text-anchor="middle">2021</text>
    <text x="520" y="80" text-anchor="middle">2022</text>
  </g>
  <g fill="#1A1719">
    <circle cx="40"  cy="60" r="4"/>
    <circle cx="160" cy="60" r="4"/>
    <circle cx="280" cy="60" r="4"/>
    <circle cx="400" cy="60" r="4"/>
    <circle cx="520" cy="60" r="4"/>
  </g>
  <g font-family="var(--sans)" font-size="11" fill="#1A1719">
    <text x="40"  y="40" text-anchor="middle">Event A</text>
    <text x="160" y="40" text-anchor="middle">Event B</text>
    <text x="280" y="100" text-anchor="middle">Event C (below)</text>
    <text x="400" y="40" text-anchor="middle">Event D</text>
    <text x="520" y="100" text-anchor="middle">Event E (below)</text>
  </g>
  <!-- highlight the most important event with red flag -->
  <g>
    <rect x="276" y="20" width="8" height="20" fill="#E3120B"/>
    <text x="280" y="14" text-anchor="middle" font-family="var(--sans)" font-size="11" font-weight="700" fill="#E3120B">KEY EVENT</text>
  </g>
</svg>
```

## Helper: scale function (JavaScript)

When the data is too tedious to convert by hand, use a small JS helper to map data → pixel coordinates. The same math works in Python, D3, or any language.

```js
// Linear scale: maps data domain to pixel range
function scale(value, dMin, dMax, pMin, pMax) {
  return pMin + ((value - dMin) / (dMax - dMin)) * (pMax - pMin);
}

// Band scale: for categorical x positions (horizontal bars, side-by-side bars)
function band(index, count, pMin, pMax, gap = 20) {
  const bandWidth = (pMax - pMin) / count;
  return pMin + index * bandWidth + gap / 2;
}

// example: x positions for 5 categories in [100, 500]
// band(0, 5, 100, 500) -> 110
// band(1, 5, 100, 500) -> 190
// ...
```

## Output checklist (per chart)

- [ ] Background is `#FFFFFF` (no cream unless print simulation requested)
- [ ] 10×30 red flag in the top-left of the chart block
- [ ] 2 px red top border on the chart block
- [ ] Kicker in red, all-caps, 11–13 px
- [ ] Title is a sentence with a verb
- [ ] Standfirst is optional, one sentence
- [ ] Source line at the bottom, 12 px, grey
- [ ] No gridlines beyond axis ticks
- [ ] No emoji, no decorative icons
- [ ] Self-contained: no external `<link>`, no `<script>`, no `<img>`
- [ ] File is HTML (one file) or SVG (one file), not a folder
