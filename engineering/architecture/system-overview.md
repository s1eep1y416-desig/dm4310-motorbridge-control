# 系统架构与参考核对

这是计划架构。当前已建立全部目录层级、可安装 Python 职责包与环境/检查入口，具体业务功能尚未实现。
目录名称与层级以 AGENTS 原文为准，见 [完整目标目录](target-layout.md)。本文只解释分层和阶段落实，不能替代原文结构。

## 本项目的分层

| 层 | 计划职责 | 引入时点 |
|---|---|---|
| 应用 | CLI 示例、ROS 2 节点、机器人任务 | S1/S3 起 |
| controllers | 单/多关节状态机与控制流程 | S2/S5 |
| trajectory | 插值、离线采样、跟踪 | S5 |
| kinematics | 模型、FK、IK、Jacobian | S6 |
| dynamics | Pinocchio、逆动力学与重力项 | S7 |
| actuator | 状态抽象、MotorBridge 适配、设备管理 | S1/S5 |
| safety | 参数验证、限制、超时、故障处理 | S1 起，贯穿控制路径 |
| 传输 | MotorBridge 实际 ABI、CAN/串口设备 | 确认后使用，不重复实现完整底层驱动 |

依赖方向：应用 → 控制/算法 → 设备抽象 → SDK/传输。kinematics、dynamics 和 trajectory 可离线运行，actuator 不依赖 ROS 2。
命令必须经过模式、参数和限制检查；反馈保留身份、有效性与可证明的时间信息，再进入控制和日志。
统一关节状态计划包含 name、position(rad)、velocity(rad/s)、可确认的 effort、时间语义、故障与有效性；没有真实来源的字段保留未知。

## 控制权与 ROS 2

CLI、Python ROS 驱动、ros2_control 只能在明确互斥或可验证切换下控制同一设备。
先构造 S3 的节点接口，再在 S4 验证标准 Hardware Interface；共享配置和状态来源，避免两个驱动各维护一份真实状态。
ros2_control 的控制器管理与硬件资源生命周期需要按所选版本验证。框架通过硬件 read、控制器更新和 write 组织循环，硬件插件与普通 Python ROS 节点是不同集成点。[官方架构说明](https://control.ros.org/jazzy/doc/getting_started/getting_started.html)
具体 C++/C ABI 或桥接方式在 S4-001 决策，当前没有选择未经验证的兼容接口。

## reBot 参考核对及边界

核对日期：2026-10-09。参考的是模块分工，不迁移六轴参数、增益或结构尺寸。

- [reBotArm_control_py](https://github.com/Seeed-Projects/reBotArm_control_py)：确认公开仓库及说明入口；Python 核心目录完整树本次受 GitHub API 限流和读取错误影响，未完成逐文件审查。actuator/controllers/kinematics/dynamics 的实际模块使用另由下述 ROS 源码 import 直接印证；trajectory 的具体源码职责仍待后续核对，不写成已验证。
- [reBotArmController_ROS2](https://github.com/Seeed-Projects/reBotArmController_ROS2/tree/7506dc0fc5c2a7787dcb974d89d13f9f49d16d61)：核对源码树及 `hardware_manager.py`、`rebotarm_controller.py`。此提交的包包括 rebotarmcontroller、rebotarm_msgs、rebotarm_bringup、rebotarm_moveit_config、rebotarm_moveit_demos、rebotarm_agent、rebotarm_mujoco_rs；比网页 README 的五包描述更广，计划以实际树为准。
- [reBot-DevArm](https://github.com/Seeed-Projects/reBot-DevArm)：作为整体机器人项目资料入口；本次未核对其机械参数、BOM、许可证或硬件适配，不将它们引入本项目。

[HardwareManager 源码](https://github.com/Seeed-Projects/reBotArmController_ROS2/blob/7506dc0fc5c2a7787dcb974d89d13f9f49d16d61/src/rebotarmcontroller/rebotarmcontroller/hardware_manager.py) 使用 `RebotArm`、`RebotArmEndPose`、重力计算及 FK/模型加载接口；[节点源码](https://github.com/Seeed-Projects/reBotArmController_ROS2/blob/7506dc0fc5c2a7787dcb974d89d13f9f49d16d61/src/rebotarmcontroller/rebotarmcontroller/rebotarm_controller.py) 将硬件管理、发布、服务与动作分开。
对本项目可取的设计判断：核心控制与 ROS 对接分离，先做最小单关节接口，再按需扩展模型与多关节。该判断不是上述参考项目对本设备兼容性的保证。

本项目 safety、knowledge、learning、experiments、engineering 是自身约定，不声称都来自 reBot。
只参考与链接，没有复制上游源码；若未来复用源码，必须先核对具体提交的许可证，不能因为仓库公开就假定可任意复制。

## 目录演进

依据用户“先把仓库弄完”的要求，原文目录已预留，Python 核心包与 pyproject.toml 已建立并纳入安装/导入验证。
各业务 .py 文件按实际接口设计创建；S1/S2 实现通信与控制，S3/S4 建立有效 ROS 包，S5–S7 实现多关节、运动学与动力学。
预留的 ROS 目录通过 COLCON_IGNORE 隔离，直到发行版、依赖和包描述确认；自定义消息、MoveIt 仍只在有需求时实现。
