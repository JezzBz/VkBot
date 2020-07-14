# -*- coding: utf8 -*-
# Импортируем созданный нами класс Server
from server import Server
# Получаем из config.py наш api-token
vk_api_token='f6c799dd26087993bdc4ae2b921f041271be1ce3c3b9e653901bde5d2e5d9999600f1b5b929a66a71c826'


server1 = Server(vk_api_token,195855572, "server1")
# vk_api_token - API токен
# 172998024 - id сообщества
# "server1" - имя сервера

server1.start()
