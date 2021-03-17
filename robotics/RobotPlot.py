import roboticstoolbox as rtb
import tkinter as tk
import json
# IK
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

puma = rtb.models.DH.Puma560()
panda = rtb.models.DH.Panda()


class RobotPlotSection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # List of robots
        self.manipulators = [puma, panda]
        self.manipulatorNames = []

        for i in range(len(self.manipulators)):
            self.manipulatorNames.append(self.manipulators[i].name)

#        self.loadManipulatorList()


        # Initial Robot Plot
        self.robotPlot = self.createRobotPLot("panda")

        self.canvas = FigureCanvasTkAgg(self.robotPlot.fig, self)
        self.canvas.draw()
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack(expand=1, fill="both")

        # Button Handlers
        self.canvas.get_tk_widget().bind('<Button-1>', self.buttonPressedHandler)
        self.canvas.get_tk_widget().bind('<ButtonRelease-1>', self.mouseReleasedHandler)
        self.canvas.get_tk_widget().bind('<B1-Motion>', self.mouseDragHandler)

        self.x_pressed = False
        self.y_pressed = False
        self.y_previous = 0
        self.x_previous = 0

    def buttonPressedHandler(self, event):
        self.x_pressed = True
        self.y_pressed = True
        self.x_previous = event.x
        self.y_previous = event.y
        print("X: " + event.x.__str__())

    def mouseReleasedHandler(self, event):
        self.x_pressed = False
        self.y_pressed = False

    def mouseDragHandler(self, event):
        if (self.x_pressed == True) & (self.y_pressed == True):
            self.robotPlot.ax.azim = self.robotPlot.ax.azim + ((self.x_previous - event.x) / 20)
            self.robotPlot.ax.elev = self.robotPlot.ax.elev + ((event.y - self.y_previous) / 20)
            self.canvas.draw()

    def updateRobotPlot(self, selected):
        print("Update Robot Plot")

        print(self.manipulators.__str__())
        print(self.manipulatorNames)

        pyplot = rtb.backends.PyPlot()
        pyplot.launch()

        for rb in self.manipulators:
            if selected == rb.name:
                pyplot.add(rb)
                print("we made it")

        pyplot.close()
        pyplot.ax.azim = 45
        pyplot.ax.elev = 45

        self.canvas.get_tk_widget().destroy()
        self.robotPlot = pyplot
        self.canvas = FigureCanvasTkAgg(self.robotPlot.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()

        # Button Handlers
        self.canvas.get_tk_widget().bind('<Button-1>', self.buttonPressedHandler)
        self.canvas.get_tk_widget().bind('<ButtonRelease-1>', self.mouseReleasedHandler)
        self.canvas.get_tk_widget().bind('<B1-Motion>', self.mouseDragHandler)

        self.x_pressed = False
        self.y_pressed = False
        self.y_previous = 0
        self.x_previous = 0

    def createRobotPLot(self, robotName):
        pyplot = rtb.backends.PyPlot()
        pyplot.launch()
        pyplot.add(panda)
        pyplot.close()
        return pyplot

    def addManipulatorToList(self, manipulator):
        self.manipulators.append(manipulator)
        self.manipulatorNames.append(manipulator.name)
        self.controller.controlSection.tab4.updateManipulatorList(self.manipulators)  # updates the arm config list gui
        print(manipulator.__str__())
        # print(json.dumps(manipulator))
        jsonStringArray = "["
        writeManipulatorsToFile(self.manipulators)

    # Reads the manipulator list in the file and returns the,
    def loadManipulatorList(self):

        with open('data.json', 'r') as f:
            allLines = f.readlines()
            fileString = ""

            for line in allLines:
                fileString = fileString + line

            jsonObject = (json.loads(fileString))
            print(jsonObject)

            # Clear lists
            self.controller.controlSection.tab4.optionList.clear()
            self.manipulatorNames.clear()
            self.manipulators.clear()

            for name, listDict in jsonObject.items():
                for key, data_list in listDict.items():
                    manipulatorLinkList = []
                    for data in data_list:
                        manipulatorLinkList.append(
                            rtb.DHLink(theta=data['theta'], d=data['d'], alpha=data['alpha'],
                                       a=data['a'], sigma=data['sigma'], offset=data['offset']))

                print(manipulatorLinkList)
                print(name)

                manipulator = rtb.DHRobot(L=manipulatorLinkList, name=name)
                self.addManipulatorToList(manipulator)

                self.controller.controlSection.sectionFrame.tab4.optionList.append(name)




            print("fileString: " + fileString)
        f.close()


def writeManipulatorsToFile(manipulatorList):
    print("ok")
    with open('data.json', 'w') as f:
        finalString = "{"

        for manip in manipulatorList:
            jsonString = json.dumps(manip, default=manipulator_encoder)
            jsonString = ((jsonString[: -1])[1:])  # Remove first and last characters
            finalString = finalString + jsonString + ","

        finalString = finalString[:-1] + "}"
        print(finalString)
        json.dump(json.loads(finalString), f)

    f.close()


def manipulator_encoder(manipulator):
    if isinstance(manipulator, rtb.DHRobot):
        linkArr = []
        i = 1
        for link in manipulator.links:
            linkDict = {"theta": link.theta, "d": link.d, "a": link.a, "alpha": link.alpha, "sigma": link.sigma, "offset":link.offset}
            linkArr.append(linkDict)

        manipulatorObject = {manipulator.name: {"link-list": linkArr}}

        return manipulatorObject

    raise TypeError(f'Object {manipulator} is not of type DH Robot')
