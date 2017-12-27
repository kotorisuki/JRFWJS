# -*- coding: utf-8 -*-
# 读取json文件中的数据，进行批量处理

import time
import datetime
from datetime import date
import json
from integration import integration
import unittest 
  
def data_input(filename,i):
    with open(filename) as json_file:
        data = json.load(json_file)
    pv,yy,dd,cc=integration(data[i]['coupon_rate'],
                            data[i]['face_value'],
                            data[i]['time_start'],
                            data[i]['year'],
                            data[i]['time_cur'],
                            data[i]['frequency'])
    re={'Pv':pv,'Yield':yy,'Duration':dd,'Convexity':cc}
    return re
    
    
class data_inputTest(unittest.TestCase): 
    def test_data0(self): 
        result0 = data_input('testdata.json',0)
        self.assertEquals({"Duration": 0.7109501186043212, "Pv": 6844.94742274849, "Convexity": 1.206930207901585, "Yield": 0.0135},result0)
    def test_data1(self): 
        result1 = data_input('testdata.json',1)
        self.assertEquals({"Duration": 1.6271985139440581, "Pv": 28526.71386534062, "Convexity": 3.25666320387966, "Yield": 0.04499229026754925},result1)
    def test_data2(self):
        result2 = data_input('testdata.json',2)
        self.assertEquals({"Duration": 3.128450476070277, "Pv": 85302.38345074847, "Convexity": 11.25997370525321, "Yield": 0.04502131345697369},result2)
    def test_data3(self):
        result3 = data_input('testdata.json',3)
        self.assertEquals({"Duration": 1.2649564403460927, "Pv": 64925.80014308274, "Convexity": 2.0324275760224726, "Yield": 0.044914690731194584},result3)
    def test_data4(self):
        result4 = data_input('testdata.json',4)
        self.assertEquals({"Duration": 2.3243916617111675, "Pv": 24426.77782790494, "Convexity": 7.768601040994157, "Yield": 0.04478945963236214},result4)
    def test_data5(self):
        result5 = data_input('testdata.json',5)
        self.assertEquals({"Duration": 2.187435847162574, "Pv": 30315.569429092444, "Convexity": 5.983187849788128, "Yield": 0.044911975194088516},result5)
    def test_data6(self):
        result6 = data_input('testdata.json',6)
        self.assertEquals({"Duration": 1.6144981592521783, "Pv": 84395.3501263557, "Convexity": 4.19224249456516, "Yield": 0.04436328408347934},result6)
    def test_data7(self):
        result7 = data_input('testdata.json',7)
        self.assertEquals({"Duration": 0.6433693088510586, "Pv": 71326.67443395947, "Convexity": 1.0487235829647386, "Yield": 0.0135},result7)
    def test_data8(self):
        result8 = data_input('testdata.json',8)
        self.assertEquals({"Duration": 0.3189814220353989, "Pv": 36299.65914583313, "Convexity": 0.4164816804457566, "Yield": 0.0135},result8)
    def test_data9(self):
        result9 = data_input('testdata.json',9)
        self.assertEquals({"Duration": 1.9651191877782221, "Pv": 61402.17838012832, "Convexity": 4.6231584868976885, "Yield": 0.04499502298987301},result9) 
                     
    
if __name__ == "__main__":
    unittest.main() 
