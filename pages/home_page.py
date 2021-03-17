import tkinter as tk
from tkinter import ttk

from tabs import control_tabs as ct
from tabs import arm_config_tab
from robotics import RobotPlot as rb
import roboticstoolbox as rtb

LARGEFONT = ("Verfana", 35)


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1250, height=650)


        # Plot section frame
        self.grid_columnconfigure(1, weight=20)
        self.grid_rowconfigure(0, weight=5)
        self.plotSection = PlotSection(self, self)
        self.plotSection.grid(row=0, column=1, columnspan=4, rowspan=2, padx=(0, 10), pady=(33, 10), sticky="nsew")

        # Control Section Frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=3)
        self.controlSection = ControlSection(self, self)
        self.controlSection.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        # Settings Section Frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        settingsSection = SettingsSection(self, self)
        settingsSection.grid(row=1, column=0, padx=(10, 12), pady=(0, 10), sticky="nsew")

    def updatePlot(self):
        text = self.controlSection.tab4.listText.get()
        print(text)
        self.plotSection.sectionFrame.updateRobotPlot(text)

    def getManipulatorList(self):
        return self.plotSection.sectionFrame.manipulatorNames


class ControlSection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame

        # customed_style = ttk.Style()
        # customed_style.configure('control.TNotebook.Tab', padding=[5, 5], font=('Helvetica', 12), highlightthickness=2,highlightbackground = "red", highlightcolor= "red" )
        self.sectionFrame = ttk.Notebook(self)

        tab1 = ct.manual_control(self.sectionFrame, self)
        tab2 = ct.run_prog(self.sectionFrame, self)
        tab3 = ct.create_prog(self.sectionFrame, self)
        self.tab4 = arm_config_tab.arm_config(self.sectionFrame, controller)

        self.sectionFrame.add(self.tab4, text="Arm Configuration")
        self.sectionFrame.add(tab1, text="Manual Control")
        self.sectionFrame.add(tab2, text="Run Program")
        self.sectionFrame.add(tab3, text="Create Program")

        self.sectionFrame.pack(expand=1, fill="both")


class SettingsSection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame

        sectionFrame = tk.Frame(self, highlightbackground="black",
                                highlightthickness=1)
        sectionFrame.pack(expand=1, fill="both")


class PlotSection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # have to init constructor of tk.Frame

        self.grid_columnconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)

        self.sectionFrame = rb.RobotPlotSection(self, controller)

        self.sectionFrame.pack(expand=1, fill="both")
