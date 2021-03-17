import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verfana", 35)


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=900, height=650, highlightbackground="black",
                          highlightthickness=1)

        # mainFrame = ttk.Frame(self)

        # Control Section Frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        controlSection = ControlSection(self, self)
        controlSection.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Settings Section Frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        settingsSection = SettingsSection(self, self)
        settingsSection.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Plot section frame
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        plotSection = PlotSection(self, self)
        plotSection.grid(row=0, column=1, columnspan=4, rowspan=2, padx=10, pady=10, sticky="nsew")


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


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth=1, highlightbackground="black",
                          highlightthickness=1)


class About(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, borderwidth=1, highlightbackground="black",
                          highlightthickness=1)
