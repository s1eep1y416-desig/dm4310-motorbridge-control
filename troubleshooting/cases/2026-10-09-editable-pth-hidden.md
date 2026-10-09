# 可编辑安装后无法导入核心包

日期：2026-10-09。范围：本地仓库基础工具链，不是电机或学习业务故障。

## 现象与环境

macOS 26.4 arm64，Python 3.12.14。本仓库 .venv 中 pip install -e 成功，但新的隔离 Python 进程导入 robot_control 时出现 ModuleNotFoundError。

## 证据与定位

分发元数据和 src 包文件存在，生成的 __editable__.dm4310_motorbridge_control-0.1.0.pth 内容指向正确路径。
失败时文件 st_flags=32832，其中 UF_HIDDEN=32768。当前解释器 site.py 的 addpackage 会跳过带隐藏标记的 .pth。
重新安装后的同次调用可导入，后续独立调用再次失败，并再次观测到 UF_HIDDEN。哪个外部组件重新设置该标记尚未确认，不把这一点写成已查明根因。

## 处理

环境脚本改为构建并安装普通 wheel，去掉对 editable .pth 的依赖，没有修改解释器或通过 sys.path 注入源码。
曾尝试的隐藏属性修复未能形成稳定结果，最终脚本不保留该处理。源码改变后需重新运行安装脚本。

## 验证

标准 wheel 0.1.0 安装成功。之后独立执行 integration 测试，从仓库外、隔离 Python 中导入八个核心包：1 项通过，未加载 MotorBridge/ROS/仿真库。
没有执行真实硬件或电机业务测试。
