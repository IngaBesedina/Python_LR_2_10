#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def el_sum(*args):
    if args:
        i1 = args.index(0)
        i2 = len(args) - 1 - args[::-1].index(0)
        return sum(args[i1+1:i2])
    else:
        return None


if __name__ == "__main__":
    print(el_sum(2, 0, 3, 0, 5, 4, 0, 8, 5))
    print(el_sum(3, 4, 0, -7, 0, -6, -4, 0, 8, -5, 7))
    print(el_sum(-7, 2, 1, 3, 0, 5, -4, 8, 9, 0, 8, 5))
