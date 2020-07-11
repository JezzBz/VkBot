
class VkBot:

    def __init__(self, user_id):

        print("Создан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ['Команды',"Старт", "Багаж", "Здоровье"]
    def new_message(self, message):

    #Старт
        if message.upper() == self._COMMANDS[0]:
            return f"{text}, {self._USERNAME}!"

    #Багаж
        elif message.upper() == self._COMMANDS[1]:
            return f"{bagage}, {self._USERNAME}!"

    # Здоровье
        elif message.upper() == self._COMMANDS[2]:
            return f"{heal}, {self._USERNAME}!"

    #Команды
        elif message.upper() == self._COMMANDS[3]:
            return f"Старт,Багаж,Здоровье, {self._USERNAME}!"

        else:
            return "Напишите 'Команды'"
