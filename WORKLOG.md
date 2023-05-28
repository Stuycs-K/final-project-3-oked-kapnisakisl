# Work Log

## David Oke

### 5-19-23

- Began Research on Audio File Structure (MP3/WAV) & Started Testing Audio Files in Python

### 5-20-23

- Began Updating Readme and Worklog

### 5-23-23

- Found a better way to print/modify audio file binary.

### 5-25-23

- Discussed actual process with Lefteri, sorted out which ideas to use.

### 5-26-23

-Improved readability of current code, made changes to minimize effects of stop codon.
-Worked with Lefteri on plans for decode portion.

### 5-27-23

- Cleaned up code in encode
- Added a MUCH larger audio and message file, allowed file imports/exports for both
- Added decode file, made it decode whatever is in the encoded audio file (mindblowing)
- Made it possible to encode/decode using 1, 2, and 4 bit storage variations (2, 3, 5 counting the stop codon)

## Lefteri Kapnisakis

### 5-19-23

- Sat with David and also messed with test file

### 5-22-23

- Got printing in binary of audio file working
- Found out wav is 44 byte header.

### 5-23-23

- Modified bits at end of every 8 bits, but takes forver because string array is treated like string, which I wanted so i could print but very annoying.

### 5-24-23

- Switched back to byte array? instead of bit array, and instead of just using bin()
- Started on trying to figure out encoding scheme, and using & to clear last 3 bits.

### 5-25-23

- Wrote encoding into data, no way to decode yet but code runs, prints look good
- Discussed actual process with David, sorted out which ideas to use

### 5-26-23

- Worked with David, moved codon to least significant bit to reduce static, now just need decode then can move on to more complex things