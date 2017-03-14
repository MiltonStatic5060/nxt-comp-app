from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from GamePad import *

class DiagWindow(StackLayout):
    def serve(self):
        self.btn = Button(text=str(gamepad1.left_trigger), width=40 + 1 * 5, size_hint=(None, 0.15))
        self.add_widget(self.btn)
    def update(self, dt):
        self.btn.text = gamepad1.left_trigger



class DiagApp(App):
    def build(self):
        window = DiagWindow()
        window.serve()
        Clock.schedule_interval(window.update,1.0/60.0)
        return window
    def buildx(self):
        root = StackLayout()
        for i in range(25):
            btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            root.add_widget(btn)
        root.add_widget(Button(text=str(gamepad1.left_trigger), width=40 + i * 5, size_hint=(None, 0.15)))
        return root


DiagApp().run()
