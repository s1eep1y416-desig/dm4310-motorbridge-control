# 知识索引

通用知识保存一个主要版本；日常学习过程与项目设计通过链接关联。当前不生成空理论文章，不宣称任何主题已掌握。

## 现有学习材料

2026-10-10 已提供 S1-001 学习材料，用户理解与实践尚未评估；此前删除的旧材料没有恢复。

- [当前理论：MotorBridge 入门](motor-control/motorbridge.md)。
- [当前设计：状态显示程序](../engineering/interfaces/motor-api.md)。
- 按需参考：[机器人控制链路与证据](robotics/robot-architecture.md)、[首次接硬件前的资料整理](../engineering/architecture/s1-001-evidence-card-design.md)；不再作为首日必交作业。
- [今日任务：操作、文件名、问题与验收](../learning/daily/2026-10-10-S1-001.md)。

尚未形成经过用户解释/实践验证的掌握结论。
[MotorBridge 接口基线](../engineering/motorbridge-api-baseline.md) 是版本相关工程记录；[来源映射](../docs/source-map.md) 保存项目规范来源。

## 按主题、阶段和模块

| 主题 | 阶段 | 工程关联 | 当前状态 |
|---|---|---|---|
| MotorBridge 对象、连接、反馈；按需补 CAN/ID | S1 | examples / actuator / 配置 | S1-001 已提供材料，理解未评估 |
| 电机模式、PID、采样周期 | S2 | controllers / safety | 待任务学习 |
| 力矩、减速比、摩擦与惯量 | S2/S6/S7 | 设备与动力学模型 | 待资料与模型证据 |
| ROS 2 接口、QoS、TF2 | S3/S6 | ROS 工作区 | 待环境确认 |
| ros2_control 生命周期 | S4 | Hardware Interface | 待接口选型 |
| 多设备与轨迹 | S5 | actuator / trajectory | 待阶段开发 |
| 线性代数、变换、旋转、四元数 | S6 | kinematics | 可提前离线学习 |
| FK、IK、Jacobian、奇异性 | S6 | kinematics / 模型 | 待数学与实验验证 |
| 刚体动力学、重力、阻抗、零空间 | S7/S8 | dynamics / controllers | 零空间须匹配冗余条件 |

具体任务与阶段查 [任务池](../roadmap/backlog.md) 和 [验收标准](../roadmap/milestones.md)。
按实验查 [实验入口](../experiments/README.md)，按问题查 [待解决事项](../troubleshooting/index.md)。目前没有真实实验或已验证故障案例可链接。

## 成熟度

L0 尚未学习；L1 了解概念；L2 能解释；L3 能独立实现；L4 能验证和调试；L5 能迁移应用。
缺证据时记“未评估”，通过本人解释、代码、实验和迁移案例逐级记录，生成文章不自动提升等级。
形成条目时使用 [理论模板](../templates/theory-note.md)，记录来源、参数单位、适用范围、代码与实验关联和验证状态。

## 一手资料入口

- [MotorBridge 源码](https://github.com/motorbridge/motorbridge)：S1/S2，必须匹配实际安装版本。
- [reBot Python 核心](https://github.com/Seeed-Projects/reBotArm_control_py)：架构参考；本次未完成全部源码审查。
- [reBot ROS 2](https://github.com/Seeed-Projects/reBotArmController_ROS2)：S3 的分层参考，不直接复制六轴参数。
- [ros2_control 官方入门与架构](https://control.ros.org/jazzy/doc/getting_started/getting_started.html)：S4；此链接指向 Jazzy，实际发行版尚待选择。
- [ROS 2 官方教程](https://docs.ros.org/en/jazzy/Tutorials.html)：S3 的候选阅读入口；本次网页访问受到站点限制，未据此断言当前安装要求。
- [Pinocchio 官方仓库](https://github.com/stack-of-tasks/pinocchio)：S7；版本与 API 在进入阶段时再核对。
- 达妙设备协议/型号手册：待提供或从设备厂商对应型号资料确认；本次没有编造下载链接。

入口于 2026-10-09 检查；标注访问限制的资料仍待实际阅读。不会默认这些项目的最新版本已与本机兼容。
