# -*- coding: utf-8 -*-
from ch_list1 import ch_pack,bunker
from time import time
from kboard import create_empty_keyboard

def Game_start(vk_api,filename):
    Gamefile=open(filename,'r')
    Game=Gamefile.readlines()
    Gamefile.close()
    for line in Game:
        vk_api.messages.send(     peer_id=line.split('-')[1],
                                  message=ch_pack(),
                                  keyboard=create_empty_keyboard(),
                                  random_id=time())
    vk_api.messages.send(     peer_id=Game[0].split('-')[0],
                              message=bunker(),
                              keyboard=create_empty_keyboard(),
                              random_id=time())
