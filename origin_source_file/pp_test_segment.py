# -*- coding: utf-8 -*-
#直接运行百万数据集的测试用例，所需的时间。

import time
from datetime import date
import pp
import json
import datetime
import matplotlib.pyplot as plt


mm = (0,31,28,31,30,31,30,31,31,30,31,30,31)
def time_input(timeStart, yn, timeCurrent,frequency,mm):
    
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
    te=datetime.date(yearEnd,mouthSE,daySE) 
    return num_interest,t,ts,te

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


class Coupon:
    def __init__(self,cid,yn,f,timeStart,yields):
        self.cid = cid
        self.yn = yn
        self.f  = f
        self.timeStart = timeStart
        self.yields = yields
    def get_yield(self,n):
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

def get_yields(yn,n,t,f,ts,SCoupon):
    syield = [0.0135]      #第一个为活期利率
    max_interval = 10000

    for i in SCoupon:  #从数据库中查找最接近的债券年利率
        if((i.yn == yn )and(i.f==f)):  #债券年限和付息频率相同
            tmp = abs((ts - i.timeStart).days) 
            if(tmp<max_interval): #发行时间最接近
                max_interval=tmp
                CC = i
    syield.extend(i.get_yield(n))
    return syield




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
        
def yieldTimeDraw(n,y):
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

# 作用：根据历史债券信息，预估债券在任意时刻的现值pv，并计算综合年化收益率，久期和凸性
def integration(c,v,timeStart,yn,timeCurrent,f,SCoupon,mm):
    n,t,ts,te = time_input(timeStart, yn, timeCurrent,f,mm)
    syield=get_yields(yn,n,t,f,ts,SCoupon) #获得相似债券yield
    #yieldTimeDraw(te,n,syield[1:n+1],f)#画出年利率随时间变化的图像
    #Draw("Date","Yield","Time-Yield-Curve",range(n+1),syield) #画出年利率随时间变化的图像
    #Draw("Date","Yield","Time-Yield-Curve",range(n),syield[1:n+1]) #画出年利率随时间变化的图像
    pv = PVCalc(c,v,t,n,f,syield) #计算现值pv
    if(pv):
        if(n!=0):
            yy=(gznewton(pv,c,v,n,t,1.1,0.000001,f)-1)*f #计算综合年利率
        else:
            yy=syield[0]
        dd=DurationCalc(c,v,f,t,n,yy,pv) #计算久期
        cc=ConvexityCalc(c,v,f,t,n,yy,pv) #计算凸性
        return pv,yy,dd,cc
    else:
        return 0,0,0,0
    return 0,0,0,0

def data_input(filename,job_server):
    with open(filename) as json_file:
        data = json.load(json_file)
    cnt = len(data)
    print 'readfile:',filename,',length:',cnt
    global SCoupon,mm
    batch_size=40000
    result=[]
    num_p=cnt/batch_size
    jobs=[]
    st=time.time()
    for i in range(num_p):
        jobs.append(job_server.submit(batch_input, (data[batch_size*i:batch_size*(i+1)],SCoupon,mm,), (integration,), (),globals=globals()))
    jobs.append(job_server.submit(batch_input, (data[batch_size*num_p:cnt],SCoupon,mm,), (integration,), (),globals=globals()))
    return jobs
    for job in jobs:
        part=job()
        result+=part
        print "Time elapsed: ", time.time() - st, "s"
    with open('result.json', 'w') as json_file:
            json_file.write(json.dumps(result))
def batch_input(data,SCoupon,mm):
    result=[]
    for data_item in data:
        pv,yy,dd,cc=integration(data_item['coupon_rate'],
                                data_item['face_value'],
                                data_item['time_start'],
                                data_item['year'],
                                data_item['time_cur'],
                                data_item['frequency'],
                                SCoupon,mm)
        re={'Pv':pv,'Yield':yy,'Duration':dd,'Convexity':cc}
        result.append(re)
    return result

def find_d(id,dt,cnn):
 
    cursor = cnn.cursor()
    try:
        
        delta = datetime.timedelta(days=10)
        dt1=(dt-delta).strftime('%Y-%m-%d')
        dt2=(dt+delta).strftime('%Y-%m-%d')

        for i in range(1,1000):
            if(i%100==0):
                print i
            cursor.execute(sql_query)
            for Liscd in cursor:
                a=Liscd
            #print (Liscd, float(Yldtomtu))
    except mysql.connector.Error as e:
        print('query error!{}'.format(e))
    finally:
        cursor.close()

cluster=1
if (cluster==1):
    #ppservers = ("192.168.1.106:35000","192.168.1.104:35000",)  
    ppservers = ("192.168.1.104:35000",)  
    job_server = pp.Server(ncpus=12,ppservers=ppservers, secret="123456")  
    '''ppservers = ("*",)  
    job_server = pp.Server(6,ppservers=ppservers)'''
else:
    ppservers=()
    job_server = pp.Server(ppservers=ppservers)
#ppservers=("*",)

#ppservers = ("10.0.0.1",)

'''if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    print 'cluster'
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers'''

job_server.print_stats()
if __name__ == '__main__':
   
    print "Starting pp with", job_server.get_ncpus(), "workers"


    start_time=time.time()


    list=[1,2,3,4,5,6]*3
    all_jobs=[]
    for i in list:
        all_jobs+=data_input('..\\MillionData\\mdata'+str(i)+'.json',job_server)
    
    # Retrieves the result calculated by job1
    # The value of job1() is the same as sum_primes(100)
    # If the job has not been finished yet, execution will wait here until result is available
    print "Time elapsed: ", time.time() - start_time, "s"
    for job in all_jobs:
        part=job()
    job_server.print_stats()
    print "Time elapsed: ", time.time() - start_time, "s"