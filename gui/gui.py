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

        self.keys = tkinter.PhotoImage(file="gui/snake_keys.png")
        self.keys_label = Label()
        self.keys_description_label = Label()
        # self.controls = GuiControls() # error: infinite loop -> child class is calling main class which is calling
        # child class
        self.author_label = Label()

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
        # for widget in self.window.winfo_children():
        #     widget.destroy()

    def menu_reload(self):
        # self.close_button.destroy()

        self.start_button = Button(self.window, text="           Start           ", command=self.start_game)
        self.start_button.grid(row=2, column=1)

        self.gui_controls = Button(self.window, text="           Controls          ",
                                   command=self.gui_show_controls)
        self.gui_controls.grid(row=3, column=1)

        self.gui_author = Button(self.window, text="           Author           ", command=self.gui_show_author)
        self.gui_author.grid(row=4, column=1)

        self.gui_quit = Button(self.window, text="           Quit          ", command=self.window.destroy)
        self.gui_quit.grid(row=5, column=1)

    def start_game(self):
        self.window.destroy()
        main_game()
        GUI()

    def gui_show_controls(self):
        # Destroy all buttons, show controls. Exit button will reload menu
        # Arrow keys picture:
        # https://image.shutterstock.com/image-vector/arrow-button-on-keyboard-icon-260nw-339331691.jpg
        self.hide_menu()
        self.keys_label = Label(self.window, image=self.keys)
        self.keys_label.grid(row=5, column=2)

        self.keys_description_label = Label(self.window, text="Use keys arrows to control your Snake. Press Up key to "
                                                              "go up, \n Down key to go down and Left and Right keys "
                                                              "to turn left and right.", bg='#fff', fg='#f00')
        self.keys_description_label.grid(row=7, column=2)
        self.close_button = Button(self.window, text="Close", command=self.gui_show_controls_destroy)
        self.close_button.grid(row=8, column=1)

    def gui_show_controls_destroy(self):
        self.keys_label.destroy()
        self.close_button.destroy()
        self.keys_description_label.destroy()
        self.menu_reload()

    def gui_show_author(self):
        self.hide_menu()
        self.author_label = Label(self.window, text="Created by Michal Malek. Upgraded version of Snake Game from 100 "
                                                    "Days of Code Python "
                                                    "Challenge. \n Keys picture from Shutterstock: \n "
                                                    "'https://image.shutterstock.com/image-vector/arrow-button-on-keybo"
                                                    "ard-icon-260nw-339331691.jpg' ", bg='#fff', fg='#f00')
        self.author_label.grid(row=6, column=1)
        self.close_button = Button(self.window, text="Close", command=self.gui_show_author_destroy)
        self.close_button.grid(row=8, column=1)

    def gui_show_author_destroy(self):
        self.close_button.destroy()
        self.author_label.destroy()
        self.menu_reload()
