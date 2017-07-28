#!/bin/env python
# -*- coding: utf-8 -*-
# This file is auto-generated.Edit it at your own peril.
from common import *

def main():
    data = random_generator_i(1000, 1, 20000)
    hist(data, breaks = 30)
    saveimg("data.png")
    pdict(summary(data))

if __name__ == "__main__":
    main()

