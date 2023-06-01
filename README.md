# README!

## Group Name: Steg-Ear-Saurus
### David Oke, Lefteri Kapnisakis


## About

This project serves to create an LSB (least significant bit) audio steganography encoder + decoder, explain the mechanisms behind it, and show differences between regular audio files and those with secret messages. Our goal using LSB was to hide messages within each byte of the audio file, hoping to minimize the noticability of the message on audio quality. The method to encode the message is using the last x number of bits to hide a message, and then an additional bit to indicate when the message is done.

## Directions
Coded in python without libraries, compilable using make. WAV files for audio recommended, but other codecs will work too.

To Encode a File into Audio:
- `make encode ARGS="<MESSAGE_FILE> <AUDIO_FILE> <OPTIONALBITS>"`

Setting OPTIONALBITS, of course, is not required. The default bit usage is 1 bit of encoded data per byte, and can also be optionally set to 2, or 4. This also changes the name of the file, which exhibits the following format:

- `<ORIGINAL_FILENAME>_encoded<BIT_USAGE_COUNT>.wav`

To Decode a File into Audio:
- `make decode ARGS="<ENCODED_FILE> <DESTINATION_FILE> <OPTINALBITS>"`

If you want the decoded message to make sense, setting decode bit usage to encode bit usage is reccomended.
