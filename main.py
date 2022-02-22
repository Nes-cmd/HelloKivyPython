from cgitb import text
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()