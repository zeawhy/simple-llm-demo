# 简单的大模型聊天机器人Demo

一个简单易用的大模型聊天机器人，支持DeepSeek和OpenAI两种API。

## 特性

- 🚀 支持DeepSeek API（推荐，性价比高）
- 🤖 支持OpenAI GPT API
- 💬 简单的命令行聊天界面
- 🔧 易于配置和使用
- 🛡️ 环境变量管理API密钥

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/zeawhy/simple-llm-demo.git
cd simple-llm-demo
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置API密钥

复制环境变量模板文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件，添加你的API密钥：

#### 使用DeepSeek（推荐）

```env
# DeepSeek API Key
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# 选择使用的模型提供商
MODEL_PROVIDER=deepseek
```

#### 使用OpenAI

```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# 选择使用的模型提供商
MODEL_PROVIDER=openai
```

### 4. 运行程序

```bash
python main.py
```

## API密钥获取

### DeepSeek API

1. 访问 [DeepSeek官网](https://platform.deepseek.com/)
2. 注册账号并登录
3. 在控制台中创建API密钥
4. 复制密钥到 `.env` 文件中

### OpenAI API

1. 访问 [OpenAI官网](https://platform.openai.com/)
2. 注册账号并登录
3. 在API Keys页面创建新的密钥
4. 复制密钥到 `.env` 文件中

## 使用说明

1. 运行程序后，会显示当前使用的AI提供商
2. 在提示符后输入你的问题
3. AI会回复你的问题
4. 输入 `quit`、`exit` 或 `退出` 来结束程序

## 示例对话

```
🤖 简单的大模型聊天机器人Demo
支持DeepSeek和OpenAI模型
输入 'quit' 或 'exit' 退出程序

✅ DeepSeek客户端初始化成功!

👤 你: 你好，请介绍一下自己
🤖 DeepSeek AI正在思考...
🤖 AI: 你好！我是一个AI助手，基于DeepSeek模型。我可以帮助你回答问题、进行对话、提供信息和协助解决问题。有什么我可以帮助你的吗？

👤 你: quit
👋 再见!
```

## 项目结构

```
simple-llm-demo/
├── main.py              # 主程序文件
├── requirements.txt     # Python依赖
├── .env.example        # 环境变量模板
├── .env                # 环境变量文件（需要创建）
├── .gitignore          # Git忽略文件
└── README.md           # 项目说明
```

## 依赖说明

- `openai`: OpenAI官方Python SDK
- `python-dotenv`: 环境变量管理
- `requests`: HTTP请求库（用于DeepSeek API）

## 注意事项

1. 请妥善保管你的API密钥，不要提交到版本控制系统
2. DeepSeek API相比OpenAI具有更好的性价比
3. 确保网络连接正常，API调用需要访问外网
4. 如遇到API调用失败，请检查密钥是否正确和账户余额

## 扩展功能

你可以基于这个demo进行扩展：

- 添加更多AI模型支持
- 实现对话历史记录
- 添加Web界面
- 支持文件上传和处理
- 添加流式输出

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！
