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
        self.start_button = Button()
        self.gui_controls = Button()
        self.gui_author = Button()
        self.gui_quit = Button()
        self.close_button = Button()
        # self.controls = GuiControls() # error: infinite loop -> child class is calling main class which is calling
        # child class
        canvas = tkinter.Canvas(master=self.window, width=self.screen_width, height=self.screen_height)
        background = tkinter.PhotoImage(file="gui/snake_title_screen.png")
        background_label = Label(image=background)
        background_label.place(x=0, y=0)
        canvas.grid(padx=0, pady=0, row=0, column=0, rowspan=10, columnspan=10)

        self.menu_reload()

        self.window.mainloop()

    def hide_menu(self):
        self.start_button.destroy()
        self.gui_controls.destroy()
        self.gui_author.destroy()
        self.gui_quit.destroy()

    def menu_reload(self):
        self.close_button.destroy()

        self.start_button = Button(self.window, text="           Start           ", command=self.start_game)
        self.start_button.grid(row=2, column=1)

        self.gui_author = Button(self.window, text="           Author           ", command=self.menu_reload)
        self.gui_author.grid(row=4, column=1)

        self.gui_quit = Button(self.window, text="           Quit          ", command=self.window.destroy)
        self.gui_quit.grid(row=5, column=1)

    def start_game(self):
        self.window.destroy()
        main_game()
        GUI()

    def gui_controls_sidebar(self):
        # Window with controls attach to game window
        pass


class GuiControls(GUI):
    # Class has to take from parent only master window
    def __init__(self):
        super().__init__()
        self.keys_label = Label()
        self.close_button = Button()
        self.keys = tkinter.PhotoImage(file="gui/snake_keys.png")

        self.gui_controls = Button(self.window, text="           Controls          ",
                                   command=self.gui_show_controls)
        self.gui_controls.grid(row=3, column=1)

    def gui_show_controls(self):
        # Destroy all buttons, show controls. Exit button will reload menu
        # Arrow keys picture:
        # https://image.shutterstock.com/image-vector/arrow-button-on-keyboard-icon-260nw-339331691.jpg
        self.hide_menu()
        self.keys_label = Label(self.window, image=self.keys)
        self.keys_label.grid(row=5, column=1)
        self.close_button = Button(self.window, text="Close", command=self.gui_show_controls_destroy)
        self.close_button.grid(row=8, column=1)

    def gui_show_controls_destroy(self):
        self.keys_label.destroy()
        self.close_button.destroy()


class GuiAuthor(GUI):
    def __init__(self):
        super().__init__()

    def author(self):
        # Destroy all buttons, show author. Exit button will reload menu
        Label(self.window, text="Created by Michal Malek. Upgraded version of Snake Game from 100 Days of Code Python "
                                "Challenge")

# TODO 1: Przepisać klasę GUI: musi zawierać jedynie podstawowe okno menu z tłem
# TODO 2: Każdy przycisk zapisać jako osobną klasę
# TODO 3: Okienko z pomocą przyczepione do okna głównego
# TODO 4: Okno gry pojawiające się w oknie głównym a nie nowym oknie
