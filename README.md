# Steg-Ear-Saurus
David Oke, Lefteri Kapnisakis

## About

This project serves to create a basic audio steganography generator, show differences between regular audio files and those with secret messages, and to explain how audio steganography works and why it's useful.

## Method

We used Least Significant Bit (LSB) stegonography to hide messages within each byte of the audio file, hoping to minimize the noticability of the message on audio quality. The method to encode the message is using the last x number of bits to hide a message, and then an additional bit to indicate when the message is done.

## Demonstration

We hope to demonstrate the differences in audio quality by encoding with different numbers of bits, and being able to hear how that changes the sound quality.