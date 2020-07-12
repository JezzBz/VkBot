# -*- coding: utf-8 -*-
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def create_keyboard():
    keyboard = VkKeyboard(one_time=False)


    keyboard.add_button("Commands", color=VkKeyboardColor.DEFAULT)
    keyboard.add_button("Heal", color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button("Char", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Bunk", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("Lugg", color=VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()
#Возвращает клавиатуру
