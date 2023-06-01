# README!

## Group Name: Steg-Ear-Saurus
### David Oke, Lefteri Kapnisakis


## About

This project serves to create an LSB (least significant bit) audio steganography encoder + decoder, explain the mechanisms behind it, and show differences between regular audio files and those with secret messages.

## Directions
Coded in python without libraries, compilable using make.

To Encode a File into Audio:
- `make encode ARGS="<MESSAGE_FILE> <AUDIO_FILE> <OPTIONALBITS>"`

Setting OPTIONALBITS, of course, is not required. The default bit usage is 1 bit of encoded data per byte, and can also be optionally set to 2, or 4. This also changes the name of the file, which exhibits the following format:

- `<ORIGINAL_FILENAME>_encoded<BIT_USAGE_COUNT>`

To Decode a File into Audio:
- `make decode ARGS="<ENCODED_FILE> <DESTINATION_FILE> <OPTINALBITS>"`

If you want the decoded message to make sense, setting decode bit usage to encode bit usage is reccomended.
