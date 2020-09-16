# -*- coding: utf-8 -*-
import os
from full_stak_start import Game_start
class Gamesession:
    def __init__(self,filename,peer_id,from_id,name,vk_api,players_c):
            self.filename=filename
            self.peer_id=peer_id
            self.from_id=from_id
            self.name=name
            self.vk_api=vk_api
            self.players_c=players_c
    def create(self):
        if not self.players_c:
            self.players_c=6
        if os.path.exists(self.filename):
            return 'Игра начата!'
        Gamefile=open(self.filename,'w+')
        if os.stat(self.filename).st_size == 0:
            Gamefile.write('{3}\n{0}-{1}-{2}'.format(self.peer_id,self.from_id,self.name,self.players_c)+'\n')
            return 'Очередь открыта. Игрок {0} добавлен в очередь'.format(self.name)
        else:
            return 'Очередь уже запущена'
        Gamefile.close()


    def add(self):
        if os.path.exists(self.filename):
            Gamefile=open(self.filename,'r')
            gr=Gamefile.read()
            Gamefile.seek(0)
            need_count=Gamefile.readlines()
            Gamefile.close()
            if need_count[-1]!='STARTED':
                count_players=len(need_count)-1
                need_count=int(need_count[0].rstrip())
                if count_players<need_count:
                    if str(self.from_id) not in gr:
                        gr=True
                    else:
                        gr=False
                    if gr:
                        Gamefile=open(self.filename,'a')
                        Gamefile.write('{0}-{1}-{2}'.format(self.peer_id,self.from_id,self.name)+'\n')
                        Gamefile.close()
                Gamefile=open(self.filename,'r')
                gr=Gamefile.read()
                Gamefile.seek(0)
                need_count=Gamefile.readlines()
                Gamefile.close()
                count_players=len(need_count)-1
                need_count=int(need_count[0].rstrip())

                if count_players==need_count:

                    return "Let's Start"
                else:
                    return "Next"
            else:
                return "StopMan"






    def mess(self):
        Gamefile=open(self.filename,'r')
        k=Gamefile.readlines()

        Gamefile.close()

        return 'Игрок {0} в очереди , всего игроков {1} '.format(self.name,len(k)-1)
    def fullstak(self):
        Game_start(self.vk_api,self.filename)
        return 'Команда собрана, игра запущена !'

    def dele(self):
        os.remove(self.filename)
        return('Игра окончена!')
