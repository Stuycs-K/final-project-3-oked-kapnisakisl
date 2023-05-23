# from bitstring import BitArray
# import sys


with open('Bruh_Sound_Effect.wav', 'rb') as f:
    data = f.read()

print(data[3] >> 4,'\n')
print(data)

# datastr = bin(int.from_bytes(data, byteorder=sys.byteorder))

# print(datastr)