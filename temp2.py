from time import sleep
import threading
from Tkinter import *

serialdata = []
data = True

class SensorThread(threading.Thread):
    def run(self):
        try:
            i = 0
            while True:
                serialdata.append("Hello %d" % i)
                i += 1
                sleep(1)
        except KeyboardInterrupt:
            exit()

class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.lbl = Label(self.root, text="")
        self.updateGUI()
        self.readSensor()

    def run(self):
        self.lbl.pack()
        self.lbl.after(1000, self.updateGUI)
        self.root.mainloop()

    def updateGUI(self):
        msg = "Data is True" if data else "Data is False"
        self.lbl["text"] = msg
        self.root.update()
        self.lbl.after(1000, self.updateGUI)

    def readSensor(self):
        self.lbl["text"] = serialdata[-1]
        self.root.update()
        self.root.after(527, self.readSensor)

if __name__ == "__main__":
    SensorThread().start()
    Gui().run()