import tkinter as tk
from tkinter import ttk
import roboticstoolbox as rtb
import json
robotNum = 0


class arm_config(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, controller)  # have to init constructor of tk.Frame
        self.controller = controller
        GEN_PAD = 10

        # Variables for Table and Robots
        self.configurationNameEntry = ttk.Entry()
        self.entries = {}
        self.DH_joints = 0
        self.tableheight = 0
        self.tablewidth = 0
        self.labels = ["theta (deg)", "d (m)", "alpha (deg)", "a (m)", "sigma (0/1)", "offset (m)"]

        # List of manipulators
        self.optionList = controller.getManipulatorList()
        self.listText = tk.StringVar()
        self.listText.set(self.optionList[0])

        self.sectionFrame = tk.Frame(self, highlightbackground="black", highlightthickness=0)
        self.createDhTable(self.sectionFrame, 4, 6)

        # Create Button, Label and Entry Widgets
        activateButton = tk.Button(self.sectionFrame, text="Activate Configuration", fg="black",
                                   command=controller.updatePlot)
        configurationLabel = tk.Label(self.sectionFrame, text="Add Configuration")
        jointEntryLabel = tk.Label(self.sectionFrame, text="    DH Links Required   ")
        configuratioButton = tk.Button(self.sectionFrame, text="Create Configuration", fg="black",
                                       command=self.manipulatorConfig)
        self.jointEntry = tk.Entry(self.sectionFrame, text="Set Link Number", width=10)
        self.jointEntry.bind('<KeyPress>', self.entryEvent)

        # Create Option menu widget
        self.om = tk.OptionMenu(self.sectionFrame, self.listText, *self.optionList)
        self.om.config(width=20)

        configurationNameLabel = tk.Label(self.sectionFrame, text="Configuration Name:")
        self.configurationNameEntry = tk.Entry(self.sectionFrame, width=15)

        # Place Widgets on grid of container
        activateButton.grid(row=0, column=0, padx=(GEN_PAD, GEN_PAD), pady=(GEN_PAD, GEN_PAD))
        self.om.grid(row=0, column=1, padx=(GEN_PAD, GEN_PAD), pady=(GEN_PAD, GEN_PAD))
        configurationLabel.grid(row=1, column=0, columnspan=2, padx=(GEN_PAD, GEN_PAD), pady=(GEN_PAD, GEN_PAD))
        jointEntryLabel.grid(row=2, column=0, padx=(GEN_PAD, GEN_PAD), pady=(GEN_PAD, GEN_PAD))
        self.jointEntry.grid(row=2, column=1, padx=(GEN_PAD, GEN_PAD), pady=(GEN_PAD, GEN_PAD))
        configurationNameLabel.grid(row=4, column=0,padx=(GEN_PAD, GEN_PAD), pady=(GEN_PAD, GEN_PAD))
        self.configurationNameEntry.grid(row=4, column=1,padx=(GEN_PAD, GEN_PAD), pady=(GEN_PAD, GEN_PAD))
        configuratioButton.grid(row=5, column=0, pady=(15, 15))



        # Pack the Container
        self.sectionFrame.pack(expand=1, fill="both")

    def createDhTable(self, masterFrame, rows, cols):
        self.tableFrame = tk.Frame(masterFrame, highlightthickness=0)
        self.entries = {}
        self.tableheight = rows
        self.tablewidth = cols
        counter = 0

        for i in range(len(self.labels)):
            label = ttk.Label(self.tableFrame, text=self.labels[i])
            label.grid(row=0, column=i, padx=(0, 0), pady=(0, 0))
            label.grid_rowconfigure(0, weight=1)
            label.grid_columnconfigure(i, weight=1)

        for row in range(self.tableheight):
            for column in range(self.tablewidth):
                self.entries[counter] = ttk.Entry(self.tableFrame, width=10)
                self.entries[counter].insert(tk.END, "0")
                self.entries[counter].grid(row=row + 1, column=column, padx=(0, 0), pady=(0, 0))
                self.entries[counter].grid_rowconfigure(row, weight=1)
                self.entries[counter].grid_columnconfigure(column, weight=1)
                counter += 1
                self.tableFrame.grid_rowconfigure(row + 1, weight=1)
                self.tableFrame.grid_columnconfigure(column, weight=1)
        self.tableFrame.grid(row=3, column=0, columnspan=2, padx=(0, 0), pady=(0, 0))

    def entryEvent(self, event):
        inputString = self.jointEntry.get()
        if event.keysym.__str__() == "Return":
            self.jointEntry.delete(0, tk.END)

            if inputString.isdigit():
                if int(inputString) < 15:
                    self.DH_joints = int(inputString)
                    print(self.DH_joints)
                    self.tableFrame.destroy()
                    self.createDhTable(self.sectionFrame, self.DH_joints, 6)

    def manipulatorConfig(self):

        manipulatorLinkList = []
        counter = 0
        global robotNum

        for row in range(self.tableheight):
            DHParameterList = []
            for column in range(self.tablewidth):
                try:
                    DHParameterList.append(float(self.entries[counter].get().__str__()))
                    counter += 1
                except:
                    print("FAILED TO APPEND ITEM TO THE LIST")
                    return

            manipulatorLinkList.append(
                rtb.DHLink(theta=DHParameterList[0], d=DHParameterList[1], alpha=DHParameterList[2],
                           a=DHParameterList[3], sigma=DHParameterList[4], offset=DHParameterList[5]))

      #  with open('data.json', 'w', encoding='utf-8') as f:
       #     json.dump(json(manipulatorLinkList), f, ensure_ascii=False, indent=4)

        #print(manipulatorLinkList[0].dumps())
        #print(json.dumps(manipulatorLinkList[0].__str__()))

        manipulatorName = self.configurationNameEntry.get().__str__()
        if manipulatorName == "":
            manipulatorName = "Manipulator " + robotNum.__str__()

        manipulator = rtb.DHRobot(L=manipulatorLinkList, name=manipulatorName)

        robotNum = robotNum + 1
        self.controller.plotSection.sectionFrame.addManipulatorToList(manipulator)
        self.optionList = self.controller.getManipulatorList()

    def updateManipulatorList(self, manipulatorList):
        self.om['menu'].delete(0, "end")
        for rb in self.controller.getManipulatorList():
            self.om['menu'].add_command(label=rb, command=tk._setit(self.listText, rb))
