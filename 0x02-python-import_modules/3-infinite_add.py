#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    result = 0
    cargv = len(sys.argv) - 1
    for ind in range(cargv):
        result = result + int(sys.argv[ind + 1])
        print("{}".format(result))
