#!/usr/bin/python3
alt = 0
for num in range(122, 96, -1):
    print("{}".format(chr(num - alt)), end="")
    alt = 32 if alt == 0 else 0
