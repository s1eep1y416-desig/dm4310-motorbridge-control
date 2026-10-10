# MotorBridge 接口基线

核对日期：2026-10-09。来源：桌面环境 `.venv/lib/python3.13/site-packages/motorbridge-0.5.6.dist-info/METADATA` 与 `motorbridge/core.py`、`models.py`。
静态确认版本 **0.5.6**，Requires-Python `>=3.10`；未导入 ABI、未实例化 Controller、未连接硬件。

| 已核对 Python 接口 | 可据源码确认的职责 | 尚需确认 |
|---|---|---|
| `Controller.from_dm_serial(serial_port, baud)` | 调用 DM 串口 ABI 构造 | 本机适配器/驱动及真实端口 |
| `Controller(channel)` / `from_socketcanfd(channel)` | 分别调用相应 ABI 构造 | 平台传输映射与设备兼容性 |
| `add_damiao_motor(motor_id, feedback_id, model)` | 创建设备句柄 | DM4310P 与 SDK 模型键对应关系 |
| `request_feedback()` | 调用请求反馈 ABI | 各模式/固件查询语义 |
| `poll_feedback_once()` | 调用轮询 ABI；Python 层无 timeout 参数 | 底层阻塞上限、新帧保证 |
| `get_state()` | 无值时返回 None，有值时转换 CState | 缓存更新/过期语义 |
| `ensure_mode(mode, timeout_ms=1000)` | 调用模式切换 ABI | 与 enable 的设备适用顺序 |
| `enable()` / `disable()` | 调用使能/失能 ABI | 设备实际执行与失败反馈 |
| `send_mit(pos, vel, kp, kd, tau)` | 发送 MIT 输入 | 适用固件、单位、增益与输出范围 |
| `send_pos_vel(pos, vlim)` / `send_vel(vel)` | 相应模式输入 | 设备能力与限制 |
| `close_bus()` / `close()` | 总线/句柄资源关闭 | 实际停止行为不能由资源释放推断 |

`MotorState` 字段：can_id、arbitration_id、status_code、pos、vel、torq、t_mos、t_rotor。
该 Python 数据结构没有 timestamp、sequence 或独立 enabled 标志；适配层不能假造这些反馈。
接收时间可以在可验证的真实接收边界记录，但读取缓存时间不能冒充接收时间。
`torq` 是 SDK 字段名，此处未确认其对应本电机固件的物理语义；真实关节 effort（N·m）需额外依据。

模式枚举可见 MIT、POS_VEL、VEL、FORCE_POS 等；枚举存在不等于 DM4310P 每种模式已验证。
本次保留真实调用名，不提出未经证实的新 API，也不提供连接/运动命令作为任务启动入口。

- `core.py` SHA-256：`2dd908f992db2ce4641af6bdfdcd049d335211fc458c267875b908967a70dcf4`。
- `models.py` SHA-256：`274e9bc65da3bc85f769d39c56904e0f7a16ceae0ba143b9533acc09ab033a7a`。

[MotorBridge 官方仓库](https://github.com/motorbridge/motorbridge) 用于后续查匹配版本源代码，不能以远端最新接口替代上面的本地 0.5.6 基线。

## 2026-10-10 第一课环境复核

本地版本仍为 0.5.6，core.py/models.py 的 SHA-256 与上表相同。用 `/Users/jkhkjg/Desktop/motorbridge/.venv/bin/python -I -B` 验证 Python 3.13.15、包元数据及 MotorState 的导入和合成构造；通过 unittest.mock.patch 令 ctypes.CDLL 调用直接失败，检查仍通过。因此本课可仅用实际 SDK 数据类离线学习，未加载 motor ABI、创建 Controller 或连接设备。此结果不证明总线或电机可用，也不替代用户练习。

课程入口见 [MotorBridge 讲义](../knowledge/motor-control/motorbridge.md)，设计见 [motor-api.md](interfaces/motor-api.md)。
