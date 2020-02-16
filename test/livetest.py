import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()
class LiveUpdate():
    def __init__(self):
        self.tempData = []
        self.pressureData = []
        self.heightData = []
    def addAndPlot(self,i):
        self.tempData.append(sensor.read_temperature())
        self.pressureData.append(sensor.read_pressure())
        cHeight = (288.15/-0.0065)*((self.pressureData[-1]/101325)**(-(-0.0065*8.3144598)/(9.80665*0.028964))-1)
        self.heightData.append(cHeight)
        tempAxis.clear()
        tempAxis.plot(self.tempData)
        pressureAxis.clear()
        pressureAxis.plot(self.pressureData)
        heightAxis.clear()
        heightAxis.plot(self.heightData)
        #print("height: ",end = "")
        #print((288.15/-0.0065)*((self.pressureData[-1]/101325)**(-(-0.0065*8.3144598)/(9.80665*0.028964))-1))
graph,axis = plt.subplots(3)
tempAxis = axis[0]
pressureAxis = axis[1]
heightAxis = axis[2]
tempReadings = LiveUpdate()
tempReadings.addAndPlot(1)
ani = animation.FuncAnimation(graph,tempReadings.addAndPlot,1)
plt.show()