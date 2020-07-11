from vk_bot import VkBot
from vk_api import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll
from server_manage import server1,vk_api_token
print("Server started")
vk = vk_api.VkApi(token=vk_api_token)
vk._auth_token()

vk.get_api()


longpoll = VkBotLongPoll(vk,group_id=195855572)

for event in longpoll.listen():

    print(event.object.text)
    if event.type == VkEventType.MESSAGE_NEW:
        print(event.text)
        if event.to_me:

            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            server1.send_msg( event.object.peer_id, bot.new_message(event.object.text))

            print('Text: ', event.text)
