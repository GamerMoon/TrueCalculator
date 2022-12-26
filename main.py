## main.py ##

from tkinter import *
from time import sleep as wait
import re

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("TrueCalculator")
        self.root.geometry("570x600+100+200")
        self.root.configure(background='#17161b')
        self.root.resizable(False, False)

        self.equation = ""

    def show(self, value):
        if not self.equation.startswith("Invalid equation, ERROR "): # if the equation DOES NOT starts with invalid equation,
            self.equation += value
            self.label_result.config(text=self.equation)
        else:
            self.label_result.config(text='0')

    def clear(self):
        self.equation = ""
        self.label_result.config(text=self.equation)

    def init_result(self):
        self.label_result = Label(self.root, width=25, height=2, text="", font=("arial", 30))  # initializes the result box
        self.label_result.pack()
    
    def combine(self):
        pattern = r'^[\d+\(\)\*\/\+-]*$' # pattern for the re module
        match = re.match(pattern, self.equation)
        if len(self.equation) == 0:
            self.label_result.config(text='')
        else:
            match = re.match(pattern, self.equation)
            if match:
                try:
                    self.result = str(eval(self.equation))
                    self.equation = self.result
                    self.label_result.config(text=self.equation)
                except Exception as e:
                    self.label_result.config(text="Invalid equation, ERROR 1") # error 1 and 2 means invalid syntax
            else:
                self.label_result.config(text='Invalid equation, ERROR 2')

    def init_buttons(self):
        root = self.root
        buttons = [ # buttons! you can change the width, height, and the position also
            ["C", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#3697f5", lambda: self.clear(), (10, 100)],
            ["/", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('/'), (150, 100)],
            ["%", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('%'), (290, 100)],
            ["*", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('*'), (430, 100)],
            ["7", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('7'), (10, 200)],
            ["8", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('8'), (150, 200)],
            ["9", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('9'), (290, 200)],
            ["-", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('-'), (430, 200)],
            ["4", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('4'), (10, 300)],
            ["5", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('5'), (150, 300)],
            ["6", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('6'), (290, 300)],
            ["+", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('+'), (430, 300)],
            ["1", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('1'), (10, 400)],
            ["2", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('2'), (150, 400)],
            ["3", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('3'), (290, 400)],
            ["0", 11, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('0'), (10, 500)],
            [".", 5, 1, ("arial", 30, "bold"), 1, "#fff", "#2a2d36", lambda: self.show('.'), (290, 500)],
            ["=", 5, 3, ("arial", 30, "bold"), 1, "#fff", "#fe9037", lambda: self.combine(), (430, 400)],
        ]

        for button in buttons:
            text, width, height, font, bd, fg, bg, command, position = button
            Button(root, text=text, width=width, height=height, font=font, bd=bd, fg=fg, bg=bg, command=command).place(x=position[0], y=position[1])
            # buttons by loop :D

    def start_loop(self):
        self.root.mainloop()
        return False

if __name__ == "__main__":
    calc = Application()
    calc.init_buttons()
    calc.init_result()
    calc.start_loop()
