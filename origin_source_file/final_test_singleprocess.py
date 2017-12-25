# -*- coding: utf-8 -*-
#直接运行百万数据集的测试用例，所需的时间。

import time
from LargeDataCalc import data_input

if __name__ == '__main__':
    t1 = time.time()
    for i in range(1,7):
		data_input('..\\MillionData\\mdata'+str(i)+'.json')
    t2 = time.time()
    print "运行百万数据集时，调用子进程比直接运行父进程多花的时间:%f" % (t2-t1)
