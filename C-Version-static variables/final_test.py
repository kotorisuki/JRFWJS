# -*- coding: utf-8 -*-
from LargeDataCalc import data_input
import time


if __name__ == '__main__':
    t1 = time.time()
    data_input('..\\milliondata.json')
    t2 = time.time()
    print "ºÄÊ±£º%f" % (t2-t1)
