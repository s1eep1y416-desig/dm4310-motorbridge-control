# Python 控制核心

`robot_control` 采用 src 布局，通过根目录 pyproject.toml 安装。七个职责包已创建，可独立导入；尚未实现电机业务功能。
actuator 负责设备/状态，controllers 负责控制流程，kinematics 负责运动学，dynamics 负责动力学，trajectory 负责轨迹，safety 负责限制/超时/故障，utils 负责通用工具。
不在导入时创建控制器、打开设备或加载可选硬件 SDK。API 和实现文件由对应任务建立，避免未经确认的占位接口成为错误契约。
