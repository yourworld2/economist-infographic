# economist-infographic — Skill Bundle v2
# 经济学人风格信息图技能包 v2

> **EN** — A drop-in skill for generating single, self-contained editorial charts and 16:9 PPT slides in *The Economist*'s Graphic Detail style. Four preset moods (newspaper-serious / classic-crimson / colorful-explainer / monochrome-spare). All 5 HTML demos + 1 PPTX + 1 PNG preview verified end-to-end; PPTX regeneration verified September 2026 (identical slide XML, 38/38 internal parts).
>
> **中文** —— 即插即用的 skill，产出单文件、自包含的编辑风格图表与 16:9 PPT slide，风格对标 *The Economist* Graphic Detail 栏目。4 种 mood 预设（newspaper-serious / classic-crimson / colorful-explainer / monochrome-spare）。5 个 HTML + 1 个 PPTX + 1 个 PNG preview 全部端到端验证；2026 年 9 月复验 PPTX 重新生成（slide XML 完全一致，38/38 内部部件）。

**v2 changes / v2 变更**：修复 `build_ppt.py` 8KB 截断（原文件尾部丢失 1187 字节，无法运行）；脚本输出路径参数化（`--output`）；重组为标准技能目录（SKILL.md 在根）；demos 移入 `examples/` 并配双语索引。

---

## 📦 What's in this bundle / 包内结构

```
economist-infographic/
├── SKILL.md                            8-step procedure, self-check, output contract / 8 步流程、自检、输出契约
├── references/                         9 files / 参考文件
│   ├── skill-index.md                  ← bilingual, read first / 双语，先看这个
│   ├── tokens.md                       design tokens (colour / type / grid)
│   ├── moods.md                        4 mood recipes / 4 种 mood 配方
│   ├── chart-types.md                  per-type rules / 各图表类型规则
│   ├── code-templates.md               drop-in SVG/HTML templates
│   ├── visual-signature.md             flag, border, kicker, source line
│   ├── ppt-adaptation.md               PPT sizing & python-pptx recipe
│   ├── sources.md                      provenance & confidence / 来源与置信度
│   └── cases.md                        12 real Graphic Detail cases / 真实案例
├── examples/                           verified outputs / 验证过的产出
│   ├── INDEX.md                        bilingual demo index / 双语 demo 索引
│   ├── eval_serious_china_gdp.html     newspaper-serious
│   ├── eval_producer_china_gdp.html    classic-crimson (default)
│   ├── eval_colorful_china_gdp.html    colorful-explainer
│   ├── eval_monochrome_china_gdp.html  monochrome-spare
│   ├── eval_baseline_china_gdp.html    baseline (no skill, for contrast)
│   ├── eval_ppt_output.pptx            16:9 PPTX (30 KB)
│   └── ppt_preview.png                 PNG render of the PPTX
└── scripts/
    └── build_ppt.py                    runnable PPTX generator / 可跑 PPTX 生成器
```

---

## 🚀 Quick start (5 min) / 5 分钟上手

### EN

1. **Install the skill** — copy the `economist-infographic/` directory into your runtime's skills directory (or import the `.skill` package in Coze).
2. **Read first** — open `references/skill-index.md` (bilingual, 13 sections).
3. **See what good output looks like** — open any of the 5 `.html` files in `examples/` in your browser.
4. **Try the PPTX** — open `examples/eval_ppt_output.pptx` in PowerPoint / Keynote / LibreOffice.
5. **Regenerate the PPTX** — `python3 scripts/build_ppt.py [--output path]` (requires `python-pptx`).
6. **Use the skill in your agent** — when your prompt matches the trigger phrases, the skill auto-loads.

### 中文

1. **装 skill** —— 把 `economist-infographic/` 整个目录复制到 runtime 的 skills 目录（或在扣子中导入 `.skill` 包）。
2. **第一件事** —— 打开 `references/skill-index.md`（双语，13 章节）。
3. **看"好产出"长啥样** —— 浏览器打开 `examples/` 里任意一个 `.html`。
4. **看 PPTX 效果** —— 用 PowerPoint / Keynote / LibreOffice 打开 `examples/eval_ppt_output.pptx`。
5. **重跑 PPTX** —— 跑 `python3 scripts/build_ppt.py [--output 路径]`（需要 `python-pptx`）。
6. **在 agent 里用** —— prompt 匹配触发关键词时，skill 自动加载。

---

## ✅ Verified environment / 验证环境

| Tool | Status | Use |
|---|---|---|
| `python-pptx 1.0.2` | ✅ Required for PPTX | `pip install python-pptx` |
| Any modern browser | ✅ Required for HTML | Open `.html` directly |
| `LibreOffice` (optional) | ✅ Verified | Renders PPTX to PDF/PNG |
| `cairosvg` / `rsvg-convert` / `inkscape` | ⚠️ Optional | Only for higher-fidelity PPTX embedding (Approach 2/3) |

If you only have `python-pptx`, **Approach 1 (native shapes)** still works — `scripts/build_ppt.py` exercises it and produces a fully-editable 30 KB PPTX.

只装 `python-pptx` 也能跑（Approach 1）。`scripts/build_ppt.py` 就是这条路，30 KB 完全可编辑的 PPTX。

---

## 🧪 Smoke test after install / 装完快速验证

Open any of these prompts in your agent (with the skill loaded):

> **EN** — "Make an Economist-style information graphic in HTML, showing China's GDP growth 2010-2024. Data: 2010:10.6, 2011:9.6, 2012:7.9, 2013:7.8, 2014:7.4, 2015:7.0, 2016:6.9, 2017:6.9, 2018:6.8, 2019:6.0, 2020:2.2, 2021:8.4, 2022:3.0, 2023:5.2, 2024:5.0. Mood: classic-crimson."

> **中文** —— "做一个经济学人风格的 HTML 信息图，展示中国 GDP 2010-2024 增长。数据：2010:10.6, 2011:9.6, ..., 2024:5.0。Mood 用 classic-crimson。"

The output should be:
- Single self-contained HTML file ≤ 60 KB
- 10×30 red flag + 2 px red top border + red kicker
- Title is a sentence with a verb (e.g. "China's growth has cooled...")
- "Source: ..." line at the bottom
- Passes the 12-item self-check in `references/skill-index.md` §10

If all five hold, the skill is wired up correctly. / 5 项都满足，说明 skill 接通了。

---

## 🔧 Customising / 二次开发

| You want to... | Edit |
|---|---|
| Add a new mood | `SKILL.md` (description + 8-step procedure) + add a row to `references/moods.md` |
| Add a new chart type | Add a section to `references/chart-types.md` + a drop-in template to `references/code-templates.md` |
| Update design tokens | `references/tokens.md` (cross-check with `https://design-system.economist.com/foundations/*`) |
| Add a real Graphic Detail case | `references/cases.md` (URL, topic, chart type, palette, confidence) |
| Re-build the PPTX | `scripts/build_ppt.py` (Approach 1; swap to Approach 2/3 if you have `cairosvg` etc.) |

After any change, re-run the smoke test above. / 改完后跑一遍上面的 smoke test。

---

## 📋 Provenance / 来源

**EN** — Built June 2026 by Mavis; v2 repairs and restructure September 2026. Sources documented in `references/sources.md` and `cases.md`. Token values cross-checked with `https://design-system.economist.com/`. Real cases observed on `https://www.economist.com/graphic-detail` and `/interactive/`.

**中文** —— 2026 年 6 月由 Mavis 构建；2026 年 9 月 v2 修复与重组。来源详见 `references/sources.md` 和 `cases.md`。Token 数值与 `https://design-system.economist.com/` 交叉验证。真实案例取自 `https://www.economist.com/graphic-detail` 和 `/interactive/`。

---

## ⚠️ Known limits / 已知限制

- **Sandbox / CI may lack SVG rasterisers** → `build_ppt.py` uses Approach 1 (native shapes) which only needs `python-pptx`.
- **Output is static** (no hover/transitions/D3). Use the same design tokens for interactive builds.
- **RGB only** (no CMYK). Hand off SVG to pre-press for CMYK conversion.
- **Single chart per output**. Multi-slide decks repeat the recipe per slide.
- **Skill input must be a clean flat table** (rows × columns). Do data cleaning in pandas / Power Query / dbt *outside* the skill.

- **沙盒 / CI 可能缺 SVG 渲染器** → `build_ppt.py` 走 Approach 1（native shapes），只依赖 `python-pptx`。
- **输出是静态的**（无 hover/transition/D3）。交互版本请自行用相同 tokens。
- **只输出 RGB**（无 CMYK）。印刷请把 SVG 交给印前处理。
- **单次输出单图**。多页 PPT 套件需逐页重复 recipe。
- **输入必须是清洗过的 flat table**（行 × 列）。数据清洗在 pandas / Power Query / dbt 之类的工具里做，**不要塞进 skill**。

---

## 📬 Feedback / 反馈

If you update tokens, add a mood, or add a case, please commit it back to the team skill library so everyone benefits.

如果更新了 tokens、加了 mood、或加了 case，也请提交回团队 skill 库，让大家都能受益。
