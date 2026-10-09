# 原文完整目标目录

来源：[AGENTS.md.pdf](../../docs/source/AGENTS-V1.2.pdf) 第 6 节（p7–13）。下方保留原文目录名称与层级，移除 PDF 分页和版面噪声。
原文 §6.1/§33.3 同时要求按阶段创建当前需要的文件，不要求初始化时生成全部代码或空笔记。

```text
dm4310-motorbridge-control/
│
├── AGENTS.md
├── README.md
├── PROJECT.md
├── pyproject.toml
├── .gitignore
│
├── config/
│   ├── README.md
│   ├── motors.example.yaml
│   ├── safety.example.yaml
│   └── robot_2dof.example.yaml
│
├── src/
│   └── robot_control/
│       ├── __init__.py
│       │
│       ├── actuator/
│       │   ├── __init__.py
│       │   ├── motorbridge_adapter.py
│       │   ├── motor_manager.py
│       │   └── motor_state.py
│       │
│       ├── controllers/
│       │   ├── __init__.py
│       │   ├── single_joint.py
│       │   ├── multi_joint.py
│       │   ├── state_machine.py
│       │   └── gravity_compensation.py
│       │
│       ├── kinematics/
│       │   ├── __init__.py
│       │   ├── robot_model.py
│       │   ├── forward_kinematics.py
│       │   ├── inverse_kinematics.py
│       │   └── jacobian.py
│       │
│       ├── dynamics/
│       │   ├── __init__.py
│       │   ├── robot_model.py
│       │   ├── pinocchio_model.py
│       │   └── gravity.py
│       │
│       ├── trajectory/
│       │   ├── __init__.py
│       │   ├── interpolator.py
│       │   ├── trajectory_planner.py
│       │   └── trajectory_tracker.py
│       │
│       ├── safety/
│       │   ├── __init__.py
│       │   ├── limits.py
│       │   ├── watchdog.py
│       │   └── fault_handler.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── units.py
│           └── data_logger.py
│
├── examples/
│   ├── S1_can_and_id/
│   │   ├── scan_motor.py
│   │   ├── set_id.py
│   │   ├── read_state.py
│   │   └── enable_disable.py
│   │
│   ├── S2_single_motor/
│   │   ├── mit_control.py
│   │   ├── pos_vel_control.py
│   │   ├── vel_control.py
│   │   └── feedback_logging.py
│   │
│   ├── S3_ros2_basics/
│   ├── S4_ros2_control/
│   ├── S5_multi_motor/
│   ├── S6_fk_ik/
│   ├── S7_dynamics/
│   └── S8_3dof_robot/
│
├── ros2_ws/
│   └── src/
│       │
│       ├── dm_motor_driver/
│       │   ├── dm_motor_driver/
│       │   ├── package.xml
│       │   ├── setup.py
│       │   └── setup.cfg
│       │
│       ├── dm_motor_hardware/
│       │   ├── include/
│       │   ├── src/
│       │   ├── package.xml
│       │   └── CMakeLists.txt
│       │
│       ├── dm_robot_description/
│       │   ├── urdf/
│       │   │   ├── arm_2dof.urdf.xacro
│       │   │   └── arm_3dof.urdf.xacro
│       │   ├── meshes/
│       │   ├── rviz/
│       │   └── package.xml
│       │
│       ├── dm_robot_bringup/
│       │   ├── launch/
│       │   ├── config/
│       │   └── package.xml
│       │
│       ├── dm_robot_interfaces/
│       │   ├── msg/
│       │   ├── srv/
│       │   ├── action/
│       │   ├── package.xml
│       │   └── CMakeLists.txt
│       │
│       └── dm_robot_moveit_config/
│           # 后续有需要时创建
│
├── simulation/
│   ├── fake_hardware/
│   ├── mujoco/
│   ├── models/
│   └── scripts/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── hardware/
│   └── fixtures/
│
├── roadmap/
│   ├── README.md
│   ├── master-roadmap.md
│   ├── milestones.md
│   ├── prerequisites.md
│   └── backlog.md
│
├── knowledge/
│   ├── index.md
│   │
│   ├── mathematics/
│   │   ├── linear-algebra.md
│   │   ├── coordinate-transform.md
│   │   ├── rotation-matrix.md
│   │   ├── euler-angles.md
│   │   └── quaternion.md
│   │
│   ├── mechanics/
│   │   ├── torque.md
│   │   ├── inertia.md
│   │   ├── gear-ratio.md
│   │   └── friction.md
│   │
│   ├── motor-control/
│   │   ├── motor-basics.md
│   │   ├── mit-control.md
│   │   ├── pos-vel-control.md
│   │   ├── velocity-control.md
│   │   └── motorbridge.md
│   │
│   ├── control-theory/
│   │   ├── pid.md
│   │   ├── cascaded-control.md
│   │   ├── sampling-time.md
│   │   ├── discrete-control.md
│   │   └── stability.md
│   │
│   ├── can-communication/
│   │   ├── can-basics.md
│   │   ├── can-frame.md
│   │   ├── motor-id.md
│   │   └── dm-protocol.md
│   │
│   ├── ros2/
│   │   ├── nodes.md
│   │   ├── topics-services-actions.md
│   │   ├── joint-state.md
│   │   ├── tf2.md
│   │   ├── ros2-control.md
│   │   └── hardware-interface.md
│   │
│   ├── robotics/
│   │   ├── robot-architecture.md
│   │   ├── urdf.md
│   │   └── coordinate-frames.md
│   │
│   ├── kinematics/
│   │   ├── forward-kinematics.md
│   │   ├── inverse-kinematics.md
│   │   ├── dh-parameters.md
│   │   ├── jacobian.md
│   │   └── singularities.md
│   │
│   └── dynamics/
│       ├── rigid-body-dynamics.md
│       ├── mass-matrix.md
│       ├── pinocchio.md
│       ├── gravity-compensation.md
│       ├── impedance-control.md
│       └── null-space-control.md
│
├── engineering/
│   ├── architecture/
│   │   ├── system-overview.md
│   │   ├── motor-driver.md
│   │   ├── control-data-flow.md
│   │   ├── ros2-integration.md
│   │   └── safety-architecture.md
│   │
│   ├── design-decisions/
│   │   └── README.md
│   │
│   ├── hardware/
│   │   ├── dm4310.md
│   │   ├── can-adapter.md
│   │   ├── power-supply.md
│   │   └── safety-limits.md
│   │
│   └── interfaces/
│       ├── motor-api.md
│       └── joint-interfaces.md
│
├── experiments/
│   ├── single-motor/
│   ├── multi-motor/
│   ├── ros2/
│   ├── kinematics/
│   ├── dynamics/
│   └── datasets/
│
├── troubleshooting/
│   ├── index.md
│   ├── unresolved.md
│   └── cases/
│
├── learning/
│   ├── progress.md
│   ├── daily/
│   ├── assessments/
│   │   ├── S1/
│   │   ├── S2/
│   │   ├── S3/
│   │   ├── S4/
│   │   ├── S5/
│   │   ├── S6/
│   │   ├── S7/
│   │   └── S8/
│   └── reviews/
│
├── templates/
│   ├── theory-note.md
│   ├── engineering-note.md
│   ├── experiment-report.md
│   ├── troubleshooting-case.md
│   ├── code-review.md
│   ├── daily-task.md
│   ├── stage-assessment.md
│   └── adr.md
│
└── scripts/
    ├── check_environment.py
    └── setup_environment.sh
```

## 当前落实状态

用户要求先完成新仓库，再确定学习路线。本次已按上方树预留全部目录层级，并用 .gitkeep 保留没有内容的叶目录。

| 部分 | 当前实现 | 待对应任务实现 |
|---|---|---|
| Python 核心 | pyproject.toml、八个可导入包 | 各模块的具体控制/数学接口与代码 |
| config | motors、safety、robot_2dof 示例 | 有证据的设备参数与真实模型 |
| tests | 分区与安装/导入集成检查 | 用户业务单元测试、真实硬件测试 |
| examples / simulation | 所有原文目录层级 | 示例、替身和有效仿真模型 |
| ros2_ws | 原文目录层级及 COLCON_IGNORE | 选定发行版后的有效 ROS 包 |
| knowledge / engineering / experiments / learning | 目录、现有索引、模板与记录 | 实际产生的文章、设计、数据和考核 |
| scripts | 环境初始化、环境报告、仓库检查 | 后续真实依赖的按需扩展 |

预留目录不表示功能已完成；未创建原文列出的空理论文章或未经确认的业务接口文件。
CURRENT_TASK、来源映射、初始化检查等为辅助入口，不改写主规范。
