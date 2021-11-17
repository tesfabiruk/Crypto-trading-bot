import json
from binance.websockets import BinanceSocketManager
from binance.client import Client
import tulipy as ti
from talib import MA_Type
import json,talib,numpy
import websocket
import pprint
from binance import *
from binance.enums import *
from decimal import Decimal
from datetime import datetime
import datetime
import time
import sys
import pandas as pd
import openpyxl
from openpyxl import load_workbook


pup={}
pupf={}
dup=[]


"from market selling to market buying "

def findupp(df):
    n=0
    j=0
    i=0
    k=0
    r=0
    print(len(df))
    global pup
    while j<=(len(df)-2) and i<=(len(df)-2):
        "print(j)"
        startcomp=float(df.loc[j][[2]])+((float(df.loc[j][[2]])*2)/1000)
        startcomptime=pd.to_datetime(df.loc[j][[0]])
        compsttime=df.loc[j][[0]]
        compst=float(df.loc[j][[2]])+((float(df.loc[j][[2]])*2)/1000)
        th=len(df)-i-1
        if th>=5:
            z=1500
        else:
            z=th*60    
        chngt=0
        while chngt<z:
            comped=float(df.loc[i][[4]])-((float(df.loc[i][[4]])*3)/1000)
            compchng=comped-compst
            chngct=comped/1000
            if compchng>=chngct:
                compst=comped
                
                compeddtime=pd.to_datetime(df.loc[i][[1]])
                ttchng=compeddtime[1]-startcomptime[0]
                tttchng=ttchng/numpy.timedelta64(1, 's')
                
                r=i
                i=i+1
            else:
                i=i+1
            compedtime=pd.to_datetime(df.loc[i][[1]])
            tchng=compedtime[1]-startcomptime[0]
            ttchng=tchng/numpy.timedelta64(1,'s')
            '''            
            print(tchng)
            print('start',startcomptime[0])    
            print('end',compedtime[1])
            print(ttchng)
            '''
            chngt=int(ttchng)
            "print('chngt',chngt)"
        endcomp=compst
        if endcomp>startcomp:
            compchngg=endcomp-startcomp
            dup=[j,r,df.loc[j][[1]],df.loc[i][[0]],chngt,compchngg,float(df.loc[j][[2]]),float(df.loc[j][[3]]),float(df.loc[j][[4]]),float(df.loc[j][[5]]),float(df.loc[j][[6]]),float(df.loc[j][[7]]),float(df.loc[j][[8]]),float(df.loc[j][[9]])]
            pup[n]=dup
            n=n+1
        '''
        if len(pup)>4:
            print(pup)
            filterupp(pup)
        '''   
        j=j+1
        k=j
        i=k+1
    print("finshed")
    """
    print(pup[0])
    print(pup[1])
    path='FilteredCoinsData/THETA/Day_One.xlsx'
    dff= pd.DataFrame.from_dict(pup, orient ='index')
    dff.to_excel(path, sheet_name='data')
    print("sent")
    """
    filterupp(pup)
    pup={}
   
    
            
            
def filterupp(pup):
    global pupf
    i=0
    m=0
    q=1
    sr=0
    while m<len(pup):
        print(m)
        dc=0
        pcone=pup[m]
        rp=q+1
        i=0
        while i<(len(pup)-rp) and dc>=0:
            pctwo=pup[q]
            pupchng=pcone[6]*5/1000
            pctwotim=numpy.array(pctwo[2],dtype=numpy.datetime64)
            "print('pctim',pctwotim)"
            pconetim=numpy.array(pcone[3],dtype=numpy.datetime64)
            if pctwotim<=pconetim:
                if pctwo[4]>=pcone[4]:
                    if pctwo[5]>(pcone[5]+pupchng):    
                        pcone=pctwo
                        q=q+1
                    else:
                        q=q+1              
                elif pctwo[4]<=pcone[4]:
                    if pcone[5]>(pctwo[5]+pupchng):                        
                        q=q+1
                    else:
                        pcone=pctwo
                        q=q+1
                i=i+1
            else:
                dc=-1
                i=-1
                q=q+1
        if pcone[5]>(pcone[6]*5/1000):
            if pcone[0]>100:
                pupf[sr]=pcone
                sr=sr+1
            
        if dc==0:
            m=q+1
            q=q+2
        else:
            m=q
            q=q+1

    path='FilteredCoinsDataV4/THETA/Filtered.xlsx'
    dfft= pd.DataFrame.from_dict(pupf, orient ='index')
    dfft.to_excel(path, sheet_name='filtereddata')
    print("sent")
    pupf={}
                
         
    
pathk='CoinsDataV3/THETA/FiveMinData.xlsx'    
df = pd.read_excel (pathk, sheet_name='data')
findupp(df)
    

