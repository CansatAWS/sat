import RFM69.RFM69 as RFM69
from RFM69.RFM69registers import *
import time
import matplotlib


data ={}

def sendMessage(name, sensor, message, max_packet_size = 40):
    Node_ID = 10
    Network_ID = 1
    Is_promiscuous = False
    radio = RFM69.RFM69(RF69_433MHZ,Node_ID,Network_ID,True,intPin = 22,rstPin = 18)
    radio.rcCalibration()
    radio.setHighPower(True)
    radio.encrypt(0)
    radio.promiscuous(Is_promiscuous)
    packet = "<" + message +","+ sensor +"," + name +">"
    
    for i in range (0,len(packet), max_packet_size):
        radio.send(100, packet[i:max_packet_size*i])

def constructReceived(packet):
    packet = packet[1:len(packet)-1] +("\n")
    packets = packet.split(",")
    file = open(packets[1]+".txt","a+")
    file.write(packet)
    return packets
print(constructReceived("<name,data, sensor,>"))

def listen():
    packet = aquirePacket()
    packet = ""
    while True:
        if packet[len(packet)] == ">":
            packets = constructReceived(packet)
            data[packets[2]]
            updateGraph(packets[0], packets[1])
            return packets
        else:
            packet += packet
        

