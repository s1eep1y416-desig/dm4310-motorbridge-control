# 任务池

> 规划在 REPO-001 仓库验证通过后复核。日期与估时可调整；S1-001 已开始，尚无已验收学习任务。

阶段开发任务池共 38 项。2026-10-10 S1-001 最终离线代码复核通过，待用户运行记录和概念复述，状态 In Progress；其余 37 项为 Backlog。没有用户任务被预先标为完成。旧每日任务仍保持删除。证据见 [代码审查](../learning/reviews/2026-10-10-S1-001-review.md)。

估时为专注学习/实现时间，另保留每周复盘、补练与等待。多于两小时的任务拆成多个学习单元，不要求一天做完。未来模块的输出名称在执行时确定。

2026-10-10 补充“代码与材料所在文件夹”列。所有路径相对于仓库根目录 `/Users/jkhkjg/Desktop/dm4310-motorbridge-control/`。查看 [各阶段目录分工](master-roadmap.md#每个阶段在哪个文件夹写代码) 可区分核心、示例、测试及记录。路径表示该任务的落点，不代表文件已实现；纯设计任务无需为了填满目录提前写代码。未单列的理论和实验记录按阶段目录表归档。S1-004 开始提取核心，后续示例调用核心，阶段验收不能只交示例。

| ID | 核心任务 | 估时 | 依赖 | 提交物 | 完成判据 | 状态 | 代码与材料所在文件夹 |
|---|---|---|---|---|---|---|---|
| S1-001 | MotorBridge 入门与状态显示 | 2h | 无；使用现有 SDK 环境 | 用户状态显示程序、三组离线输出、对象关系解释 | 正确处理 MotorState/None、角度单位与三组输入；用户独立解释 | In Progress | 探索：`examples/S1_can_and_id/`；本项暂不强制提取核心 |
| S1-002 | SDK 连接入口与设备参数 | 2h | S1-001 | 连接方式选择、添加电机调用设计、参数/未知项简表 | 能解释 Controller 与 add_damiao_motor 参数；结合调用理解 ID 与收发，不猜设备值 | Backlog | 调用探索：`examples/S1_can_and_id/`；参数方案：`engineering/interfaces/`、`engineering/hardware/`；配置：`config/` |
| S1-003 | SDK 状态契约与反馈新鲜度 | 2h | S1-002 | API/字段表、状态有效性设计、阻塞边界问题单 | 接口来自实际版本；明确无法证明新鲜度的情况 | Backlog | 状态契约：`engineering/interfaces/`；为 `src/robot_control/actuator/` 的实现准备 |
| S1-004 | MotorBridge 状态读取封装与离线验证 | 4h | S1-003 | 用户读取封装、可替换 SDK 输入、单元测试 | 正常/无反馈/陈旧/错误身份有独立用例 | Backlog | 核心：`src/robot_control/actuator/`；测试：`tests/unit/`、`tests/fixtures/`；调用：`examples/S1_can_and_id/` |
| S1-005 | 使能失能与异常清理 | 4h | S1-004 | 状态图、用户代码、失败路径测试 | 配置缺失不打开设备；清理异常可见 | Backlog | 核心：`src/robot_control/actuator/`、`src/robot_control/safety/`；测试：`tests/unit/`、`tests/integration/` |
| S1-006 | 真实身份、状态与生命周期实验 | 2–4h | S1-005；设备条件及授权 | 首次连接前补齐环境/设备证据、配置、原始状态、使能/失能和通信异常记录 | 真实证据齐全；若缺硬件则阻塞本任务 | Backlog | 调用：`examples/S1_can_and_id/`；验证：`tests/hardware/`；证据：`engineering/hardware/`、`experiments/single-motor/` |
| S1-007 | S1 审查、考核与补缺 | 2–4h | S1-006；用户提交 | 审查整改、用户回答、阶段报告 | 满足 S1 全部门槛 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S1/`；修复回到原模块 |
| S2-001 | 模式与受限命令接口 | 4h | S1-007 | MIT/POS_VEL/VEL 对照、状态机、限幅/拒绝设计 | 解释设备内部环；验证单位和不合法输入 | Backlog | 核心：`src/robot_control/controllers/`、`src/robot_control/safety/`；测试：`tests/unit/` |
| S2-002 | 到位等待与三类超时 | 4–6h | S2-001 | 用户实现与正常/高速未停/超时/失联测试 | 区分反馈年龄、命令超时和整段运动超时 | Backlog | 核心：`src/robot_control/controllers/`、`src/robot_control/safety/`；测试：`tests/unit/`、`tests/fixtures/` |
| S2-003 | 反馈日志与控制周期 | 4h | S2-002 | 时间戳定义、日志、周期与误差分析脚本 | 区分计划周期和实测周期；保留原始数据 | Backlog | 核心：`src/robot_control/utils/`、`src/robot_control/controllers/`；调用：`examples/S2_single_motor/`；测试：`tests/unit/` |
| S2-004 | 单电机受限模式实验 | 4–6h | S2-003；设备条件及授权 | 参数依据、位置/速度/适用 MIT 实验及曲线 | 真实误差和周期满足预先指标 | Backlog | 调用：`examples/S2_single_motor/`；验证：`tests/hardware/`；记录：`experiments/single-motor/` |
| S2-005 | 故障退出与恢复回归 | 4h | S2-004 | 故障矩阵、Mock/真机边界、失败日志 | 安全关键分支无未闭环缺陷 | Backlog | 核心：`src/robot_control/safety/`、`src/robot_control/controllers/`；测试：`tests/unit/`、`tests/integration/`、`tests/hardware/` |
| S2-006 | S2 验收与薄弱点补练 | 2–4h | S2-005；用户提交 | 代码审查、回答、阶段证据包 | 满足 S2 门槛 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S2/`；修复回到原模块 |
| S3-001 | ROS 环境与基础通信 | 4–6h | S2-006；理论可提前 | 环境矩阵、最小 Topic/Service/Action 练习 | 环境可复现；解释通信选择 | Backlog | 包：`ros2_ws/src/dm_motor_driver/`；教学调用：`examples/S3_ros2_basics/`；测试：包内 `test/`（计划） |
| S3-002 | JointState 与参数节点 | 4–6h | S3-001 | 用户节点、状态单位、参数与 Fake 测试 | 数组/关节顺序和参数验证正确 | Backlog | 包：`ros2_ws/src/dm_motor_driver/`；测试：包内 `test/`（计划）、`tests/integration/` |
| S3-003 | Launch、控制权与真机接口 | 4–6h | S3-002；设备条件及授权 | 启动关闭、受限命令、真实日志、故障记录 | 唯一控制权；退出/失联按设计处理 | Backlog | 包：`ros2_ws/src/dm_motor_driver/`、`ros2_ws/src/dm_robot_bringup/`；测试：`tests/integration/`、`tests/hardware/` |
| S3-004 | S3 验收 | 2–4h | S3-003；用户提交 | 审查、回答、复现说明 | 满足 S3 门槛 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S3/`；修复回到原模块 |
| S4-001 | 硬件接口选型与生命周期 | 4–6h | S3-004 | ABI/C++ 接口核对、时延预算、ADR | 不把 Python 包装误认标准硬件插件 | Backlog | 方案：`engineering/design-decisions/`、`engineering/interfaces/`；实现目标：`ros2_ws/src/dm_motor_hardware/` |
| S4-002 | Fake Hardware 与控制器 | 6–8h | S4-001 | 硬件插件、URDF 接口、控制器配置及集成测试 | 加载/激活/停用/故障行为可验证 | Backlog | 包：`ros2_ws/src/dm_motor_hardware/`、`ros2_ws/src/dm_robot_description/`、`ros2_ws/src/dm_robot_bringup/`；测试：包内 `test/`（计划）、`tests/integration/` |
| S4-003 | 真实 read/write 与循环观测 | 4–6h | S4-002；设备条件及授权 | 单关节真实集成、周期与停止日志 | 时序预算及安全标准满足 | Backlog | 包：`ros2_ws/src/dm_motor_hardware/`；测试：`tests/hardware/`；记录：`experiments/ros2/` |
| S4-004 | S4 验收 | 2–4h | S4-003；用户提交 | 审查与阶段证据包 | 满足 S4 门槛 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S4/`；修复回到原模块 |
| S5-001 | 双设备身份与状态管理 | 4–6h | S4-004；第二电机 | 配置与管理器、关节映射、Fake 双状态测试 | ID/关节顺序唯一；不混淆状态 | Backlog | 核心：`src/robot_control/actuator/`；配置：`config/`；测试：`tests/unit/`、`tests/fixtures/` |
| S5-002 | 轨迹插值与协调调度 | 6–8h | S5-001 | 双关节轨迹、离线采样、边界测试 | 连续性/约束符合所选轨迹定义 | Backlog | 核心：`src/robot_control/trajectory/`、`src/robot_control/controllers/`；测试：`tests/unit/` |
| S5-003 | 双关节轨迹与故障联动 | 4–6h | S5-002；设备条件及授权 | 真实日志、同步误差、单关节故障实验 | 另一关节不持续不安全输出 | Backlog | 核心：`src/robot_control/controllers/`、`src/robot_control/safety/`；调用：`examples/S5_multi_motor/`；测试：`tests/integration/`、`tests/hardware/` |
| S5-004 | S5 验收 | 2–4h | S5-003；用户提交 | 审查与阶段证据包 | 满足 S5 门槛 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S5/`；修复回到原模块 |
| S6-001 | 坐标系与二自由度模型 | 4–6h | 数学基础；真机基于 S5-004 | 参数/单位表、坐标图、URDF | 模型与机构映射有证据 | Backlog | 核心：`src/robot_control/kinematics/`；模型：`ros2_ws/src/dm_robot_description/`、`config/`；测试：`tests/unit/` |
| S6-002 | 独立 FK 与参考比对 | 4–6h | S6-001 | FK 实现、特殊姿态手算、自动对照 | 输出坐标系和参考模型一致 | Backlog | 核心：`src/robot_control/kinematics/`；测试：`tests/unit/`；调用：`examples/S6_fk_ik/` |
| S6-003 | IK、多解与可达性 | 6–8h | S6-002 | IK 实现、FK 回代、边界/不可达测试 | 拒绝无效目标；多解选择有理由 | Backlog | 核心：`src/robot_control/kinematics/`；测试：`tests/unit/`；调用：`examples/S6_fk_ik/` |
| S6-004 | Jacobian 与末端实验 | 6–8h | S6-003；真机需 S5-004/授权 | 差分验证、奇异分析、真实末端数据 | 数学与真实误差按各自标准评估 | Backlog | 核心：`src/robot_control/kinematics/`；测试：`tests/unit/`、`tests/hardware/`；记录：`experiments/kinematics/` |
| S6-005 | S6 验收 | 2–4h | S6-004；用户提交 | 审查、数学解释、实验报告 | 满足 S6 门槛 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S6/`；修复回到原模块 |
| S7-001 | 动力学参数与方程 | 4–6h | S6-005；理论可提前 | 参数来源、单位、惯量与重力约定 | 模型信息可追溯且物理一致 | Backlog | 核心：`src/robot_control/dynamics/`；参数：`config/`；依据：`engineering/hardware/`、`knowledge/dynamics/` |
| S7-002 | Pinocchio 与独立重力验证 | 6–8h | S7-001 | 模型加载、重力项代码、独立解析对照 | 不以同一库的两个调用互证代替独立参考 | Backlog | 核心：`src/robot_control/dynamics/`；测试：`tests/unit/`、`tests/integration/`；调用：`examples/S7_dynamics/` |
| S7-003 | 受限重力补偿实验 | 6–8h | S7-002；支撑/限制/授权 | 真实补偿前后数据、输出限制、停止验证 | 模型与输出语义匹配，实验有对照 | Backlog | 核心：`src/robot_control/controllers/`、`src/robot_control/safety/`；调用：`examples/S7_dynamics/`；测试：`tests/hardware/`；记录：`experiments/dynamics/` |
| S7-004 | S7 验收 | 2–4h | S7-003；用户提交 | 审查与阶段报告 | 满足 S7 门槛 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S7/`；修复回到原模块 |
| S8-001 | 第三关节与三维模型 | 4–6h | S7-004；第三关节 | 模型、身份/顺序、限位、FK/IK 回归 | 三维位置任务与自由度匹配 | Backlog | 扩展：`src/robot_control/actuator/`、`src/robot_control/kinematics/`、`ros2_ws/src/dm_robot_description/`、`config/`；测试：`tests/unit/` |
| S8-002 | 三关节轨迹与 ROS 集成 | 6–8h | S8-001 | 轨迹/接口、离线回归、部署说明 | 复用已有模块，控制权明确 | Backlog | 扩展：`src/robot_control/controllers/`、`src/robot_control/trajectory/`、`ros2_ws/src/` 中相关包；测试：`tests/integration/` 及包内测试 |
| S8-003 | 综合实验与故障复现 | 6–8h | S8-002；设备条件及授权 | 真实轨迹/故障/停止数据、复现记录 | 达到预先指标并关闭关键问题 | Backlog | 调用：`examples/S8_3dof_robot/`；测试：`tests/integration/`、`tests/hardware/`；记录：`experiments/` 对应主题目录 |
| S8-004 | 综合验收与工程复盘 | 4–6h | S8-003；用户提交 | 最终报告、学习评估、复用清单 | 满足 S8 门槛，诚实记录能力范围 | Backlog | 复核本阶段核心与测试；记录：`learning/reviews/`、`learning/assessments/S8/`；修复回到原模块 |

## 新仓库起点

REPO-001 已完成目录、安装和导入测试基础。2026-10-10 用户要求直接从 MotorBridge 开始，S1-001 保留 ID 并改为 SDK 对象与状态显示练习，见 [今日任务](../learning/daily/2026-10-10-S1-001.md)。旧设备盘点不再是首日必交项，相关证据首次连接前补齐；S1-004 等后续任务仍未下发。
旧项目 DM-001 仅是到位/超时主题的参考资料，不复制其源码、不继承任务完成状态。S2-002 在本仓库独立实现。

## 延期记录格式

任务 ID / 原状态 / 日期 / 原因 / 可独立推进内容 / 恢复条件 / 下一检查点。
硬件缺失只阻塞相应实验；考核未答、代码未交和缺原始数据都不能用新任务替代。
