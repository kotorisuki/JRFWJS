# -*- coding: utf-8 -*-
# wc:估计的精度
#c:利率
#v:本金
#n:剩余付息次数
#t:到下一次付息的时间/两次付息间隔
#p0:债券的当前价格
#y0:估计的到期收益率
#f:付息频率
#使用牛顿迭代法，估计出目标债券的到期收益率

def gznewton(p0,c,v,n,t,y0,wc,f):
    done = 0
    y = y0
    while (done==0):
        fy=p0*(y**(n+t))-(c*v/f)-v
        fy1=p0*(n+t)*(y**(n+t-1))
        for i in range(n):
            fy=fy-(c*v/f)*(y**(n-i))
            fy1=fy1-(c*v/f)*(n-i)*(y**(n-i-1))
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


def PVCalc(c,v,t,n,f,y):
    if((n+1)!=len(y)):
        print "输入格式不对，请重新计算！"
    else:
        pv = 0
        for i in range(0,n+1):
            pv += (c*v/f)/((1 + (y[i]/f))**(i+t))
        pv +=  v/((1+(y[n]/f))**(n+t))
        return pv
    
def DurationCalc(c,v,f,t,n,y,pv):
    dur = 0
    for i in range(0,n+1):
        dur += (((c*v)/(f*f))*(i+t))/((1 + (y/f))**(i+t+1))
    dur +=  ((v/f)*(n+t))/((1+(y/f))**(n+t+1))
    return dur/pv

def ConvexityCalc(c,v,f,t,n,y,pv):
    con = 0
    for i in range(0,n+1):
        con += (((c*v)/(f*f*f))*(i+t)*(i+t+1))/((1 + (y/f))**(i+t+2))
    con +=  ((v/(f*f))*(n+t)*(n+t+1))/((1+(y/f))**(n+t+2))
    return con/pv

