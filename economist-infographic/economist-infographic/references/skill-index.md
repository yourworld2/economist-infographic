# Skill Index — `economist-infographic`
# 技能索引 — `economist-infographic`

> **30-second summary / 30 秒速览**: produces single, self-contained editorial charts or 16:9 PPT slides in *The Economist*'s Graphic Detail style. Outputs `.html` / `.svg` / `.pptx`. Four preset moods (newspaper-serious / classic-crimson / colorful-explainer / monochrome-spare) let the same data speak in different voices.
>
> 产出单文件、自包含的编辑风格图表或 16:9 PPT slide，风格对标 *The Economist* Graphic Detail 栏目。输出 `.html` / `.svg` / `.pptx` 三种格式。内置 4 种 mood 预设（newspaper-serious / classic-crimson / colorful-explainer / monochrome-spare），让同一份数据可以"换声线"产出多种视觉表达。

---

## 1. TL;DR / 速览

**EN** — Open the file. Read this index first if you have never used the skill. Then jump to the relevant `references/*.md`. The full procedure lives in `SKILL.md`.

**中文** — 第一次用这个 skill？先读这个索引。看完后按需要跳到 `references/*.md` 的对应章节。完整 8 步流程在 `SKILL.md`。

---

## 2. Trigger phrases / 触发关键词

### English / 英文

- "information graphic" / "infographic" / "news graphic" / "editorial chart"
- "data visualization chart" / "Daily Chart"-style chart
- "Economist-style chart" / "Economist-style visual" / "chart in the style of The Economist"
- "make me a chart that looks like *The Economist*"
- "embed Economist-style visuals in PPT / article / report"

### 中文 / Chinese

- 经济学人风格信息图 / 经济学人风格图表
- 新闻图表 / 每日图表风格
- PPT 数据图 / 报告插图
- Econ Sans 风格图表 / 杂志风格图表

### Do NOT use for / 不触发的场景

| English | 中文 |
|---|---|
| General UI design | 通用 UI 设计 |
| Logo work / brand identity | Logo / 品牌识别设计 |
| Web component libraries | Web 组件库 |
| Real-time / multi-component dashboards | 实时 / 多组件仪表盘 |
| Decorative graphics (no data) | 装饰性插图（无数据）|
| 3D / radar / sankey / bubble charts | 3D / 雷达 / 桑基 / 气泡图 |
| CMYK print pre-press | CMYK 印刷预压 |
| Multi-slide deck generation | 多页 PPT 套件自动生成 |

---

## 3. The four moods / 4 种 mood 预设

| Mood | English voice | 声线 (中文) | Title font | 配色 signature | When to pick / 何时用 |
|---|---|---|---|---|---|
| **classic-crimson** *(default)* | Daily Chart / Graphic Detail | 每日图表主声线 | Econ Sans 22 px (sans) | Single red protagonist + greys | **When unsure**. The most recognisable "Economist" voice. / 拿不准就用这个，最有辨识度。 |
| **newspaper-serious** | Authoritative, quiet | 严肃社论 | **Milo TE 22 px (serif)** | Near-monochrome, red ≤ 2 occurrences | Macro / policy / elections / finance / war / recession. / 宏观、政策、选举、金融、战争。 |
| **colorful-explainer** | Friendly, multi-hue, educational | 友好多色科普 | Econ Sans 24 px (sans) | **4 palette hues**; red is flag-only | Tech / consumer / science / election maps. / 科技、消费、科普、选举地图。 |
| **monochrome-spare** | Op-ed / research note / minimal | 极简研究笔记 | **Milo TE 22 px (serif)** | Black ink + at most one Chicago-30 accent; **1 px red rule replaces flag** | Op-eds, methodology charts, charts that must recede. / 社论、方法论、页脚小图。 |

Full recipes: `references/moods.md`. 完整配方：`references/moods.md`。

---

## 4. Chart types at a glance / 图表类型速查

| Type | EN — Use when | 中文 — 何时用 | Notes / 备注 |
|---|---|---|---|
| Line (single) | Trend over time, ≤ 2 series | 单一时间趋势，≤ 2 系列 | 2 px stroke, 3 px points, last-point callout / 末点标注 |
| Line (multi) | Trend, ≤ 4 series; else small multiples | 趋势，≤ 4 系列，否则用小倍数 | Direct-label, not legend / 直接标注，别用 legend |
| Bar (horizontal, sorted) | Compare categories at one time | 同时点比较多个类别 | Sort descending, longest at top / 降序排列 |
| Bar (vertical) | Same, vertical orientation | 同上，纵向版 | Same rules / 规则相同 |
| Bar (stacked) | Composition over time | 跨时间的结构组成 | ≤ 4 segments → direct-label, no ticks / ≤ 4 段直接标注 |
| Area (stacked) | Parts-of-whole over time | 跨时间的部分与整体 | Light-to-dark single-hue ramp / 单色浅深递进 |
| Scatter | Two continuous variables | 两个连续变量关系 | 4–6 px dots, semi-transparent |
| Thermometer / bullet | Single metric vs target | 单指标 vs 目标 | Max 4 series, else use small multiples |
| Timeline (horizontal) | Events along time axis | 沿时间轴的事件 | Alternating above/below to avoid label collisions |
| Choropleth | Geographic variation | 地理分布 | Sequential palette, never rainbow / 顺序色板，不要彩虹 |
| Small multiples | Too many series for one chart | 太多系列拆成多面板 | 2×2 or 2×3 grid, shared scales |
| Dual-axis | Two metrics, shared x, different scales | 双指标共享 x 轴 | Use sparingly; small multiples preferred / 谨慎使用 |

**Forbidden / 禁用**: 3D anything, pie/doughnut with > 4 slices, radar, sankey, decorative emoji/illustration in the chart area, rainbow palettes.

Full per-type rules: `references/chart-types.md`. Drop-in templates: `references/code-templates.md`.

---

## 5. Visual signature (non-negotiable) / 视觉签名（缺一不可）

**EN** — Every output must contain all five of these. Drop one and it stops reading as "Economist":

1. **10×30 px red flag** in the top-left of the chart block, overlapping the top border. `monochrome-spare` substitutes a 1 px red rule.
2. **2 px red top border** spanning the chart block width.
3. **Kicker** (all-caps, 11–13 px, red or ink, bold sans) immediately right of the flag.
4. **Title** — one complete sentence with a verb, stating the finding, not the topic.
5. **Source line** at the bottom, 12–13 px, grey, left-aligned, starting with `Source:`.

**中文** — 每张产出图都必须包含以下 5 个元素，少一个就不"经济学人"了：

1. **10×30 px 红色 flag** 在 chart block 左上角，叠在 top border 上。`monochrome-spare` mood 用 1 px 红色 rule 替代。
2. **2 px 红色 top border** 横贯整个 chart block 宽度。
3. **Kicker**（全大写、11–13 px、红色或黑色、粗体 sans），紧贴 flag 右侧。
4. **标题** —— 含动词的完整陈述句，讲述发现，不要用话题标签。
5. **Source 行** 在底部，12–13 px，灰色，左对齐，以 `Source:` 开头。

Full breakdown: `references/visual-signature.md`. 完整说明：`references/visual-signature.md`。

---

## 6. Output formats / 输出格式

| Format | File size | Dependencies 依赖 | When to use / 何时用 |
|---|---|---|---|
| `.html` (inline SVG + CSS) | ≤ 60 KB | None / 无 | Drop into an article, web page, or report. / 嵌入文章、网页或报告。 |
| `.svg` (single file) | ≤ 40 KB | None / 无 | Open in any browser or vector tool. / 浏览器或矢量工具打开。 |
| `.pptx` (Approach 1 — native shapes) | ~30 KB | `python-pptx` only | Editable in PowerPoint. Most common production case. / 可在 PowerPoint 编辑，最常见的生产路径。 |
| `.pptx` (Approach 2 — SVG-embed) | Smaller / 更小 | `python-pptx` + `cairosvg` / `rsvg-convert` | Vector quality, non-editable text. / 矢量质量，文字不可编辑。 |
| `.pptx` (Approach 3 — PNG rasterise) | Larger / 更大 | Above + `inkscape` or `libreoffice` | Last resort. / 兜底方案。 |

**Before generating PPTX, run the tooling check in `references/ppt-adaptation.md`** — it tells you which approach is viable in your environment.

**生成 PPTX 之前，先跑 `references/ppt-adaptation.md` 顶部的 tooling check** —— 它会告诉你当前环境能跑哪条路径。

---

## 7. Typical prompt templates / 典型 Prompt 模板

### 7.1 Single chart (web embed) / 单图（网页嵌入）
> **EN** — "Make me an Economist-style information graphic in HTML, showing the trend of [TOPIC] from [YEAR RANGE]. The data is: [LIST OF DATA POINTS]. Use the **classic-crimson** mood. Single self-contained file."
>
> **中文** — "做一个经济学人风格的 HTML 信息图，展示 [TOPIC] 从 [YEAR RANGE] 的趋势。数据是：[DATA POINTS]。用 **classic-crimson** mood。单文件自包含。"

### 7.2 Single chart for PPT / 单图用于 PPT
> **EN** — "Generate a 16:9 PPTX slide with an Economist-style chart of [TOPIC]. The data is: [DATA]. Use the **newspaper-serious** mood."
>
> **中文** — "生成一个 16:9 PPTX slide，经济学人风格的 [TOPIC] 图表。数据：[DATA]。用 **newspaper-serious** mood。"

### 7.3 Specific mood request / 指定 mood
> **EN** — "Produce an Economist-style chart, but use the **colorful-explainer** mood — I want to see 4 distinct hues for the 4 phases: [PHASE 1: years/values], [PHASE 2: ...], etc."
>
> **中文** — "做一个经济学人风格的图，用 **colorful-explainer** mood——我想看到 4 种不同颜色对应 4 个阶段：[阶段 1：年份/数值], [阶段 2：...], 等。"

### 7.4 No mood specified (default) / 不指定 mood
> **EN** — "Build me an Economist-style chart of [TOPIC]." → defaults to `classic-crimson`.
>
> **中文** — "做一个经济学人风格的 [TOPIC] 图。" → 默认走 `classic-crimson`。

### 7.5 Sparse data pushback / 数据太少时 pushback
> **EN** — "This is too sparse for the requested chart type; I'd suggest a single-sentence callout or a small table instead. OK to proceed?"
>
> **中文** — "数据太少，原图类型画不出东西。建议改用一句话说明或者小表格。可以这么处理吗？"

### 7.6 Too many series pushback / 太多系列时 pushback
> **EN** — "Line charts cap at 4 series. I'd suggest small multiples (one panel per series) instead. OK?"
>
> **中文** — "折线图最多 4 个系列，建议拆成小倍数（每系列一个面板）。可以吗？"

---

## 8. References file map / References 文件导航

| File / 文件 | EN — What's in it | 中文 — 内容 | Open it when / 何时打开 |
|---|---|---|---|
| `SKILL.md` | 8-step procedure, 4 mood summary, self-check, output contract, failure handling, minimal example, mood comparison, PPT verification | 8 步流程、4 种 mood 速查、自检清单、输出契约、失败处理、最小示例、mood 对比、PPT 验证 | You need the full procedure / 需要完整流程时 |
| `references/skill-index.md` *(this file)* | One-page newcomer summary | 一页式新人上手索引 | First time using the skill / 第一次用这个 skill |
| `references/tokens.md` | Full design tokens (colour, type, grid, accessibility) | 完整 design tokens（颜色、字体、网格、可访问性）| You need exact hex / px / font values / 需要具体数值时 |
| `references/moods.md` | 4 mood recipes in full detail | 4 种 mood 的完整配方 | Picking or switching a mood / 选/换 mood |
| `references/chart-types.md` | Per-type rules (line / bar / scatter / pie / choropleth / etc.) | 各类型规则 | Choosing a chart type or debugging a layout / 选图表类型或调版式 |
| `references/code-templates.md` | Drop-in HTML + SVG templates | 可复制粘贴的 HTML + SVG 模板 | You want to copy-paste and modify / 想直接复制改改 |
| `references/visual-signature.md` | Flag, border, kicker, title, source line, leader block | flag、border、kicker、title、source 行 | The chart doesn't look "Economist" enough / 不够"经济学人"时 |
| `references/ppt-adaptation.md` | PPT sizing, tooling check, python-pptx recipe | PPT 尺寸、tooling check、python-pptx recipe | Output is `.pptx` or 16:9 slide / 输出是 PPTX 时 |
| `references/sources.md` | URLs, repos, articles, confidence ratings | 来源 URL、repo、文章、置信度 | You need to know where a rule came from / 想知道规则出处 |
| `references/cases.md` | 12 real Graphic Detail / interactive cases + 4 third-party analyses | 12 个真实案例 + 4 套外部分析 | You need evidence the rules match the masthead / 需要规则有据可查 |
| `examples/INDEX.md` | Index of 7 verified end-to-end demo files | 7 个端到端验证 demo 索引 | You want to see what "good output" looks like / 想看"好产出"长啥样 |

---

## 9. Demo files location / Demo 文件位置

See **`examples/INDEX.md`** for the bilingual index of all 7 verified demo files (5 HTML + 1 PPTX + 1 PNG preview). All passed the Step 8 self-check. Regenerate the PPTX with `python3 scripts/build_ppt.py`.

完整 demo 索引见 **`examples/INDEX.md`**（含 5 个 HTML + 1 个 PPTX + 1 个 PNG preview，全部通过自检清单）。重新生成 PPTX：`python3 scripts/build_ppt.py`。

---

## 10. Self-check before delivery / 交付前自检清单

**EN** — Run through this list before handing any chart to the user. **Any failure → fix it, do not deliver.**

- [ ] Title is a sentence with a verb, not a topic label.
- [ ] Background is white `#FFFFFF` or cream `#F5F4EF`. Never a saturated colour.
- [ ] 10×30 red flag present in top-left of chart block (or 1 px red rule in `monochrome-spare`).
- [ ] 2 px red top border spans full chart block width (or 1 px in `monochrome-spare`).
- [ ] Source line present, starts with `Source:`, in grey, 12–13 px.
- [ ] Maximum 2 saturated hues in the chart area (4 in `colorful-explainer`).
- [ ] No pie/doughnut with > 4 slices.
- [ ] No gridlines beyond axis ticks.
- [ ] All text meets WCAG AA contrast (≥ 4.5:1) against background.
- [ ] Self-contained: no `<link>`, no `<script>`, no external `<img>`.

**中文** — 交付前过一遍。任何一项不过 → 修好再交付，别带病交付。

- [ ] 标题是含动词的句子，不是话题标签。
- [ ] 背景是白色 `#FFFFFF` 或奶油 `#F5F4EF`，绝不用饱和色。
- [ ] 10×30 红 flag 在左上角（`monochrome-spare` 用 1px 红 rule）。
- [ ] 2px 红 top border 贯穿全宽（`monochrome-spare` 用 1px）。
- [ ] Source 行存在，以 `Source:` 开头，灰色，12–13 px。
- [ ] chart area 至多 2 个饱和色（`colorful-explainer` 允许多至 4 个）。
- [ ] 不用 > 4 切片的饼/环图。
- [ ] 除轴刻度外无网格线。
- [ ] 文字与背景对比度 ≥ WCAG AA（4.5:1）。
- [ ] 自包含：无 `<link>`、`<script>`、外部 `<img>`。

---

## 11. Known limitations (be honest with the user) / 已知限制（如实告知用户）

| EN — Limitation | 中文 — 限制 |
|---|---|
| Sandbox / CI often lacks `cairosvg` / `rsvg-convert` / `inkscape`. **Approach 1 (native shapes)** is the only viable PPT path. Editable in PowerPoint, just slightly less geometrically precise. | 沙盒 / CI 经常缺 `cairosvg` / `rsvg-convert` / `inkscape`，**Approach 1（native shapes）** 是 PPT 唯一可行路径。可编辑，几何精度略低。 |
| Output is static. No hover, no transitions, no D3 interactivity. | 输出是静态的，没有 hover/transition/D3 交互。 |
| Single chart per output. Multi-slide decks repeat the recipe per slide. | 单次输出单图。多页 PPT 套件需逐页重复 recipe。 |
| RGB only. No CMYK conversion / bleed / crop marks. | 只输出 RGB，没有 CMYK 转换 / 出血线 / 裁切标记。 |
| 2024+ production stack unverified. Tokens (`#E3120B`, Milo TE, Econ Sans Condensed) are stable; chart code patterns may have evolved. | 2024+ 生产栈未验证。Tokens（`#E3120B`、Milo TE、Econ Sans Condensed）稳定；图表代码模式可能已变。 |

---

## 12. How to maintain this skill / 如何维护

**EN**

- The skill syncs from this directory at session end. Any edit here propagates to the team's shared skill library.
- **Adding a new mood**: edit `SKILL.md` (description + 8-step procedure) and add a row to `references/moods.md`. Update this index.
- **Adding a new chart type**: add a section to `references/chart-types.md` and a drop-in template to `references/code-templates.md`.
- **Updating tokens**: edit `references/tokens.md` and re-check the public design system at `https://design-system.economist.com/foundations/colour/palettes` and `/typography/typefaces`.
- **Adding a real case**: add to `references/cases.md` with URL, topic, chart type, palette observed, and confidence rating.
- **After any change**, re-run an end-to-end eval: pick a real prompt, render with the updated skill, verify the output still passes the self-check.

**中文**

- Skill 在 session 结束时从这个目录自动同步到团队共享库，编辑即生效。
- **加新 mood**：编辑 `SKILL.md`（description + 8 步流程），在 `references/moods.md` 加一行，更新本索引。
- **加新图表类型**：在 `references/chart-types.md` 加章节，在 `references/code-templates.md` 加模板。
- **更新 token**：编辑 `references/tokens.md`，复查 `https://design-system.economist.com/foundations/colour/palettes` 和 `/typography/typefaces`。
- **加新案例**：在 `references/cases.md` 加 URL、主题、图表类型、配色、置信度。
- **任何改动后** 跑一次端到端 eval：找个真实 prompt、用更新后的 skill 渲染、验证仍过自检清单。

---

## 13. The masthead's own design principles / 经济学人官方 6 条设计原则

**EN** — When in doubt, fall back on these six (from `https://design-system.economist.com/foundations/principles/design-principles`):

1. **Less is more.** Drop gridlines, drop redundant axis lines, drop legends when direct labels work.
2. **Deliberate typography.** One serif (Milo TE) for voice, one sans (Econ Sans) for mechanics. Never two serifs at once.
3. **Visual harmony.** Single accent family per chart; grayscale everything else.
4. **Clear wayfinding.** Direct labels > callout lines > legend. The reader should never have to glance at a key.
5. **Intelligence and wit.** Title is a sentence with a verb stating the finding.
6. **Recognisable consistency.** Flag, top border, kicker, source line — same on every chart.

**中文** — 拿不准时回到这 6 条（出自 `https://design-system.economist.com/foundations/principles/design-principles`）：

1. **Less is more**（少即是多）。能省的网格线、轴线、legend 都省。
2. **Deliberate typography**（字体讲究）。衬线（Milo TE）做声线，sans（Econ Sans）做骨架。绝不同时用两种衬线。
3. **Visual harmony**（视觉和谐）。一个 accent 色族 + 其余灰阶。
4. **Clear wayfinding**（指路清晰）。直接标注 > 引出线 > legend，读者不该回头看图例。
5. **Intelligence and wit**（智识与机锋）。标题要含动词陈述发现。
6. **Recognisable consistency**（一致的辨识度）。flag、top border、kicker、source 行——每张图都一样。
