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
from datetime import datetime

openstheta=[]
closestheta=[]
highstheta=[]
lowstheta=[]
volumestheta=[]

hropenstheta=[]
hrclosestheta=[]
hrhighstheta=[]
hrlowstheta=[]
hrvolumestheta=[]

thetadataa={}
hthetadataa={}

RSI_PERIODD=14

x="2t4nsqpgUwk2jL3zD2n6pcndUy61tlhpmLNS9iavoaAcPatjVYzftaJFJF9o8NYR"
y="mZPpl3G4N5xjVuvZCzSdDm3oJaJBAjcRdbOs5bFfpoJ3LHW24tXL1tvveNH6IiZY"
client = Client(x,y)

def dataclct(str,opens,closes,highs,lows,volumes,dataa,hropens,hrcloses,hrhighs,hrlows,hrvolumes,hrdataa):
    
        TRADE_SYMBOL=str

        cmplow=[]
        cmphigh=[]
        cmpvol=[] 
        opmodf=0                
        global openstheta
        global closestheta
        global highstheta
        global lowstheta
        global volumestheta

        global hropenstheta
        global hrclosestheta
        global hrhighstheta
        global hrlowstheta
        global hrvolumestheta
        
        h=client.get_historical_klines(symbol=TRADE_SYMBOL,interval='5m',start_str='07/01/2020@10:00am',end_str=None)
        cnt=0
        hcnt=0
        for kline in h:
            
            'pprint.pprint(kline)'
            
            opens.append(float(kline[1]))
            closes.append(float(kline[4]))
            highs.append(float(kline[2]))
            lows.append(float(kline[3]))
            volumes.append(float(kline[5]))
            
            if len(closes)==1:
                    hps=float(kline[0])/1000
                    hopen=float(kline[1])
            hpd=float(kline[6])/1000

            cmplow.append(float(kline[3]))
            cmphigh.append(float(kline[2]))
            cmpvol.append(float(kline[5]))

            tcg=hpd-hps

            if opmodf==1:
                    opmodf=0
                    hopen=float(kline[1])
                    
            if tcg>=3500:
                    hrsttime=hps
                    hredtime=hpd
                    'print(tcg)'  
                    hclose=float(kline[4])
                    
                    for cl in range(len(cmplow)):
                            if cl==0:
                                    lww=cmplow[0]
                            else:
                                    if cmplow[cl]<lww:
                                            lww=cmplow[cl]
                    hlow=lww

                    for ch in range(len(cmphigh)):
                            if ch==0:
                                    hhh=cmphigh[0]
                            else:
                                    if cmphigh[cl]>hhh:
                                            hhh=cmphigh[ch]
                    hhigh=hhh

                    hvol=numpy.sum(cmpvol)
                                        
                    hropens.append(hopen)
                    hrcloses.append(hclose)
                    hrhighs.append(hhigh)
                    hrlows.append(hlow)
                    hrvolumes.append(hvol)

                    hhopen=hopen
                    hhclose=hclose
                    
                    'hopen=float(kline[1])'
                    opmodf=1
                    
                    cmplow=[]
                    cmphigh=[]
                    cmpvol=[]

                    hrsttime=datetime.fromtimestamp(hps)
                    hredtime=datetime.fromtimestamp(hpd)
                    
                    hps=float(kline[6])/1000
            
            if len(closes)>400:

                np_open = numpy.array(opens)
                np_close = numpy.array(closes)
                np_high = numpy.array(highs)
                np_low = numpy.array(lows)
                np_volume = numpy.array(volumes)

                rsii = ti.rsi(np_close,RSI_PERIODD)
                rsinp = rsii
                rsinp = rsinp[numpy.logical_not(numpy.isnan(rsinp))]
                fastk, fastd = ti.stoch(rsinp, rsinp, rsinp, 14, 3, 3)
                
                rsi = ti.rsi(np_close,6)
                wmasv = ti.wma(np_close,7)
                wmatf = ti.wma(np_close,25)

                mfi= ti.mfi(np_high,np_low,np_close,np_volume,14)

                mdi= talib.MINUS_DI(np_high,np_low,np_close,14)
                mdm= talib.MINUS_DM(np_high,np_low,14)

                htprd=talib.HT_DCPERIOD(np_close)

                var=talib.VAR(np_close, timeperiod=14, nbdev=1)

                stdev=talib.BETA(np_high,np_low,timeperiod=14)
                
                roc=(((closes[-1]+1)/(closes[-2]+1))-1)*100
                tps=float(kline[0])/1000
                tpd=float(kline[6])/1000
                sttime=datetime.fromtimestamp(tps)
                edtime=datetime.fromtimestamp(tpd)
                dataa[cnt]=[sttime,edtime,float(kline[1]),float(kline[4]),float(kline[2]),float(kline[3]),rsi[-1],fastk[-1],fastd[-1],wmasv[-1],wmatf[-1],roc,float(kline[5]),mfi[-1],mdi[-1],mdm[-1],var[-1],stdev[-1],hcnt]
                'toexcel(dataa,"THETABTC")'
                cnt=cnt+1

                'hour data'
                if tcg>=3500:
                        np_open = numpy.array(hropens)
                        np_close = numpy.array(hrcloses)
                        np_high = numpy.array(hrhighs)
                        np_low = numpy.array(hrlows)
                        np_volume = numpy.array(hrvolumes)

                        rsii=[]
                        rsinp=[]
                        fastk=[]
                        fastd=[]

                        rsii = ti.rsi(np_close,RSI_PERIODD)
                        rsinp = rsii
                        rsinp = rsinp[numpy.logical_not(numpy.isnan(rsinp))]
                        fastk, fastd = ti.stoch(rsinp, rsinp, rsinp,14, 3, 3)
                        
                        rsi = talib.RSI(np_close,6)
                        wmasv = ti.wma(np_close,7)
                        wmatf = ti.wma(np_close,25)

                        mfi= ti.mfi(np_high,np_low,np_close,np_volume,14)

                        mdi= talib.MINUS_DI(np_high,np_low,np_close,14)
                        mdm= talib.MINUS_DM(np_high,np_low,14)

                        htprd=talib.HT_DCPERIOD(np_close)

                        var=talib.VAR(np_close, timeperiod=14, nbdev=1)

                        stdev=talib.BETA(np_high,np_low,timeperiod=14)
                        
                        roc=(((closes[-1]+1)/(closes[-2]+1))-1)*100

                        hrdataa[hcnt]=[hrsttime,hredtime,hhopen,hhclose,hhigh,hlow,rsi[-1],fastk[-1],fastd[-1],wmasv[-1],wmatf[-1],roc,hvol,mfi[-1],mdi[-1],mdm[-1],var[-1],stdev[-1]]
                        hcnt=hcnt+1
                
                
        'dont include the last data'
        
def toexcel(keytss,keytsst,str):
    
    TRADE_SYMBOL=str
    
    df = pd.DataFrame.from_dict(keytss,orient ='index')
   
    if TRADE_SYMBOL=="KNCBTC":
            pathf='CoinsDataV3/KNC/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="OCEANBTC":
            pathf='CoinsDataV3/OCEAN/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="SRMBTC":
            pathf='CoinsDataV3/SRM/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="LENDBTC":
            pathf='CoinsDataV3/LEND/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="THETABTC":
            pathf='CoinsDataV3/THETA/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="LRCBTC":
            pathf='CoinsDataV3/LRC/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="XTZBTC":
            pathf='CoinsDataV3/XTZ/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="DIABTC":
            pathf='CoinsDataV3/DIA/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="BATBTC":
            pathf='CoinsDataV3/BAT/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="AVABTC":
            pathf='CoinsDataV3/AVA/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="KAVABTC":
            pathf='CoinsDataV3/KAVA/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="CRVBTC":
            pathf='CoinsDataV3/CRV/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="SXPBTC":
            pathf='CoinsDataV3/SXP/FiveMinData.xlsx'
    elif TRADE_SYMBOL=="BTCUSDT":
            pathf='CoinsDataV3/BTC/BtcFiveMinData.xlsx'
        
    df.to_excel(pathf, sheet_name='data')

    dft= pd.DataFrame.from_dict(keytsst,orient ='index')
   
    if TRADE_SYMBOL=="KNCBTC":
            patht='CoinsDataV3/KNC/HrData.xlsx'
    elif TRADE_SYMBOL=="OCEANBTC":
            patht='CoinsDataV3/OCEAN/HrData.xlsx'
    elif TRADE_SYMBOL=="SRMBTC":
            patht='CoinsDataV3/SRM/HrData.xlsx'
    elif TRADE_SYMBOL=="LENDBTC":
            patht='CoinsDataV3/LEND/HrData.xlsx'
    elif TRADE_SYMBOL=="THETABTC":
            patht='CoinsDataV3/THETA/HrData.xlsx'
    elif TRADE_SYMBOL=="LRCBTC":
            patht='CoinsDataV3/LRC/HrData.xlsx'
    elif TRADE_SYMBOL=="XTZBTC":
            patht='CoinsDataV3/XTZ/HrData.xlsx'
    elif TRADE_SYMBOL=="DIABTC":
            patht='CoinsDataV3/DIA/HrData.xlsx'
    elif TRADE_SYMBOL=="BATBTC":
            patht='CoinsDataV3/BAT/HrData.xlsx'
    elif TRADE_SYMBOL=="AVABTC":
            patht='CoinsDataV3/AVA/HrData.xlsx'
    elif TRADE_SYMBOL=="KAVABTC":
            patht='CoinsDataV3/KAVA/HrData.xlsx'
    elif TRADE_SYMBOL=="CRVBTC":
            patht='CoinsDataV3/CRV/HrData.xlsx'
    elif TRADE_SYMBOL=="SXPBTC":
            patht='CoinsDataV3/SXP/HrData.xlsx'
    elif TRADE_SYMBOL=="BTCUSDT":
            patht='CoinsDataV3/BTC/HrData.xlsx'
        
    dft.to_excel(patht, sheet_name='data')
        
dataclct("THETABTC",openstheta,closestheta,highstheta,lowstheta,volumestheta,thetadataa,hropenstheta,hrclosestheta,hrhighstheta,hrlowstheta,hrvolumestheta,hthetadataa)
toexcel(thetadataa,hthetadataa,"THETABTC")
print('sent')
