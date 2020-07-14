# -*- coding: utf-8 -*-
import os
from full_stak_start import Game_start
class Gamesession:
    def __init__(self,filename,peer_id,from_id,name,vk_api):
            self.filename=filename
            self.peer_id=peer_id
            self.from_id=from_id
            self.name=name
            self.vk_api=vk_api
    def create(self):


        Gamefile=open(self.filename,'w+')
        if os.stat(self.filename).st_size == 0:
            Gamefile.write('{0}-{1}-{2}'.format(self.peer_id,self.from_id,self.name)+'\n')
            return 'Очередь открыта. Игрок {0} добавлен в очередь'.format(self.name)
        else:
            return 'Очередь уже запущена'
        Gamefile.close()


    def add(self):
        if os.path.exists(self.filename):
            Gamefile=open(self.filename,'r')
            gr=Gamefile.read()
            Gamefile.seek(0)
            count_players=len(Gamefile.readlines())
            Gamefile.close()
            if count_players<6:
                if str(self.from_id) not in gr:
                    gr=True
                else:
                    gr=False
                if gr:
                    Gamefile=open(self.filename,'a')
                    Gamefile.write('{0}-{1}-{2}'.format(self.peer_id,self.from_id,self.name)+'\n')
                    Gamefile.close()
            print(count_players)
            if count_players+1>=2:
                return False
            else:
                return True


    def mess(self):
        Gamefile=open(self.filename,'r')
        k=Gamefile.readlines()
        Gamefile.close()

        return 'Игрок {0} в очереди , всего игроков {1} '.format(self.name,len(k))
    def fullstak(self):
        return 'Команда собрана, игра запущена !'
        Game_start(self.vk_api,self.filename)
