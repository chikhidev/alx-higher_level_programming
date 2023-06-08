#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    i = 1

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    while i <= count:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

