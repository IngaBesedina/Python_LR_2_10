#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def average_geometric(*args):
    product = 1
    for num in args:
        product *= num

    return round(math.pow(product, 1/len(args)), 2)


if __name__ == "__main__":
    rez = average_geometric(3, 4, 8, 6, 5)
    print(rez)
