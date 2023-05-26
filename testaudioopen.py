# from bitstring import BitArray
# import sys

###GLOBAL VARIABLES!!!
HEADER_LEN = 300

#Mr k suggestion demonstrate audio quality difference from 1->2 -> 3 -> 4 bytes of payload
message = "hzi!"
messagebytes = bytearray(message,'utf-8')

print(messagebytes[0])
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
for i in range (HEADER_LEN,len(data)):
    #i represents the byte we are on.
    data[i] = (data[i] & 248)#I think 248 is right? all but last 3 on
    #print("preand:",bin(data[i]),"postand:",bin(data[i]))
ticker = HEADER_LEN
for x in message:
    byte = ord(x)
    print("bin x:",bin(byte))
    for z in range (0,4):
        check = (byte & (64 + 128))
        byte = byte << 2#Move the byte we are reading left 2 so we can read next 2
        #print("preshift:",check)
        check = (check >> 6) # Right now, we are reading first 2 bits (bits on left.) so looks like 11000000. Move all the way to the right, so aligned for write
        #print("postshift:",check)
        print("old data:",format((data[ticker]), '#010b'),end=' ')
        data[ticker] = (data[ticker] ^ check)#write now correctly shifted data into data
        print("new data:",format((data[ticker]),'#010b')) # format just keeps leading 0's same as bin() otherwise
        ticker += 1
        if(ticker >= len(data)):
            print("RAN OUT OF ENCODING SPACE!!!!!!!!!!!")
        #Go through every 2 bits, writing, then shifting left(?) 2

#Now we need to add stop codon(s)
print(ticker)
for i in range(ticker,len(data)):
    data[i] = (data[i] ^ 4)
#for x in range( HEADER_LEN,len(data)):
#    print("x:",x,"bin:",bin(outdata[x]))
