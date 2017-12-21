# -*- coding: utf-8 -*-

import time
from LargeDataCalc import data_input

if __name__ == '__main__':
    t1 = time.time()
    for i in range(1,7):
		data_input('..\\MillionData\\mdata'+str(i)+'.json')
    t2 = time.time()
    print "耗时:%f" % (t2-t1)
