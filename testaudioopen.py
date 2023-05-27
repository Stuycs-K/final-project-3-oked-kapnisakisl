# from bitstring import BitArray
# import sys

###GLOBAL VARIABLES!!!
HEADER_LEN = 200
NUMBER_OF_BITS = 2

#Mr k suggestion demonstrate audio quality difference from 1->2->4 bits of payload
message = "hello there!"
messagebytes = bytearray(message,'utf-8')

print("first letter ascii:", messagebytes[0])
with open('Bruh_Sound_Effect.wav', 'rb') as f:
    data = f.read()

data = bytearray(data)
for i in range (HEADER_LEN,len(data)):
    #i represents the bytewe are on.
    data[i] = (data[i] & (255 - (pow(2, NUMBER_OF_BITS+1) -1)))#I think this is right? all but last #ofbits+1 on

ticker = HEADER_LEN
for x in message:
    message_byte = ord(x)
    print("bin x:",bin(message_byte))
    for z in range (0,(8/NUMBER_OF_BITS)):
        message_fragment = (message_byte & (64 + 128))

        message_byte = message_byte << NUMBER_OF_BITS#Move the message_byte we are reading left #ofbits so we can read next #ofbits

        message_fragment = (message_fragment >> (8-(NUMBER_OF_BITS+1))) # Right now, we are reading first bits (bits on left.) so looks like 11000000. Move all the way to the right, so aligned for write

        print("old data:",format((data[ticker]), '#010b'),end=' ')

        data[ticker] = (data[ticker] ^ message_fragment)#write now correctly shifted data into data

        print("new data:",format((data[ticker]),'#010b')) # format just keeps leading 0's same as bin() otherwise

        ticker += 1

        if(ticker >= len(data)):
            print("RAN OUT OF ENCODING SPACE!!!!!!!!!!!")
        #Go through every 2 bits, writing, then shifting left(?) 2

#Now we need to add stop codon(s)
print(ticker)
for i in range(ticker,len(data)):
    data[i] = (data[i] | 1)
#for x in range( HEADER_LEN,len(data)):
#    print("x:",x,"bin:",bin(outdata[x]))

with open('Bruh_Sound_Effect_encoded2.wav', 'wb') as f:
    f.write(data)