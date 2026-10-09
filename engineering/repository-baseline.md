# 初始化事实核对

日期：2026-10-09。性质：本次仓库初始化的只读资料核对，不是学习者代码审查或阶段评估。

## 现有项目

检查位置：`/Users/jkhkjg/Documents/ChatGPT/dmctrl-main`。
本地分支 `main`；HEAD `243cdf8c4880056840db70bc128ecdf8ef596230`。
`git status --short --branch` 显示相对本地缓存的 origin/main 落后 11 个提交；本次没有 fetch，不把该数字称为实时远端差距。
暂存区已有移动：`src/pos_vel.py -> src/dm4310_control/pos_vel.py`。未暂存、提交、切分支或改变这些文件。
origin 为 `s1eep1y416-desig/dmctrl`；upstream 为 `s1eep1y416-desig/dm4310-motorbridge-control`。它们仅是旧项目的远端，未配置到本新仓库。

读取 README、pyproject.toml、CURRENT_STATUS.md、pos_vel_wait.py、CLI 测试文件及源代码目录：

- 已存在 CLI、POS_VEL 示例、move_and_wait 和 test_cli.py。
- 依赖声明 `motorbridge>=0.5.6,<0.6`；这是范围，不证明该 checkout 的实际环境版本。
- 此次读到的 `pos_vel_wait.py` 的 TOLERANCE、VELOCITY_TOLERANCE、MOVE_TIMEOUT 均为 None。
- 当前文件有位置/速度联合判定和 finally 清理，但本次没有执行它，也没有重跑旧测试。
- 旧 CURRENT_STATUS.md 的理解/成绩和历史测试只是旧记录，没有转记为本仓库的证据。
- 与过去记忆中的更新版本存在差异，任务规划以当前文件核对为基线，迁入前需另选明确版本。

## 另一份同名草稿

位置：`/Users/jkhkjg/Documents/Codex/2026-10-09/ji/outputs/dm4310-motorbridge-control`。
已有治理文档、main 分支、无提交和远端。只读查看 README、PROJECT、CURRENT_TASK 和路线，未复用其中的“已完成”或授权声明作为本次事实。
用户在本次明确选择“建立新仓库，旧项目作为参考”，因此本次交付位于当前聊天 outputs 下。

## 可复用内容与迁入边界

可参考旧项目的需求、接口选择、异常案例和测试设计；未来迁入时逐文件核对来源提交、许可证、导入与测试。
不直接拷贝硬件地址、模型键、增益、限位或旧学习成绩。旧文件出现并不等于正确、可运行或已由用户独立掌握。
实际 MotorBridge 环境与接口见 [SDK 基线](motorbridge-api-baseline.md)；参考架构见 [系统设计](architecture/system-overview.md)。

## 当前实现状态

| 类别 | 结论 |
|---|---|
| 新仓库管理文档与检查工具 | 已建立；检查结果见 [初始化验证记录](initialization-validation.md) |
| 电机、ROS 2、运动学、动力学业务实现 | 本仓库未实现，按任务逐步建设 |
| 旧项目业务测试 | 本次未运行 |
| SDK ABI/驱动兼容性 | 未运行验证 |
| 真实设备通信/控制 | 未进行 |
| 学习者任务/能力 | 尚未按新路线评估 |
