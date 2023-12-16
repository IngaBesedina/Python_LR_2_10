#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_mean(*args):
    if args:
        args_sum = sum([1/a for a in args])
        return round(len(args) / args_sum, 2)

    else:
        return None


if __name__ == "__main__":
    rez = harmonic_mean(3, 4, 8, 6, 5)
    print(rez)
