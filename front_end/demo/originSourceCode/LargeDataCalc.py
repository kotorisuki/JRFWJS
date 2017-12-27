# -*- coding: utf-8 -*-
# 读取json文件中的数据，进行批量处理

import json
from integration import integration

def data_input(filename, resultfilename):
    with open(filename) as json_file:
        data = json.load(json_file)
    cnt = len(data)
    result=[]
    for i in xrange(cnt):
        pv,yy,dd,cc,dp=integration(data[i]['coupon_rate'],
                                data[i]['face_value'],
                                data[i]['time_start'],
                                data[i]['year'],
                                data[i]['time_cur'],
                                data[i]['frequency'])
        re={'Pv':pv,'Yield':yy,'Duration':dd,'Convexity':cc,'DirtyPrice':dp}
        result.append(re)
        #if(i%1000 == 0):
            #print "PV：%f" % pv
            #print "yield：%f" % yy
            #print "Duration：%f" % dd
            #print "Convexity：%f" % cc
            #print "==============%d============="%i
    with open(resultfilename, 'w') as json_file:
            json_file.write(json.dumps(result))
