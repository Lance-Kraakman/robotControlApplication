import tkinter as tk
from tkinter import ttk
import roboticstoolbox as rtb

class manual_control(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame
        sectionFrame = tk.Frame(self, highlightbackground="black",
                                highlightthickness=1)
        sectionFrame.pack(expand=1, fill="both")


class run_prog(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame
        sectionFrame = tk.Frame(self, highlightbackground="black",
                                highlightthickness=1)
        sectionFrame.pack(expand=1, fill="both")


class create_prog(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame
        sectionFrame = tk.Frame(self, highlightbackground="black",
                                highlightthickness=1)
        sectionFrame.pack(expand=1, fill="both")




