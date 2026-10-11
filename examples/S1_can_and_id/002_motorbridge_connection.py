from motorbridge import Controller, Motor


def open_dm_serial(serial_port: str, baud: int) -> Controller:
    """使用指定串口和波特率创建 MotorBridge Controller。

    调用本函数会尝试访问真实通信设备；S1-002 只定义，不执行。
    """
    return Controller.from_dm_serial(serial_port, baud)


def add_damiao_motor(
    controller: Controller,
    motor_id: int,
    feedback_id: int,
    model: str,
) -> Motor:
    """在已有 Controller 上登记一台达妙电机并返回 Motor 句柄。

    调用本函数会访问真实通信资源；参数必须经过设备证据确认。
    S1-002 只定义，不执行。
    """
    return controller.add_damiao_motor(
        motor_id,
        feedback_id,
        model,
    )
