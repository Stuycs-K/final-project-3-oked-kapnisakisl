import sys
###GLOBAL VARIABLES!!!
HEADER_LEN = 260000
NUMBER_OF_BITS = 1

#Mr k suggestion demonstrate audio quality difference from 1->2->4 bits of payload
if(len(sys.argv) > 4):# default is 1 when no args, 2 means one thing, so need 3
    print("Args entered incorrectly; Should be: make encode ARGS=\"<MESSAGEFILE> <TARGETFILE> <OPTIONALBITS>\"")
filetoencode = sys.argv[2]
messagetoencode = sys.argv[1]
if(len(sys.argv) == 4):
    NUMBER_OF_BITS = int(sys.argv[3])
    print("Setting # bits to",int(sys.argv[3]))

with open(messagetoencode, 'r') as f:
    message = f.read()

messagebytes = bytearray(message,'utf-8')

with open(filetoencode, 'rb') as f:
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
    for z in range (0,(8//NUMBER_OF_BITS)):

        message_fragment = (message_byte & int((((2)**(NUMBER_OF_BITS*-1))-1)*(-256)))#takes the relevantly sized piece of the message we need to place in the audio binary

        message_byte = message_byte << NUMBER_OF_BITS#Move the message_byte we are reading left #ofbits so we can read next #ofbits

        message_fragment = (message_fragment >> (8-(NUMBER_OF_BITS+1))) # Right now, we are reading first bits (bits on left.) so looks like 11000000. Move all the way to the right, so aligned for write

        data[ticker] = (data[ticker] ^ message_fragment)#write now correctly shifted data into data

        ticker += 1

#Now we need to add stop codon
for i in range(ticker,ticker+1):
    data[i] = (data[i] | 1)
splitname = filetoencode.split(".",1)#Split only once, hopefully at the .wav or whatever the format was

outname = splitname[0] + "_encoded" + str(NUMBER_OF_BITS) + "." + splitname[1]#Should allow to keep file format, weird behavior if periods in name.
with open(outname, 'wb') as f:
    f.write(data)