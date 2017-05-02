#!/usr/bin/python3
# create a variable with ascii value 97(a)
alpha = 97
# create a while loop to loop from a to z
while alpha <= 122:
    # need a if statement for q and e to omit
    if alpha == 101 or alpha == 113:
        # want my code to skip letter by adding 1 to it
        alpha += 1
        # if it hits i want to continue running
        continue
    print("{}".format(chr(alpha)), end="")
    alpha += 1
