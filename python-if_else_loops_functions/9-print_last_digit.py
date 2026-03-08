#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number) % 10  # son rəqəm
    print("{}".format(last), end="")  # çap et (end="" ilə eyni sətrdə)
    return last  # qaytar
