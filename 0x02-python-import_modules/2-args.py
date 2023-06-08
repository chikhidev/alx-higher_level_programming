#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

