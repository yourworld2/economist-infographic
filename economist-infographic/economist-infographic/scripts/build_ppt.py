#!/usr/bin/env python3
"""Generate a 16:9 PPT for the China GDP chart using python-pptx native shapes.

Approach 1 in references/ppt-adaptation.md: fully editable native shapes, no
external dependencies. Works in sandboxes where SVG rasterisers (cairosvg,
rsvg-convert, inkscape) are absent.

Usage:
    python3 build_ppt.py [--output eval_ppt_output.pptx]
"""
import argparse
import os
import subprocess

# ---- Step 1: environment check -----------------------------------------
print("=== STEP 1: ENVIRONMENT CHECK ===")

def have_python_module(name):
    try:
        __import__(name)
        return True
    except Exception:
        return False

def have_binary(name):
    try:
        r = subprocess.run(["which", name], capture_output=True, text=True, timeout=5)
        return bool(r.stdout.strip())
    except Exception:
        return False

env_status = {
    "python-pptx": have_python_module("pptx"),
    "cairosvg":    have_python_module("cairosvg"),
    "Pillow":      have_python_module("PIL"),
    "wand":        have_python_module("wand"),
    "playwright":  have_python_module("playwright"),
    "lxml":        have_python_module("lxml"),
    "rsvg-convert": have_binary("rsvg-convert"),
    "inkscape":     have_binary("inkscape"),
}
for k, v in env_status.items():
    print(f"  {k}: {'installed' if v else 'not found'}")

if not env_status["python-pptx"]:
    raise SystemExit("python-pptx is required: pip install python-pptx")

import pptx
print(f"  python-pptx version: {pptx.__version__}")

# ---- Step 2: design constants ------------------------------------------
SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5

# Margin: 5% of slide width = 0.67" on each side
MARGIN = 0.67

# Top border runs from x=MARGIN to x=SLIDE_W-MARGIN, full width
BORDER_LEFT   = MARGIN
BORDER_RIGHT  = SLIDE_W_IN - MARGIN
BORDER_WIDTH  = BORDER_RIGHT - BORDER_LEFT  # 12.0"
BORDER_TOP    = MARGIN                      # 0.67"
BORDER_THICK  = 0.04                        # ~3pt, visible on projectors

# Flag: 0.13" x 0.40", overlapping top border
FLAG_W = 0.13
FLAG_H = 0.40
FLAG_X = MARGIN
FLAG_Y = MARGIN  # sit on top of border

# Kicker: 0.2" right of flag
KICKER_X = FLAG_X + FLAG_W + 0.20
KICKER_Y = FLAG_Y + 0.04
KICKER_W = 6.0
KICKER_H = 0.32

# Title: 1 sentence, full width minus margins
TITLE_X = MARGIN + 0.30
TITLE_Y = MARGIN + 0.55
TITLE_W = SLIDE_W_IN - 2*MARGIN - 0.30
TITLE_H = 0.85

# Standfirst
STAND_X = TITLE_X
STAND_Y = TITLE_Y + TITLE_H + 0.05
STAND_W = TITLE_W
STAND_H = 0.35

# Chart area: upper 2/3
CHART_X = MARGIN + 0.30
CHART_Y = STAND_Y + STAND_H + 0.20
CHART_W = SLIDE_W_IN - 2*MARGIN - 0.40
CHART_H = 3.50

# Source
SRC_X = MARGIN + 0.30
SRC_Y = CHART_Y + CHART_H + 0.20
SRC_W = TITLE_W
SRC_H = 0.30

# ---- Step 3: build the slide -------------------------------------------
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

RED   = RGBColor(0xE3, 0x12, 0x0B)
INK   = RGBColor(0x1A, 0x17, 0x19)
GREY  = RGBColor(0x69, 0x6A, 0x6C)
TINT  = RGBColor(0xFB, 0xE6, 0xE5)  # pale red tint for shaded bands

prs = Presentation()
prs.slide_width  = Inches(SLIDE_W_IN)
prs.slide_height = Inches(SLIDE_H_IN)
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank

def fill_solid(shape, rgb):
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb
    shape.line.fill.background()

def add_rect(left_in, top_in, w_in, h_in, rgb):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left_in), Inches(top_in), Inches(w_in), Inches(h_in),
    )
    fill_solid(shp, rgb)
    return shp

def add_line(x1, y1, x2, y2, rgb, weight_pt=1.5):
    ln = slide.shapes.add_connector(
        1,  # MSO_CONNECTOR.STRAIGHT
        Inches(x1), Inches(y1), Inches(x2), Inches(y2),
    )
    ln.line.color.rgb = rgb
    ln.line.width = Pt(weight_pt)
    return ln

def add_text(left_in, top_in, w_in, h_in, text, size_pt, color,
             bold=False, italic=False, name="Calibri", align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(
        Inches(left_in), Inches(top_in), Inches(w_in), Inches(h_in))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Emu(0)
    tf.margin_top  = tf.margin_bottom = Emu(0)
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size_pt)
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = name
    r.font.color.rgb = color
    return tb

# 1. Red top border
add_rect(BORDER_LEFT, BORDER_TOP, BORDER_WIDTH, BORDER_THICK, RED)

# 2. Flag
add_rect(FLAG_X, FLAG_Y, FLAG_W, FLAG_H, RED)

# 3. Kicker
add_text(KICKER_X, KICKER_Y, KICKER_W, KICKER_H,
         "CHINA'S ECONOMY", 14, RED, bold=True)

# 4. Title
add_text(TITLE_X, TITLE_Y, TITLE_W, TITLE_H,
         "China's growth has cooled to less than half its 2010 pace",
         30, INK, bold=True)

# 5. Standfirst
add_text(STAND_X, STAND_Y, STAND_W, STAND_H,
         "Real annual GDP growth, %, 2010–2024",
         16, GREY)

# 6. Chart (native shapes) ----------------------------------------------
DATA = [
    (2010, 10.6), (2011,  9.6), (2012,  7.9), (2013,  7.8), (2014,  7.4),
    (2015,  7.0), (2016,  6.9), (2017,  6.9), (2018,  6.8), (2019,  6.0),
    (2020,  2.2), (2021,  8.4), (2022,  3.0), (2023,  5.2), (2024,  5.0),
]

Y_MIN, Y_MAX = 0, 12
# Inner plot area within the chart box
PLOT_L = CHART_X + 0.55
PLOT_R = CHART_X + CHART_W - 0.20
PLOT_T = CHART_Y + 0.20
PLOT_B = CHART_Y + CHART_H - 0.55
PLOT_W = PLOT_R - PLOT_L
PLOT_H = PLOT_B - PLOT_T

def x_of_year(year):
    idx = year - 2010
    return PLOT_L + idx * (PLOT_W / (len(DATA) - 1))

def y_of_val(val):
    return PLOT_T + (Y_MAX - val) * (PLOT_H / (Y_MAX - Y_MIN))

# Covid shaded band (2019-2022), drawn first so it sits behind the data line.
# python-pptx has no fill transparency, so we fake it with a pale tint.
band_l = x_of_year(2019) - (x_of_year(2020) - x_of_year(2019)) * 0.5
band_r = x_of_year(2022) + (x_of_year(2022) - x_of_year(2021)) * 0.5
add_rect(band_l, PLOT_T, band_r - band_l, PLOT_H, TINT)

# Axis lines
add_line(PLOT_L, PLOT_T, PLOT_L, PLOT_B, INK, 1.5)   # y axis
add_line(PLOT_L, PLOT_B, PLOT_R, PLOT_B, INK, 1.5)   # x axis

# Y axis tick labels (0, 2, 4, 6, 8, 10, 12)
for v in [0, 2, 4, 6, 8, 10, 12]:
    y = y_of_val(v)
    add_text(PLOT_L - 0.45, y - 0.13, 0.40, 0.26,
             str(v), 12, INK, align=PP_ALIGN.RIGHT)

# X axis tick labels (every other year)
for year in [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]:
    x = x_of_year(year)
    add_text(x - 0.30, PLOT_B + 0.05, 0.60, 0.26,
             str(year), 12, INK, align=PP_ALIGN.CENTER)

# Data line segments
for i in range(len(DATA) - 1):
    y0, y1 = DATA[i][1], DATA[i+1][1]
    add_line(x_of_year(DATA[i][0]), y_of_val(y0),
             x_of_year(DATA[i+1][0]), y_of_val(y1),
             RED, 3.0)

# Data points (small filled circles)
for year, val in DATA:
    shp = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        Inches(x_of_year(year) - 0.06),
        Inches(y_of_val(val) - 0.06),
        Inches(0.12), Inches(0.12),
    )
    fill_solid(shp, RED)

# Annotations
# 2010: 10.6% (above the point)
add_text(x_of_year(2010) - 0.30, y_of_val(10.6) - 0.45, 0.60, 0.26,
         "10.6%", 13, RED, bold=True, align=PP_ALIGN.CENTER)
# 2020 trough: 2.2% (below the point)
add_text(x_of_year(2020) - 0.30, y_of_val(2.2) + 0.08, 0.60, 0.26,
         "2.2%", 13, RED, bold=True, align=PP_ALIGN.CENTER)
# 2021 rebound: 8.4% (above)
add_text(x_of_year(2021) - 0.30, y_of_val(8.4) - 0.45, 0.60, 0.26,
         "8.4%", 13, RED, bold=True, align=PP_ALIGN.CENTER)
# 2024 end: 5.0% (above)
add_text(x_of_year(2024) - 0.40, y_of_val(5.0) - 0.45, 0.50, 0.26,
         "5.0%", 13, RED, bold=True, align=PP_ALIGN.CENTER)

# Covid annotation
covid_x = (x_of_year(2020) + x_of_year(2021)) / 2
add_text(covid_x - 0.80, PLOT_B + 0.30, 1.60, 0.26,
         "covid whiplash, 2020–22", 11, GREY, italic=True, align=PP_ALIGN.CENTER)

# 7. Source line
add_text(SRC_X, SRC_Y, SRC_W, SRC_H,
         "Source: National Bureau of Statistics of China",
         12, GREY, italic=True)

# Save
parser = argparse.ArgumentParser(description="Generate the 16:9 Economist-style PPTX demo")
parser.add_argument("--output", default="eval_ppt_output.pptx",
                    help="output .pptx path (default: ./eval_ppt_output.pptx)")
args = parser.parse_args()

out_path = args.output
prs.save(out_path)
size = os.path.getsize(out_path)
print(f"\n=== STEP 3: PPT GENERATED ===")
print(f"  Path: {out_path}")
print(f"  Size: {size} bytes ({size/1024:.1f} KB)")
print(f"  Slide count: {len(prs.slides)}")
print(f"  Slide size: {prs.slide_width/914400:.3f}\" x {prs.slide_height/914400:.3f}\"")
print(f"  Shape count on slide 1: {len(slide.shapes)}")
