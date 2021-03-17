import tkinter as tk
from tkinter import ttk
from pages import about_page as ap, settings_page as sp, home_page as hp


class tkinterApp(tk.Tk):
    # Class constructor
    def __init__(self):
        tk.Tk.__init__(self)  # Call constructor of tk.Tk
        self.title("Robot Control App")
        customed_style = ttk.Style()
        customed_style.configure('Custom.TNotebook.Tab', paddx=(10,0), pady=(10,10), font=('Helvetica', 15))
        tabControl = ttk.Notebook(self, style='Custom.TNotebook')

        tab1 = hp.Home(tabControl, self)
        tab2 = sp.Settings(tabControl, self)
        tab3 = ap.About(tabControl, self)

        tabControl.add(tab1, text='Home')
        tabControl.add(tab2, text='About')
        tabControl.add(tab3, text='Settings')

        tabControl.pack(expand=1, fill="both")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.minsize(1250, 600)

    def show_frame(self, cont):
        # frame = self.frames[cont]
        # frame.tkraise()
        print("Cunt")


app = tkinterApp()
app.mainloop()
