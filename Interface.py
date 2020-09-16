from kivy.app import  App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
# from kivy.core.window import Window
from ch_list1 import ch_pack
# Window.size=(1920,1080)
class Container(BoxLayout):
    text_label=ObjectProperty()
    button_label=ObjectProperty()
    def change_text(self):
        self.text_label.text = ch_pack()

class Myapp(App):
    def build(self):

        return Container()

if __name__ == '__main__':
    Myapp().run()
