from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
import json

class Navigator(Screen):
    pass

class SplashScreen(Screen):
    pass

class FirstScreen(Screen):
    def set_quest(self,topic):
        with open('preguntas.json', 'r') as file:
            data = json.load(file)
            self.manager.get_screen('primer').set_questions(data.get(topic, []))
        self.manager.current = 'primer'

class AboutScreen(Screen):
    pass

class Primer(Screen):

    current_question = NumericProperty(0)
    time_remaining = NumericProperty(30)
    button_color = ListProperty()
    questions = ListProperty()
    dialog = None

    def set_questions(self, questions):
        self.questions = questions
        
    
    def on_enter(self, *args):
        self.start_timer()
        self.reset_button_colors()

    def start_timer(self):
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.time_remaining -= 1
        self.ids.timer_label.text = f"Tiempo restante: {self.time_remaining}s"

        if self.time_remaining == 0:
            self.next_question()

    def check_answer(self, selected_index,button):

        correct_index = self.questions[self.current_question]['correct_answer']
        if selected_index == correct_index:
            self.button_color = [0, 1, 0, 1]
            button.background_color=(0.2, 0.2, 0.2, 1)
            App.get_running_app().root.get_screen('results').resultados += 1

            Clock.unschedule(self.update_timer)
            self.dialog = MDDialog(
                text=f"Respuesta correcta\n{self.questions[self.current_question]['feedback']}",
                md_bg_color=(0.522, 0.949, 0.541, 0.63),
                buttons=[
                    MDRaisedButton(
                        text="OK",
                        md_bg_color=(1, 0.090, 0.090, 0.63),
                        on_press=lambda *args: self.next_question(self.dialog)
                    ),
                ],
            )
            self.dialog.open()
        else:
            Clock.unschedule(self.update_timer)

            self.dialog = MDDialog(
                text=f"Incorrecto:\n{self.questions[self.current_question]['feedback']}",
                md_bg_color=(1, 0.090, 0.090, 0.63),
                buttons=[
                    MDRaisedButton(
                        text="OK",
                        md_bg_color=(0.522, 0.949, 0.541, 0.63),
                        theme_text_color="Custom",
                        on_press=lambda *args: self.next_question(self.dialog)
                    ),
                ],
            )
            self.dialog.open()
            button.background_color=(1,0,0,1)
            self.button_color = [1, 0, 0, 1]
            

    def next_question(self,dialog):
        dialog.dismiss()
        self.start_timer()
        if self.current_question < len(self.questions)-1:
            self.current_question += 1
            self.time_remaining = 30
            self.ids.timer_label.text = f"Tiempo restante: {self.time_remaining}s "
        else:
            App.get_running_app().root.get_screen('results').total_preguntas = len(self.questions)
            App.get_running_app().root.current  = "results"
            Clock.unschedule(self.update_timer)

    def reset_button_colors(self):
        for button in self.ids.grid_layout.children:
            if isinstance(button, Button):
                button.background_color = [0.2, 0.2, 0.2, 1]

class Results(Screen):
    resultados = NumericProperty(0)
    total_preguntas = NumericProperty(1)
    def clear_results(self):
        App.get_running_app().root.get_screen('primer').current_question = 0
        self.resultados = 0

    def reintentar(self):
        App.get_running_app().root.get_screen('primer').current_question = 0
        self.manager.current = 'primer'

class App(MDApp):

    sm = ScreenManager()
    sm.add_widget(SplashScreen(name='splashscreen'))
    sm.add_widget(FirstScreen(name='firstscreen'))
    sm.add_widget(AboutScreen(name='about'))
    sm.add_widget(Primer(name='primer'))
    sm.add_widget(Results(name='results'))

    def build(self):

        Window.size = (320,520)
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_file('kv.kv')
        return screen

    def on_start(self):
        Clock.schedule_once(self.splash, 5)

    def splash(self,*args):
        self.root.current  = "firstscreen"

if __name__ == '__main__':
    App().run()

    