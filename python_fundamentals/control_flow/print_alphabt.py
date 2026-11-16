#!/usr/bin/env python3
letters = ""
for c in range(ord('a'), ord('z') + 1):
    if chr(c) != 'q' and chr(c) != 'e':
        letters += chr(c)
print(letters)
