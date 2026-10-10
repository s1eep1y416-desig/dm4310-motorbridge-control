# MotorBridge 入门：从 Python 接口开始

日期：2026-10-10。对应 S1-001。本文按本机已安装的 MotorBridge **0.5.6** 编写；学习者理解尚未评估。

## 先知道自己要写哪一层

你要写的是使用 MotorBridge 的 Python 程序。SDK 提供设备连接、电机命令和状态访问能力；先学会调用这些接口，逐步把它们组织成自己的关节控制模块。

```text
你的程序
  └─ Controller：一条通信连接，管理这条连接上的设备
       └─ Motor：一个电机的操作对象
            ├─ 发送请求或控制命令
            └─ get_state() → MotorState 或 None
```

这张图描述 API 对象关系，不表示已经连接真实设备。完整项目分层可按需阅读 [系统架构](../../engineering/architecture/system-overview.md)。

## 三个对象，各负责什么

| 对象 | 在程序中的角色 | 你现在要认识的接口 |
|---|---|---|
| `Controller` | 管理通信连接、添加设备、轮询反馈 | `add_damiao_motor(...)`、`poll_feedback_once()`、`close_bus()`、`close()` |
| `Motor` | 操作一个已添加的电机 | `request_feedback()`、`get_state()`、`enable()`、`disable()`、`ensure_mode(...)` |
| `MotorState` | 保存一次可读取的状态值，不负责连接或发命令 | `pos`、`vel`、`torq`、身份与温度等字段 |

`controller.add_damiao_motor(motor_id, feedback_id, model)` 返回 `Motor`；这里是把设备添加到 SDK 的管理对象，不等于改写电机内部 ID。真实三个参数以后从设备资料确认。

本地 `Motor.get_state()` 返回 `MotorState | None`：底层 `has_value` 为假时返回 `None`，否则把状态字段转换成 Python 对象。`None` 是没有可返回状态，不能解释为位置和速度都为零。

## 读懂一段反馈流程

下面只用于阅读，假定 `controller` 与 `motor` 已由后续连接任务正确建立；今天不执行这三行：

```python
motor.request_feedback()
controller.poll_feedback_once()
state = motor.get_state()
```

依次表达：请求这台电机反馈、让通信对象执行一次反馈轮询、取得该电机当前可读状态。三者不是同一个操作。Python 包装没有给 `poll_feedback_once()` 提供 timeout 参数，也没有通过返回值直接告知本次接收了哪一台设备的新帧。

实际接收方式、阻塞时长和缓存更新须结合具体传输实现核对。今天只认识调用分工，后续 S1-003 再处理反馈新鲜度；不能单凭 `get_state()` 非空就认定刚收到了反馈。

## MotorState 里有什么

| 字段 | 入门时怎样阅读 |
|---|---|
| `can_id`、`arbitration_id` | 身份/报文相关标识，真实映射在连接任务中核对 |
| `status_code` | 状态码；含义要查设备协议，不能自行把 0 当作一切正常 |
| `pos`、`vel` | 位置与速度；本次合成练习约定 rad、rad/s，真机还需核对轴、方向和单位 |
| `torq` | 原样保存的 SDK 字段；当前未确认 DM4310P 固件语义，不直接标成关节 N·m |
| `t_mos`、`t_rotor` | 温度相关字段；实际单位、有效范围由协议确认 |

该版本的 `MotorState` 没有 timestamp、sequence 或 enabled 字段。显示数值与判定反馈有效是两个工作，本课只做前者。

角度显示换算：`角度(deg) = 位置(rad) × 180 / π`。例如 π rad 对应 180°。只改变显示单位，不代表对电机下发新位置；也没有处理减速比或电机轴到关节轴的转换。

## 后面怎样控制一个电机

先认识三个入口，具体参数、单位、限制和实验在 S2 展开：

| 模式 | Python 入口 | 学习重点 |
|---|---|---|
| POS_VEL | `motor.send_pos_vel(pos, vlim)` | 目标位置和速度限制 |
| VEL | `motor.send_vel(vel)` | 目标速度与停止条件 |
| MIT | `motor.send_mit(pos, vel, kp, kd, tau)` | 位置、速度、增益与额外输出项 |

模式通过 `ensure_mode(...)` 准备；模式准备、使能和退出的设备适用顺序应按实际版本与设备核对。发送成功不能代替反馈到位判断。今天不填真实运动参数。

## 今天的小程序

你独立实现 `describe_state(state)`，把 `MotorState` 或 `None` 变成一行易读文字。使用 SDK 自己的数据类型，先让程序能展示没有反馈、静止和有速度的三种合成输入。

可用的导入提示：

```python
from math import degrees
from motorbridge import MotorState
```

`MotorState` 是 frozen dataclass：创建时填入上表八个字段；要使用新的值就构造另一个对象。合成输入由你给定，不代表电机实测，不需要创建 `Controller` 或 `Motor`。

接下来读 [本次程序设计](../../engineering/interfaces/motor-api.md)，按 [任务卡](../../learning/daily/2026-10-10-S1-001.md) 写自己的程序。

## 版本、源码和学习环境

本课执行解释器：`/Users/jkhkjg/Desktop/motorbridge/.venv/bin/python`，Python 3.13.15、MotorBridge 0.5.6。练习代码仍保存在新仓库。新仓库自己的 Python 3.12 环境用于仓库检查，尚未安装 SDK；本课复用已存在的 SDK 环境，不自动安装或迁移依赖。

2026-10-10 实测只导入并构造合成 `MotorState`，测试中禁止 `ctypes.CDLL` 加载本地库，仍成功。这只验证本课数据类型可用，没有创建通信对象、加载 motor ABI 或访问电机，也没有代写学习者练习。

本机一手源码目录：`/Users/jkhkjg/Desktop/motorbridge/.venv/lib/python3.13/site-packages/motorbridge/`。初学只定位 `core.py` 的 `Controller`、`Motor.get_state` 和 `models.py` 的 `MotorState`，不要求从头读 ABI 源码。

- 版本和文件哈希见 [接口基线](../../engineering/motorbridge-api-baseline.md)。本文接口结论来自本地匹配版本的源码。
- [MotorBridge 官方仓库](https://github.com/motorbridge/motorbridge)：2026-10-10 核对公开资料入口；远端默认分支不替代本课 0.5.6 基线。

材料提供不等于已掌握；结论等待你的代码、运行记录和解释。
