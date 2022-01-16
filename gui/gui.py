import tkinter
from tkinter import *
from core.game import main_game


class GUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Snake Game")
        self.screen_width = 600
        self.screen_height = 600
        self.window.resizable(width=False, height=False)

        canvas = tkinter.Canvas(master=self.window, width=self.screen_width, height=self.screen_height)
        background = tkinter.PhotoImage(file="gui/snake_title_screen.png")
        background_label = Label(image=background)
        background_label.place(x=0, y=0)
        canvas.grid(padx=0, pady=0, row=0, column=0, rowspan=10, columnspan=10)

        self.start_button = Button(self.window, text="           Start           ", command=self.start_game).grid(
            row=2,
            column=1)

        self.qui_controls = Button(self.window, text="           Controls          ").grid(row=3, column=1)

        self.gui_author = Button(self.window, text="           Author           ").grid(row=4, column=1)

        self.gui_quit = Button(self.window, text="           Quit          ", command=self.window.destroy).grid(
            row=5,
            column=1)

        self.window.mainloop()

    def menu_reload(self):
        # Function to reload a menu
        pass

    def start_game(self):
        self.window.destroy()
        main_game()
        GUI()

    def gui_controls(self):
        # Destroy all buttons, show controls. Exit button will reload menu
        pass

    def gui_controls_sidebar(self):
        # Window with controls attach to game window
        pass

    def author(self):
        # Destroy all buttons, show author. Exit button will reload menu
        Label(self.window, text="Created by Michal Malek. Upgraded version of Snake Game from 100 Days of Code Python "
                                "Challenge")


# screen = GUI()
