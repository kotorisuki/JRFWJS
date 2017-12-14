# -*- coding: utf-8 -*-
# 整合程序
# 作用：根据历史债券信息，计算债券在任意时刻的现值pv，其预计的综合年化收益率，久期和凸性

from time_input import time_input
from newton import gznewton
from newton import PVCalc
from newton import DurationCalc
from newton import ConvexityCalc
from syield import get_yields
from draw import Draw
from draw import yieldTimeDraw

#v :债券本金
#c :债券的利率
#timeStart:债券发行日期(格式：XXXX\XX\XX):\n")
#timeEnd:债券结算日期(格式：XXXX\XX\XX):\n")
#timeCurrent:债券出售日期(格式：XXXX\XX\XX)
#f :债券付息频率
#yn:债券的年限
#n:剩余整数付息间隔
#t：到下一次付息的间隔
#ts:债券发行日期 datetime类
#te:债券结算日期 date类

# 作用：根据历史债券信息，预估债券在任意时刻的现值pv，并计算综合年化收益率，久期和凸性
def integration1(c,v,timeStart,timeEnd,timeCurrent,f):
    yn,n,t,ts,te = time_input(timeStart, timeEnd, timeCurrent,f)
    syield=get_yields(yn,n,t,f,ts) #获得相似债券yield
    yieldTimeDraw(te,n,syield[1:n+1],f)#画出年利率随时间变化的图像
    #Draw("Date","Yield","Time-Yield-Curve",range(n+1),syield) #画出年利率随时间变化的图像
    #Draw("Date","Yield","Time-Yield-Curve",range(n),syield[1:n+1]) #画出年利率随时间变化的图像
    pv = PVCalc(c,v,t,n,f,syield) #计算现值pv
    yy=(gznewton(pv,c,v,n,t,1.1,0.000001,f)-1)*f #计算综合年利率
    dd=DurationCalc(c,v,f,t,n,yy,pv) #计算久期
    cc=ConvexityCalc(c,v,f,t,n,yy,pv) #计算凸性
    return pv,yy,dd,cc

# 作用：给定任意时刻的现值pv，计算其综合年化收益率，久期和凸性；并根据历史债券信息，评估是否应该购买这只债券
def integration2(c,v,timeStart,timeEnd,timeCurrent,f,pv):
    yn,n,t,ts,te = time_input(timeStart, timeEnd, timeCurrent,f)
    yy=(gznewton(pv,c,v,n,t,1.1,0.000001,f)-1)*f #计算综合年利率
    dd=DurationCalc(c,v,f,t,n,yy,pv) #计算久期
    cc=ConvexityCalc(c,v,f,t,n,yy,pv) #计算凸性
    syield=get_yields(yn,n,t,f,ts) #获得相似债券yield
    es_pv = PVCalc(c,v,t,n,f,syield) #预估现值pv.
    ww = ((es_pv - pv)*100)/pv #评估的参数
    return ww,yy,dd,cc


