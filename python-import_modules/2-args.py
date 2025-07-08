#!/usr/bin/python3
import sys 
total = 0
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        total += int(arg)
    if total == 0:
        print("{} {}".format(total, "arguments.", end=arg))
    elif total == 1:
        print("{} {}".format(total, "argument:", end=arg))
    elif total > 1:
        print("{} {}".format(total, "arguments:", end=arg))
    else:
        pass
