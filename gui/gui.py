import tkinter
from tkinter import *


class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Snake Game")
        self.screen_width = 500
        self.screen_height = 500
        self.window.resizable(width=False, height=False)

        canvas = tkinter.Canvas(master=self.window, width=self.screen_width, height=self.screen_height)
        background = tkinter.PhotoImage(file="snake_title_screen.png")
        background_label = Label(image=background)
        background_label.place(x=0, y=0)
        canvas.grid(padx=0, pady=0, row=0, column=0, rowspan=10, columnspan=10)

        self.window.mainloop()

    def gui_start_game(self):
        pass

    def gui_controls(self):
        pass

    def gui_author(self):
        pass

    def gui_controls_sidebar(self):
        pass


screen = GUI()
