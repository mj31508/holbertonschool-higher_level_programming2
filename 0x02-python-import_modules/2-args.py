#!/usr/bin/python3

if __name__=="__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print("{} argument.".format(argc - 1))
    elif args == 2:
        print("{} argumrnt:".format(argc - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(argc - 1))
        for i in rage(1, args):
            print("{}: {}".format(i, sys.argv[i]))
