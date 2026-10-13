# 拆招 `chaizhao`

> 拆解话语中的逻辑谬误，并逐条举证的通用 Agent Skill。
> A universal [Agent Skill](https://agentskills.io) that dissects logical fallacies in any statement — with evidence, not vibes.

兼容所有遵循 [Agent Skills 开放规范](https://agentskills.io/specification)的 Agent（Claude / OpenAI / Cursor / Gemini / GitHub Copilot / Microsoft 等），也支持以纯提示词方式接入任何 LLM。

---

## 它做什么

一段话进去，一份**证据链完整**的谬误清单出来：

```text
输入  「我认识一个人抽了一辈子烟活到九十，所以吸烟有害健康是骗人的。」

输出  ① 轶事证据（Anecdotal）· 置信度：高
      锚点：「我认识一个人抽了一辈子烟活到九十」
      机制：用个案对抗统计证据——"我认识的人"不是样本，是巧合
      举证：个案不改概率，正如中一次奖证明不了买彩票是理财
      反驳句：一个反例推翻不了统计规律
```

每条谬误都带五个字段：**原文锚点 → 定名（中英）→ 机制拆解 → 举证 → 反驳句**，缺任何一环不报告。

## ✨ 特性

- **先钢人，后定罪**：先把对方论证补成最强版本再判定，从机制上压制"谬误贴标签"式的过度定罪
- **62 种谬误全库**（对齐 [Wikipedia 谬误总表](https://en.wikipedia.org/wiki/List_of_fallacies)全部主要类目 + Copi《逻辑学导论》三分法）：概念歧义 / 不当概括 / 因果经济 / 人身动机 / 诉诸 / 论辩操作 / 统计概率 / **形式谬误** 八大类，另含 30+ 变体归并
- **九套方法论按需加载**：论证重构、谬误全库、**形式检验**、易混辨析、防误伤自查、举证弹药、经典案例库、反驳工程、输出模式——SKILL.md 做路由，核心自包含
- **证据链纪律**：锚点、定名、机制、举证、反驳句缺一不报；宁缺毋滥，不硬凑数量
- **承重分析**：区分"拆掉结论就塌"的承重谬误与装饰性毛病；事实错误、价值分歧单独标注不冒充谬误
- **高发误判清单**：情感诉求≠谬误、诉诸权威≠谬误、简化≠谬误……定罪前强制自查
- **正面工具**：归谬法、证明过多、平行替换、概念澄清、反例构造——不只是找茬，还给拆法
- **五种输出模式**：分析体（默认）/ 口播稿 / 反驳卡片 / 辩论简报 / 教学体
- **零依赖**：纯提示词方法论，不需要脚本、API 或网络

## 🧠 方法论（四步）

```
① 钢人重构   结论 ← 理由A + 理由B（隐含前提C），按最有利于说话人的方式补全
② 扫描定罪   对照 62 类速查表（含形式检验：先判形式有效，再查内容谬误）
③ 逐条举证   锚点 → 定名 → 机制 → 举证（8 类弹药选 1–2）→ 反驳句
④ 总评       承重谬误 ⚠ ｜ 事实错误 ｜ 价值分歧 ｜ 论证强度
```

**八类举证弹药**：类比迁移 · 平行替换 · 经典案例 · 数据锚点（无把握标「待核实」，绝不编造）· 反例构造 · 概念澄清 · 归谬法 · 证明过多

## 📦 安装

通用规则：把 `skills/chaizhao/` 整个目录放进 Agent 的 skills 目录即可（开放格式，一处安装，多端可用）。

| Agent | 安装方式 |
|---|---|
| **Claude Code** | `git clone https://github.com/zerozhh/chaizhao.git && mkdir -p ~/.claude/skills && cp -r chaizhao/skills/chaizhao ~/.claude/skills/`（项目级安装则放入 `.claude/skills/`） |
| **Claude Desktop / claude.ai** | 设置 → Capabilities → Skills → 上传 `skills/chaizhao` 打包的 zip |
| **Codex CLI** | 将 `SKILL.md` 全文追加到 `AGENTS.md`，或以文件方式引用 |
| **Cursor** | 复制 `SKILL.md` 内容到 `.cursor/rules/chaizhao.mdc`（或 Rules 设置） |
| **Gemini CLI** | 将 `SKILL.md` 加入 `GEMINI.md` 上下文，或 `gemini extensions install` |
| **OpenCode 等其他 Agent** | 复制 `skills/chaizhao/` 到对应 skills 目录 |
| **任意 LLM（无 skill 机制）** | `SKILL.md` 自包含核心方法论（含速查表），全文粘贴为 system prompt / 自定义指令即可使用 |

## 🚀 用法

```text
/chaizhao 「（贴入任何一段话）」
```

自然语言同样触发：

- 「帮我拆一下这段话的逻辑问题：……」
- 「这段反驳成立吗？」+ 截图文字 / 文件
- 「用拆招分析这段话，输出口播稿」→ 视频脚本模式

## 📁 结构

```
chaizhao/
├── README.md
├── LICENSE
└── skills/
    └── chaizhao/
        ├── SKILL.md              # 路由 + 四步法 + 62 类速查表（自包含，可单独粘贴使用）
        └── references/           # 九套方法论，按需加载（渐进披露）
            ├── fallacies.md      # 62 类谬误全条目：定义/信号/弹药/反驳句 + 30+ 变体归并
            ├── formal-checks.md  # 形式检验：条件句四式/三段论/概率形式 + 有效形式对照表
            ├── reconstruction.md # 论证重构：语域判定/论证图/省略前提补全/概念澄清术
            ├── ammunition.md     # 举证弹药八式：构造步骤 + 质检标准 + 失败模式
            ├── canon.md          # 经典案例库：公共例证按谬误索引（巴斯夏/罗素茶壶/守株待兔…）
            ├── rebuttal.md       # 反驳工程：三个打击点/强度阶梯/提问式反驳/防守
            ├── modes.md          # 五种输出模式：分析体/口播稿/反驳卡片/辩论简报/教学体
            ├── confusions.md     # 易混谬误辨析 + 元谬误（谬误谬误）+ 定罪决策树
            └── pitfalls.md       # 十三高发误判 + 定罪前八问自查清单
```

遵循 [Agent Skills 规范](https://agentskills.io/specification)的渐进披露：`name`/`description` 常驻（约 100 token）→ 触发后加载 `SKILL.md` → 需要时才读 `references/`。

## 🛠 设计原则

- **方法论，不是案例库**：内置的是拆解方法与通用经典例证（巴斯夏蜡烛寓言、二战弹孔、罗素的茶壶等），不绑定任何特定文本
- **防误伤优先**：钢人先行 + 高发误判自查，宁可漏报不可错报
- **可验证**：引用具体数字只用公认可查事实，无把握一律标「待核实」

## 🗺 Roadmap

- [x] 多方辩论的逐发言评分（✅ v1.2.0 已实现：「辩论简报」模式）
- [ ] 英文谬误包（`fallacies-en` 参考文件，62 类对齐翻译 + 英文话语惯用变体）
- [ ] 评测基准集（evals）：以误报率 / 漏报率为核心指标的回归测试
- [ ] 事实核查工具联动（`scripts/`，「待核实」标注的自动补证）
- [ ] CI 规范校验（GitHub Actions 跑 `skills-ref validate`，frontmatter 违规即红灯）
- [ ] 提交 [agentskills.io](https://agentskills.io) 社区目录与 awesome 类清单收录

## 📜 License

[MIT](LICENSE)