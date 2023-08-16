#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    cargv = len(sys.argv) - 1
    if cargv == 0:
        print("0 arguments.")
    elif cargv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(cargv))
    for c, argv in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(c, argv))
