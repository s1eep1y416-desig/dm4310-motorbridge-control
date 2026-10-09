# 测试入口

在仓库根目录，先使用 scripts/setup_environment.sh 安装本地包，再执行：

```bash
.venv/bin/python -m unittest discover -s tests/integration -p 'test_*.py' -v
.venv/bin/python scripts/check_repository.py
```

当前 integration 测试只验证安装后的包可在隔离解释器中导入，且不会隐式导入硬件/ROS SDK。
这不是电机业务测试、仿真或真机验证。unit 当前为用户后续业务测试保留，尚无单元测试用例。
硬件测试放 hardware，普通检查命令只显式选择 unit/integration，不递归运行 hardware。
fixtures 保存明确标注来源的测试输入，合成状态不能冒充真实实验数据。
