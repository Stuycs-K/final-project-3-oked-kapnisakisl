###GLOBAL VARIABLES!!!
HEADER_LEN = 260000
NUMBER_OF_BITS = 1

message = ""

with open('The-Neighbourhood-Softcore_encoded1.wav', 'rb') as f:
    data = f.read()

data = bytearray(data)
message_binary = bytearray(len(data)//(8//NUMBER_OF_BITS) + 100)
# print(len(data)) #37066884
# print(len(message_binary)) #4633460

message_ticker = 0
data_byte = HEADER_LEN
while(data_byte < len(data)-8):

    # print("bin x:",bin(data_byte))
    shifts_remain_in_messagebyte = 6
    for z in range (0,(8//NUMBER_OF_BITS)):

        data_fragment = (data[data_byte] & int(2**(NUMBER_OF_BITS+1))-2)#takes the relevantly sized piece of the audio (least significant bits except the last) we need to place back in the message

        #places each fragment into the correct position of the message binary
        if (shifts_remain_in_messagebyte > 0):
            message_binary[message_ticker] = message_binary[message_ticker] | (data_fragment << shifts_remain_in_messagebyte)
        
        if (shifts_remain_in_messagebyte == 0):
            message_binary[message_ticker] = message_binary[message_ticker] | (data_fragment)

        if (shifts_remain_in_messagebyte < 0):
            message_binary[message_ticker] = message_binary[message_ticker] | (data_fragment >> (shifts_remain_in_messagebyte*-1))

        shifts_remain_in_messagebyte -= 1
        data_byte += 1
    
    # print(message_binary[message_ticker])
    message_ticker += 1

# print(message_binary)

with open('decoded_text.txt', 'w') as f:
    f.write(message_binary.decode('utf-8', errors='ignore'))