# 原始规范与落地映射

来源：[用户提供的 AGENTS.md.pdf](source/AGENTS-V1.2.pdf)，41 页，V1.2 — reBot Architecture Edition。
SHA-256：`2ecd4e98e45e48463402054eb04afe833b5d70ab1fe307151f07b787b3e93c77`。
PDF 提取包含部分乱码标点，因此本仓库为结构化整理，不声称逐字转录。原始副本保留用于核对。
2026-10-09 用户明确“以 agent.md 为主”：原文是项目规范依据，根 AGENTS.md 是执行入口；本映射与辅助计划不能覆盖原规范。

| 原文内容 | PDF 章节/页 | 落地 |
|---|---|---|
| 定位、角色、规则分层 | §1–3，p1–4 | AGENTS.md、PROJECT.md |
| 环境与配置 | §4，p4–5 | PROJECT.md、config/ |
| reBot 参考与目标目录 | §5–7，p6–15 | [完整目录](../engineering/architecture/target-layout.md)、engineering/architecture/system-overview.md |
| 六个月、S1–S8 | §8–16，p15–24 | roadmap/master-roadmap.md、milestones.md、backlog.md |
| 开发、教学、安全、控制数学 | §17–20，p24–28 | AGENTS.md、learning/WORKFLOW.md、roadmap/prerequisites.md |
| 知识、ADR、实验、故障、审查 | §21–25，p28–32 | knowledge/、engineering/、experiments/、troubleshooting/、templates/ |
| 评分、门槛和量化指标 | §26，p32–34 | roadmap/milestones.md、templates/stage-assessment.md |
| 每日任务、延期、协作 | §27–28，p34–36 | learning/、CURRENT_TASK.md |
| 去重、Git、复用与报告 | §29–32，p36–39 | AGENTS.md、templates/、README.md |
| 初始化与近期策略 | §33–35，p39–41 | 本次最小仓库、事实基线、S1/S2 优先任务 |

## 本次明确的设计选择

- 原文目录为长期目标；此次仅建立可用的管理基础，不生成全部未来控制代码。
- 采用目录示例的项目名称；封面简称与同名旧远端均记录而不自动覆盖。
- 六个月基准按本次日期编排；任务时间和拆分为本次建议，不是原文逐日承诺。
- 每日过程使用原文 `learning/daily/`；理论、设计按原文职责归 knowledge/、engineering/。初次生成的任务和合并材料已按用户要求删除；旧资料没有迁移。
- 原文没有固定 01–07 七对话顺序，此前带入的约定已撤销其强制地位；开发、教学、阶段验收分别遵循 §17、§18、§26。
- 原文允许多聊天分工；本次不据此启动代理、创建聊天或定时任务。
- 未获证据的事实保留待确认，未给学习者评分，没有把文档生成当成阶段通过。
