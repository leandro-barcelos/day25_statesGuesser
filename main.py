from tkinter import *
import pandas as pd
import sys

root = Tk()

states = pd.read_csv("src/states.csv")


class Application:
    def __init__(self) -> None:
        self.root = root
        self.user_input = StringVar()
        self.screen()
        self.input_window()
        self.correct_names = []
        root.mainloop()

    def screen(self):
        self.root.title("Brazil States (0/27)")
        self.root.configure(bg='black')
        bg = PhotoImage(file='Map.png')
        bg_label = Label(self.root, image=bg)
        bg_label.photo = bg
        bg_label.pack()
        self.root.geometry(f"{bg.width()}x{bg.height()}+150+50")
        self.root.resizable(False, False)

    def input_window(self):
        input_window = Toplevel(self.root)
        input_window.title("Input Window")
        input_window.geometry("400x150+895+50")
        input_window.lift()
        input_window.resizable(False, False)

        state_label = Label(input_window, text="Enter the state name:", font=('Calibri Light', 16))
        state_label.place(x=16, y= 15)

        self.state_input = Entry(input_window,textvariable=self.user_input, font=('Calibri Light', 16))
        self.state_input.place(x=16, y=60, width=370, height=25)

        submit = Button(input_window, text="Submit", font=('Calibri Light', 16), command=self.submit)
        submit.place(x=150, y=105)


    def submit(self):
        name = self.user_input.get()
        self.check_name(name)
        self.user_input.set('')

    def check_name(self, entry):
        if entry.lower() in states:
            nl = Label(self.root, text=states[entry.lower()][0])
            nl.place(x=states[entry.lower()][1], y=states[entry.lower()][2])
            self.correct_names.append(nl)
            self.root.title(f"Brazil States ({len(self.correct_names)}/27)")
        elif entry.lower() == 'desisto':
            sys.exit()
        else:
            pass


Application()