import kivy
from kivy.app import App
from kivy.uix.label import Label

# Optional: Specify the required Kivy version
# kivy.require('1.11.1') # Replace with your current Kivy version if needed

class MyFirstKivyApp(App):
    def build(self):
        """
        Builds the root widget of the application.
        In this case, it returns a Label widget with "Hello World!".
        """
        return Label(text="Hello World!")

if __name__ == "__main__":
    # Initializes and runs the Kivy application
    MyFirstKivyApp().run()
