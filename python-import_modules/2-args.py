#!/usr/bin/python3
import sys 
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if arg == 0:
            print("0 arguments.")
        elif arg == 1:
            print("1 argument: {}".format(arg))
        elif arg > 1:
            print("{} arguments: {}".format(arg, arg))
