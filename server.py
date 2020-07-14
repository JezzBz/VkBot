# -*- coding: utf-8 -*-
import vk_api.vk_api
from kboard import create_keyboard,create_empty_keyboard
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
        print('Server Started!')
        for event in self.long_poll.listen():
            # Пришло новое сообщение
            if event.type == VkBotEventType.MESSAGE_NEW:


                if event.object.message['from_id']==event.object.message['peer_id']:
                    bot = VkBot(event.from_user)

                    keyboard=create_keyboard()

                    print(event.object.message['from_id'],':',event.object.message['text'])
                    bot.send_msg(send_id=event.object.message['from_id'], message=bot.new_message(event.object.message['text']),vk_api=self.vk_api,keyboard=keyboard)

                elif event.object.message['from_id']!=event.object.message['peer_id']:
                    bot = VkBot(event.from_user)
                    keyboard=create_empty_keyboard()
                    bot.send_msg(send_id=event.object.message['peer_id'], message=bot.chat_new_message(text=event.object.message['text'],peer_id=event.object.message['peer_id'],from_id=event.object.message['from_id']),keyboard=keyboard,vk_api=self.vk_api)
