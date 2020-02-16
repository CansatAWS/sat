import RFM69.RFM69 as RFM69
from RFM69.RFM69registers import *
import time
Node_ID = 10
Network_ID = 1
Is_promiscuous = False
radio = RFM69.RFM69(RF69_433MHZ,Node_ID,Network_ID,True,intPin = 22,rstPin = 18)
radio.rcCalibration()
radio.setHighPower(True)
radio.encrypt(0)
radio.promiscuous(Is_promiscuous)
print("Radio initialisation successful")
while True:
    radio.send(100,"Hello World!")
    print("sent OK")
    time.sleep(1)