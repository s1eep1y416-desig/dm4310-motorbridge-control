# 六个月开发与学习路线

> 规划在 REPO-001 仓库验证通过后复核。日期与估时可调整；S1-001 已于 2026-10-11 验收完成，S1 阶段继续进行。

规划窗口：2026-10-09 至 2027-04-08，约 26 周。起点为仓库基础完成后；下表日期为初始排期建议，若开始日期变化则整体顺延，不是自动通过时间。
最低目标：完成有真实实验与故障证据的双电机机械臂系统。挑战目标：完成三自由度综合系统。

| 阶段 | 参考窗口 | 核心能力 | 关键成果 |
|---|---|---|---|
| S1 | 10-09～10-22 | MotorBridge 对象、连接、反馈、使能/失能；结合接口学习 ID/CAN | 能用 SDK 读取单电机状态并处理异常 |
| S2 | 10-23～11-12 | MotorBridge、MIT/POS_VEL/VEL、反馈闭环 | 受限单关节控制、日志及异常验证 |
| S3 | 11-13～11-26 | ROS 2 Node、Topic/Service/Action、参数 | 可启动、可停止、可观测的 ROS 2 接口 |
| S4 | 11-27～12-08 | ros2_control、生命周期、read/update/write | 一个标准硬件接口及控制器集成 |
| S5 | 12-09～12-29 | 双电机、时间戳、轨迹、故障联动 | 双关节协调控制与同步误差报告 |
| S6 | 12-30～2027-02-08 | 二自由度建模、FK/IK、Jacobian、URDF/TF | 数学验证、模型比对、末端实验 |
| S7 | 2027-02-09～03-15 | Pinocchio、动力学、重力补偿 | 模型参数、独立对照与受限补偿实验 |
| S8 | 2027-03-16～04-08 | 第三关节、三维位置任务、系统集成 | 三自由度综合工程与复现报告 |

阶段详见 [验收标准](milestones.md)，候选开发任务详见 [任务池](backlog.md)。旧每日任务和首两周日程已按用户要求删除；随后授权的 [定时学习安排](../learning/SCHEDULE.md) 从 2026-10-10 开始，按实际进度下发新任务。

## 每个阶段在哪个文件夹写代码

2026-10-10 补充目录说明。以下路径均相对于仓库根目录 `/Users/jkhkjg/Desktop/dm4310-motorbridge-control/`；保留原阶段、任务 ID、依赖和完成记录。目录已预留不代表功能已经实现。

| 阶段 | 核心代码写在哪里、负责什么 | 示例写在哪里 | 自动化测试写在哪里 |
|---|---|---|---|
| S1 连接与反馈 | [src/robot_control/actuator/](../src/robot_control/actuator/)：MotorBridge 连接、状态、资源生命周期；[src/robot_control/safety/](../src/robot_control/safety/)：最小故障处理 | [examples/S1_can_and_id/](../examples/S1_can_and_id/)：初期 SDK 探索，随后调用核心读取状态 | [tests/unit/](../tests/unit/)：状态和失败分支；[tests/integration/](../tests/integration/)：适配器协作；[tests/hardware/](../tests/hardware/)：隔离的真实通信验证 |
| S2 单关节控制 | [src/robot_control/controllers/](../src/robot_control/controllers/)：单关节、到位等待与状态机；[src/robot_control/safety/](../src/robot_control/safety/)：限制、超时；[src/robot_control/utils/](../src/robot_control/utils/)：日志 | [examples/S2_single_motor/](../examples/S2_single_motor/)：调用位置、速度、MIT 控制与日志功能 | [tests/unit/](../tests/unit/)：命令、到位与超时；[tests/integration/](../tests/integration/)：控制流程；[tests/hardware/](../tests/hardware/)：受限实验 |
| S3 ROS 2 基础 | [ros2_ws/src/dm_motor_driver/](../ros2_ws/src/dm_motor_driver/)：正式驱动包；[ros2_ws/src/dm_robot_bringup/](../ros2_ws/src/dm_robot_bringup/)：启动与参数；复用 S1/S2 核心 | [examples/S3_ros2_basics/](../examples/S3_ros2_basics/)：发布、订阅和命令调用演示 | 计划包内 `ros2_ws/src/dm_motor_driver/test/`：节点测试；[tests/integration/](../tests/integration/)：跨包调用 |
| S4 ros2_control | [ros2_ws/src/dm_motor_hardware/](../ros2_ws/src/dm_motor_hardware/)：Hardware Interface；[ros2_ws/src/dm_robot_description/](../ros2_ws/src/dm_robot_description/)：硬件接口描述；[ros2_ws/src/dm_robot_bringup/](../ros2_ws/src/dm_robot_bringup/)：控制器配置与启动 | [examples/S4_ros2_control/](../examples/S4_ros2_control/)：加载和调用控制器 | 计划包内 `ros2_ws/src/dm_motor_hardware/test/`：插件、生命周期与 read/write；[tests/integration/](../tests/integration/)：系统集成 |
| S5 多关节控制 | [src/robot_control/actuator/](../src/robot_control/actuator/)：多电机管理；[src/robot_control/controllers/](../src/robot_control/controllers/)：多关节协调；[src/robot_control/trajectory/](../src/robot_control/trajectory/)：插值与调度；扩展已有安全模块 | [examples/S5_multi_motor/](../examples/S5_multi_motor/)：双关节轨迹与故障联动演示 | [tests/unit/](../tests/unit/)：映射、轨迹；[tests/integration/](../tests/integration/)：多设备协作与故障；[tests/hardware/](../tests/hardware/)：双关节实验 |
| S6 运动学 | [src/robot_control/kinematics/](../src/robot_control/kinematics/)：模型、FK、IK、Jacobian；[ros2_ws/src/dm_robot_description/](../ros2_ws/src/dm_robot_description/)：机构描述 | [examples/S6_fk_ik/](../examples/S6_fk_ik/)：输入关节角或末端目标，展示求解结果 | [tests/unit/](../tests/unit/)：独立参考、回代、可达性与有限差分；[tests/integration/](../tests/integration/)：模型一致性 |
| S7 动力学 | [src/robot_control/dynamics/](../src/robot_control/dynamics/)：模型、Pinocchio 与重力计算；[src/robot_control/controllers/](../src/robot_control/controllers/)：补偿流程；复用安全模块 | [examples/S7_dynamics/](../examples/S7_dynamics/)：计算与补偿演示 | [tests/unit/](../tests/unit/)：独立重力参考、单位与方向；[tests/integration/](../tests/integration/)：模型和控制组合；[tests/hardware/](../tests/hardware/)：补偿实验 |
| S8 系统集成 | 扩展 [src/robot_control/](../src/robot_control/) 中已有模块；在 [ros2_ws/src/](../ros2_ws/src/) 的驱动、硬件、描述、bringup 包完成三关节集成；按需修改 [config/](../config/) | [examples/S8_3dof_robot/](../examples/S8_3dof_robot/)：完整系统任务入口，不复制三套控制逻辑 | [tests/unit/](../tests/unit/)：前序回归；[tests/integration/](../tests/integration/)：整机集成；[tests/hardware/](../tests/hardware/)：综合实验；相关 ROS 包内测试 |

ROS 包内 `test/` 是未来实现时创建的位置，不是已存在或已通过的测试。Python 测试按目录职责放入根目录 tests/；硬件测试单独运行。

### 从 examples 到核心模块的联系

- S1-001～S1-003 可以在示例中探索 SDK，接口与状态规则先在设计文档说明。
- S1-004 开始在 `src/robot_control/actuator/` 提取读取与状态逻辑；S1-005 将生命周期和故障处理纳入核心。
- S2 及后续开发继续扩展对应核心目录。示例通过 `import robot_control...` 调用已安装的核心包；测试直接调用核心。Python ROS 节点可以复用核心；S4 的语言和 SDK 连接方案由 S4-001 决定。
- 稳定的可复用功能进入核心，示例保留配置选择、调用和展示。每阶段的示例不能替代核心代码、测试、实际功能和知识掌握验收；不要求第一天设计完整架构。

### 理论、设计与实验记录放在哪里

沿用现有目录，不搬到另一套结构：理论放 `knowledge/`，设计放 `engineering/`，实验放 `experiments/`，学习与验收过程放 `learning/`；`docs/` 继续保存原始规范与来源映射。

| 阶段 | 理论知识目录 | 实验记录目录 |
|---|---|---|
| S1 | `knowledge/motor-control/`、`knowledge/can-communication/` | `experiments/single-motor/` |
| S2 | `knowledge/motor-control/`、`knowledge/control-theory/` | `experiments/single-motor/` |
| S3～S4 | `knowledge/ros2/` | `experiments/ros2/` |
| S5 | `knowledge/control-theory/`、`knowledge/robotics/` | `experiments/multi-motor/` |
| S6 | `knowledge/mathematics/`、`knowledge/kinematics/`、`knowledge/robotics/` | `experiments/kinematics/` |
| S7 | `knowledge/mechanics/`、`knowledge/dynamics/` | `experiments/dynamics/` |
| S8 | 复用上述理论目录，系统说明放 `engineering/architecture/` | 按实验主题复用 `experiments/multi-motor/`、`experiments/ros2/` 等目录 |

各阶段设计按主题归 `engineering/architecture/`、`engineering/interfaces/`、`engineering/hardware/`；审查放 `learning/reviews/`，阶段验收放 `learning/assessments/S1/`～`S8/`。具体文件名在每日任务下发时确定，原任务完成状态不因补充目录而改变。

## 实际起点

可用：原文目录、Python 包安装、环境检查、文档检查与一个包导入集成测试。
尚未实现：设备适配、反馈处理、安全状态机、控制算法、真实 ROS 包和机器人模型。
2026-10-10 用户要求直接从 MotorBridge 开始。因此先读 SDK 接口并写一个状态显示小程序，再随需求提取读取封装与测试；不要求先完成完整设备证据卡或独立 CAN 课程。设备资料在连接前补齐，ID、单位、反馈和退出随实际接口学习。见 [路线调整决定](../engineering/design-decisions/ADR-0002-motorbridge-first.md)。

入门顺序：S1-001 对象与状态显示 → S1-002 连接入口与设备参数 → S1-003 反馈机制 → S1-004 状态读取封装 → S1-005 生命周期 → S1-006 真机实验 → S1-007 复核。之后 S2 学位置/速度/MIT 与到位等待，再进入 ROS 2。原文目录及阶段验收保留。

## 三段安排

第一至第二个月先形成单电机闭环与 ROS 接口；第三至第四个月形成双关节与运动学能力；第五至第六个月处理动力学与系统集成。
S3/S4 若因主机或接口选型延期，应顺延真实控制任务，而不是压缩 S1/S2 的异常验证。
如果第三关节未准备好，优先完成 S5/S6 的双关节证据与 S7 的模型验证；S8 保留未通过，不影响对最低目标单独评价。

## 每周节奏与进阶规则

每个核心单元约两小时，每周五个核心单元、一个复盘单元、一个可选缓冲日。任务池中的估时不包含未知硬件故障与采购等待。
每周复盘检查：本周实际证据、独立完成部分、薄弱点、未闭环故障、下一核心任务。
调整排期时保留任务 ID、原定目标与变更理由。到月底只做状态复核，不自动升级阶段。

理论、数学、模型与 Fake Hardware 可以按独立前置条件提前学习；真实控制依赖顺序为 S1 → S2 → S3 → S4 → S5 → S6 → S7 → S8。
阶段评分、安全与硬件门槛统一由 milestones.md 定义。

## 长期复用

新项目复用 AGENTS.md、templates/ 与 knowledge/ 的通用理论，重新建立 PROJECT.md、设备配置、路线和验收值。
完成阶段后提炼真正验证过的知识，不复制电机参数、机械模型或未解决假设。每月检查链接、事实版本、任务状态和知识重复。
