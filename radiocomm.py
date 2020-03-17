def sendMessage(name, sensor, message, max_packet_size = 40):
    packet = "<" + message +","+ sensor +"," + name +">"
    packets = []
    for i in range (0,len(packet), max_packet_size):
        packets.append(packet[i,max_packet_size*i])

def constructReceived(packet):
    packet = packet[1:len(packet)-1] +("\n")
    packets = packet.split(",")
    file = open(packets[1]+".txt","a+")
    file.write(packet)
    
    
print(constructReceived("<name,data, sensor,>"))
