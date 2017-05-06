#!/usr/bin/python3
if __name__=="__main__":
    import sys
    total = 0
    args = len(sys.argv)
    for i in range(1, args):
        total += (int(sys.argv[i]))
    print("{}".format(total))
