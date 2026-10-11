# S1-002 MotorBridge 连接骨架设计

日期：2026-10-11。关联 [任务卡](../../learning/daily/2026-10-11-S1-002.md)与[连接讲义](../../knowledge/motor-control/motorbridge-connection.md)。这是离线设计，不表示设备已经连接或参数已经确认。

## 目标和边界

本课只建立与真实 SDK 一致的最小调用边界：

```text
调用者提供经过确认的参数
        ↓
open_dm_serial(serial_port, baud)
        ↓
Controller
        ↓
add_damiao_motor(controller, motor_id, feedback_id, model)
        ↓
Motor
```

两个函数由学习者写在 `examples/S1_can_and_id/002_motorbridge_connection.py`。本文件不提前实现答案；实现必须直接调用本机 0.5.6 已存在的 SDK 方法，不能虚构扫描、自动猜 ID 或静默回退接口。

## 学习者要实现的接口

```python
def open_dm_serial(serial_port: str, baud: int) -> Controller:
    ...


def add_damiao_motor(
    controller: Controller,
    motor_id: int,
    feedback_id: int,
    model: str,
) -> Motor:
    ...
```

要求：

- 使用 `from motorbridge import Controller, Motor` 的真实公开类型。
- 每个函数只转交明确输入并返回 SDK 对象，不添加未要求的默认参数、扫描、重试或异常吞噬。
- 在函数 docstring 中注明调用会访问真实通信资源，今天不得执行。
- 模块顶层只允许导入、常量和函数定义；不得创建 `Controller` 或 `Motor`。
- 不编写 `enable()`、`disable()`、反馈读取或任何运动命令。

## 参数事实表

学习者在 `engineering/hardware/s1-002-device-parameters.md` 建立六行表格：

| 参数 | 当前值 | 证据来源 | 状态 | 作用 | 填错的风险 |
|---|---|---|---|---|---|
| `serial_port` |  |  | 已确认 / 未知 |  |  |
| `baud` |  |  | 已确认 / 未知 |  |  |
| `motor_id` |  |  | 已确认 / 未知 |  |  |
| `feedback_id` |  |  | 已确认 / 未知 |  |  |
| 电机型号 |  |  | 已确认 / 未知 |  |  |
| SDK `model` 键 |  |  | 已确认 / 未知 |  |  |

SDK 默认值和历史示例可以写进“证据来源”用于对比，但不能因此把状态写成“已确认”。未知值保留“未知”，并写明后续需要什么证据。

## 验证层级

今天只允许：

1. Python 源码编译检查，证明语法有效但不执行模块。
2. 人工审查函数是否调用正确 SDK 入口。
3. 审查参数表是否区分默认值、示例值和设备事实。

今天不能证明：串口存在、ABI 能打开适配器、ID 正确、电机在线、反馈可用或资源能够安全退出。连接、反馈和生命周期证据分别在后续任务建立。
