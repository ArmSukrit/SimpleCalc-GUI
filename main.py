from math import sqrt
from os import system
from kivy import require
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

require("2.0.0")

GITHUB_REPO = "https://github.com/ArmSukrit/SimpleCalc-GUI"


class DefaultPage(GridLayout):
    input_label = ObjectProperty(None)
    output_label = ObjectProperty(None)

    appending_operators = ["+", "-", "x", "/"]
    numbers_str = [str(e) for e in range(0, 10)]
    buttons = {
        "%": None,
        "xd": None,
        "C": None,
        "<": None,
        "1/x": None,
        "x^2": None,
        "sqrt(x)": None,
        "/": "/",
        "7": "7",
        "8": "8",
        "9": "9",
        "x": "*",
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
    released_eq_button = False

    def get_input_text(self):
        return self.input_label.text

    def set_input_text(self, string="0"):
        self.input_label.text = str(string)

    def set_output_text(self, string=""):
        self.output_label.text = str(string)

    def add_equal_sign(self):
        self.set_input_text(self.get_input_text() + " =")

    def evaluate(self):
        if self.get_input_text()[-1] in self.numbers_str:
            try:
                evaluated = eval(self.input_label.text)
            except ZeroDivisionError:
                self.set_output_text("cannot divide by 0")
                return
            except SyntaxError:  # in case output is text
                self.set_input_text("0")
                return

            if self.released_eq_button:
                self.released_eq_button = False
                self.add_equal_sign()
                self.set_output_text(str(evaluated))
            else:
                return evaluated

    def percent(self):
        evaluated = self.evaluate()
        self.set_input_text(f"({self.get_input_text()})/100 =")
        self.set_output_text(f"{float(evaluated) / 100.0}")

    def xd(self):
        system("start " + GITHUB_REPO)

    def c(self):
        self.set_input_text("0")
        self.set_output_text("")

    def backspace(self):
        self.set_output_text("")
        input_text = self.get_input_text()
        if not input_text == "0":
            if len(input_text) == 1:
                self.set_input_text('0')
            else:
                if input_text[-1] == "=":
                    self.set_input_text(input_text[:-3])
                    if not self.get_input_text():
                        self.set_input_text("0")
                else:
                    self.set_input_text(self.get_input_text()[:-1])

    def reverse(self):
        evaluated = self.evaluate()
        self.set_output_text(str(1/evaluated))
        self.set_input_text(f"1/({self.get_input_text()})")
        self.add_equal_sign()

    def square(self):
        evaluated = self.evaluate()
        self.set_output_text(evaluated * evaluated)
        self.set_input_text(f"({self.get_input_text()})^2")
        self.add_equal_sign()

    def sqroot(self):
        self.set_output_text(sqrt(self.evaluate()))
        self.set_input_text(f"sqrt({self.get_input_text()})")
        self.add_equal_sign()

    def neg_pos(self):
        if self.get_input_text()[0] != "-":
            self.set_input_text(f"-({self.get_input_text()})")
        else:
            self.set_input_text(self.get_input_text()[1:])

    func_buttons = {"%": percent, "xd": xd, "C": c, "<": backspace,
                    "1/x": reverse, "x^2": square, "sqrt(x)": sqroot, "+/-": neg_pos, "=": evaluate}

    def on_release(self, button):
        print(f'"{button.text}"' + " is released!")
        value = button.text

        if self.output_label.text and button.text != "<":
            self.set_input_text(self.output_label.text)
            self.set_output_text("")

        if value in self.numbers_str:
            if self.input_label.text == "0":
                self.input_label.text = str(value)
            else:
                self.input_label.text += str(value)
        elif value in self.appending_operators:
            last = self.input_label.text[-1]
            if last in self.numbers_str:
                self.input_label.text += self.buttons[value]
            elif last in self.appending_operators:
                self.input_label.text = self.input_label.text[:-1] + value
        elif value == ".":
            pass
        elif value in self.func_buttons:
            if button.text == "=":
                self.released_eq_button = True
            self.func_buttons[value](self)


class SimpleCalcApp(App):
    def build(self):
        self.title = "Simple Calculator"
        return DefaultPage()


if __name__ == "__main__":
    SimpleCalcApp().run()
