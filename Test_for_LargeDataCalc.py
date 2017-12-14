import time
from LargeDataCalc import data_input


if __name__ == '__main__':
    t1 = time.time()
    data_input('rdata.json')
    t2 = time.time()
    print "耗时:%f" % (t2-t1)
