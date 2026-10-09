# ROS 2 工作区

按 AGENTS 原文预留驱动、Hardware Interface、描述、bringup、接口与 MoveIt 目录。
**这些目录当前不是可构建的 ROS 2 包。** 发行版、依赖与构建方式未确定，因此没有伪造 package.xml、CMakeLists 或运行配置。
每个预留包使用 COLCON_IGNORE，避免 colcon 将占位目录误认为可构建能力。
进入对应阶段后建立有效包、检查依赖与构建，再移除该包的 COLCON_IGNORE。
自定义消息与 MoveIt 仅在需求明确时实现；预留目录不代表已决定采用。
