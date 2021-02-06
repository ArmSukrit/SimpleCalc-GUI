from kivy.app import App
from kivy import require
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

require("2.0.0")


class DefaultPage(GridLayout):
    output_label = ObjectProperty(None)
    appending_operators = ["+", "-", "x", "/"]
    numbers_str = [str(e) for e in range(0, 10)]
    buttons = {
        "%": "%",
        "CE": "CE",
        "C": "C",
        "<": "<",
        "1/x": "1/x",
        "x^2": "x^2",
        "sqrt(x)": "sqrt(x)",
        "/": "/",
        "7": 7,
        "8": 8,
        "9": 9,
        "x": "x",
        "4": 4,
        "5": 5,
        "6": 6,
        "-": "-",
        "1": 1,
        "2": 2,
        "3": 3,
        "+": "+",
        "+/-": "+/-",
        "0": 0,
        ".": ".",
        "=": "=",
    }

    def on_release(self, button):
        value = self.buttons[button.text]
        if value in range(0, 10):
            if self.output_label.text == "0":
                self.output_label.text = str(value)
            else:
                self.output_label.text += str(value)
        elif value in self.appending_operators:
            last = self.output_label.text[-1]
            if last in self.numbers_str:
                self.output_label.text += value
            elif last in self.appending_operators:
                self.output_label.text = self.output_label.text[:-1] + value
        elif value == ".":
            pass
        else:
            pass



class SimpleCalcApp(App):
    def build(self):
        self.title = "Simple Calculator"
        return DefaultPage()


if __name__ == "__main__":
    SimpleCalcApp().run()
