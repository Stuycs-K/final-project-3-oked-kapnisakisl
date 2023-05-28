###GLOBAL VARIABLES!!!
HEADER_LEN = 260000
NUMBER_OF_BITS = 1

#Mr k suggestion demonstrate audio quality difference from 1->2->4 bits of payload
with open('Walkable_City.txt', 'r') as f:
    message = f.read()

messagebytes = bytearray(message,'utf-8')
print(len(messagebytes))

print("first letter ascii:", messagebytes[0])
with open('The-Neighbourhood-Softcore.wav', 'rb') as f:
    data = f.read()

data = bytearray(data)

#if the amount of space we need exceeds the size of the file, yell at the user, proceed if not
if (HEADER_LEN+len(messagebytes)*(8//NUMBER_OF_BITS) >= len(data)):
    raise Exception("Not enough space!!!!!!!!!!!!1")

for i in range (HEADER_LEN,HEADER_LEN+len(messagebytes)*(8//NUMBER_OF_BITS)):
    #i represents the bytewe are on.
    data[i] = (data[i] & (255 - (pow(2, NUMBER_OF_BITS+1) -1)))#I think this is right? all but last #ofbits+1 on

ticker = HEADER_LEN
for x in message:
    message_byte = ord(x)
    print("bin x:",bin(message_byte))
    for z in range (0,(8//NUMBER_OF_BITS)):

        message_fragment = (message_byte & int((((2)**(NUMBER_OF_BITS*-1))-1)*(-256)))#takes the relevantly sized piece of the message we need to place in the audio binary

        message_byte = message_byte << NUMBER_OF_BITS#Move the message_byte we are reading left #ofbits so we can read next #ofbits

        message_fragment = (message_fragment >> (8-(NUMBER_OF_BITS+1))) # Right now, we are reading first bits (bits on left.) so looks like 11000000. Move all the way to the right, so aligned for write

        print("old data:",format((data[ticker]), '#010b'),end=' ')

        data[ticker] = (data[ticker] ^ message_fragment)#write now correctly shifted data into data

        print("new data:",format((data[ticker]),'#010b')) # format just keeps leading 0's same as bin() otherwise

        ticker += 1

#Now we need to add stop codon(s)
print(ticker)
for i in range(ticker,ticker+1):
    data[i] = (data[i] | 1)
#for x in range( HEADER_LEN,len(data)):
#    print("x:",x,"bin:",bin(outdata[x]))

with open('The-Neighbourhood-Softcore_encoded1.wav', 'wb') as f:
    f.write(data)