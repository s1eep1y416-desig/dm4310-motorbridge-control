# DM4310 MotorBridge Control

独立新建的机器人控制开发仓库。以 [AGENTS.md](AGENTS.md) 及用户提供的原文为主规范，按原文目录组织。
仓库基础已完成安装和导入验证；业务实现由后续阶段逐步增加。旧项目仅作参考，没有复制其源码或继承学习成绩。

## 仓库入口

| 内容 | 入口 |
|---|---|
| 工作规则 | [AGENTS.md](AGENTS.md) |
| 实际环境、设备与未知项 | [PROJECT.md](PROJECT.md) |
| 当前工作 | [CURRENT_TASK.md](CURRENT_TASK.md) |
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
│   │   ├── safety-architecture.md  [规划]
│   │   ├── system-overview.md
│   │   └── target-layout.md
│   ├── design-decisions/
│   │   ├── ADR-0001-incremental-repository.md
│   │   └── README.md
│   ├── hardware/  [预留]
│   │   ├── can-adapter.md  [规划]
│   │   ├── dm4310.md  [规划]
│   │   ├── power-supply.md  [规划]
│   │   └── safety-limits.md  [规划]
│   ├── initialization-validation.md
│   ├── interfaces/  [预留]
│   │   ├── joint-interfaces.md  [规划]
│   │   └── motor-api.md  [规划]
│   ├── motorbridge-api-baseline.md
│   └── repository-baseline.md
├── examples/
│   ├── README.md
│   ├── S1_can_and_id/  [预留]
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
│   ├── motor-control/  [预留]
│   │   ├── mit-control.md  [规划]
│   │   ├── motor-basics.md  [规划]
│   │   ├── motorbridge.md  [规划]
│   │   ├── pos-vel-control.md  [规划]
│   │   └── velocity-control.md  [规划]
│   ├── robotics/  [预留]
│   │   ├── coordinate-frames.md  [规划]
│   │   ├── robot-architecture.md  [规划]
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
│   ├── daily/  [预留]
│   ├── progress.md
│   ├── reviews/  [预留]
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
