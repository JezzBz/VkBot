# -*- coding: utf-8 -*-
from ch_list1 import ch_pack,bunker
from Rerandom import Rrom
from time import time

import vk_api.vk_api
#from vk import method
from vk_bot_chat_collector import Gamesession

class VkBot:

    def __init__(self, user_id,):


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
    def chat_new_message(self,text,peer_id,from_id,name,vk_api):
        players_c=0
        if '-' in text:

            mess_text=text.split('-')
            if mess_text[0].upper()=='START' and mess_text[1].isdigit()  :
                players_c=mess_text[1]


                text='START'
            else:
                pass


        session=Gamesession(filename=str(peer_id)+'.txt',peer_id=peer_id,from_id=from_id,name=name,vk_api=vk_api,players_c=players_c)
        if text.upper()=='START':

                return session.create()

        elif text=='+':
            req=session.add()
            print(req)
            if req=="Next":

                return session.mess()
            elif "Let's Start":
                return session.mess()+"\n"+ session.fullstak()
            else:
                return 'Игра уже начата!'
        elif text.upper()=='FINISH':
            return session.dele()
