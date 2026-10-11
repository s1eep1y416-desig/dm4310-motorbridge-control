# MotorBridge 连接入口与设备参数

日期：2026-10-11。对应 S1-002。依据本机 MotorBridge 0.5.6 的 `motorbridge/core.py` 整理；本课只做源码阅读、参数辨析和离线代码骨架，不连接任何设备。

## 本课必会

1. 读懂 `Controller.from_dm_serial(serial_port, baud)` 的输入和返回对象。
2. 读懂 `controller.add_damiao_motor(motor_id, feedback_id, model)` 的三个参数和返回对象。
3. 区分 SDK 默认值、示例值和已经由本机设备证据确认的真实值。
4. 知道创建 `Controller` 会尝试打开真实通信入口，因此今天只能写函数定义，不能调用。

## 本课不考

- 反馈是否新鲜、轮询是否阻塞，以及缓存何时更新；这些属于 S1-003。
- 使能、失能、运动、模式切换、异常清理和急停设计。
- CAN 报文位布局、固件寄存器、修改 ID、设置零点或持久化参数。
- 背诵本机端口、波特率、ID 或模型键；这些值尚未取得完整设备证据。

## 面向硬件的调用链

```text
串口路径 + 波特率
        ↓
Controller.from_dm_serial(...)
        ↓
Controller：持有一条实际通信连接
        ↓
controller.add_damiao_motor(...)
        ↓
Motor：这条连接上的一个电机操作句柄
```

本机 0.5.6 的真实 Python 签名是：

```python
Controller.from_dm_serial(
    serial_port: str = "/dev/ttyACM0",
    baud: int = 921600,
) -> Controller

controller.add_damiao_motor(
    motor_id: int,
    feedback_id: int,
    model: str,
) -> Motor
```

`from_dm_serial()` 不是生成普通配置对象。调用时会进入底层 ABI，尝试使用给定串口创建控制器。路径不存在、权限不足、适配器不匹配或底层库失败时都可能直接报错。因此今天只把调用写进函数体，不在模块顶层或 `main()` 中执行。

`add_damiao_motor()` 在已经打开的 `Controller` 上创建一个 `Motor` 句柄。它不是“自动扫描电机”，也不等于修改电机内部 ID。传入错误值可能导致找错目标、收不到预期反馈或与其他设备冲突。

## 六个参数怎样理解

| 参数 | Python 层能确认的作用 | 当前项目状态 |
|---|---|---|
| `serial_port` | 交给 DM 串口连接入口的设备路径 | 本机真实路径未知；`/dev/ttyACM0` 只是 SDK 默认值 |
| `baud` | 交给串口入口的波特率整数 | 真实适配器要求未知；`921600` 只是 SDK 默认值 |
| `motor_id` | 添加达妙电机时传给底层的目标电机标识 | 真实值未知，首次连接前必须由设备配置或可靠资料确认 |
| `feedback_id` | 添加电机时传给底层的反馈标识参数 | 真实协议含义和本机值仍需匹配设备资料确认 |
| `model` | 传给底层的型号键字符串 | PDF 声明电机为 DM4310P，但它与 SDK 模型键的映射尚未确认 |
| `Controller` 返回值 | 管理连接和轮询等操作 | 只有真实调用成功后才存在；今天不创建 |

这里有三种不同证据：

- **SDK 默认值**：函数签名里写着什么。
- **示例值**：教程或历史代码为了演示填了什么。
- **设备事实**：当前这台适配器和电机经过铭牌、配置、协议或受控实验确认的值。

前两种不能自动升级为第三种。今天的参数表允许写“未知”，不允许用看起来合理的数字填空。

## ID 与收发的最低限度理解

一次通信至少要回答两个方向的问题：命令发给谁，反馈按什么身份回来。MotorBridge 因此要求同时提供 `motor_id` 和 `feedback_id`。当前本地 Python 包只暴露了参数名和底层调用，没有在 Python 层给出完整达妙协议定义，所以本课只形成以下可靠结论：

1. 两个 ID 承担不同角色，不能因为示例恰好相等就认为它们永远相同。
2. 添加句柄是在软件中登记预期设备身份，不是扫描，也不是改写真实电机参数。
3. 具体 CAN 标识映射必须在首次连接前结合对应设备协议和实际配置确认。

## 今天的离线边界

可以做：阅读源码、写函数签名、写参数表、做语法编译和静态审查。

不能做：实例化 `Controller`、调用 `add_damiao_motor()`、请求反馈、使能、失能、运动、修改 ID、写寄存器或连接任何硬件。

接口版本与哈希见 [MotorBridge 接口基线](../../engineering/motorbridge-api-baseline.md)，本项目的代码骨架要求见 [连接设计](../../engineering/interfaces/motor-connection.md)。
