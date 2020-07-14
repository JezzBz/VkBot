# -*- coding: utf-8 -*-
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def create_keyboard():
    keyboard = VkKeyboard(one_time=False)


    keyboard.add_button("Commands", color=VkKeyboardColor.DEFAULT)
    keyboard.add_button("Health", color=VkKeyboardColor.DEFAULT)

    keyboard.add_line()
    keyboard.add_button("Character", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()
    keyboard.add_button("Bunker", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("Luggage", color=VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()
def create_empty_keyboard():
    keyboard = VkKeyboard.get_empty_keyboard()

    return keyboard
#Возвращает клавиатуру
