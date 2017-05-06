#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir2 = dir(hidden_4)
    for dir in dir2:
        if dir[:2] is not "__":
            print(dir)
