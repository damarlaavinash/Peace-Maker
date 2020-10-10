from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import *
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')

class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("demo.jpg")
        print("Captured")

class DesktopApp(App):
    def build(self):
        return (CameraClick())

DesktopApp().run() 
