# -*- coding: utf-8 -*-
# 读取json文件中的数据，进行批量处理

import time
import datetime
from datetime import date
import json
from integration import integration

def data_input(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    cnt = len(data)
    result=[]
    for i in range(cnt):
        pv,yy,dd,cc=integration(data[i]['coupon_rate'],
                                data[i]['face_value'],
                                data[i]['time_start'],
                                data[i]['year'],
                                data[i]['time_cur'],
                                data[i]['frequency'])
        re={'Pv':pv,'Yield':yy,'Duration':dd,'Convexity':cc}
        result.append(re)
        #if(i%1000 == 0):
            #print "PV：%f" % pv
            #print "yield：%f" % yy
            #print "Duration：%f" % dd
            #print "Convexity：%f" % cc
            #print "==============%d============="%i
    with open('result.json', 'w') as json_file:
            json_file.write(json.dumps(result))


if __name__ == '__main__':
    t1 = time.time()
    data_input('rdata.json')
    t2 = time.time()
    print "耗时：%f" % (t2-t1)
