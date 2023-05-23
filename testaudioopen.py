from bitstring import BitArray

with open('Bruh_Sound_Effect.wav', 'rb') as f:
    data = f.read()

datahex = data.hex()

#print(data)

test = BitArray(hex=datahex)
#print(test.bin)
print(len(test.bin))

#Testing writing an encode, encountering some issues with the fact that we cant
#figure out header length but going for anyway assuming 46 bytes.

i = (46 * 8) #magic nums for length of header

while(i < len(test.bin)):
    test[i] = True
    i+=8
    if(i % (8*500) == 0):
        print(i / len(test.bin))

print("===================")
print(test.bin)
