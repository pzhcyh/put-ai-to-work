# 可复用的学习数据

版本：1.0 · 更新日期：2026-10-01 · 陈一豪 / Ethan

这些数据对应个人网站已公开的书稿、课程与论文导读，不是用户行为数据或模型训练评测集。可用于制作自己的阅读器、课程索引、检索工具和学习页面。

| 文件 | 当前内容 | 主要字段 |
| --- | --- | --- |
| [books.json](books.json) | 6 本书、52 章 | `books`：书名、简介、目录、全文与单章文件路径 |
| [self-study.json](self-study.json) | 3条路线、12节完整自学实践课 | `tracks` 与 `lessons`：材料、步骤、任务说明、判断题与解释、参考、自评、讲义路径 |
| [learning.json](learning.json) | 4 个基础单元、8 个进阶起始主题 | `tracks[].rows`：目标、练习、检查标准、讲义与关联章节 |
| [exercises.json](exercises.json) | 2 组教学材料、8 道判断题 | `lessons`：材料、题目、预编写答案与解释 |
| [papers.json](papers.json) | 14 篇经典论文 | `papers`：英文题名、中文导读题、作者、年份、原文链接、解释、边界与练习 |
| [reading.json](reading.json) | 10篇文章、9位作者、3条路线 | `articles` 与 `paths`：原文与作者链接、语言、发表日期、中文阅读线索、关联论文和实践路由 |
| [papers.csv](papers.csv) | 同一组论文的表格版本 | 第一行为字段名，UTF-8，标准 CSV 引号转义 |

[presentations.json](presentations.json) 另外提供两份历史课件的版本、页数、文件路径和SHA256。PPT与PDF含品牌标志等混合材料，许可范围见 [课件说明](../slides/README.md)，不使用其他数据文件的统一CC BY范围。

## 使用约定

- JSON 顶层保留 `schemaVersion`、`updated`、`creator`、`license` 和 `status`。具体记录分别在 `books`、`tracks`、`lessons` 或 `papers`。
- `file`、`full`、`readme`、`handout`、`chapterFile`、`chapterFiles` 是相对于仓库根目录的路径。`lessonAnchor` 是网站的页面锚点，不能当成本地文件。
- `exercises.json` 的 `supported` 表示“有依据”，`revise` 表示“需要修正”。答案来自题目给出的材料，不是模型实时评分。
- 论文 `title` 是英文题名，`zh` 是本站中文导读题，`url` 是原文入口。作者字段采用简写，不是完整作者列表。`metadataChecked` 是题录核对日期，不表示完成了全文复现。
- 基础课是自学材料；进阶八主题是长期学习的起点，不能据此推断已有八次授课或结业认证。
- 以 JSON 为结构化数据主文件。修改论文记录时同步 CSV 与 `papers/README.md`；修改目录时同步实际 Markdown 文件。

## 来源与维护

书籍正文位于本仓库的 `chapters/`、`books/`；四份讲义位于 `lessons/`。课程与论文数据从个人网站已公开内容整理，首版来源模块为 `book.js`、`learning.js`、`first-lesson.js`、`MaterialsLesson.jsx` 与 `papers.js`。只整理已公开的教学内容，没有上传原始内部方案或未核对的历史论文清单。

运行 `node scripts/check-data.mjs` 可检查记录唯一性、目录文件存在、章节关联、答案值和论文 CSV 一致性。此检查不验证论文事实、外部链接当前可用性或课程实际效果。

原创内容按 [CC BY 4.0](../LICENSE) 开放；第三方权利与署名方式见 [许可范围](../LICENSES.md)。若增加新的第三方素材，请单独注明来源与许可，不要默认套用本仓库许可。

## 系列自学课程

`self-study.json` 公开完整课程内容；相同内容下载保存在 `courses/self-study/course.json`，修改时同步。`lessons[].handout` 为仓库相对路径；`resources[].to` 是个人网站路由。判断题由编写者设置，网站反馈按明确选项计算，不调用模型；`checklist` 是读者自评依据，不代表系统核验成果。

各课围绕一件具体作品展开。示例数据均为虚构，不应当作真实活动、报名记录或用户成绩。公开首版预计时长仅供学习安排。进度、答案选择和实践笔记不在本数据集中。

## 作者文章与论文更新（2026-10-01）

论文逐条保留 `checked` 与 `provenance`；八篇新论文在2026-10-01核对arXiv题录与摘要，原六篇沿2026-09-26记录。`translatedTitle` 为本站题名译法，`zh` 为导读题。作者文章保留原文题名、日期和语言；导读不是全文翻译。见 [作者文章阅读室](../reading/README.md)。选文不代表作者推荐或合作关系；原文中的产品事实保留发表时背景。
