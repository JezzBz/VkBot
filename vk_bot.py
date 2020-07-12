# -*- coding: utf-8 -*-
from ch_list1 import ch_pack,bunker
from Rerandom import Rrom
from time import time
import vk_api.vk_api



class VkBot:

    def __init__(self, user_id,):

        print("Создан объект бота!")
        self._USER_ID = user_id


        self._COMMANDS = ["COMMANDS","CHAR", "LUGG", "HEAL","BUNK"]

    def send_msg(self, send_id, message,vk_api):

        vk_api.messages.send(     peer_id=send_id,
                                  message=message,
                                  random_id=time())

    def new_message(self,message):

    #Старт
        if message.upper() == self._COMMANDS[1]:


            return ch_pack()

    #Багаж
        elif message.upper() == self._COMMANDS[2]:
            return Rrom('1')

    # Здоровье
        elif message.upper() == self._COMMANDS[3]:

            return Rrom('2')
        elif message.upper() == self._COMMANDS[4]:
            return bunker()
    #Команды
        elif message.upper() == self._COMMANDS[0]:
            return "Char-рандом персонажа \nCommands-список доступных команд \nHeal-рандом нового здоровья\nLugg-рандом нового багажа\nBunk-выбор бункера + катастрофы"

        else:
            return "Напишите 'Commands'"
