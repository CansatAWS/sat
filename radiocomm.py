import math

def sendMessage(message, mType, name, max_packet_size = 40):
    header = ",name:" + name+",type:" + mType + "," 
    header = "hl:"+ str(int(((len(header)+ max_packet_size + math.log(len(header)-len(header)%10,10))/max_packet_size)))+",pl:" + str(int((max_packet_size+len(message))/max_packet_size)) + header
    return header
#hl,pl,packet,time,
#after len(hlarray) == hl
#assemble
#messageparts
#when len(plarray) == pl
#decode
#end
print(sendMessage("Messageaaaaaaaaaaaaaaaaaaaaaa5y5jjnerfgg46", "string","0011155314754j67uk8ofgt54g56h55"))

def assembleMessage(header,body):
    
