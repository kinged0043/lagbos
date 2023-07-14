import speech_recognition as sr
from deep_translator import GoogleTranslator
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class SpeechToIgboApp(App):

    def __init__(self):
        super().__init__()
        self.text_input = TextInput(text="")
        self.translator = GoogleTranslator()

    def on_button_click(self):
        # Start the speech recognition process
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        # Recognize the speech
        try:
            text = recognizer.recognize_google(audio)
            igbo_text = self.translator.translate(text, dest="ig")
            self.text_input.text = igbo_text
        except:
            pass

    def build(self):
        label = Label(text="Speech to Igbo")
        button = Button(text="Convert", on_press=self.on_button_click)
        root = Widget()
        root.add_widget(label)
        root.add_widget(button)
        root.add_widget(self.text_input)
        return root

if __name__ == "__main__":
    SpeechToIgboApp().run()