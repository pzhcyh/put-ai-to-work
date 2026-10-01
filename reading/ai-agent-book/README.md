# 开源共读：深入理解 AI Agent：设计原理与工程实践

**原著：李博杰 / Bojie Li。** 书稿版本 2.0，核对日期 2026-10-01。本目录提供第三方开源书的章节索引与本站新增导读，不属于陈一豪原创书籍系列。

[原项目](https://github.com/bojieli/ai-agent-book) · [官方阅读器（最新）](https://bojieli.github.io/ai-agent-book/astro/) · [本站专题](https://chenyihao.com/reading/ai-agent-book) · [数据](../../data/ai-agent-book.json)

## 来源与许可

上游固定提交：`dbc046eb896ac4e39aa19c7774c8bf49583b89a6`。原项目采用 [Apache-2.0](LICENSE.upstream.txt)，部分子项目适用各自许可。Copyright 2025 Bojie Li。章节题录和实验数量依据上游 README 整理，已改编为本站索引；保留署名与许可证。本站新增导读、练习和路线为 AI 辅助整理草案，按 CC BY 4.0 开放，不重新授权原书、翻译或外部代码。

已核对上游 README、LICENSE 和固定提交的文件路径。109 为上游实验数量，包含本地项目、外部复现与设计内容，本站未逐项运行或认证。官方阅读器与 PDF 入口指向最新版本，可能不同于本索引快照。

英文为社区翻译，可能滞后于中文。本目录未镜像书稿、源码，也未运行全部实验。

## 本站学习路线

### 先理解，再动手

适合：用过 AI，想理解 Agent 如何工作

章节顺序：1 → 2 → 3 → 4

交付练习：一张任务流程图、一份上下文材料和一个工具接口说明。

### 做出第一个 Agent

适合：有编程基础，准备做一个小应用

章节顺序：1 → 2 → 4 → 5 → 7

交付练习：一个能运行的小功能，加上十条可重复执行的验收任务。

### 走向可靠的协作

适合：已有原型，希望改进交互与协作

章节顺序：3 → 6 → 7 → 9 → 10 → 8

交付练习：一份失败分析、一次对照评估，以及下一轮改进决策。后训练可作为选读。

## 章节索引

### 1. AI Agent 入门

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter1.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter1.md) · [配套实验入口（上游计数 4）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter1/README.md)

本站导读：先理解模型、上下文、工具如何组成一次完成任务的循环。

本站小练习：选一项日常任务，画出输入、模型判断、工具动作和完成条件。

### 2. 上下文工程

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter2.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter2.md) · [配套实验入口（上游计数 10）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter2/README.md)

本站导读：把上下文当作需要设计、更新与压缩的工作材料。

本站小练习：给同一任务制作简略与完整两份背景材料，比较遗漏和成本。

### 3. 用户记忆和知识库

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter3.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter3.md) · [配套实验入口（上游计数 12）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter3/README.md)

本站导读：分清临时上下文、长期记忆与可查证的外部知识。

本站小练习：用五份公开资料设计知识库，写出每份资料的来源和更新时间。

### 4. 工具

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter4.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter4.md) · [配套实验入口（上游计数 5）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter4/README.md)

本站导读：理解工具接口如何把文字意图变成可检查的动作。

本站小练习：为一个查询工具写出输入、输出、失败处理和权限边界。

### 5. Coding Agent 与通用 Agent

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter5.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter5.md) · [配套实验入口（上游计数 16）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter5/README.md)

本站导读：从明确需求开始，观察编程助手如何修改、测试与交付。

本站小练习：让编程助手完成一个小功能，保留需求、变更记录与验收证据。

### 6. 交互：观察与动作空间的扩展

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter6.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter6.md) · [配套实验入口（上游计数 14）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter6/README.md)

本站导读：思考语音、屏幕和异步事件如何改变任务执行方式。

本站小练习：画一个语音交互流程，标出用户打断、工具等待与恢复的位置。

### 7. Agent 的评估

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter7.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter7.md) · [配套实验入口（上游计数 14）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter7/README.md)

本站导读：把“看起来不错”转成固定任务、指标与失败记录。

本站小练习：建立十条小测试，记录成功条件、结果、耗时与失败原因。

### 8. 模型后训练

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter8.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter8.md) · [配套实验入口（上游计数 19）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter8/README.md)

本站导读：理解何时改进应用已足够，何时才值得进入模型训练。

本站小练习：比较提示、检索、微调三种改进方案，写明数据和资源需求。

### 9. Agent 的持续进化

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter9.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter9.md) · [配套实验入口（上游计数 9）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter9/README.md)

本站导读：用运行记录发现反复出现的问题，再验证一次改进。

本站小练习：选三条失败记录，提出一项改动，用原来的测试重新比较。

### 10. 多 Agent 协作

[中文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book/chapter10.md) · [英文原文](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/book-en/chapter10.md) · [配套实验入口（上游计数 6）](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter10/README.md)

本站导读：检查任务分工、交接信息和共享状态是否真的有帮助。

本站小练习：把一个任务分给两个角色，设计交接格式并与单角色方案比较。
