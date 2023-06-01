# outline

Explain the basics of audio steganography

## What is Audio Steganography

Audio steganography is the process of hiding a message within audio, using various possible different methods.

There are a few different common types of audio steganography:

- Least Significant Bit 
- Spread Spectrum
- Phase Coding
- Echo Hiding

We will be covering LSB steganography, and the other audio steganography group (Hi Henry and Perry!) will be covering Echo Hiding. The other methods use different kinds of changes and shifts to the audio waves to encode their data.

## Least Significant Bit Steganography

LSB stegonaraphy works similarly to the way that we did image steganography, by slightly modifying the least important bits of every byte of the audio file.
 

|1|0|1|1|0|0|1|0|
|-|-|-|-|-|-|-|-|
| | | | | | |^Message bit|^stop bit|

We write the message into the last bit (or bits), and reserve the rightmost least signifcant bit to indicate when to stop reading.

#
- What is audio steg? (hiding things)
- How does LSB work? (draw/type out how bits are placed in the file to put message together)
- Mention other methods (shoutout echo hiding! henry/perry!)

Demonstrate the process using our code
- Play encoded version (1 bit) of Softcore, play non-encoded version and show how unnoticeable it is
- Show how to compile encode/decode, bit stuff as well (show that the entire book went through the process unscathed! (except apostrophes oooops))
- Show audio quality difference between 1/2/4 bit versions
- Use Audacity to show differences in spectrogram between 1/2/4/non-enc versions

HW
-make an assignment