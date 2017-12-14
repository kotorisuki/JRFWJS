# -*- coding: utf-8 -*-
# 时间输入程序 不考虑闰年的情况 每年都是365天计算

import datetime
from datetime import date
import time

cdef list mm = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def time_input(char *timeStart, int yn, char *timeCurrent,int frequency):
    cdef int yearStart,yearEnd,yearCurrent,mouthSE,daySE,mouthCurrent,dayCurrent,year_rest,day,i,num_interest
    cdef double t
    #ts,te
    
    yearStart = int(timeStart[0:4])
    yearEnd = yearStart+yn
    yearCurrent = int(timeCurrent[0:4])
    mouthSE = int(timeStart[5:7])
    daySE = int(timeStart[8:10])
    mouthCurrent = int(timeCurrent[5:7])
    dayCurrent = int(timeCurrent[8:10])
    #计算债券的总年份
    #year = yearEnd-yearStart
    #计算剩余整年份
    if(mouthSE > mouthCurrent):
        year_rest = yearEnd - yearCurrent
    elif(mouthSE < mouthCurrent):
        year_rest = yearEnd - yearCurrent -1
    elif(daySE > dayCurrent): #月份相等时比较天数
        year_rest = yearEnd - yearCurrent 
    else:
        year_rest = yearEnd - yearCurrent -1
    #计算出售日到下次整年付息日的天数
    if(mouthSE > mouthCurrent):
        day = mm[mouthSE]- dayCurrent
        day += daySE
        i = mouthCurrent + 1
        while(i!= mouthSE):
            day += mm[i]
            i += 1 
    elif(mouthSE < mouthCurrent):
        day = mm[mouthCurrent]- daySE
        day += dayCurrent
        i = mouthSE + 1
        while(i!= mouthCurrent):
            day += mm[i]
            i += 1
        day = 365 - day
    elif(daySE > dayCurrent): #月份相等时比较天数
        day = daySE - dayCurrent
    else:
        day = 365 + daySE - dayCurrent
    #计算剩余整数付息间隔
    num_interest = year_rest*frequency + (day*frequency)/365 
    #计算距离下次付息日的天数/两次付息间隔
    t = float(day*frequency)/365 - (day*frequency)/365
    #表示发行时间
    ts=datetime.date(yearStart,mouthSE,daySE)
    te=date(yearEnd,mouthSE,daySE) 
    return num_interest,t,ts,te

    
