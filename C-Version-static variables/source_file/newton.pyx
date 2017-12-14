# -*- coding: utf-8 -*-
# wc:精度
#c:coupon rate
#v:本金
#n:剩余整数付息
#t:到下一次付息的时间/两次付息间隔
#p0:现在的价格
#y0:是猜测值

from libc.math cimport pow as cpow

cdef double _gznewton(double p0,double c,double v,int n,double t,double y0,double wc,int f):
    cdef int i, done = 0
    cdef double fy, fy1, Newton, y = y0
    while (done==0):
        fy=p0*(y**(n+t))-(c*v/f)-v
        fy1=p0*(n+t)*(y**(n+t-1))
        for i in range(n):
            fy=fy-(c*v/f)*cpow(y,n-i)
            fy1=fy1-(c*v/f)*(n-i)*cpow(y,n-i-1)
        if fy1!=0:
            Newton = y -(fy/fy1)
            if (abs(Newton-y)<wc):#估计值小于精度
                done = 1
            elif (abs(Newton-y0)>0.2):
                print Newton
                print "请重新估计" #防止进入无限循环
                break
            else:
                y = Newton
        else:
            done=1
    return Newton

def gznewton(double p0,double c,double v,int n,double t,double y0,double wc,int f):
    return _gznewton(p0,c,v,n,t,y0,wc,f)


cdef double _PVCalc(double c,double v,double t,int n,int f,list y):
    cdef int i
    cdef double pv
    if((n+1)!=len(y)):
        print "输入格式不对，请重新计算！"
    else:
        pv = 0
        for i in range(0,n+1):
            pv += (c*v/f)/cpow(1 + (y[i]/f),i+t)
        pv +=  v/cpow(1+(y[n]/f),n+t)
        return pv
    
def PVCalc(double c,double v,double t,int n,int f,list y):
    return _PVCalc(c,v,t,n,f,y)
    
cdef double _DurationCalc(double c,double v,int f,double t,int n,double y,double pv):
    cdef double dur = 0
    cdef int i
    for i in range(0,n+1):
        dur += (((c*v)/(f*f))*(i+t))/cpow(1 + (y/f),i+t+1)
    dur +=  ((v/f)*(n+t))/cpow(1 + (y/f),n+t+1)
    return dur/pv

def DurationCalc(double c,double v,int f,double t,int n,double y,double pv):
    return _DurationCalc(c,v,f,t,n,y,pv)

cdef double _ConvexityCalc(double c,double v,int f,double t,int n,double y,double pv):
    cdef double con = 0
    cdef int i
    for i in range(0,n+1):
        con += (((c*v)/(f*f*f))*(i+t)*(i+t+1))/cpow(1 + (y/f),i+t+2)
    con +=  ((v/(f*f))*(n+t)*(n+t+1))/cpow(1 + (y/f),n+t+2)
    return con/pv

def ConvexityCalc(double c,double v,int f,double t,int n,double y,double pv):
    return _ConvexityCalc(c,v,f,t,n,y,pv)

