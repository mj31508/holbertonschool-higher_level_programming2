#!/usr/bin/python3
def print_square(size):
        if size < 0:
            raise ValueError("size must be > 0")
        elif isinstance(size,float) and size < 0:
            raise VauleError("size must be an integer")
        elif not isinstance(size,int):
            raise TypeError("size must be an integer")
        else:
            for row in range(size):
                for column in range(size):
                    print('#', end="")
                print()
