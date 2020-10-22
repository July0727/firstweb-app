#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def create_args_string(num):
    L = []
    for n in range(num):
        L.append(n)
    return ', '.join(L)


print(create_args_string(4))
