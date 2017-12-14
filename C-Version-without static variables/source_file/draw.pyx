# -*- coding: UTF-8 -*-
#画图程序

import matplotlib.pyplot as plt

def Draw(xl,yl,t,x,y):
    plt.figure(figsize=(8,4))#图片大小
    plt.plot(x, y, 'b*')
    plt.plot(x, y, 'b')
    plt.xlabel(xl)#横坐标名称
    plt.ylabel(yl)#纵坐标名称
    plt.title(t)#图像名称
    #plt.legend()
    plt.show()

def yieldTimeDrawL(te,n,y,f): 
    #plt.figure(figsize=(8,4))#图片大小
    #plt.axis([-1,len(y),0,max(y)+0.01])
    #plt.plot(range(n), y, 'b*')
    #plt.plot(range(n), y, 'b')
    #plt.xlabel("Date")#横坐标名称
    #plt.ylabel("Yield")#纵坐标名称
    #plt.title("Time-Yield-Curve")#图像名称
    #plt.legend()
    #plt.show()
    if(len(y)!=0):
        fig = plt.figure(figsize=(8,4))#图片大小
        ax = fig.add_subplot(111)
        xlabels = []
        for i in range(n):
            x_y = te.year - int((n-i)/f)
            if(((120 + te.month - (int(12/f)*(n-i)))%12)!=0):
                x_m = (120 + te.month - (int(12/f)*(n-i)))%12
            else:
                x_m = 12
            x_d = te.day
            xlabels.append("%04d-%02d-%02d" % (x_y,x_m,x_d))
        ax.plot(range(n), y, 'b*')
        ax.plot(range(n), y, 'b')
        ax.set_xticks(range(len(xlabels)))
        ax.set_xticklabels(xlabels)
        ax.set_xlim(-1,len(y))
        ax.set_ylim(0,max(y)+0.01)
        plt.show()
        
def yieldTimeDraw(te,n,y,f):
    if(len(y)!=0):
        plt.figure(figsize=(8,4))#图片大小
        plt.axis([-1,len(y),0,max(y)+0.01])
        plt.plot(range(n), y, 'b*')
        plt.plot(range(n), y, 'b')
        plt.xlabel("Date")#横坐标名称
        plt.ylabel("Yield")#纵坐标名称
        plt.title("Time-Yield-Curve")#图像名称
        #plt.legend()
        plt.show()
