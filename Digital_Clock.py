#import module (pip install kivy)
from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
import time
# set window size
Window.size = (400, 150)
Builder.load_string("""
<Layout>
    ClockLabel:
        id: clock_label
        size_hint: 0.75,1
        font_size: 80
        color: 'green'
        markup: True
""")
# create layout class
class Layout(BoxLayout):
    pass
# clocklabel class to display
# updated time label
class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)
    def update(self, *args):
        self.text = f"[u]{time.strftime('%I:%M:%S')}[/u]"
# Extend kivy's App class
# with new class  
class DigitalClockApp(App):
    def build(self):
        return Layout()
# create object
clock = DigitalClockApp()
# run app
clock.run()