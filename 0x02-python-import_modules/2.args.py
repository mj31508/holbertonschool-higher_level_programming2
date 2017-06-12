#!/usr/bin/python3


from sys import argv

if __name__ == "__main__":

    num_args = len(argv)

    if num_args == 1:
        print("{} argument.".format(num_args - 1))
    if num_args == 2:
        print("1 argument:\n{}: {} ".format(num_args - 1))
    for num in range(1, num_args):
        print("{:d}: {:s}".format(num, argv[num]))
