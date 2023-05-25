# from bitstring import BitArray
# import sys

message = "hi!"
messagebytes = bytearray(message,'utf-8')

print(messagebytes[0])
with open('Bruh_Sound_Effect.wav', 'rb') as f:
    data = f.read()
    
print(data[3])
print(bin(data[3]))

data = bytearray(data)
print("data3,", data[3])
#dataray[3] = 248
#print("testing!!")
#print(dataray[3])
#print(bin(dataray[3]))
#this shows the bytes are 8 bits (duh) but it doesnt print leading 0s.

#print(data)
outputdata = data
for i in range (50,len(data)):
    #i represents the byte we are on.
    byte = data[i]
    outputdata[i] = (data[i] & 248)#I think 248 is right? all but last 3 on
#We need to figure out encoding scheme here.
    #outdata = data[i]



#And it with all but last bit on, then or it with what we want. And should clear, or should add.


# datastr = bin(int.from_bytes(data, byteorder=sys.byteorder))

# print(datastr)

#test = BitArray(hex=datahex)
#print(test.bin)
#print(len(test.bin))

#Testing writing an encode, encountering some issues with the fact that we cant
#figure out header length but going for anyway assuming 46 bytes.

#i = (46 * 8) #magic nums for length of header

#while(i < len(test.bin)):
#    test[i] = True
#    i+=8
 #   if(i % (8*500) == 0):
#        print(i / len(test.bin))

#print("===================")
#print(test.bin)