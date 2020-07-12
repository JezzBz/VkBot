# -*- coding: utf-8 -*-
import vk_api.vk_api
from kboard import create_keyboard
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_bot import  VkBot


class Server:


    def __init__(self, api_token, group_id, server_name):

        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()



    def start(self):
        for event in self.long_poll.listen():
            # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:
                #print('Text: ', event.object.message)
                keyboard=create_keyboard()
                bot = VkBot(event.from_user)
                print(event.object.message['from_id'],':',event.object.message['text'])
                bot.send_msg(send_id=event.object.message['from_id'], message=bot.new_message(event.object.message['text']),vk_api=self.vk_api,keyboard=keyboard)
