#Kivy Calc w/o kv file

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.spelling import Spelling

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
#set app size
#Window.size = (500, 700)

Builder.load_string("""
<MyLayout>
    padding: 50
    BoxLayout:
        orientation: "vertical"
        size:root.width, root.height
        Label:
            id:word_label
            text_size:self.size
            halign:"center"
            valign:"center"
            text:"Enter a word"
            font_size:32
            
        TextInput:
            id:word_input
            multiline:False
            size_hint:(1, .5)
            padding_y: (70,50)
            
        Button:
            size_hint:(1,0.5)
            font_size:32
            text:"Submit"
            on_press:root.on_press()
                    
""")

class MyLayout(Widget):
    def on_press(self):
        # Create an instance of Spelling
        s = Spelling()
        # Select the language
        s.select_language("en_US")
        try:
            suggestion = s.suggest(self.ids.word_input.text)
        except:
            self.ids.word_label.text = ''
        if (suggestion):
            x = ''
            for word in suggestion:
                x = f'{x}\n{word}'
            self.ids.word_label.text = f'{x}'

class SpellCheckerApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == "__main__":
    SpellCheckerApp().run()
    