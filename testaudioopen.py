with open('Bruh_Sound_Effect.wav', 'rb') as f:
    data = f.read()

datahex = data.hex()

print(datahex)