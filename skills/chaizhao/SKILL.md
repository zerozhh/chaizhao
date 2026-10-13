---
name: chaizhao
description: 拆招——拆解话语中的逻辑谬误并逐条举证的通用分析技能。先钢人重构论证再定罪，每条谬误输出完整证据链：原文锚点、谬误定名（中英）、机制拆解、举证、反驳句，并区分承重谬误与次要毛病。62 类谬误全库（含形式谬误与有效形式对照）、八类举证弹药、五种输出模式（分析体/口播稿/反驳卡片/辩论简报/教学体）。当用户贴出一段话、评论、语录、文章、演讲、对话或辩论发言，问「说得对吗」「有没有逻辑问题」「怎么回怼」「帮我反驳」「分析这场辩论」「教我识别谬误」时使用；英文触发词：find logical fallacies, analyze this argument, is this reasoning valid, help me rebut。/chaizhao <文本> 直接触发。
license: MIT
metadata:
  version: "1.2.0"
---

# 拆招 · 逻辑谬误拆解与举证

把一段话里藏的逻辑谬误逐条拆出来，每一条都拿出证据：先还原论证，再定名，再用类比、经典案例或数据证明它确实是谬误，最后给一句可以直接用的反驳。

本文件自包含核心方法论与全量速查表——无文件读取能力的 agent 只取本文件即可工作。支持按需加载的 agent，按下面的文件地图深入。

## 文件地图（按需加载）

| 你要做的事 | 读这个 |
|---|---|
| 还原论证、补隐含前提、澄清概念、判语域 | [references/reconstruction.md](references/reconstruction.md) |
| 查单个谬误的定义、识别信号、弹药、反驳句 | [references/fallacies.md](references/fallacies.md) |
| 文本含显式条件句/三段论/概率推理，先做形式检验 | [references/formal-checks.md](references/formal-checks.md) |
| 两个谬误拿不准；判断"推理错了结论是否也错" | [references/confusions.md](references/confusions.md) |
| 定罪前防误伤自查 | [references/pitfalls.md](references/pitfalls.md) |
| 构造举证（类比/平行替换/归谬/反例…怎么造、怎么质检） | [references/ammunition.md](references/ammunition.md) |
| 找公共经典例证（巴斯夏、罗素茶壶、守株待兔…） | [references/canon.md](references/canon.md) |
| 设计反驳策略、写反驳句、防守 | [references/rebuttal.md](references/rebuttal.md) |
| 选输出形态（分析体/口播稿/反驳卡片/辩论简报/教学体） | [references/modes.md](references/modes.md) |

## 决策流程

```
① 声音归因（单一声音则跳过；有引用/转述/假想敌仍需归因，见「输入与声音归因」）
   ↓
① 钢人重构 → reconstruction.md
   ↓
② 扫描定罪 → fallacies.md（条目） + confusions.md（拿不准时）
   ├─ 文本含显式条件句/三段论/概率叠加 → formal-checks.md（先形式后内容）
   ↓
③ 定罪自查 → pitfalls.md（防误伤，必过）
   ↓
④ 逐条举证 → ammunition.md（造弹药） + canon.md（找例证）
   ↓
⑤ 反驳设计 → rebuttal.md
   ↓
⑥ 选模式输出 → modes.md
```

## 输入与声音归因

- 分析对象：`$ARGUMENTS`、用户消息中的文本、文件路径或上文对话均可
- **声音归因**（决策流程第 ① 步）：
  - 多人对话 → 按说话人切分，分别还原各方论证再分析
  - 单一声音 → 跳过切分；**但**文本中若含引用、转述、「有人可能会说」式假想敌、骂抽象"你们"的泛指，仍需归因——把每句主张归到正确的主人
  - 铁律：**只对作者自己的推理定罪**。假想敌/被转述者的谬误不记在作者头上；但作者把假想敌歪曲得比原话更蠢再打，构成**作者**的稻草人（D4）
- 文本太短或缺关键语境时先声明，再给基于当前信息的初步拆解

## 四步法（核心）

### 第 1 步 · 钢人重构（先补全，再拆招）

1. 提取结论与理由，还原论证链：`结论 ← 理由A + 理由B（隐含前提C）`
2. 隐含前提按**最有利于说话人**的方式补全——补全后不谬的，不定罪
3. 先澄清关键概念边界（弹性词：「安全」「自由」「虐待」），概念澄清常常直接消解一半"问题"
4. 先判语域：玩笑、修辞、营销文案不按严格论证标准苛责

→ 深入方法见 [references/reconstruction.md](references/reconstruction.md)

### 第 2 步 · 扫描定罪

对照下方速查表扫描，锁定类别后核对识别信号，确认推理断裂点**真实存在**（不是似是而非的联想）。同一处文本只取最准确的一个名。

**含显式推理结构的文本**（如果…那么 / 所有…都 / 概率叠加）：先做形式检验——形式无效定 H 类，形式有效再查 A–G 类。这防止把有效推理（否定后件 MT）误判成谬误（否定前件）。

→ 条目详情见 [references/fallacies.md](references/fallacies.md)；形式检验见 [references/formal-checks.md](references/formal-checks.md)；易混对比见 [references/confusions.md](references/confusions.md)

### 第 3 步 · 逐条举证（证据链，缺任何一环就不报）

每条定罪给完整证据链：

1. **原文锚点**：逐字引用最小充分片段
2. **定名**：规范中文名 + 英文名
3. **机制拆解**：默认了什么前提、在哪里断裂（一两句讲透）
4. **举证**：八类弹药选 1–2 个最有力的——类比迁移 · 平行替换 · 经典案例 · 数据锚点（无把握标「待核实」，**绝不编造精确数字**）· 反例构造 · 概念澄清 · 归谬法 · 证明过多
5. **反驳句**：一句可直接使用、有画面感的反驳

→ 造弹药见 [references/ammunition.md](references/ammunition.md)；找例证见 [references/canon.md](references/canon.md)；写反驳见 [references/rebuttal.md](references/rebuttal.md)

### 第 4 步 · 总评

- 标出**承重谬误** ⚠：拆掉它结论就塌的谬误（要害），与装饰性毛病区分
- 单独列出**事实错误**（不算逻辑谬误）与**价值分歧**（不是逻辑问题）
- 一句话总评：推理失败不等于结论为假——补强后能否成立、缺什么证据

## 谬误速查表（62 种）

| 编号 | 谬误 | 一句话信号 |
|---|---|---|
| A1 | 偷换概念 Equivocation | 关键词在前提和结论里不是一个意思 |
| A2 | 进可攻退可守 Motte-and-Bailey | 强主张被驳就退回弱主张 |
| A3 | 不当类比 Weak Analogy | "就像…"承担证明功能但结构断裂 |
| A4 | 合成/分割谬误 Composition/Division | 个体性质推整体，或整体性质摊个体 |
| A5 | 范畴错置 Category Mistake | 从"我不需要"推出"你做了也不算" |
| A6 | 语法歧义 Amphiboly | 歧义在句子结构，不在词义 |
| A7 | 具体化谬误 Reification | 抽象概念被当成能行动的实体 |
| A8 | 不完整比较 Incomplete Comparison | "快了三倍"——比什么？ |
| A9 | 虚假等价 False Equivalence | "都一样"——抹掉程度与性质差异 |
| A10 | 连续统谬误 Continuum | 说不出精确界线就否认差异存在 |
| B1 | 以偏概全 Hasty Generalization | 样本太小或无代表性就下普遍结论 |
| B2 | 轶事证据 Anecdotal | "我身边有个案例"对抗统计 |
| B3 | 幸存者偏差 Survivorship | 只统计"活下来的"样本 |
| B4 | 德州神枪手 Cherry Picking | 先有结论再挑数据 |
| C1 | 虚假因果 False Cause | 先后/相关当因果 |
| C2 | 破窗谬误 Broken Window | 只见看得见的收益，不见看不见的成本 |
| C3 | 滑坡谬误 Slippery Slope | 一步推到灾难，链条无必然 |
| C4 | 倒果为因 Reverse Causation | 因果方向搞反 |
| C5 | 单一原因 Single Cause | 多因问题归到一个原因 |
| D1 | 人身攻击 Ad Hominem | 攻击说话人代替反驳观点 |
| D2 | 你也一样 Tu Quoque | "你也干过"当反驳 |
| D3 | 诉诸动机 Appeal to Motive | "他肯定收了钱" |
| D4 | 稻草人 Strawman | 歪曲对方观点再打 |
| D5 | 断章取义 Contextomy | 剥离语境引用原话 |
| D6 | 井中投毒 Poisoning the Well | 先抹黑再让人开口 |
| D7 | 起源谬误 Genetic Fallacy | 用主张的出身判断真假 |
| D8 | 联想谬误 Association | "他跟坏人来往，所以他坏" |
| E1 | 诉诸不当权威 False Authority | 跨领域权威或冒充共识 |
| E2 | 诉诸大众 Appeal to Popularity | 人多 = 对 |
| E3 | 诉诸情感/恐惧 Appeal to Emotion | 情绪、道德绑架代替论证 |
| E4 | 诉诸传统 Appeal to Tradition | 一直如此 = 应该如此 |
| E5 | 诉诸自然 Appeal to Nature | 纯天然 = 好 |
| E6 | 诉诸无知 Appeal to Ignorance | 没被证伪 = 真 |
| E7 | 诉诸后果 Appeal to Consequences | 结论可怕 = 结论假 |
| E8 | 公正世界谬误 Just-World | 由结果倒推品行，世界必公平 |
| E9 | 诉诸新异 Appeal to Novelty | 新 = 好，旧 = 落后 |
| E10 | 应然实然混淆 Is–Ought | "存在即合理"——实然应然互推 |
| E11 | 诉诸难以置信 Appeal to Incredulity | 我想不出 = 假 |
| F1 | 虚假两难 False Dilemma | 只给两个选项 |
| F2 | 循环论证 Circular | 结论混进前提 |
| F3 | 转移举证责任 Burden Shifting | "你证明不了错就是对的" |
| F4 | 移动球门柱 Moving Goalposts | 达标就换标准 |
| F5 | 红鲱鱼 Red Herring | 换话题 |
| F6 | 苦难奥林匹克 Relative Privation | 比惨取消正当性 |
| F7 | 涅槃谬误 Nirvana | 不完美就别做 |
| F8 | 断言重复 Argument by Assertion | 说一万遍 = 真 |
| F9 | 折中谬误 Argument to Moderation | "一个巴掌拍不响"——取中 = 对 |
| F10 | 错上加错 Two Wrongs | "他也先动手的" |
| F11 | 诉诸纯洁 No True Scotsman | 反例出现就重新定义集合 |
| F12 | 特设性辩护 Special Pleading | "我情况特殊"——只给自己开例外 |
| F13 | 复合问题 Loaded Question | 问题里藏着未承认的前提 |
| G1 | 基率忽略 Base Rate Neglect | 忽略先验概率 |
| G2 | 赌徒谬误 Gambler's Fallacy | 独立事件谈"该轮到了" |
| G3 | 回归均值误读 Regression | 极端后回落被当成干预的功劳 |
| G4 | 唯量化谬误 McNamara | 量不了 = 不存在 |
| G5 | 沉没成本 Sunk Cost | "都付出这么多了，不能停" |
| G6 | 合取谬误 Conjunction | 更具体的故事"更可能" |
| H1 | 肯定后件 Affirming the Consequent | 若P则Q；Q；∴P ✗ |
| H2 | 否定前件 Denying the Antecedent | 若P则Q；非P；∴非Q ✗ |
| H3 | 中项不周延 Undistributed Middle | 都属于C，∴ A就是B ✗ |
| H4 | 四词项谬误 Four Terms | 中项一词两义 |
| H5 | 诉诸可能性 Appeal to Probability | "万一呢"——可能当必然 |

## 输出格式（分析体 · 默认）

```markdown
# 拆招：<主题>

**原话**：>「……」
**论证还原**：结论「…」← 理由A、理由B（隐含前提：…）

这段话里藏着 **N** 个逻辑谬误：

## 1. <中文名>（English）· 置信度：高 ⚠承重
> 「……」

**机制**：……
**举证**：……
**反驳句**：……

## 2. ……

## 总评
- 承重谬误：#…
- 事实错误/价值分歧（非谬误）：…
- 论证强度：……
```

- N 按置信度 ≥ 中 的条目计；「存疑」项只在用户要求穷尽模式时附上
- 输出语言跟随输入语言
- 其他四种模式（口播稿/反驳卡片/辩论简报/教学体）与模式选择启发 → [references/modes.md](references/modes.md)

## 裁决纪律（防误伤）

1. **钢人先行**：善意补全后不谬的，不定罪；语域是玩笑、修辞、营销时先声明
2. **三类问题分开**：事实错误 ≠ 逻辑谬误 ≠ 论据薄弱，分别标注
3. **相关性断裂才定罪**：情感诉求、专家意见、类比本身不是谬误——承担了不该承担的证明功能才是
4. **宁缺毋滥**：引不出来的不报，不硬凑数量
5. **对事不对人**：拆论证不评价人品；反驳句克制、有杀伤力但不人身攻击
6. **推理失败 ≠ 结论为假**：总评必须给结论独立的真假判断路径
7. **有效形式不是谬误**：MP/MT/析取三段论都是合法推理——形式检验先行，防止把「否定后件」误判成「否定前件」

→ 完整自查清单见 [references/pitfalls.md](references/pitfalls.md)
