from vk_bot import VkBot
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
