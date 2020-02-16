import RFM69.RFM69 as RFM69
from RFM69.RFM69registers import *
import time
Node_ID = 100
Network_ID = 1
Is_promiscuous = False
radio = RFM69.RFM69(RF69_433MHZ,Node_ID,Network_ID,True,intPin = 22,rstPin = 18)
radio.rcCalibration()
radio.setHighPower(True)
radio.encrypt(0)
radio.promiscuous(Is_promiscuous)
print("Radio initialisation successful")
message_count = 0
while True:
    if radio.receiveDone():
        message = "".join(map(chr,radio.DATA))
        print(message)
        remote_node = radio.SENDERID
        RSSI = radio.RSSI
        message_count += 1
        radio.receiveBegin()
    else:
        time.sleep(0.1)