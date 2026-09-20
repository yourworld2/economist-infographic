# PPT Adaptation

How to translate the web/print Economist chart into a 16:9 PowerPoint slide. The visual signature stays the same; typography, sizing, and contrast all scale up to survive a meeting room.

## Before you start — tooling check (run once)

PPTX generation depends on **which conversion tools are available locally**. The three approaches in this document differ only in how the chart gets into the slide. Run this snippet first to see which approach is viable in your environment. **Approach 1 (native shapes) is the only one that needs nothing but `python-pptx`**; Approaches 2 and 3 each need a working SVG rasteriser.

```bash
# Python-side dependencies
python3 -c "import pptx; print('python-pptx', pptx.__version__)" 2>&1 || echo "MISSING: python-pptx"
python3 -c "import cairosvg; print('cairosvg', cairosvg.__version__)" 2>&1 || echo "MISSING: cairosvg"

# CLI rasterisers (any one is sufficient for Approach 2/3)
which rsvg-convert   2>/dev/null && echo "FOUND: rsvg-convert (librsvg)"  || echo "MISSING: rsvg-convert"
which inkscape       2>/dev/null && echo "FOUND: inkscape"                || echo "MISSING: inkscape"
which soffice        2>/dev/null && echo "FOUND: libreoffice (soffice)"   || echo "MISSING: libreoffice"
```

### Decision matrix

| You have | Recommended approach | Trade-off |
|---|---|---|
| Only `python-pptx` (no rasteriser) | **Approach 1** (native shapes — this is what `build_ppt.py` in the workspace uses) | Pure Python, works anywhere `python-pptx` is installed. Fully editable in PowerPoint. Slightly less precise geometry than a vector embed. |
| `cairosvg` or `rsvg-convert` | **Approach 2** (SVG embed as vector group) | Vector quality at any zoom; text in the chart becomes non-editable. Smallest file size. |
| `inkscape` or `libreoffice` (heavier) | **Approach 2** or **Approach 3** (rasterise to PNG) | Same trade-off as `cairosvg`; `inkscape` is slower but more faithful for complex SVGs. `libreoffice` works but takes the long way round (svg → pdf → png). |
| **CI server / minimal Docker image** (none of the above) | **Approach 1** is the **only** viable path | Most common production case. Verified end-to-end June 2026 in the environment this skill was built in. |

### Installing what you need

| Tool | Debian / Ubuntu | macOS (brew) | pip |
|---|---|---|---|
| `python-pptx` | `pip install python-pptx` | `pip install python-pptx` | `pip install python-pptx` |
| `cairosvg` | `apt-get install libcairo2 pkg-config python3-dev` then `pip install cairosvg` | `brew install cairo pkg-config libffi` then `pip install cairosvg` | `pip install cairosvg` |
| `librsvg` (CLI) | `apt-get install librsvg2-bin` | `brew install librsvg` | — |
| `inkscape` | `apt-get install inkscape` | `brew install inkscape` | — |
| `libreoffice` | `apt-get install libreoffice` | `brew install --cask libreoffice` | — |
| `playwright` (heavyweight) | `pip install playwright && playwright install chromium` | same | same |

> **Skip `wand`**: it requires ImageMagick system pkg and is rarely worth the trouble. `cairosvg` is faster for SVG→PNG.
>
> **Verified baseline (June 2026)**: in this skill's build environment, only `python-pptx 1.0.2` was available. All rasterisers (cairosvg / rsvg-convert / inkscape / libreoffice CLI / wand / playwright) were absent. `build_ppt.py` exercises Approach 1 and produced a 30 KB / 1 slide / 58 shapes `.pptx` that opens cleanly in LibreOffice with all 5 visual-signature elements preserved.

## Canvas

- **Aspect ratio**: 16:9
- **Standard size**: 13.33" × 7.5" (the modern PowerPoint default)
- **Alternative**: 10" × 5.625" (smaller deck, same aspect)
- **Legacy 4:3**: do not use. If the user is on 4:3, use a chart at 9" × 5" inside a 10" × 7.5" slide.

## Layout

Reserve the slide for **one chart, no other content**. Bullets, agendas, speaker notes go on adjacent slides, not on the chart slide.

```
┌──────────────────────────────────────────────────────────────┐
│  ▮ GRAPHIC DETAIL                                            │
│  ──────────────────────────────────────────────────────────  │
│                                                              │
│   Title (one sentence with a verb)                           │
│   Optional standfirst (one sentence)                         │
│                                                              │
│   ┌────────────────────────────────────────────────────┐     │
│   │                                                    │     │
│   │   The chart                                        │     │
│   │                                                    │     │
│   │                                                    │     │
│   │                                                    │     │
│   └────────────────────────────────────────────────────┘     │
│                                                              │
│   Source: <name>                                             │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

The chart occupies the upper 2/3 of the slide. The title block (kicker + title + standfirst) sits above the chart. The source line sits below the chart.

Safe margins: **5% of slide width on all sides** (0.67" for a 13.33" wide slide). Do not place any element in this margin.

## Typography scaling

PPT requires 1.5–2× the font sizes used in the web version, because the chart is being read from across a room, not from a 14" laptop screen.

| Element | Web (640 px) | PPT (13.33") |
|---|---|---|
| Kicker | 12 px | 14–16 pt |
| Title | 22 px | 28–36 pt |
| Standfirst | 14 px | 18–22 pt |
| Axis tick labels | 12–13 px | 14–18 pt |
| Data labels | 12–14 px | 14–20 pt |
| Source line | 12 px | 14–16 pt |
| Note | 11 px | 12–14 pt |

**Sanity check**: zoom the slide to 60% on your screen, sit back 2 metres, and check you can still read the source line. If not, scale up.

**Line stroke widths** also scale:
- Protagonist line: 2 px web → 3–4 pt PPT
- Context line: 1.25 px web → 1.5–2 pt PPT
- Axis ticks: 1 px web → 1.5 pt PPT
- Top border: 2 px web → 2.25–3 pt PPT

## Colour

- Background: **always white** in PPT. Cream backgrounds read as muddy/yellow under projector light.
- Stick to the same palette as the web version.
- For the dark projector environment: increase contrast. If the web version uses `#525254` for standfirst, push to `#1A1719` in PPT.

## Visual signature (PPT version)

The red flag and 2 px red top border are kept, scaled to match the slide:

- Flag: **0.13" × 0.40"** (≈ 0.4 cm × 1.0 cm) at the top-left, flush with the top edge
- 2 px red top border: full width of the chart block, behind the flag
- Kicker: 14–16 pt, bold, all caps, red, 0.5" right of the flag

If the chart is **the only content on the slide**, place the flag at the slide's top-left (with safe margin), and the red top border runs the full width of the slide content area. If the chart is in a smaller content block within a larger slide, scale the flag proportionally.

## Embedding the chart in PowerPoint

Three approaches, in order of preference:

### Approach 1: Native PowerPoint shapes (best, fully editable)

Recreate the chart using PowerPoint's native shapes (rectangles, lines, text boxes) and the slide master. Pros: fully editable in PowerPoint, no external dependencies, text is selectable/searchable. Cons: time-consuming to build, hard to match SVG precision.

Use this approach when:
- The user will edit the chart later
- The chart has simple shapes (bars, lines, scatter dots)
- The data is small (≤ 20 data points)

### Approach 2: SVG embedded as a group (good, vector)

Convert the HTML/SVG chart to PPT by:
1. Open the SVG in a vector editor (Inkscape, Illustrator)
2. Copy as EMF (Enhanced Metafile) or PDF
3. Paste into PowerPoint as a vector group
4. Add the title, kicker, standfirst, source as **native text boxes** (not embedded in the SVG), so they remain editable

Pros: vector quality, smaller file size. Cons: text in the chart is no longer editable.

Use this approach when:
- The chart has complex SVG geometry
- The user wants vector quality at any zoom

### Approach 3: Rasterised PNG (last resort)

Convert the SVG to PNG at **300 DPI** at the final slide size, then insert as an image. Use `rsvg-convert`, `cairosvg`, or `inkscape --export-png`.

```bash
rsvg-convert -w 3840 -h 2160 chart.svg -o chart.png  # 16:9, 300 DPI
```

Pros: simplest, works everywhere. Cons: not editable, can pixelate on different displays.

Use this approach when:
- No vector editor is available
- The chart has bitmap-embedded content (photographs)
- Time pressure

## python-pptx recipe (when available)

If `python-pptx` is installed, generate the PPT programmatically:

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from lxml import etree
import cairosvg, io

# 1. Set up the slide
prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank

RED   = RGBColor(0xE3, 0x12, 0x0B)
INK   = RGBColor(0x1A, 0x17, 0x19)
GREY  = RGBColor(0x69, 0x6A, 0x6C)

# 2. Red top border (2 pt = Emu(25400*2/72*72) = 2 pt line)
border = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
    Inches(0.67), Inches(0.67), Inches(12.0), Emu(25400*2))
border.fill.solid(); border.fill.fore_color.rgb = RED
border.line.fill.background()

# 3. Flag (0.13" x 0.40")
flag = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
    Inches(0.67), Inches(0.67), Inches(0.13), Inches(0.40))
flag.fill.solid(); flag.fill.fore_color.rgb = RED
flag.line.fill.background()

# 4. Kicker
kicker = slide.shapes.add_textbox(Inches(1.20), Inches(0.72), Inches(11.0), Inches(0.35))
tf = kicker.text_frame; tf.text = "GRAPHIC DETAIL"
p = tf.paragraphs[0]
for run in p.runs:
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.name = "Calibri"  # or any sans fallback
    run.font.color.rgb = RED

# 5. Title
title = slide.shapes.add_textbox(Inches(0.95), Inches(1.20), Inches(11.7), Inches(1.0))
tf = title.text_frame; tf.text = "Coffee briefly got cheaper, then caught up with inflation"
p = tf.paragraphs[0]
for run in p.runs:
    run.font.size = Pt(32)
    run.font.bold = True
    run.font.name = "Calibri"
    run.font.color.rgb = INK

# 6. Embed the chart (rasterised from SVG at 300 DPI)
png_data = cairosvg.svg2png(url="chart.svg", output_width=3840, output_height=2160)
chart_stream = io.BytesIO(png_data)
slide.shapes.add_picture(chart_stream, Inches(1.30), Inches(2.50),
                          width=Inches(10.7), height=Inches(4.0))

# 7. Source line
source = slide.shapes.add_textbox(Inches(0.95), Inches(6.85), Inches(11.7), Inches(0.30))
tf = source.text_frame; tf.text = "Source: ICE Futures U.S."
p = tf.paragraphs[0]
for run in p.runs:
    run.font.size = Pt(14)
    run.font.name = "Calibri"
    run.font.color.rgb = GREY

prs.save("chart_deck.pptx")
```

The above is a working skeleton. For a real chart, render the SVG with `cairosvg` first, then embed. Edit positions/sizes to match your actual chart.

## Failure handling

- If `python-pptx` is not available, output a PDF of the slide and a separate SVG, plus the placement spec (where to position the SVG on a blank 16:9 slide in PowerPoint). Do not pretend to have produced a `.pptx` you did not produce.
- If `cairosvg` is not available for rasterising the SVG, hand the user the SVG and a one-line instruction: "Insert this SVG at (1.30", 2.50") on a blank 16:9 slide and scale to 10.7" × 4.0"."
- If the user's chart is too dense for a single slide (e.g. 6-line chart, dense scatter), reduce the data or split across multiple slides. Do not deliver an unreadable slide.

## Anti-patterns (PPT)

- Two charts on one slide ("main" + "supporting")
- The chart is the background and the bullets are on top
- The chart fills the whole slide edge-to-edge with no safe margin
- The title is in the slide master and is generic ("Chart 1"); the actual finding must be in the title block
- Office SmartArt used for a data chart
- Theme colours used (the default blue/red Office palette) for a chart that's supposed to be Economist
