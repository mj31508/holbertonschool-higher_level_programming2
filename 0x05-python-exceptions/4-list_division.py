#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    end = []
    for i in range(list_length):
        try:
            end.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("wrong type")
            end.append(0)
        except IndexError:
            print("out of range")
            end.append(0)
        except ZeroDivisionError:
            print("division by 0")
            end.append(0)
        finally:
            pass
    return(end)
