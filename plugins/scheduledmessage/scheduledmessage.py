# encoding:utf-8

import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from channel.chat_message import ChatMessage
from common.log import logger
from plugins import *
from functools import partial

import schedule
import time


@plugins.register(
    name="ScheduledMessage",
    desire_priority=0,
    hidden=True,
    desc="A plugin that sends scheduled messages",
    version="0.1",
    author="kevintao",
)
class ScheduledMessage(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_SCHEDULED_MESSAGE] = self.on_scheduled_message
        # self.start_scheduled_message_job()
        logger.info("[ScheduledMessage] inited")

    # def start_scheduled_message_job(self):

    #     e_context = PluginManager().emit_event(
    #         EventContext(
    #             Event.ON_SCHEDULED_MESSAGE,
    #             {"channel": self, "reply": ""},
    #         )
    #     )
    #     scheduled_func = partial(self.on_scheduled_message, e_context=e_context)
    #     schedule.every(10).seconds.do(scheduled_func)  # 设置定时任务，每10秒执行一次 scheduled_func

    #     # 设置定时任务：每天18:00发送一条消息
    #     # schedule.every().day.at("18:00").do(self.send_scheduled_message)
    #     # 设置定时任务：每10秒
    #     # schedule.every(10).seconds.do(self.on_scheduled_message)
    #     # schedule.every(10).seconds.do(self.get_help_text)

    #     # 启动定时任务的调度循环
    #     while True:
    #         logger.debug("[ScheduledMessage] do True")
    #         schedule.run_pending()
    #         time.sleep(1)

    # def send_scheduled_message(self):
    #     # 创建一个 Context 对象和 Reply 对象，用于发送消息
    #     context = Context(type=ContextType.TEXT, content="Scheduled message")
    #     reply = Reply(type=ReplyType.TEXT, content="This is a scheduled message")

    #     # 调用 _send_reply 函数发送消息
    #     self._send_reply(context, reply)

    def on_scheduled_message(self, e_context: EventContext):
        logger.debug("[ScheduledMessage] do on_scheduled_message")

        # 可以在此方法中处理定时消息的相关事件
        # 可以访问 e_context["channel"] 和 e_context["context"] 来获取相关信息
        # e_context["context"].type = ContextType.TEXT
        # msg: ChatMessage = e_context["context"]["msg"]
        # e_context["context"].content = f"请你随机使用一种风格介绍你自己，并告诉用户输入#help可以查看帮助信息。"
        # e_context.action = EventAction.BREAK  # 事件结束，进入默认处理逻辑
        # return
    
        reply = Reply()
        reply.type = ReplyType.TEXT
        # TODO 配置自动发送内容
        reply.content = "Send ScheduledMessage!"
        e_context["reply"] = reply
        e_context.action = EventAction.BREAK  # 事件结束，进入默认处理逻辑，一般会覆写reply

    def get_help_text(self, **kwargs):
        logger.debug("[ScheduledMessage] do get_help_text")
        help_text = "定时发送消息\n"
        return help_text
