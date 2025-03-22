# Firecrawl MCP 测试

这个示例展示了如何使用Firecrawl API配合MCP工具进行网页抓取、网站地图生成和结构化数据提取。

## 前置条件

1. 安装所需的Python包：
```bash
pip install firecrawl-py python-dotenv
```

2. 获取Firecrawl API密钥：
   - 注册并登录 [Firecrawl](https://firecrawl.dev/)
   - 复制你的API密钥

3. 设置环境变量：
   - 复制 `.env.example` 为 `.env` 文件
   - 填入你的API密钥

## 功能测试

该示例测试了Firecrawl的三个主要功能：

1. **网页抓取**：从单个URL获取内容，以markdown和HTML格式返回。
2. **网站地图**：获取网站的所有链接。
3. **结构化提取**：使用AI从网页中提取结构化数据。

## 使用方法

```bash
python mcp_firecrawl_test.py
```

## 结果解释

测试结果将显示在终端中，同时会在本地目录中生成以下文件：

- `scrape_result.json`：网页抓取结果
- `map_result.json`：网站地图结果
- `extract_result.json`：结构化提取结果

## 使用MCP工具的好处

Cursor中的MCP工具可以帮助你：

1. 轻松管理文件系统操作，如创建目录和写入文件
2. 与GitHub集成，方便代码管理和团队协作
3. 提供更加直观的工作流程，让开发更加高效

## 项目结构

```
firecrawl-mcp-test/
├── .env.example         # 环境变量配置示例
├── .env                 # 环境变量配置（需手动创建）
├── README.md            # 项目说明文档
├── mcp_firecrawl_test.py # 测试脚本
├── requirements.txt     # 依赖需求文件
└── results/             # 测试结果存储目录（自动创建）
```

## 更多资源

- [Firecrawl官方文档](https://docs.firecrawl.dev/)
- [Firecrawl Python SDK](https://docs.firecrawl.dev/sdks/python)