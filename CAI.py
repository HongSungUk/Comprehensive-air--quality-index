# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:59:25 2021

@author: Hong Sung Uk
"""
import pandas as pd

I_LO = [0, 51, 101, 251]
I_HI = [50, 100, 250, 500]

data = {'sulfur_dioxide': [0, 0.02, 0.021, 0.05, 0.051, 0.15, 0.151, 1], 'carbon_monoxide': [0, 2, 2.1, 9, 9.1, 15, 15.1, 50], 
        'ozone': [0, 0.03, 0.031, 0.09, 0.091, 0.15, 0.151, 0.6], 'nitrogen_monoxide': [0, 0.03, 0.031, 0.06, 0.061, 0.2, 0.201, 2],
        'PM10': [0, 30, 31, 80, 81, 150, 151, 2000], 'PM2.5': [0, 15, 16, 35, 36, 75, 76, 1000]} #### 이 친구들이 PM10, PM2.5의 맥스 수치를 오기 해놓음, 그래서 수정함 (원본 : 600, 500 / 수정본 : 2000, 1000) ##
df=pd.DataFrame(data).T

# 아황산가스(ppm)
def sulfur_dioxide(pol):
    if df.loc['sulfur_dioxide'][0] <= pol <= df.loc['sulfur_dioxide'][1] :
        I_p = (I_HI[0]-I_LO[0])/(df.loc['sulfur_dioxide'][1]-df.loc['sulfur_dioxide'][0]) * (pol-df.loc['sulfur_dioxide'][0]) + I_LO[0]
    elif df.loc['sulfur_dioxide'][1] < pol <= df.loc['sulfur_dioxide'][3] :
        I_p = (I_HI[1]-I_LO[1])/(df.loc['sulfur_dioxide'][3]-df.loc['sulfur_dioxide'][2]) * (pol-df.loc['sulfur_dioxide'][2]) + I_LO[1]
    elif df.loc['sulfur_dioxide'][3] < pol <= df.loc['sulfur_dioxide'][5] :
        I_p = (I_HI[2]-I_LO[2])/(df.loc['sulfur_dioxide'][5]-df.loc['sulfur_dioxide'][4]) * (pol-df.loc['sulfur_dioxide'][4]) + I_LO[2]
    elif df.loc['sulfur_dioxide'][5] < pol <= df.loc['sulfur_dioxide'][7] :
        I_p = (I_HI[3]-I_LO[3])/(df.loc['sulfur_dioxide'][7]-df.loc['sulfur_dioxide'][6]) * (pol-df.loc['sulfur_dioxide'][6]) + I_LO[3]        
    return I_p

# 일산화탄소(ppm)
def carbon_monoxide(pol):
    if df.loc['carbon_monoxide'][0] <= pol <= df.loc['carbon_monoxide'][1] :
        I_p = (I_HI[0]-I_LO[0])/(df.loc['carbon_monoxide'][1]-df.loc['carbon_monoxide'][0]) * (pol-df.loc['carbon_monoxide'][0]) + I_LO[0]
    elif df.loc['carbon_monoxide'][1] < pol <= df.loc['carbon_monoxide'][3] :
        I_p = (I_HI[1]-I_LO[1])/(df.loc['carbon_monoxide'][3]-df.loc['carbon_monoxide'][2]) * (pol-df.loc['carbon_monoxide'][2]) + I_LO[1]
    elif df.loc['carbon_monoxide'][3] < pol <= df.loc['carbon_monoxide'][5] :
        I_p = (I_HI[2]-I_LO[2])/(df.loc['carbon_monoxide'][5]-df.loc['carbon_monoxide'][4]) * (pol-df.loc['carbon_monoxide'][4]) + I_LO[2]
    elif df.loc['carbon_monoxide'][5] < pol <= df.loc['carbon_monoxide'][7] :
        I_p = (I_HI[3]-I_LO[3])/(df.loc['carbon_monoxide'][7]-df.loc['carbon_monoxide'][6]) * (pol-df.loc['carbon_monoxide'][6]) + I_LO[3]        
    return I_p

# 오존(ppm)
def ozone(pol):
    if df.loc['ozone'][0] <= pol <= df.loc['ozone'][1] :
        I_p = (I_HI[0]-I_LO[0])/(df.loc['ozone'][1]-df.loc['ozone'][0]) * (pol-df.loc['ozone'][0]) + I_LO[0]
    elif df.loc['ozone'][1] < pol <= df.loc['ozone'][3] :
        I_p = (I_HI[1]-I_LO[1])/(df.loc['ozone'][3]-df.loc['ozone'][2]) * (pol-df.loc['ozone'][2]) + I_LO[1]
    elif df.loc['ozone'][3] < pol <= df.loc['ozone'][5] :
        I_p = (I_HI[2]-I_LO[2])/(df.loc['ozone'][5]-df.loc['ozone'][4]) * (pol-df.loc['ozone'][4]) + I_LO[2]
    elif df.loc['ozone'][5] < pol <= df.loc['ozone'][7] :
        I_p = (I_HI[3]-I_LO[3])/(df.loc['ozone'][7]-df.loc['ozone'][6]) * (pol-df.loc['ozone'][6]) + I_LO[3]        
    return I_p

# 이산화질소(ppm)    
def nitrogen_monoxide(pol):
    if df.loc['nitrogen_monoxide'][0] <= pol <= df.loc['nitrogen_monoxide'][1] :
        I_p = (I_HI[0]-I_LO[0])/(df.loc['nitrogen_monoxide'][1]-df.loc['nitrogen_monoxide'][0]) * (pol-df.loc['nitrogen_monoxide'][0]) + I_LO[0]
    elif df.loc['nitrogen_monoxide'][2] <= pol <= df.loc['nitrogen_monoxide'][3] :
        I_p = (I_HI[1]-I_LO[1])/(df.loc['nitrogen_monoxide'][3]-df.loc['nitrogen_monoxide'][2]) * (pol-df.loc['nitrogen_monoxide'][2]) + I_LO[1]
    elif df.loc['nitrogen_monoxide'][4] <= pol <= df.loc['nitrogen_monoxide'][5] :
        I_p = (I_HI[2]-I_LO[2])/(df.loc['nitrogen_monoxide'][5]-df.loc['nitrogen_monoxide'][4]) * (pol-df.loc['nitrogen_monoxide'][4]) + I_LO[2]
    elif df.loc['nitrogen_monoxide'][6] <= pol <= df.loc['nitrogen_monoxide'][7] :
        I_p = (I_HI[3]-I_LO[3])/(df.loc['nitrogen_monoxide'][7]-df.loc['nitrogen_monoxide'][6]) * (pol-df.loc['nitrogen_monoxide'][6]) + I_LO[3]        
    return I_p

# 초미세먼지 PM_10(ug/m^3)   
def PM10(pol):
    if df.loc['PM10'][0] <= pol <= df.loc['PM10'][1] :
        I_p = (I_HI[0]-I_LO[0])/(df.loc['PM10'][1]-df.loc['PM10'][0]) * (pol-df.loc['PM10'][0]) + I_LO[0]
    elif df.loc['PM10'][2] <= pol <= df.loc['PM10'][3] :
        I_p = (I_HI[1]-I_LO[1])/(df.loc['PM10'][3]-df.loc['PM10'][2]) * (pol-df.loc['PM10'][2]) + I_LO[1]
    elif df.loc['PM10'][4] <= pol <= df.loc['PM10'][5] :
        I_p = (I_HI[2]-I_LO[2])/(df.loc['PM10'][5]-df.loc['PM10'][4]) * (pol-df.loc['PM10'][4]) + I_LO[2]
    elif df.loc['PM10'][6] <= pol <= df.loc['PM10'][7] :
        I_p = (I_HI[3]-I_LO[3])/(df.loc['PM10'][7]-df.loc['PM10'][6]) * (pol-df.loc['PM10'][6]) + I_LO[3]        
    return I_p

# 초미세먼지 PM_2.5(ug/m^3)   
def PM25(pol):
    if df.loc['PM2.5'][0] <= pol <= df.loc['PM2.5'][1] :
        I_p = (I_HI[0]-I_LO[0])/(df.loc['PM2.5'][1]-df.loc['PM2.5'][0]) * (pol-df.loc['PM2.5'][0]) + I_LO[0]
    elif df.loc['PM2.5'][2] <= pol <= df.loc['PM2.5'][3] :
        I_p = (I_HI[1]-I_LO[1])/(df.loc['PM2.5'][3]-df.loc['PM2.5'][2]) * (pol-df.loc['PM2.5'][2]) + I_LO[1]
    elif df.loc['PM2.5'][4] <= pol <= df.loc['PM2.5'][5] :
        I_p = (I_HI[2]-I_LO[2])/(df.loc['PM2.5'][5]-df.loc['PM2.5'][4]) * (pol-df.loc['PM2.5'][4]) + I_LO[2]
    elif df.loc['PM2.5'][6] <= pol <= df.loc['PM2.5'][7] :
        I_p = (I_HI[3]-I_LO[3])/(df.loc['PM2.5'][7]-df.loc['PM2.5'][6]) * (pol-df.loc['PM2.5'][6]) + I_LO[3]        
    return I_p

# 미세먼지 24시간 예측이동 평균 (열단위로 입력하면 됨)
def PM_10_avg(pm_raw):
    pm_raw = pm_raw.replace(0,1)
    pm_raw = pd.DataFrame(pm_raw)
    pm_raw_12avg = pm_raw.rolling(window = 12, min_periods = 1, center = False).mean()    
    
    pm_raw2 = pd.DataFrame([])
    for i in range(len(pm_raw)):
        if pm_raw.iloc[i,0] < 70:
            pm_raw2 = pm_raw2.append(pm_raw.iloc[i])
        elif pm_raw.iloc[i,0] >= 70 and (pm_raw.iloc[i,0]/pm_raw_12avg.loc[i] < 0.9)[0] or (pm_raw.iloc[i,0]/pm_raw_12avg.loc[i] > 1.7)[0]:
            pm_raw2 =pm_raw2.append(pm_raw.iloc[i])
        elif pm_raw.iloc[i,0] >= 70 and (1.7>=pm_raw.iloc[i,0]/pm_raw_12avg.iloc[i,0] >= 0.9):
            pm_raw2 = pm_raw2.append(0.75*pm_raw.iloc[i])
            
    pm_raw_4avg = pm_raw2.rolling(window = 4, min_periods = 1, center = False).mean()        
    
    result = round((pm_raw_4avg*12+pm_raw_12avg*12)/24)
    return result

def PM_25_avg(pm_raw):
    pm_raw = pm_raw.replace(0,1)
    pm_raw = pd.DataFrame(pm_raw)
    pm_raw_12avg = pm_raw.rolling(window = 12, min_periods = 1, center = False).mean()    
    
    pm_raw2 = pd.DataFrame([])
    for i in range(len(pm_raw)):
        if pm_raw.iloc[i,0] < 30:
            pm_raw2 = pm_raw2.append(pm_raw.iloc[i])
        elif pm_raw.iloc[i,0] >= 30 and (pm_raw.iloc[i,0]/pm_raw_12avg.loc[i] < 0.9)[0] or (pm_raw.iloc[i,0]/pm_raw_12avg.loc[i] > 1.7)[0]:
            pm_raw2 =pm_raw2.append(pm_raw.iloc[i])
        elif pm_raw.iloc[i,0] >= 30 and (1.7>=pm_raw.iloc[i,0]/pm_raw_12avg.iloc[i,0] >= 0.9):
            pm_raw2 = pm_raw2.append(0.75*pm_raw.iloc[i])
            
    pm_raw_4avg = pm_raw2.rolling(window = 4, min_periods = 1, center = False).mean()        
            
    result = round((pm_raw_4avg*12+pm_raw_12avg*12)/24)
    return result

# 통합 CAI (Comprehensive air-quality index)
def CAI(sd, cm, oz, nm, P10, P25):
    sulfur_dioxide_I = sulfur_dioxide(sd)
    carbon_monoxide_I = carbon_monoxide(cm)
    ozone_I = ozone(oz)
    nitrogen_monoxide_I = nitrogen_monoxide(nm)
    PM10_I = PM10(P10)
    PM25_I = PM25(P25)
    
    CAI_list = [sulfur_dioxide_I, carbon_monoxide_I, ozone_I, nitrogen_monoxide_I, PM10_I, PM25_I]
    
    Bad_CAT_list = [sulfur_dioxide_I >= 101, carbon_monoxide_I >= 101, ozone_I >= 101, nitrogen_monoxide_I >= 101, PM10_I >= 101, PM25_I >= 101]
    
    
    if Bad_CAT_list.count(True) == 2:
        CAI = max(CAI_list) + 50
    elif Bad_CAT_list.count(True) >= 3:
        CAI = max(CAI_list) + 75
    else : 
        CAI = max(CAI_list)
    
    # 중요 오염물질 계산
    CAI_imp = df.index[CAI_list.index(max(CAI_list))]  
    CAI = round(CAI)
    return CAI, CAI_list, CAI_imp

## 예시 ##
raw_data = pd.read_csv('data\\2018_2019cnu.csv')
raw_data = raw_data.interpolate(method='values')
raw_data['avg_P10'] = PM_10_avg(raw_data['PM10'])
raw_data['avg_P25'] = PM_10_avg(raw_data['PM25'])

raw_data['CAI'] = raw_data[['SO2', 'CO', 'O3', 'NO2', 'avg_P10', 'avg_P25']].apply(lambda x : CAI(x[0], x[1], x[2], x[3], x[4], x[5])[0], axis=1)
raw_data['CAI_value'] = raw_data[['SO2', 'CO', 'O3', 'NO2', 'avg_P10', 'avg_P25']].apply(lambda x : CAI(x[0], x[1], x[2], x[3], x[4], x[5])[1], axis=1)
raw_data['CAI_main_factor'] = raw_data[['SO2', 'CO', 'O3', 'NO2', 'avg_P10', 'avg_P25']].apply(lambda x : CAI(x[0], x[1], x[2], x[3], x[4], x[5])[2], axis=1)
raw_data.to_csv('2018_2019cnu_re.csv', index=False)