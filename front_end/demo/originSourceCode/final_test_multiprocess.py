# -*- coding: utf-8 -*-

import time
from multiprocessing import Pool
from LargeDataCalc import data_input
import os

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    data_input('..\\MillionData\\mdata'+str(name+1)+'.json')
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    
    print 'Parent process %s.' % os.getpid()
    t1 = time.time()
    p = Pool()
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    t2 = time.time()
    print 'All subprocesses done.'
    print "耗时:%f" % (t2-t1)
