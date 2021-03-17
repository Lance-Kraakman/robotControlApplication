import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verfana", 35)


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth=1, highlightbackground="black",
                          highlightthickness=1)


class ControlSection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame

        sectionFrame = tk.Frame(self, highlightbackground="black",
                                highlightthickness=1)
        sectionFrame.pack(expand=1, fill="both")


class SettingsSection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame

        sectionFrame = tk.Frame(self, highlightbackground="black",
                                highlightthickness=1)
        sectionFrame.pack(expand=1, fill="both")


class PlotSection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame

        self.grid_columnconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)

        sectionFrame = tk.Frame(self, highlightbackground="black",
                                highlightthickness=1)
        sectionFrame.pack(expand=1, fill="both")



