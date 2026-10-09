# 项目事实与约束

更新：2026-10-09，Asia/Shanghai。项目名统一为 `dm4310-motorbridge-control`；PDF 封面使用 `dm-motorbridge-control`，目录示例使用前者，此处采用目录名，不代表迁移现有同名远端。

## 当前基线

| 项目 | 事实 | 证据/边界 |
|---|---|---|
| 仓库位置 | `/Users/jkhkjg/Desktop/dm4310-motorbridge-control` | 2026-10-09 按用户要求迁至桌面；原输出位置保留符号链接，仍是同一仓库 |
| 项目目标 | 六个月内验证双电机机械臂；三自由度为挑战 | 用户提供 PDF §8 |
| 当前阶段 | REPO-001 仓库基础完成；S1–S8 尚未开始 | 安装与导入验证已通过，学习能力未评估 |
| 本仓库代码 | 可安装 Python 核心包、环境工具、安装/导入集成检查；无电机业务实现 | 独立新建 |
| 学习者能力 | 待基于成果评估 | 不从旧聊天/代码存在推断掌握 |
| 电机 | PDF 声明达妙 DM4310P，1 台 | 铭牌、可用性、固件、与 SDK `4310` 的映射待确认 |
| CAN 设备 | PDF 声明已有设备 | 型号、驱动及传输方式待确认 |
| 第二/第三台电机与机械臂 | 计划项 | 未确认已购入或装配 |
| 当前编辑主机 | macOS 26.4，arm64 | 本次 platform 查询 |
| 文档工具解释器 | Python 3.12.14 | Codex 随附运行时 |
| 新仓库开发环境 | 本仓库 .venv，Python 3.12.14，项目包 0.1.0 | 标准 wheel 安装及仓库外导入验证通过；未安装硬件/ROS 依赖 |
| 现有 SDK 环境 | 桌面 motorbridge/.venv，Python 3.13.15 / MotorBridge 0.5.6 | 该解释器运行只读环境脚本及源码读取；未导入 ABI 或连接设备 |
| 当前 shell | python3 指向另一处 motorbridge/venv | 不据此断言它与桌面虚拟环境相同 |
| ROS 2 / colcon | 当前 PATH 未发现 | 不等于其他机器/未激活环境未安装 |
| 控制目标主机 | 待确认；文档目标栈包含 Ubuntu | 不把当前 Mac 当 Ubuntu |
| ROS 2 / ros2_control / Pinocchio / MuJoCo | 项目版本未选定 | 在对应阶段核对兼容矩阵后记录 |
| GitHub | [s1eep1y416-desig/dm4310-motorbridge-control](https://github.com/s1eep1y416-desig/dm4310-motorbridge-control)，私有仓库 | 2026-10-09 用户授权上传；origin 指向该新仓库，开发分支 main |

## 必须补齐的设备事实

固件、减速比及电机轴/输出轴定义、适配器、CAN 通道/串口、CAN bit/s 与串口 baud、Motor ID、Master/Feedback ID、供电与限流、零点、方向、机械行程、负载与固定、停机与急停方案。
上述值目前均待确认，不能从旧代码的 `0x01`、`0x11`、`/dev/ttyACM0` 或速度常量继承。

## 当前任务范围

本次建立本地仓库、路线、任务和管理基础。只读查看旧项目与 SDK 源码，未执行旧控制程序、测试或硬件命令。
原文默认每天约两小时、每次一个核心任务。每周五个核心学习单元、一个复盘单元、一个可选缓冲日只是本次排期建议，不是 AGENTS 的强制要求，实际可用时间待用户调整。
当前任务可在无硬件时推进。硬件是否在手未确认，不将所有阶段提前写为 Pending Hardware；仅在必需实验被硬件阻塞时使用该状态。

## 资料权威与变更

事实以本文件及可复现环境/设备证据为准；任务身份和状态以 [任务池](roadmap/backlog.md) 为准；阶段通过条件以 [里程碑](roadmap/milestones.md) 为准。
[当前任务](CURRENT_TASK.md) 与 [进度](learning/progress.md) 仅提供导航和摘要。
版本变化、硬件参数确认及路线调整记录日期、证据和理由，重要变化通过 ADR 保留。
