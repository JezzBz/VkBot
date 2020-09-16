from kivy.app import  App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Container(BoxLayout):
    text_label=ObjectProperty()
    button_label=ObjectProperty()
    def change_text(self):
        self.text_label.text = 'NIGGA'

class Myapp(App):
    def build(self):

        return Container()

if __name__ == '__main__':
    Myapp().run()
