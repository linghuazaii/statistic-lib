#!/bin/env python
# -*- coding: utf-8 -*-
# This file is auto-generated.Edit it at your own peril.
import numpy as np
import time, random

def random_generator(count, minimum = 0., maximum = 1.0, duplicate = False, seed = time.time()):
    record = None
    if duplicate == True:
        record = list()
    else:
        record = set()
    while len(record) < count:
        if duplicate == True:
            record.append(random.uniform(minimum, maximum))
        else:
            record.add(random.uniform(minimum, maximum))
    record = list(record)
    random.shuffle(record)
    return record

'''
def main():
    #pass

if __name__ == "__main__":
    main()
'''
