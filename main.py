from kivy import require
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from buttons import buttons, appending_operators, numbers_str
import functions as func

require("2.0.0")


class DefaultPage(GridLayout):
    output_label = ObjectProperty(None)

    def on_release(self, button):
        value = buttons[button.text]
        if value in numbers_str:
            if self.output_label.text == "0":
                self.output_label.text = str(value)
            else:
                self.output_label.text += str(value)
        elif value in appending_operators:
            last = self.output_label.text[-1]
            if last in numbers_str:
                self.output_label.text += value
            elif last in appending_operators:
                self.output_label.text = self.output_label.text[:-1] + value
        elif value == ".":
            pass
        elif value == "=":
            self.output_label.text += " = \n" + func.evaluate(self.output_label.text)


class SimpleCalcApp(App):
    def build(self):
        self.title = "Simple Calculator"
        return DefaultPage()


if __name__ == "__main__":
    SimpleCalcApp().run()
