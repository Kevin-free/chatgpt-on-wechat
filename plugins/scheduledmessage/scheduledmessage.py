# encoding:utf-8

import json
import os
import requests
import openai
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from channel.chat_message import ChatMessage
from common.log import logger
from plugins import *
from functools import partial
from config import conf

import time


@plugins.register(
    name="ScheduledMessage",
    desire_priority=0,
    hidden=True,
    desc="A plugin that sends scheduled messages",
    version="0.2",
    author="kevintao",
)
class ScheduledMessage(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_SCHEDULED_MESSAGE] = self.on_scheduled_message
        logger.info("[ScheduledMessage] inited")

    def on_scheduled_message(self, e_context: EventContext):
        logger.debug("[ScheduledMessage] do on_scheduled_message")

        openai.api_key = conf().get("open_ai_api_key")
        openai.api_base = conf().get("open_ai_api_base")
        message_content = "请你随机使用一种风格提醒大家健身打卡。使用中文，字数不超过20字。你要用人类的语气，会用emoji表达情绪，如：😄😉😜。"
        completion = openai.ChatCompletion.create(model=conf().get("model"), messages=[
            {"role": "user", "content": message_content}],  temperature=0.8,
                                                    top_p=0.9)
        newstext = completion['choices'][0]['message']['content']
        logger.debug("GPT生成内容：{}".format(newstext))

        reply = Reply()  # 创建一个回复对象
        reply.content = "@所有人" + newstext # 回复内容
        reply.type = ReplyType.TEXT
        e_context["reply"] = reply # 通过 event_context 传递
        e_context.action = EventAction.BREAK_PASS

    def get_help_text(self, **kwargs):
        logger.debug("[ScheduledMessage] do get_help_text")
        help_text = "定时发送消息\n"
        return help_text
