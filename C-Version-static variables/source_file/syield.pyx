# -*- coding: utf-8 -*-

#v :债券本金
#c :债券的利率
#yn:债券的年限
#timeStart/ts:债券发行日期
#f :债券付息频率

import datetime

class Coupon:
    def __init__(self,char *cid,int yn,int f,timeStart,list yields):
        #timeStart,yields
        self.cid = cid
        self.yn = yn
        self.f  = f
        self.timeStart = timeStart
        self.yields = yields
    def get_yield(self,int n):
        return self.yields[len(self.yields)-n:len(self.yields)]
    
C1 = Coupon("s0001",1,1,datetime.date(2012,05,21),[0.045])
C4 = Coupon("z0001",1,1,datetime.date(2014,05,21),[0.042])
C7 = Coupon("w0001",1,1,datetime.date(2016,05,21),[0.039])
C2 = Coupon("s0002",1,2,datetime.date(2012,05,21),[0.042,0.043])
C5 = Coupon("z0002",1,2,datetime.date(2014,05,21),[0.040,0.037])
C8 = Coupon("w0002",1,2,datetime.date(2016,05,21),[0.035,0.037])
C3 = Coupon("s0003",1,3,datetime.date(2012,05,21),[0.042,0.044,0.045])
C6 = Coupon("z0003",1,3,datetime.date(2014,05,21),[0.035,0.034,0.032])
C9 = Coupon("w0003",1,3,datetime.date(2016,05,21),[0.035,0.034,0.032])

C10 = Coupon("w0004",2,1,datetime.date(2012,05,21),[0.047,0.048])
C11 = Coupon("w0005",2,1,datetime.date(2014,05,21),[0.046,0.047])
C12 = Coupon("w0006",2,1,datetime.date(2016,05,21),[0.042,0.044])
C13 = Coupon("z0004",2,2,datetime.date(2012,05,21),[0.045,0.044,0.047,0.045])
C14 = Coupon("z0005",2,2,datetime.date(2014,05,21),[0.042,0.043,0.043,0.044])
C15 = Coupon("z0006",2,2,datetime.date(2015,05,21),[0.043,0.042,0.039,0.042])
C16 = Coupon("s0004",2,2,datetime.date(2016,05,21),[0.039,0.042,0.042,0.042])
C17 = Coupon("s0005",2,3,datetime.date(2012,05,21),[0.045,0.046,0.045,0.045,0.046,0.046])
C18 = Coupon("s0006",2,3,datetime.date(2014,05,21),[0.042,0.043,0.043,0.044,0.042,0.043])
C19 = Coupon("s0007",2,3,datetime.date(2016,05,21),[0.035,0.034,0.039,0.041,0.038,0.042])

C20 = Coupon("w0007",3,1,datetime.date(2012,05,21),[0.047,0.048,0.049])
C21 = Coupon("w0008",3,1,datetime.date(2014,05,21),[0.046,0.047,0.047])
C22 = Coupon("w0009",3,1,datetime.date(2016,05,21),[0.043,0.044,0.043])
C23 = Coupon("z0007",3,2,datetime.date(2012,05,21),[0.047,0.045,0.045,0.044,0.047,0.045])
C24 = Coupon("z0008",3,2,datetime.date(2014,05,21),[0.042,0.044,0.043,0.044,0.043,0.044])
C25 = Coupon("z0009",3,2,datetime.date(2015,05,21),[0.043,0.042,0.042,0.039,0.043,0.042])
C26 = Coupon("s0008",3,2,datetime.date(2016,05,21),[0.039,0.041,0.043,0.042,0.042,0.042])
C27 = Coupon("s0009",3,3,datetime.date(2012,05,21),[0.045,0.046,0.045,0.045,0.046,0.045,0.045,0.046,0.046])
C28 = Coupon("s0010",3,3,datetime.date(2014,05,21),[0.042,0.043,0.044,0.043,0.044,0.043,0.044,0.042,0.043])
C29 = Coupon("s0011",3,3,datetime.date(2016,05,21),[0.035,0.034,0.037,0.041,0.039,0.040,0.041,0.038,0.042])

C30 = Coupon("w0010",5,1,datetime.date(2010,05,21),[0.052,0.049,0.048,0.046,0.047])
C31 = Coupon("w0011",5,1,datetime.date(2011,05,21),[0.048,0.046,0.047,0.046,0.046])
C32 = Coupon("w0012",5,1,datetime.date(2012,05,21),[0.047,0.046,0.046,0.047,0.044])
C33 = Coupon("z0010",5,2,datetime.date(2009,05,21),[0.052,0.051,0.049,0.048,0.048,0.047,0.046,0.045,0.047,0.046])
C34 = Coupon("z0011",5,2,datetime.date(2010,05,21),[0.048,0.049,0.046,0.047,0.047,0.048,0.046,0.047,0.046,0.047])
C35 = Coupon("z0012",5,2,datetime.date(2011,05,21),[0.047,0.046,0.046,0.047,0.046,0.045,0.047,0.048,0.044,0.044])
C36 = Coupon("s0012",5,2,datetime.date(2012,05,21),[0.047,0.045,0.047,0.046,0.045,0.046,0.044,0.045,0.044,0.043])
C37 = Coupon("s0013",5,3,datetime.date(2011,05,21),[0.047,0.046,0.048,0.046,0.045,0.047,0.046,0.045,0.047,0.047,0.048,0.046,0.044,0.045,0.044])
C38 = Coupon("s0014",5,3,datetime.date(2012,05,21),[0.048,0.049,0.047,0.046,0.047,0.045,0.047,0.048,0.046,0.046,0.047,0.045,0.046,0.047,0.045])
C39 = Coupon("s0015",5,3,datetime.date(2013,05,21),[0.047,0.047,0.046,0.046,0.043,0.045,0.046,0.045,0.046,0.047,0.046,0.045,0.044,0.046,0.045])

SCoupon =[C1,C2,C3,C4,C5,C6,C7,C8,C9,
          C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,
          C20,C21,C22,C23,C24,C25,C26,C27,C28,C29,
          C30,C31,C32,C33,C34,C35,C36,C37,C38,C39]


def get_yields(int yn,int n,float t,int f,ts):
    #ts,i,CC
    cdef int tmp, max_interval = 10000
    cdef list syield = [0.0135]      #第一个为活期利率
    for i in SCoupon:  #从数据库中查找最接近的债券年利率
        if((i.yn == yn )and(i.f == f)):  #债券年限和付息频率相同
            tmp = abs((ts - i.timeStart).days) 
            if(tmp<max_interval): #发行时间最接近
                max_interval=tmp
                CC = i
    syield.extend(i.get_yield(n))
    return syield
