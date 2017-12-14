# -*- coding: utf-8 -*-

from integration import integration1
from integration import integration2

pv,yy,dd,cc=integration1(0.042,100.0,"2010/11/11","2015/11/11","2012/12/1",2)
print "PV：%f" % pv
print "yield：%f" % yy
print "Duration：%f" % dd
print "Convexity：%f" % cc
print "============================"
	
ww2,yy2,dd2,cc2 =integration2(0.042,100.0,"2010/11/11","2015/11/11","2012/12/1",2,95.8)
print "yield：%f" % yy2
print "Duration：%f" % dd2
print "Convexity：%f" % cc2
print "评估参数：%.2f%%" % ww2
print "============================"
	
ww3,yy3,dd3,cc3=integration2(0.042,100.0,"2010/11/11","2015/11/11","2012/12/1",2,103.8)
print "yield：%f" % yy3
print "Duration：%f" % dd3
print "Convexity：%f" % cc3
print "评估参数：%.2f%%" % ww3
print "============================"