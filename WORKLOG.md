# Work Log

## David Oke

### 5-19-23

- Began Research on Audio File Structure (MP3/WAV) & Started Testing Audio Files in Python

### 5-20-23

- Began Updating Readme and Worklog

### 5-23-23

- Found a better way to print/modify audio file binary.

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

- Wrote encoding into data, no way to check if it works but code runs
- Discussed actual process with David, sorted out which ideas to use