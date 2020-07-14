# -*- coding: utf-8 -*-


class Gamesession:
    def __init__(self,filename,peer_id,from_id,name):
            self.filename=filename
            self.peer_id=peer_id
            self.from_id=from_id
            self.name=name
    def create(self):
        Gamefile=open(self.filename,'w+')
        Gamefile.write('{0}-{1}-{2}\n'.format(self.peer_id,self.from_id,self.name))
        Gamefile.close()
    def add(self):
        Gamefile=open(self.filename,'r')
        k=Gamefile.readlines()
        Gamefile.seek(0)

        return 'Игрок {0} добавлен в очередь, всего игроков{1} '.format(k[-1].split('-')[-1],len(k))
        Gamefile.close()
