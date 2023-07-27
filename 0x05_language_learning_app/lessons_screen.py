from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class LessonsScreen(Screen):
    def __init__(self, language, **kwargs):
        super(LessonsScreen, self).__init__(**kwargs)
        self.language = language

        layout = BoxLayout(orientation='vertical')
        label_name = Label(text=self.language["name"] + " Lessons")
        # Add lessons content here
        layout.add_widget(label_name)
        self.add_widget(layout)

