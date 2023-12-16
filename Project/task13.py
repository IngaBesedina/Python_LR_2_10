#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_cheque(**goods):
    for item, price in goods.items():
        print(f"{item}: {price}$")


if __name__ == "__main__":
    print_cheque(apples=5, oranges=10, bananas=8, peaches=3)
