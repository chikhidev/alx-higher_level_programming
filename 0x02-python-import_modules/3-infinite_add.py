#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    res = 0
    for i in range(argc - 1):
        res += int(sys.argv[i + 1])

    print("{}".format(res))
