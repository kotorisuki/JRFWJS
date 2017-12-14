# -*- coding: UTF-8 -*-
#画图程序

import matplotlib.pyplot as plt
from datetime import date
import time

def Draw(xl,yl,t,x,y):
    plt.figure(figsize=(8,4))#图片大小
    plt.plot(x, y, 'b*')
    plt.plot(x, y, 'b')
    plt.xlabel(xl)#横坐标名称
    plt.ylabel(yl)#纵坐标名称
    plt.title(t)#图像名称
    #plt.legend()
    plt.show()

def yieldTimeDraw(te,n,y,f): 
    #plt.figure(figsize=(8,4))#图片大小
    #plt.axis([-1,len(y),0,max(y)+0.01])
    #plt.plot(range(n), y, 'b*')
    #plt.plot(range(n), y, 'b')
    #plt.xlabel("Date")#横坐标名称
    #plt.ylabel("Yield")#纵坐标名称
    #plt.title("Time-Yield-Curve")#图像名称
    #plt.legend()
    #plt.show()
    fig = plt.figure(figsize=(8,4))#图片大小
    ax = fig.add_subplot(111)
    #xlabels = [(te-datetime.timedelta(days=int((n-i-1)*365/f))).strftime("%Y-%m-%d") for i in range(n)]
    xlabels = ["%04d-%02d-%02d"%(te.year - int(i/f),(te.month + (int(12/f)*(i%f)))%12,te.day) for i in range(n)] 
    ax.plot(range(n), y, 'b*')
    ax.plot(range(n), y, 'b')
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    ax.set_xlim(-1,len(y))
    ax.set_ylim(0,max(y)+0.01)
    plt.show()
