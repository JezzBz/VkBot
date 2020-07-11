from ch_list1 import ch_pack
from Rerandom import Rrom
from time import time
import vk_api.vk_api



class VkBot:

    def __init__(self, user_id,):
        _COMMANDS = ['Команды',"Старт", "Багаж", "Здоровье"]
        print("Создан объект бота!")
        self._USER_ID = user_id
        #self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ['КОМАНДЫ',"СТАРТ", "БАГАЖ", "ЗДОРОВЬЕ"]
    #def _get_user_name_from_vk_id(self, user_id):
    #    request = requests.get("https://vk.com/id"+str(user_id))
        #bs = bs4.BeautifulSoup(request.text, "html.parser")

        #user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
    def send_msg(self, send_id, message,vk_api):
        """
        Отправка сообщения через метод messages.send
        :param send_id: vk id пользователя, который получит сообщение
        :param message: содержимое отправляемого письма
        :return: None
        """
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

    #Команды
        elif message.upper() == self._COMMANDS[0]:
            return "Старт,Багаж,Здоровье"

        else:
            return "Напишите 'Команды'"
