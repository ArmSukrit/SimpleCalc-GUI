from math import sqrt

from kivy import require
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

require("2.0.0")


class DefaultPage(GridLayout):
    input_label = ObjectProperty(None)
    output_label = ObjectProperty(None)

    appending_operators = ["+", "-", "x", "/"]
    numbers_str = [str(e) for e in range(0, 10)]
    buttons = {
        "%": None,
        "CE": None,
        "C": None,
        "<": None,
        "1/x": None,
        "x^2": None,
        "sqrt(x)": None,
        "/": "/",
        "7": "7",
        "8": "8",
        "9": "9",
        "x": "x",
        "4": "4",
        "5": "5",
        "6": "6",
        "-": "-",
        "1": "1",
        "2": "2",
        "3": "3",
        "+": "+",
        "+/-": None,
        "0": "0",
        ".": ".",
        "=": None,
    }

    def evaluate(self):
        # todo: evaluate a given expression using some kind of API
        result = float(0)
        return f"{expr} = \n\t {result}"

    def percent(self):
        evaluated = evaluate(expr)
        return f"{evaluated}/100 = " + float(evaluated) / 100.0

    def ce(self):
        pass

    def c(self):
        pass

    def backspace(self):
        self

    def reverse(self):
        evaluated = evaluate(expr)
        pass

    def square(self):
        evaluated = evaluate(expr)
        return f"{evaluated}^2 = {evaluated * evaluated}"

    def neg_pos(self):
        # +/-
        pass

    func_buttons = {"%": percent, "CE": ce, "C": c, "<": backspace,
                    "1/x": reverse, "x^2": square, "sqrt(x)": square, "+/-": sqrt, "=": evaluate}

    def on_release(self, button):
        value = self.buttons[button.text]
        if value in self.numbers_str:
            if self.input_label.text == "0":
                self.input_label.text = str(value)
            else:
                self.input_label.text += str(value)
        elif value in self.appending_operators:
            last = self.input_label.text[-1]
            if last in self.numbers_str:
                self.input_label.text += value
            elif last in self.appending_operators:
                self.input_label.text = self.input_label.text[:-1] + value
        elif value == ".":
            pass
        elif value in self.func_buttons:
            self.output_label.text = self.func_buttons[value]()


class SimpleCalcApp(App):
    def build(self):
        self.title = "Simple Calculator"
        return DefaultPage()


if __name__ == "__main__":
    SimpleCalcApp().run()
