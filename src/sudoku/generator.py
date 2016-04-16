#!/usr/bin/python
import random

def generate(size, hints):


    length = size

    res = []
    for i in range(size):
        inter = []
        for j in range(size):
            inter.append(0)
        res.append(inter)
    

    for i in range(hints):
        x = random.randint(0, length-1)
        y = random.randint(0, length-1)

        res[x][y] = random.randint(1, length)

    return res


