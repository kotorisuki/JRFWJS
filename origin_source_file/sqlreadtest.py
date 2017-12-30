# -*- coding: utf-8 -*-

#v :债券本金
#c :债券的利率
#yn:债券的年限
#timeStart/ts:债券发行日期
#f :债券付息频率
#n :给定债券剩下的付息次数 
#t :给定债券的到期时间
#syield ：与给定债券相似的债券的到期收益率

#找到与给定债券相似的债券的到期收益率

import datetime
import mysql.connector                 
import time




config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'database': 'test',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
cursor = cnn.cursor()
try:
    dt=datetime.date(1997,10,7)
    delta = datetime.timedelta(days=10)
    st=time.time()
    dt1=(dt-delta).strftime('%Y-%m-%d')
    dt2=(dt+delta).strftime('%Y-%m-%d')
    for i in range(1,501):
        sql_query = "select Liscd from betterinfo where Liscd=1 union all select Liscd from betterinfo where Liscd=2 "\
            "union all select Liscd from betterinfo where Liscd=3 "\
            "union all select Liscd from betterinfo where Liscd=4 "\
            "union all select Liscd from betterinfo where Liscd=5 "\
            "union all select Liscd from betterinfo where Liscd=6 "\
            "union all select Liscd from betterinfo where Liscd=7 "\
            "union all select Liscd from betterinfo where Liscd=8 "\
            "union all select Liscd from betterinfo where Liscd=9 "\
            "union all select Liscd from betterinfo where Liscd=10 "\
            "union all select Liscd from betterinfo where Liscd=11 "\
            "union all select Liscd from betterinfo where Liscd=12 "\
            "union all select Liscd from betterinfo where Liscd=13 "\
            "union all select Liscd from betterinfo where Liscd=14 "\
            "union all select Liscd from betterinfo where Liscd=15 "\
            "union all select Liscd from betterinfo where Liscd=16 "\
            "union all select Liscd from betterinfo where Liscd=17 "\
            "union all select Liscd from betterinfo where Liscd=18 "\
            "union all select Liscd from betterinfo where Liscd=19 "\
            "union all select Liscd from betterinfo where Liscd=10 "\
            "union all select Liscd from betterinfo where Liscd=11 "\
            "union all select Liscd from betterinfo where Liscd=12 "\
            "union all select Liscd from betterinfo where Liscd=13 "\
            "union all select Liscd from betterinfo where Liscd=14 "\
            "union all select Liscd from betterinfo where Liscd=15 "\
            "union all select Liscd from betterinfo where Liscd=16 "\
            "union all select Liscd from betterinfo where Liscd=17 "\
            "union all select Liscd from betterinfo where Liscd=18 "\
            "union all select Liscd from betterinfo where Liscd=19 "\
            "union all select Liscd from betterinfo where Liscd=10 "\
            "union all select Liscd from betterinfo where Liscd=11 "\
            "union all select Liscd from betterinfo where Liscd=12 "\
            "union all select Liscd from betterinfo where Liscd=13 "\
            "union all select Liscd from betterinfo where Liscd=14 "\
            "union all select Liscd from betterinfo where Liscd=15 "\
            "union all select Liscd from betterinfo where Liscd=16 "\
            "union all select Liscd from betterinfo where Liscd=17 "\
            "union all select Liscd from betterinfo where Liscd=18 "\
            "union all select Liscd from betterinfo where Liscd=19 "\
            "union all select Liscd from betterinfo where Liscd=20;"
        cursor.execute(sql_query)
        for Liscd in cursor:
            #print (Liscd, float(Yldtomtu))
            a=1
        if(i%50==0):
            print "do ",i," sql operation time:",time.time()-st
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()