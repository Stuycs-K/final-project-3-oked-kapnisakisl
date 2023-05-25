# from bitstring import BitArray
# import sys

###GLOBAL VARIABLES!!!
HEADER_LEN = 50

#Mr k suggestion demonstrate audio quality difference from 1->2 -> 3 -> 4 bytes of payload
message = "hzi!"
messagebytes = bytearray(message,'utf-8')
with open('Bruh_Sound_Effect.wav', 'rb') as f:
    data = f.read()
    
print(data[3])
print(bin(data[3]))

data = bytearray(data)
print("dataray3",data[3])
#dataray[3] = 248
#print("testing!!")
#print(dataray[3])
#print(bin(dataray[3]))
#this shows the bytes are 8 bits (duh) but it doesnt print leading 0s.
#print(data)
outdata = data
for i in range (HEADER_LEN,len(data)):
    #i represents the byte we are on.
    byte = data[i]
    outdata[i] = (data[i] & 248)#I think 248 is right? all but last 3 on
ticker = HEADER_LEN
for x in message:
    #print("bin x:",bin(ord(x)))
    check = (ord(x) & (64 + 128))
    #print("preshift:",check)
    check = (check >> 6) # Right now, we are reading first 2 bits (bits on left.) so looks like 11000000. Move all the way to the right, so aligned for write
    #print("postshift:",check)
    outdata[ticker] = (outdata[ticker] ^ check)#write now correctly shifted data into outdata
    ticker += 1
    if(ticker >= len(data)):
        print("RAN OUT OF ENCODING SPACE!!!!!!!!!!!")
    #Go through every 2 bits, writing, then shifting left(?) 2

        #data[i]
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
