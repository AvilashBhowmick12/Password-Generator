import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import random

kivy.require('1.0.9')

# Set the window size
Window.size = (768, 864)

Builder.load_string('''
<PasswordGenerator>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgb: 0.427, 0.459, 0.651
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        size_hint_y: None
        height: '30dp'
        Label:
            text: 'Password Generator'
            font_size: '24sp'
            bold: True
    BoxLayout:
        size_hint_y: None
        height: '10dp'  # Padding below the label
    BoxLayout:
        size_hint_y: None
        height: '30dp'
        Label:
            text: 'Password length:'
        TextInput:
            id: length
            multiline: False
    BoxLayout:
        size_hint_y: None
        height: '30dp'
        TextInput:
            id: password
            disabled: True
        Button:
            text: 'Copy'
            on_press: app.copy_to_clipboard(password.text)
    Label:
        text: 'Password Settings'
        size_hint_y: None
        height: '30dp'
    GridLayout:
        cols: 2
        rows: 6
        size_hint_y: None
        height: '180dp'
        Label:
            text: 'Lowercase (a-z)'
        CheckBox:
            id: lowercase
            active: True
        Label:
            text: 'Uppercase (A-Z)'
        CheckBox:
            id: uppercase
        Label:
            text: 'Numbers (0-9)'
        CheckBox:
            id: numbers
        Label:
            text: 'Symbols (!-$^+)'
        CheckBox:
            id: symbols
        Label:
            text: 'Exclude Duplicate'
        CheckBox:
            id: exclude_duplicate
        Label:
            text: 'Include Spaces'
        CheckBox:
            id: include_spaces
    BoxLayout:
        size_hint_y: None
        height: '10dp'
    Button:
        text: 'Generate Password'
        size_hint_y: None
        height: '30dp'
        on_press: app.generate_password()
''')

class Password:
    def __init__(self):
        self.lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.numbers = ['1','2','3','4','5','6','7','8','9','0']
        self.special_characters = ["~","!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","|","[","]","/","?","<",">"]
        self.spaces = [' ']
        self.pwdList = []

    def generate(self, length, include_lowercase, include_uppercase, include_numbers, include_symbols, include_spaces, exclude_duplicates):
        for i in range(length):
            available_chars = []
            if include_lowercase:
                available_chars += self.lowercase_letters
            if include_uppercase:
                available_chars += self.uppercase_letters
            if include_numbers:
                available_chars += self.numbers
            if include_symbols:
                available_chars += self.special_characters
            if include_spaces:
                available_chars += self.spaces
            
            if not available_chars:
                break
            
            char = random.choice(available_chars)
            
            if exclude_duplicates and (char in self.pwdList):
                continue
            
            self.pwdList.append(char)
        
        random.shuffle(self.pwdList)

    def display(self):
        return ''.join(self.pwdList)

class PasswordGenerator(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return PasswordGenerator()

    def on_start(self):
        from kivy.core.window import Window
        Window.size = (420, 355)

    def generate_password(self):
        length = int(self.root.ids.length.text)
        include_lowercase = self.root.ids.lowercase.active
        include_uppercase = self.root.ids.uppercase.active
        include_numbers = self.root.ids.numbers.active
        include_symbols = self.root.ids.symbols.active
        exclude_duplicates = self.root.ids.exclude_duplicate.active
        include_spaces = self.root.ids.include_spaces.active

        ob = Password()
        ob.generate(length, include_lowercase, include_uppercase, include_numbers, include_symbols, include_spaces, exclude_duplicates)
        password = ob.display()

        self.root.ids.password.text = password

    def copy_to_clipboard(self, password):
        from kivy.core.clipboard import Clipboard
        Clipboard.copy(password)

if __name__ == '__main__':
    MyApp().run()
