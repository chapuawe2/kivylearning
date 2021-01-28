import kivy

from kivy.app import App 
from kivy.uix.label import Label

class Create(App):
	def build(self):
		return Label(text="Hello World", font_size=34)

if __name__ == '__main__':
	Create().run()
