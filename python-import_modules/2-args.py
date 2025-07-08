#!/usr/bin/python3
import sys 
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        arg_count = len(sys.argv) - 1
        if arg_count == 0:
            print("0 arguments.")
        elif arg_count == 1:
            print("1 argument: {}".format(arg))
        elif arg_count > 1:
            print("{} arguments: {}".format(arg_count, arg))
