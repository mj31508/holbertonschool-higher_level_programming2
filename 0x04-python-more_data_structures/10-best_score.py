#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    return max(my_dict, key=lambda i: my_dict[i])
