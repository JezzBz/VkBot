import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_bot import  VkBot


class Server:
#api_token='f6c799dd26087993bdc4ae2b921f041271be1ce3c3b9e653901bde5d2e5d9999600f1b5b929a66a71c826'

    def __init__(self, api_token, group_id, server_name: str="Empty"):

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
                print('Text: ', event.object.message)

                bot = VkBot(event.from_user)
                print(event.object.message['from_id'])
                bot.send_msg(send_id=event.object.message['from_id'], message=bot.new_message(event.object.message['text']),vk_api=self.vk_api)
