# Docker 部署服务

## docker-compose 快速启动

1. 修改 Dockerfile

`projects/chatgpt-on-wechat/Dockerfile`

```Shell
FROM ghcr.io/zhayujie/chatgpt-on-wechat:master

ENTRYPOINT ["/entrypoint.sh"]
```

2. 创建 Docker 镜像

```Shell
docker build -t img-cow .
```

3. 修改 docker-compose.yaml

`projects/chatgpt-on-wechat/docker/docker-compose.yaml`

```yaml
version: '2.0'
services:
  chatgpt-on-wechat:
    image: img-cow
    container_name: ctr-chatgpt-on-wechat
    environment:
      OPEN_AI_API_BASE: 'https://openai.ifree.love/v1'
      OPEN_AI_API_KEY: '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'
      OPEN_AI_PROXY: ''
      SINGLE_CHAT_PREFIX: ''
      SINGLE_CHAT_REPLY_PREFIX: ''
      GROUP_CHAT_PREFIX: '["@bot"]'
      GROUP_NAME_WHITE_LIST: '["ChatGPT测试群", "ChatGPT测试群2"]'
      IMAGE_CREATE_PREFIX: '["画", "看", "找"]'
      CONVERSATION_MAX_TOKENS: 1000
      SPEECH_RECOGNITION: "False"
      CHARACTER_DESC: '你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。'
      EXPIRES_IN_SECONDS: 3600
```

4. Docker Compose 常用命令：

Docker Compose 是一个用于定义和管理多个 Docker 容器的工具。它使用 YAML 文件来配置应用程序的服务、网络和卷等，然后可以使用简单的命令来启动、停止和管理整个应用程序的容器组。

Docker Compose 常用的命令包括：

1. `docker-compose up`: 构建并启动应用程序的容器。`-d`守护启动
2. `docker-compose down`: 停止并删除应用程序的容器。
3. `docker-compose start`: 启动已经创建的应用程序的容器。
4. `docker-compose stop`: 停止正在运行的应用程序的容器。
5. `docker-compose restart`: 重启应用程序的容器。
6. `docker-compose ps`: 列出当前正在运行的容器。
7. `docker-compose logs`: 查看应用程序的容器日志。`-f`实时输出
8. `docker-compose exec`: 在正在运行的容器中执行命令。
9. `docker-compose build`: 构建应用程序的容器镜像。

这些命令可以通过在包含有效的 Docker Compose 配置文件的目录中运行来使用。配置文件名通常为 `docker-compose.yml` 或 `docker-compose.yaml`。
