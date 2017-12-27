# -*- coding: utf-8 -*-
#随机生成大量测试数据，保存在rdata.json中
#测试数据格式{'time_start'："XXXX/XX/XX",'year'：1,'frequency':1,'face_value':100,'coupon_rate':0.04,'time_cur':"XXXX/XX/XX"}
import json
import random
import time
import datetime
from datetime import date

ryear=[1,2,3,5]; #债券年限随机选取1,2,3,5
a1=(2010,1,1,0,0,0,0,0,0)        #设置开始日期时间元组（2010-01-01 00：00：00）
a2=(2017,12,1,23,59,59,0,0,0)    #设置结束日期时间元组（2017-12-01 23：59：59）

class RData(object):
    def __init__(self,num):
        self.n = num 
        self.rds=[]
    def generate(self):
        for i in range(self.n):
            random.seed()
            start=time.mktime(a1)    #生成开始时间戳
            end=time.mktime(a2)      #生成结束时间戳 
            t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
            date_touple=time.localtime(t)          #将时间戳生成时间元组
            if(time.strftime("%Y/%m/%d",date_touple)[5:7]=="02" and time.strftime("%Y/%m/%d",date_touple)[8:10]=="29"):
                continue
            ry = ryear[random.randint(0,3)]    #随机生成债券年限
            ct = random.randint(1,ry*365) #随机天数
            cdtime = datetime.datetime.fromtimestamp(t) + datetime.timedelta(days = ct)  #生成出售时间
            t={'time_start':time.strftime("%Y/%m/%d",date_touple),
               'year':ry,
               'frequency':random.randint(1,3),
               'face_value':random.randrange(100,100000,100),
               'coupon_rate':random.uniform(0.03,0.05),
               'time_cur':cdtime.strftime("%Y/%m/%d")} 
            self.rds.append(t)
    def store(self):
        with open('rdata.json', 'w') as json_file:
            json_file.write(json.dumps(self.rds))

if __name__ == '__main__':
    rd = RData(10000)
    rd.generate()
    rd.store()
    print "done"
