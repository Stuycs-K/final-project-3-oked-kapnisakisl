import sys
###GLOBAL VARIABLES!!!
HEADER_LEN = 260000
NUMBER_OF_BITS = 1
message = ""
if(len(sys.argv) > 4 or len(sys.argv) < 3):# default is 1 when no args, 2 means one thing, so need 3
    print("Args entered incorrectly; Should be: make decode ARGS=\"<FILE> <FILETOWRITE> <OPTIONALBITS>\"")
filetodecode = sys.argv[1]
filetowrite = sys.argv[2]
if(len(sys.argv) == 4):
    NUMBER_OF_BITS = int(sys.argv[3])
    print("Setting # bits to",int(sys.argv[3]))


with open(filetodecode, 'rb') as f:
    data = f.read()

data = bytearray(data)
message_binary = bytearray(len(data)//(8//NUMBER_OF_BITS) + 100)

message_ticker = 0
data_byte = HEADER_LEN
while(data_byte < len(data)-8 and (data[data_byte] & 1) != 1):

    shifts_remain_in_messagebyte = 7-NUMBER_OF_BITS
    for z in range (0,(8//NUMBER_OF_BITS)):

        data_fragment = (data[data_byte] & int(2**(NUMBER_OF_BITS+1))-2)#takes the relevantly sized piece of the audio (least significant bits except the last) we need to place back in the message

        #places each fragment into the correct position of the message binary
        if (shifts_remain_in_messagebyte > 0):
            message_binary[message_ticker] = message_binary[message_ticker] | (data_fragment << shifts_remain_in_messagebyte)
        
        if (shifts_remain_in_messagebyte == 0):
            message_binary[message_ticker] = message_binary[message_ticker] | (data_fragment)

        if (shifts_remain_in_messagebyte < 0):
            message_binary[message_ticker] = message_binary[message_ticker] | (data_fragment >> (shifts_remain_in_messagebyte*-1))

        shifts_remain_in_messagebyte -= NUMBER_OF_BITS
        data_byte += 1
    
    message_ticker += 1

with open(filetowrite, 'w') as f:
    f.write(message_binary.rstrip(b'\x00').decode('utf-8', errors='ignore'))