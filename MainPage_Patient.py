from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class HomePagePatient(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file('MainPage_Patient.kv')

HomePagePatient().run()