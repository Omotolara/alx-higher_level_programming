#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0
    for argv in sys.argv[1:]:
        sum = sum + int(sys.argv[argv + 1])
        print("{}".format(sum))
