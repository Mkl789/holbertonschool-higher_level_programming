#!/usr/bin/python3
import sys 
total = 0
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        total += int(arg)
    if total == 1:
        print("{} {}".format(total, "argument:"))
    elif total > 1:
        print("{} {}".format(total, "arguments:"))
    else:
        print("{} {}".format(total, "arguments."))
