# DM4310 MotorBridge Control

独立新建的机器人控制开发仓库。以 [AGENTS.md](AGENTS.md) 及用户提供的原文为主规范，按原文目录组织。
仓库基础已完成安装和导入验证；业务实现由后续阶段逐步增加。旧项目仅作参考，没有复制其源码或继承学习成绩。

本仓库围绕“学习理论 → 设计方案 → 独立编写代码 → 测试与实验 → 审查和学习记录”组织。以下路径均以仓库根目录为起点；本机存放位置见 [PROJECT.md](PROJECT.md)。

- [每天从哪里开始](#每天从哪里开始)
- [各目录放什么](#各目录放什么)
- [理论学习与工程设计](#理论学习与工程设计)
- [核心代码的模块分工](#核心代码的模块分工)
- [测试、仿真、实验与故障记录](#测试仿真实验与故障记录)
- [ROS 2 工作区](#ros-2-工作区)
- [路线、学习记录与验收](#路线学习记录与验收)
- [根目录与辅助文件](#根目录与辅助文件)
- [完整项目目录](#完整项目目录)
- [建立开发环境](#建立开发环境)
- [验证仓库](#验证仓库)
- [版本管理](#版本管理)

## 仓库入口

| 内容 | 入口 |
|---|---|
| 工作规则 | [AGENTS.md](AGENTS.md) |
| 实际环境、设备与未知项 | [PROJECT.md](PROJECT.md) |
| 当前工作 | [CURRENT_TASK.md](CURRENT_TASK.md) |
| 首日材料（2026-10-10 已改为 MotorBridge 入门） | [S1-001 任务卡](learning/daily/2026-10-10-S1-001.md) · [MotorBridge 讲义](knowledge/motor-control/motorbridge.md) · [程序设计](engineering/interfaces/motor-api.md) |
| 原文完整目录与落实情况 | [目标目录](engineering/architecture/target-layout.md) |
| Python 控制核心 | [src](src/README.md) |
| 测试说明 | [tests](tests/README.md) |
| ROS 2 预留工作区 | [ros2_ws](ros2_ws/README.md) |
| 学习路线与任务 | [roadmap](roadmap/README.md) |
| 定时学习安排 | [时间、续做与复盘规则](learning/SCHEDULE.md) |
| 学习进度 | [learning/progress.md](learning/progress.md) |
| 知识与资料 | [knowledge/index.md](knowledge/index.md) |
| 记录模板 | [templates](templates/README.md) |
| 初始化验证 | [验证记录](engineering/initialization-validation.md) |

## 每天从哪里开始

1. 打开 [CURRENT_TASK.md](CURRENT_TASK.md)，找到当前任务 ID、状态和任务卡入口。
2. 阅读任务卡关联的理论讲义。讲义放在 knowledge/ 对应主题目录，先理解概念、公式、单位和适用条件。
3. 阅读 engineering/ 中对应的设计说明，明确模块职责、输入输出、调用流程、异常处理与方案理由。
4. 按任务卡指定的目录和文件名完成独立实践。正式 Python 功能归 src/robot_control/，测试归 tests/，调用示例归 examples/；资料盘点任务按文档提交物完成，不强行写代码。
5. 执行任务要求的验证，保留命令与实际结果。实验报告和数据归 experiments/，当天的完成情况与问题归 learning/daily/。
6. 在当前协作聊天中说明“任务 ID 已完成，请审查”，给出文件位置、验证结果和思考题回答。助手检查实际提交，提出修改意见；修正并复核达标后更新任务状态。

每次下发由助手确定具体文件夹和文件名，列明新建、修改或阅读，说明用途、用户应写内容、创建步骤、执行目录和验证命令。助手提供理论材料与设计提示，学习者完成指定的核心实践；没有提交代码不做正式代码审查，没有回答问题不评定理论掌握。

定时安排从 2026-10-10 起按北京时间执行：09:00 安排学习，22:00 检查进度；周六复盘，周日补做或复习。首次晨间没有学习记录时从 S1-001 MotorBridge 入门与状态显示起步。未完成任务保留原 ID 继续，详见 [定时学习安排](learning/SCHEDULE.md)。定时安排本身不代表已经生成讲义或完成学习。

当前学习顺序：MotorBridge 对象与状态显示 → SDK 连接与反馈 → 单电机位置/速度/MIT 控制 → ROS 2 → 多关节及运动学、动力学。CAN/ID、环境和设备参数随实际调用补充。首日程序位于 `examples/S1_can_and_id/001_motorbridge_intro.py`；目录仍沿用 AGENTS 原文名称。首日环境报告和完整设备证据卡已被新练习替代，设备证据首次真实连接前补齐，见 [调整决定](engineering/design-decisions/ADR-0002-motorbridge-first.md)。

## 各目录放什么

| 目录 | 保存的内容 | 使用场景 |
|---|---|---|
| [roadmap/](roadmap/README.md) | 长期路线、前置条件、任务池和阶段验收标准 | 查看接下来学什么、需要提交什么、怎样才能进入下一阶段 |
| [knowledge/](knowledge/index.md) | 按主题组织的理论讲义与通用知识 | 学 CAN、控制理论、运动学、动力学；复习概念与公式 |
| [engineering/](engineering/architecture/system-overview.md) | 本项目的架构、接口、硬件事实和方案取舍 | 写代码前查设计依据，修改方案时保留理由 |
| [src/robot_control/](src/README.md) | 可安装、可复用的 Python 控制与算法代码 | 实现设备适配、控制流程、轨迹和数学算法 |
| [config/](config/README.md) | 设备、模型和安全限制的配置 | 将设备参数与实现分开；当前示例中的未知参数保持待确认 |
| [examples/](examples/README.md) | 按 S1–S8 划分的调用示例 | 演示如何调用正式模块；可复用功能仍保存在 src/robot_control/ |
| [tests/](tests/README.md) | 单元、集成、硬件测试和测试输入 | 检查正常、边界、异常行为是否符合预期 |
| [simulation/](simulation/README.md) | 设备替身、仿真模型和运行工具 | 无硬件时验证接口、算法或模型行为 |
| [experiments/](experiments/README.md) | 实验方案、原始数据、曲线和分析 | 记录实际测量条件、结果及误差，保留复现依据 |
| [troubleshooting/](troubleshooting/index.md) | 未解决问题和已排查故障案例 | 记录现象、复现步骤、原因、修复和回归检查 |
| [learning/](learning/WORKFLOW.md) | 每日任务、进度、审查和阶段考核 | 追踪个人学习过程，以及哪些能力已有证据 |
| [ros2_ws/](ros2_ws/README.md) | 后续 ROS 2 包与机器人集成工作区 | 将核心代码接入 ROS 节点、控制器和机器人模型 |
| [templates/](templates/README.md) | 理论、实验、审查、故障和考核等记录模板 | 创建对应记录时按模板填写真实内容 |
| scripts/ | 环境建立、环境报告和仓库检查脚本 | 安装项目、核对依赖环境、检查目录与文档链接 |
| [docs/](docs/source-map.md) | 原始规范及其来源映射 | 查证目录与规则的原文依据 |

## 理论学习与工程设计

knowledge/ 保存能复用到其他项目的概念和方法，engineering/ 保存这些知识在本项目中的具体应用。两类文档分别维护主版本，通过任务卡和相对链接关联。

| knowledge/ 子目录 | 学习主题 |
|---|---|
| mathematics/ | 线性代数、坐标变换、旋转矩阵、欧拉角和四元数 |
| mechanics/ | 力矩、惯量、减速比、摩擦等力学基础 |
| motor-control/ | 电机基础、MotorBridge、MIT、位置速度模式和速度模式 |
| control-theory/ | PID、串级控制、采样周期、离散控制和稳定性 |
| can-communication/ | CAN 通信、报文、Motor ID、反馈 ID 和设备协议 |
| ros2/ | 节点、Topic/Service/Action、JointState、TF2 和 ros2_control |
| robotics/ | 机器人架构、URDF 和坐标系组织 |
| kinematics/ | 正运动学 FK、逆运动学 IK、DH、Jacobian 和奇异性 |
| dynamics/ | 刚体动力学、质量矩阵、Pinocchio、重力补偿和阻抗控制；零空间内容按机构自由度与任务条件适用 |

| engineering/ 子目录 | 设计内容 | 需要回答的问题 |
|---|---|---|
| architecture/ | 模块边界、调用关系、状态与数据流 | 系统有哪些部分，谁调用谁，数据经过哪些环节？ |
| interfaces/ | 函数、类及模块之间的约定 | 输入输出是什么，单位是什么，失败时怎样返回或报错？ |
| hardware/ | 本项目设备、适配器、供电与限制的证据 | 实际使用什么设备，参数依据在哪，哪些事实仍待确认？ |
| design-decisions/ | 架构决策记录 ADR（Architecture Decision Record） | 为什么选择这个方案，比较过什么方案，有什么代价或限制？ |

例如“反馈超时”主题：knowledge/ 解释反馈年龄和超时原理；engineering/ 说明本项目在哪里记录时间、何时拒绝状态、如何退出；src/robot_control/ 实现对应逻辑；tests/ 提供正常与失联等用例；experiments/ 保存实际观测与分析；learning/daily/ 链接这些文件并记录当次学习过程。这是文件归属示例，不表示相关功能已经实现。

## 核心代码的模块分工

src/robot_control/ 是 Python 包的源码位置，通过根目录 pyproject.toml 安装后使用。以下为各模块的目标职责；当前已建立可导入的包结构，业务接口随任务明确后再实现。

| 子包 | 负责什么 | 典型内容 |
|---|---|---|
| actuator/ | 对接实际设备与 MotorBridge，管理设备身份和状态 | SDK 适配器、单/多设备管理、状态有效性与设备到关节的映射 |
| controllers/ | 组织控制流程和状态切换 | 单关节、多关节控制、状态机、重力补偿流程 |
| trajectory/ | 生成并采样随时间变化的目标 | 插值、轨迹规划与跟踪逻辑 |
| kinematics/ | 计算关节状态与末端位置之间的关系 | 机器人几何模型、FK、IK、Jacobian |
| dynamics/ | 根据模型计算力与运动的关系 | 动力学模型、Pinocchio 对接、重力项 |
| safety/ | 集中处理限制、超时和故障规则 | 参数校验、限位、看门狗、故障处理 |
| utils/ | 提供跨模块复用的小工具 | 单位转换、数据日志等 |

计划的调用关系是：examples/ 或 ROS 2 应用调用核心接口；controllers/ 组织流程，按需调用 trajectory/、kinematics/ 和 dynamics/；actuator/ 负责设备交互，safety/ 参与命令校验、反馈有效性与故障处理。纯数学模块应能脱离设备与 ROS 2 运行。具体调用链由对应设计文档定义，当前不存在已完成的整套控制链路。

## 测试、仿真、实验与故障记录

tests/ 中的文件负责执行检查与断言；simulation/ 提供离线运行环境和模型；experiments/ 保存某次实验的条件、数据与分析；troubleshooting/ 保存问题的诊断过程。它们通过任务 ID、代码版本和文件链接相互关联。

| 位置 | 具体用途 |
|---|---|
| tests/unit/ | 小范围功能测试，例如配置校验、算法边界、状态处理和异常分支 |
| tests/integration/ | 验证模块或安装环境配合；当前已有仓库外隔离导入检查 |
| tests/hardware/ | 必须连接真实设备才能执行的测试；与普通自动化检查分开 |
| tests/fixtures/ | 可复用的测试输入，注明真实、录制或合成来源 |
| simulation/fake_hardware/ | 用设备替身提供可控反馈、异常和故障序列 |
| simulation/mujoco/ | 后续 MuJoCo 仿真集成内容 |
| simulation/models/、simulation/scripts/ | 仿真使用的模型与运行工具 |
| experiments/single-motor/、experiments/multi-motor/ | 单电机与多电机实验报告、条件和结果 |
| experiments/ros2/、experiments/kinematics/、experiments/dynamics/ | ROS 集成、运动学和动力学实验记录 |
| experiments/datasets/ | 原始数据及其来源说明，报告应关联具体数据与版本 |
| troubleshooting/unresolved.md | 当前尚未解决的问题与下一步排查方向 |
| troubleshooting/cases/ | 可复现的故障案例、定位依据、修复和回归结果 |

实验开始前明确目标、单位、条件、测量方法和通过判据，结束后保存真实结果。静态检查、Mock、仿真和真机实验分别记录；普通测试命令只执行指定的软件测试目录。当前尚无控制业务测试、有效仿真模型或真实硬件实验结果。

## ROS 2 工作区

ros2_ws/src/ 按原文预留了以下包位置。它们尚不是可构建的 ROS 2 包，当前使用 COLCON_IGNORE 保持隔离；进入对应阶段后核对发行版、建立有效包并通过构建，再移除相应标记。

| 预留包 | 目标职责 |
|---|---|
| dm_motor_driver/ | 将核心设备能力封装为 ROS 2 节点，提供状态、受限命令和参数接口 |
| dm_motor_hardware/ | 对接 ros2_control 的硬件接口、生命周期和状态读取/命令写入；实现方式需核对所选版本 |
| dm_robot_description/ | 保存 URDF/Xacro 机器人描述、meshes 几何资源和 RViz 配置 |
| dm_robot_bringup/ | 保存 launch 启动文件及系统运行配置 |
| dm_robot_interfaces/ | 在标准接口不满足需求时定义 msg、srv、action；是否使用随需求确认 |
| dm_robot_moveit_config/ | 后续确有规划需求时使用的 MoveIt 配置位置 |

src/robot_control/ 保存可复用核心功能，ros2_ws/ 保存 ROS 2 接入与系统组装。两者通过明确接口协作，设备控制权需统一管理。

## 路线、学习记录与验收

| 文件或目录 | 用途 |
|---|---|
| [roadmap/master-roadmap.md](roadmap/master-roadmap.md) | S1–S8 阶段目标与可调整的时间窗口 |
| [roadmap/backlog.md](roadmap/backlog.md) | 任务 ID、依赖、估时、提交物、完成判据和当前状态 |
| [roadmap/prerequisites.md](roadmap/prerequisites.md) | 环境、知识与设备前置条件 |
| [roadmap/milestones.md](roadmap/milestones.md) | 各阶段验收标准、评分与必需实验证据 |
| learning/daily/ | 每日任务卡、当天完成情况、思考题回答或其链接、问题与下一步 |
| learning/reviews/ | 基于实际提交产生的代码审查意见和复核结果 |
| learning/assessments/S1/～S8/ | 各阶段理论考核、证据复核与验收报告 |
| [learning/progress.md](learning/progress.md) | 学习进度、阶段状态与能力证据摘要 |
| [learning/WORKFLOW.md](learning/WORKFLOW.md) | 教学、开发、审查与记录的工作流程 |
| [learning/SCHEDULE.md](learning/SCHEDULE.md) | 定时时间、每日下发、续做和周复盘规则 |

每日任务依据任务卡验收，较大任务可以跨多天完成。阶段验收按 milestones.md：理论 25 分、独立开发 35 分、实验 30 分、文档 10 分，总分至少 80 分，同时满足全部安全关键项、必需交付物与实验、无阻塞 Critical 问题等条件。没有必需真机证据不能判阶段通过；日期推进或助手生成文档都不代表学习者已经掌握。

## 根目录与辅助文件

| 文件或目录 | 作用 |
|---|---|
| README.md | 项目总入口、目录说明、环境建立与检查方法 |
| [AGENTS.md](AGENTS.md) | 主执行规范，约束助手和协作流程；辅助计划不能改写原文规则 |
| [PROJECT.md](PROJECT.md) | 当前设备、环境、版本、项目位置与待确认事实 |
| [CURRENT_TASK.md](CURRENT_TASK.md) | 当前任务与下一步入口，开始学习时先阅读 |
| [pyproject.toml](pyproject.toml) | Python 包名称、版本、Python 要求、依赖和构建规则 |
| [.gitignore](.gitignore) | 指定不进入 Git 的环境、缓存、构建产物及本地配置 |
| [.vscode/settings.json](.vscode/settings.json) | VS Code 的项目解释器与测试入口配置 |
| .venv/ | 本机 Python 虚拟环境；通过安装脚本生成，不上传 GitHub |
| .git/ | Git 历史、分支和远端元数据，由 Git 管理 |
| .gitkeep | 保留当前空目录的占位文件，不代表目录内功能已经实现 |
| COLCON_IGNORE | 位于预留 ROS 包目录内，供 colcon 忽略尚未准备好的包位置 |
| [scripts/setup_environment.sh](scripts/setup_environment.sh) | 创建或复用本地虚拟环境，构建并安装项目包 |
| [scripts/check_environment.py](scripts/check_environment.py) | 只读报告当前解释器、包元数据与工具可见性 |
| [scripts/check_repository.py](scripts/check_repository.py) | 检查必要文件、目录、Markdown 文件链接、任务引用与 Python 语法 |
| [docs/source/AGENTS-V1.2.pdf](docs/source/AGENTS-V1.2.pdf) | 用户提供的原始规范副本，用于回查目录和流程依据 |
| [docs/source-map.md](docs/source-map.md) | 原文要求与本仓库文件之间的对应关系 |

templates/ 提供理论笔记、工程笔记、实验报告、故障案例、代码审查、每日任务、阶段考核和 ADR 八类模板。使用时复制到对应业务目录，填写真实内容，模板本身不算完成记录。

## 完整项目目录

下方覆盖当前提交范围内的全部目录与文件，并列出 AGENTS 原文规划的后续文件。标记含义：

- 无标记的文件已经存在；包和目录存在不代表业务功能已经实现。
- `[规划]` 表示原文规定的目标文件，尚未创建，随学习任务逐步实现。
- `[预留]` 表示当前仅用 `.gitkeep` 保留的目录；树中省略 `.gitkeep` 文件本身。
- `.git/`、`.venv/`、缓存、构建产物和本地私有配置不属于上传内容，因此不列入目录树。

<!-- project-tree:start -->
```text
dm4310-motorbridge-control/
├── .gitignore
├── .vscode/
│   └── settings.json
├── AGENTS.md
├── config/
│   ├── motors.example.yaml
│   ├── README.md
│   ├── robot_2dof.example.yaml
│   └── safety.example.yaml
├── CURRENT_TASK.md
├── docs/
│   ├── source/
│   │   └── AGENTS-V1.2.pdf
│   └── source-map.md
├── engineering/
│   ├── architecture/
│   │   ├── control-data-flow.md  [规划]
│   │   ├── motor-driver.md  [规划]
│   │   ├── ros2-integration.md  [规划]
│   │   ├── s1-001-evidence-card-design.md
│   │   ├── safety-architecture.md  [规划]
│   │   ├── system-overview.md
│   │   └── target-layout.md
│   ├── design-decisions/
│   │   ├── ADR-0001-incremental-repository.md
│   │   ├── ADR-0002-motorbridge-first.md
│   │   └── README.md
│   ├── hardware/  [预留]
│   │   ├── can-adapter.md  [规划]
│   │   ├── dm4310.md  [规划]
│   │   ├── power-supply.md  [规划]
│   │   └── safety-limits.md  [规划]
│   ├── initialization-validation.md
│   ├── interfaces/
│   │   ├── joint-interfaces.md  [规划]
│   │   └── motor-api.md
│   ├── motorbridge-api-baseline.md
│   └── repository-baseline.md
├── examples/
│   ├── README.md
│   ├── S1_can_and_id/
│   │   ├── 001_motorbridge_intro.py
│   │   ├── enable_disable.py  [规划]
│   │   ├── read_state.py  [规划]
│   │   ├── scan_motor.py  [规划]
│   │   └── set_id.py  [规划]
│   ├── S2_single_motor/  [预留]
│   │   ├── feedback_logging.py  [规划]
│   │   ├── mit_control.py  [规划]
│   │   ├── pos_vel_control.py  [规划]
│   │   └── vel_control.py  [规划]
│   ├── S3_ros2_basics/  [预留]
│   ├── S4_ros2_control/  [预留]
│   ├── S5_multi_motor/  [预留]
│   ├── S6_fk_ik/  [预留]
│   ├── S7_dynamics/  [预留]
│   └── S8_3dof_robot/  [预留]
├── experiments/
│   ├── datasets/  [预留]
│   ├── dynamics/  [预留]
│   ├── kinematics/  [预留]
│   ├── multi-motor/  [预留]
│   ├── README.md
│   ├── ros2/  [预留]
│   └── single-motor/  [预留]
├── knowledge/
│   ├── can-communication/  [预留]
│   │   ├── can-basics.md  [规划]
│   │   ├── can-frame.md  [规划]
│   │   ├── dm-protocol.md  [规划]
│   │   └── motor-id.md  [规划]
│   ├── control-theory/  [预留]
│   │   ├── cascaded-control.md  [规划]
│   │   ├── discrete-control.md  [规划]
│   │   ├── pid.md  [规划]
│   │   ├── sampling-time.md  [规划]
│   │   └── stability.md  [规划]
│   ├── dynamics/  [预留]
│   │   ├── gravity-compensation.md  [规划]
│   │   ├── impedance-control.md  [规划]
│   │   ├── mass-matrix.md  [规划]
│   │   ├── null-space-control.md  [规划]
│   │   ├── pinocchio.md  [规划]
│   │   └── rigid-body-dynamics.md  [规划]
│   ├── index.md
│   ├── kinematics/  [预留]
│   │   ├── dh-parameters.md  [规划]
│   │   ├── forward-kinematics.md  [规划]
│   │   ├── inverse-kinematics.md  [规划]
│   │   ├── jacobian.md  [规划]
│   │   └── singularities.md  [规划]
│   ├── mathematics/  [预留]
│   │   ├── coordinate-transform.md  [规划]
│   │   ├── euler-angles.md  [规划]
│   │   ├── linear-algebra.md  [规划]
│   │   ├── quaternion.md  [规划]
│   │   └── rotation-matrix.md  [规划]
│   ├── mechanics/  [预留]
│   │   ├── friction.md  [规划]
│   │   ├── gear-ratio.md  [规划]
│   │   ├── inertia.md  [规划]
│   │   └── torque.md  [规划]
│   ├── motor-control/
│   │   ├── mit-control.md  [规划]
│   │   ├── motor-basics.md  [规划]
│   │   ├── motorbridge.md
│   │   ├── pos-vel-control.md  [规划]
│   │   └── velocity-control.md  [规划]
│   ├── robotics/
│   │   ├── coordinate-frames.md  [规划]
│   │   ├── robot-architecture.md
│   │   └── urdf.md  [规划]
│   └── ros2/  [预留]
│       ├── hardware-interface.md  [规划]
│       ├── joint-state.md  [规划]
│       ├── nodes.md  [规划]
│       ├── ros2-control.md  [规划]
│       ├── tf2.md  [规划]
│       └── topics-services-actions.md  [规划]
├── learning/
│   ├── assessments/  [预留]
│   │   ├── S1/  [预留]
│   │   ├── S2/  [预留]
│   │   ├── S3/  [预留]
│   │   ├── S4/  [预留]
│   │   ├── S5/  [预留]
│   │   ├── S6/  [预留]
│   │   ├── S7/  [预留]
│   │   └── S8/  [预留]
│   ├── daily/
│   │   └── 2026-10-10-S1-001.md
│   ├── progress.md
│   ├── reviews/
│   │   └── 2026-10-10-S1-001-review.md
│   ├── SCHEDULE.md
│   └── WORKFLOW.md
├── PROJECT.md
├── pyproject.toml
├── README.md
├── roadmap/
│   ├── backlog.md
│   ├── master-roadmap.md
│   ├── milestones.md
│   ├── prerequisites.md
│   └── README.md
├── ros2_ws/
│   ├── README.md
│   └── src/
│       ├── dm_motor_driver/
│       │   ├── COLCON_IGNORE
│       │   ├── dm_motor_driver/  [预留]
│       │   ├── package.xml  [规划]
│       │   ├── setup.cfg  [规划]
│       │   └── setup.py  [规划]
│       ├── dm_motor_hardware/
│       │   ├── CMakeLists.txt  [规划]
│       │   ├── COLCON_IGNORE
│       │   ├── include/  [预留]
│       │   ├── package.xml  [规划]
│       │   └── src/  [预留]
│       ├── dm_robot_bringup/
│       │   ├── COLCON_IGNORE
│       │   ├── config/  [预留]
│       │   ├── launch/  [预留]
│       │   └── package.xml  [规划]
│       ├── dm_robot_description/
│       │   ├── COLCON_IGNORE
│       │   ├── meshes/  [预留]
│       │   ├── package.xml  [规划]
│       │   ├── rviz/  [预留]
│       │   └── urdf/  [预留]
│       │       ├── arm_2dof.urdf.xacro  [规划]
│       │       └── arm_3dof.urdf.xacro  [规划]
│       ├── dm_robot_interfaces/
│       │   ├── action/  [预留]
│       │   ├── CMakeLists.txt  [规划]
│       │   ├── COLCON_IGNORE
│       │   ├── msg/  [预留]
│       │   ├── package.xml  [规划]
│       │   └── srv/  [预留]
│       └── dm_robot_moveit_config/
│           └── COLCON_IGNORE
├── scripts/
│   ├── check_environment.py
│   ├── check_repository.py
│   └── setup_environment.sh
├── simulation/
│   ├── fake_hardware/  [预留]
│   ├── models/  [预留]
│   ├── mujoco/  [预留]
│   ├── README.md
│   └── scripts/  [预留]
├── src/
│   ├── README.md
│   └── robot_control/
│       ├── __init__.py
│       ├── actuator/
│       │   ├── __init__.py
│       │   ├── motor_manager.py  [规划]
│       │   ├── motor_state.py  [规划]
│       │   └── motorbridge_adapter.py  [规划]
│       ├── controllers/
│       │   ├── __init__.py
│       │   ├── gravity_compensation.py  [规划]
│       │   ├── multi_joint.py  [规划]
│       │   ├── single_joint.py  [规划]
│       │   └── state_machine.py  [规划]
│       ├── dynamics/
│       │   ├── __init__.py
│       │   ├── gravity.py  [规划]
│       │   ├── pinocchio_model.py  [规划]
│       │   └── robot_model.py  [规划]
│       ├── kinematics/
│       │   ├── __init__.py
│       │   ├── forward_kinematics.py  [规划]
│       │   ├── inverse_kinematics.py  [规划]
│       │   ├── jacobian.py  [规划]
│       │   └── robot_model.py  [规划]
│       ├── safety/
│       │   ├── __init__.py
│       │   ├── fault_handler.py  [规划]
│       │   ├── limits.py  [规划]
│       │   └── watchdog.py  [规划]
│       ├── trajectory/
│       │   ├── __init__.py
│       │   ├── interpolator.py  [规划]
│       │   ├── trajectory_planner.py  [规划]
│       │   └── trajectory_tracker.py  [规划]
│       └── utils/
│           ├── __init__.py
│           ├── data_logger.py  [规划]
│           └── units.py  [规划]
├── templates/
│   ├── adr.md
│   ├── code-review.md
│   ├── daily-task.md
│   ├── engineering-note.md
│   ├── experiment-report.md
│   ├── README.md
│   ├── stage-assessment.md
│   ├── theory-note.md
│   └── troubleshooting-case.md
├── tests/
│   ├── fixtures/  [预留]
│   ├── hardware/
│   │   └── README.md
│   ├── integration/
│   │   └── test_package_imports.py
│   ├── README.md
│   └── unit/  [预留]
└── troubleshooting/
    ├── cases/
    │   └── 2026-10-09-editable-pth-hidden.md
    ├── index.md
    └── unresolved.md
```
<!-- project-tree:end -->

目录与职责依据 [AGENTS 原文完整目标目录](engineering/architecture/target-layout.md)。当前 Python 职责包可安装和导入，电机控制、运动学和动力学业务代码尚待实现。
ROS 2 预留目录带 COLCON_IGNORE，尚不是可构建的软件包；确认实际发行版后再补合法包描述与实现。
正式理论讲义、设计材料及每日任务从 2026-10-10 起随实际任务生成；具体学习进度见 [当前任务](CURRENT_TASK.md)。

## 建立开发环境

需要 Python 3.10+；脚本适用于当前 macOS 和后续 Linux 主机：

```bash
bash scripts/setup_environment.sh
```

指定解释器可使用 `PYTHON_BIN=/绝对路径/python3 bash scripts/setup_environment.sh`。
脚本在本仓库建立 .venv 并构建、安装本地 wheel；构建隔离可能下载 setuptools。修改 src 下源码后重新运行此脚本完成安装更新。
不安装 MotorBridge、ROS 2 或仿真器，不打开任何硬件设备。运行时依赖当前为空，真实依赖在对应阶段核对后添加。
VS Code 已配置本地 .venv 解释器路径和仅运行 integration 的测试入口，需要 VS Code Python 扩展才能使用其测试界面。

## 验证仓库

```bash
.venv/bin/python scripts/check_repository.py
.venv/bin/python -m unittest discover -s tests/integration -p 'test_*.py' -v
.venv/bin/python scripts/check_environment.py
```

当前集成检查验证：安装后的八个核心包能从仓库外的隔离 Python 进程导入，且不自动加载可选硬件/ROS 库。
这不是控制逻辑或硬件实验。unit 和 hardware 目前没有业务测试。

## 版本管理

GitHub 私有仓库：[s1eep1y416-desig/dm4310-motorbridge-control](https://github.com/s1eep1y416-desig/dm4310-motorbridge-control)，默认开发分支为 main，远端名称为 origin。
.venv、构建产物、缓存、环境变量文件和本地硬件配置忽略提交；空目录通过 .gitkeep 保留。
新增、删除或移动项目文件时同步维护上方完整目录树，并保持已存在文件与规划文件的标记准确。
Git 操作按用户明确授权执行；不要将其他项目的远端或未提交变更自动并入本项目。
