#!/bin/env python
# -*- coding: utf-8 -*-
# This file is auto-generated.Edit it at your own peril.
import numpy as np
import time, random, matplotlib, json
import matplotlib.pyplot as plt
import scipy.stats as stats

def random_generator_f(count, minimum = 0., maximum = 1.0, duplicate = False, seed = time.time()):
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

def random_generator_i(count, minimum = 0, maximum = 100, duplicate = False, seed = time.time()):
    record = None
    if duplicate == True:
        record = list()
    else:
        record = set()
    while len(record) < count:
        if duplicate == True:
            record.append(random.randint(minimum, maximum))
        else:
            record.add(random.randint(minimum, maximum))
    record = list(record)
    random.shuffle(record)
    return record

def mean(array, axis = None):
    return np.mean(array, axis)

def median(array, axis = None):
    return np.median(array, axis)

def std(array, axis = None, ddof_ = 1):
    return np.std(array, axis, ddof = ddof_)

def hist(data, breaks = 10, col = 'b'):
    plt.subplot(1,2,1)
    plt.title('Histogram')
    weights = np.ones_like(data) / float(len(data))
    plt.hist(data, breaks, weights = weights, facecolor=col, histtype = 'stepfilled', stacked = True)
    plt.grid(True)
    ax2 = plt.subplot(1,2,2)
    ax2.set_axis_off()
    ax2.invert_yaxis()
    ax2.text(0, 0, json.dumps(summary(data), indent = 4, sort_keys = True), verticalalignment = 'top')

def saveimg(img):
    plt.savefig(img)
    plt.clf()

def summary(data, axis = None):
    info = stats.describe(data, axis)
    dc = dict()
    dc['observations'] = info[0]
    dc['min'] = info[1][0]
    dc['max'] = info[1][1]
    dc['mean'] = info[2]
    dc['median'] = median(data, axis)
    dc['variance'] = info[3]
    dc['skewness'] = info[4]
    dc['kurtosis'] = info[5]
    dc['Q1'] = np.percentile(data, 25, axis)
    dc['Q2'] = np.percentile(data, 50, axis)
    dc['Q3'] = np.percentile(data, 75, axis)
    dc['IQR'] = dc['Q3'] - dc['Q1']
    dc['standard variance'] = std(data, axis)

    return dc

def pdict(data, sort = True):
    print json.dumps(data, indent = 4, sort_keys = sort)

'''
def main():
    #pass

if __name__ == "__main__":
    main()
'''
