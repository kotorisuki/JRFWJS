#连接SQL数据库
import mysql.connector  
import pp

count=0

config={'host':'127.0.0.1',#默认127.0.0.1
        'user':'root',
        'password':'root',
        'port':3306 ,#默认即为3306
        'database':'test',
        'charset':'utf8'#默认即为utf8
        }
try:
  cnn=mysql.connector.connect(**config)
except mysql.connector.Error as e:
  print('connect fails!{}'.format(e))
cursor = cnn.cursor()
try:
    string="Liscd	Trddt	Pretrdd	Opnprc	Clsprc	Dhiprc	Dloprc	Dlbndtrd	Dnvaltrd	Clsyield	Duration	Adjdurat	Convexity	Perchge	Accrtn	Idexvolt	Accurintrs	Mdirtyprc	Yeartomatu	Accuridt	Yldtomtu"
    print string.split('\t')
    sql_query = "create table bnddt("
    for i in string.split('\t'):
        if(i=="Liscd"):
            sql_query=sql_query+i+" varchar(10) NOT NULL,"
        else:
            sql_query=sql_query+i+" varchar(100) DEFAULT NULL,"
    sql_query=sql_query+"PRIMARY KEY (Liscd));"
    print sql_query
    cursor.execute(sql_query)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cnn.close()
cursor.close()

'''
file = open('BND_Bndinfo.txt')
line=file.readline()
mm=0;
while line:

    count=count+1
    if(count>3):
        if(mm<len(line.split('\t')[0])):
            mm=len(line.split('\t')[0]);
    line=file.readline()
file.close()
print mm
print count'''