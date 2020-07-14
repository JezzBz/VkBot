# -*- coding: utf-8 -*-
from ch_list1 import ch_pack,bunker
from Rerandom import Rrom
from time import time

import vk_api.vk_api
#from vk import method
from vk_bot_chat_collector import Gamesession

class VkBot:

    def __init__(self, user_id,):

        print("Создан объект бота!")
        self._USER_ID = user_id


        self._COMMANDS = ["COMMANDS","CHARACTER", "LUGGAGE", "HEALTH","BUNKER"]

    def send_msg(self, send_id, message,vk_api,keyboard):

        vk_api.messages.send(     peer_id=send_id,
                                  message=message,
                                  keyboard=keyboard,
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
            return "Character-рандом персонажа \nCommands-список доступных команд \nHealth-рандом нового здоровья\nLuggage-рандом нового багажа\nBunker-выбор бункера + катастрофы"

        else:
            return "Напишите 'Commands'"
    def chat_new_message(self,text,peer_id,from_id):

        if text.upper()=='START':
            #name= method("users.get", {"user_ids": from_id})
            name='Bogdan'
            session=Gamesession(filename=str(peer_id)+'.txt',peer_id=peer_id,from_id=from_id,name=name)
            session.create()
            return session.add()
