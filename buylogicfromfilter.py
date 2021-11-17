from sklearn.cluster import KMeans 
from sklearn import metrics 
from scipy.spatial.distance import cdist 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

intervs={}

cndnlow=[]
cndnhigh=[]

pathfnd=[]

startkeyss=[]
endkeyss=[]

startdataa={}
enddataa={}

fvstartdataa={}
pfvstartdataa={}
ppfvstartdataa={}

opens=[]
closes=[]
highs=[]
lows=[]
fvrsi=[]
fastko=[]
fastkt=[]
wmasvdt=[]
wmatfdt=[]
fvroc=[]
wmadiffc=[]

popens=[]
pcloses=[]
phighs=[]
plows=[]
pfvrsi=[]
pfastko=[]
pfastkt=[]
pwmasvdt=[]
pwmatfdt=[]
pfvroc=[]
pwmadiffc=[]

ppopens=[]
ppcloses=[]
pphighs=[]
pplows=[]
ppfvrsi=[]
ppfastko=[]
ppfastkt=[]
ppwmasvdt=[]
ppwmatfdt=[]
ppfvroc=[]
ppwmadiffc=[]


hstartdataa={}
hpstartdataa={}
hppstartdataa={}

hopens=[]
hcloses=[]
hhighs=[]
hlows=[]
hrsi=[]
hfastko=[]
hfastkt=[]
hwmasvdt=[]
hwmatfdt=[]
hroc=[]
hwmadiffc=[]

hpopens=[]
hpcloses=[]
hphighs=[]
hplows=[]
hprsi=[]
hpfastko=[]
hpfastkt=[]
hpwmasvdt=[]
hpwmatfdt=[]
hproc=[]
hpwmadiffc=[]

hppopens=[]
hppcloses=[]
hpphighs=[]
hpplows=[]
hpprsi=[]
hppfastko=[]
hppfastkt=[]
hppwmasvdt=[]
hppwmatfdt=[]
hpproc=[]
hppwmadiffc=[]

gainn=[]

cluster0=[]
cluster1=[]
cluster2=[]
cluster3=[]
cluster4=[]

Aclstz=[]
Aclso=[]
Aclstt=[]
Aclstth=[]
Aclstf=[]
Aclstfv=[]
Aclsts=[]

Bclstz=[]
Bclsto=[]
Bclstt=[]
Bclstth=[]
Bclstf=[]
Bclstfv=[]

Cclstz=[]
Cclsto=[]
Cclstt=[]
Cclstth=[]
Cclstf=[]
Cclstfv=[]

Dclstz=[]
Dclsto=[]
Dclstt=[]

bctz=[]
bco=[]
bctt=[]
bcth=[]
bctf=[]
bcsx=[]
bcsv=[]

cnbctz=[]
cnbco=[]
cnbctt=[]
cnbcth=[]
cnbctf=[]
cnbcsx=[]
cnbcsv=[]
cnbceg=[]
cnbcnn=[]
cnbctn=[]

cdaroc=[]
cuproc=[]
cdownroc=[]
cflagg=[]

pdaroc=[]
puproc=[]
pdownroc=[]
pflagg=[]

ppdaroc=[]
ppuproc=[]
ppdownroc=[]
ppflagg=[]

hcdaroc=[]
hcuproc=[]
hcdownroc=[]
hcflagg=[]

hpdaroc=[]
hpuproc=[]
hpdownroc=[]
hpflagg=[]

hppdaroc=[]
hppuproc=[]
hppdownroc=[]
hppflagg=[]

inbtw=[]

edst=[]
edgain=[]

distortions = [] 
inertias = [] 
mapping1 = {} 
mapping2 = {}

diffhsv=[]
diffhtf=[]
difflsv=[]
diffltf=[]

pdiffhsv=[]
pdiffhtf=[]
pdifflsv=[]
pdiffltf=[]

ppdiffhsv=[]
ppdiffhtf=[]
ppdifflsv=[]
ppdiffltf=[]

ppdv=[]
pdv=[]
dv=[]

vroc=[]
pvroc=[]

mfi=[]
pmfi=[]
ppmfi=[]

mdi=[]
pmdi=[]
ppmdi=[]

mdm=[]
pmdm=[]
ppmdm=[]

var=[]
pvar=[]
ppvar=[]

cor=[]
pcor=[]
ppcor=[]

hdiffhsv=[]
hdiffhtf=[]
hdifflsv=[]
hdiffltf=[]

hpdiffhsv=[]
hpdiffhtf=[]
hpdifflsv=[]
hpdiffltf=[]

hppdiffhsv=[]
hppdiffhtf=[]
hppdifflsv=[]
hppdiffltf=[]

hppdv=[]
hpdv=[]
hdv=[]

hvroc=[]
hpvroc=[]

hmfi=[]
hpmfi=[]
hppmfi=[]

hmdi=[]
hpmdi=[]
hppmdi=[]

hmdm=[]
hpmdm=[]
hppmdm=[]

hvar=[]
hpvar=[]
hppvar=[]

hcor=[]
hpcor=[]
hppcor=[]

cndn1={}
cndn2={}
cndn3={}
cndn4={}
pnll={}

cp1=0
cp2=0
cp3=0
cp4=0

c1p=0
c2p=0
c3p=0
c4p=0

def clusterdata(tnfv4,str,incnd):
    global inbtw
    global clustst
    global clusted
    global clpathfnd
    global clagain
    global clfvroc
    global clwmadiff
    global fkey
    global skey

    global efvrsi
    global efastko
    global efastkt
    global epfvrsi
    global epfastko
    global epfastkt

    global ckey
    global cckey
    global ccckey
    global cccckey

    global hcdaroc
    global hcuproc
    global hcdownroc
    global hcflagg

    global hpdaroc
    global hpuproc
    global hpdownroc
    global hpflagg

    global hppdaroc
    global hppuproc
    global hppdownroc
    global hppflagg

    global hadiffhsv
    global hadiffhtf
    global hadifflsv
    global hadiffltf

    global hpadiffhsv
    global hpadiffhtf
    global hpadifflsv
    global hpadiffltf

    global hppadiffhsv
    global hppadiffhtf
    global hppadifflsv
    global hppadiffltf

    global happdv
    global hapdv
    global hadv

    global havroc
    global hapvroc

    global hamfi
    global hapmfi
    global happmfi

    global hamdi
    global hapmdi
    global happmdi

    global hamdm
    global hapmdm
    global happmdm

    global havar
    global hapvar
    global happvar
        
    global hacor
    global hapcor
    global happcor

    global hpddiff
    global hppddiff

    global hphdiff
    global hpphdiff

    global hptdiff
    global hpptdiff

    global hclfvroc
    global hclwmadiff

    global hclagain 
    

    
    global fcdaroc
    global fcuproc
    global fcdownroc
    global fcflagg

    global fpdaroc
    global fpuproc
    global fpdownroc
    global fpflagg

    global fppdaroc
    global fppuproc
    global fppdownroc
    global fppflagg

    global fadiffhsv
    global fadiffhtf
    global fadifflsv
    global fadiffltf

    global fpadiffhsv
    global fpadiffhtf
    global fpadifflsv
    global fpadiffltf

    global fppadiffhsv
    global fppadiffhtf
    global fppadifflsv
    global fppadiffltf

    global fappdv
    global fapdv
    global fadv

    global favroc
    global fapvroc

    global famfi
    global fapmfi
    global fappmfi

    global famdi
    global fapmdi
    global fappmdi

    global famdm
    global fapmdm
    global fappmdm

    global favar
    global fapvar
    global fappvar
        
    global facor
    global fapcor
    global fappcor

    global fpddiff
    global fppddiff

    global fphdiff
    global fpphdiff

    global fptdiff
    global fpptdiff

    global fclfvroc
    global fclwmadiff

    global fclagain

    global cndn1
    global cndn2
    global cndn3
    global cndn4
    global pnll

    global cp1
    global cp2
    global cp3
    global cp4

    global c1p
    global c2p
    global c3p
    global c4p

    global cndnlow
    global cndnhigh

    global gainc

    
    
    'clustst=[]'
    clusted=[]
    clpathfnd=[]
    clustterrr=str
    
    lnn=len(tnfv4)
    if incnd==0 or incnd==2:
        skey=tnfv4
   
    if incnd==0:
        ckey=[]
        ckey=tnfv4
        print("               ...........starting cluster ..................")
        "print('c1',ckey)"
        print('length=',len(ckey))
        
    if incnd==1:
        print('cndn1=',cndn1)
        print("               ...........second cluster ..................")
        cdaroc=hcdaroc
        cuproc=hcuproc
        cdownroc=hcdownroc
        cflagg=hcflagg

        pdaroc=hpdaroc
        puproc=hpuproc
        pdownroc=hpdownroc
        pflagg=hpflagg

        ppdaroc=hppdaroc
        ppuproc=hppuproc
        ppdownroc=hppdownroc
        ppflagg=hppflagg

        adiffhsv=hadiffhsv
        adiffhtf=hadiffhtf
        adifflsv=hadifflsv
        adiffltf=hadiffltf

        padiffhsv=hpadiffhsv
        padiffhtf=hpadiffhtf
        padifflsv=hpadifflsv
        padiffltf=hpadiffltf

        ppadiffhsv=hppadiffhsv
        ppadiffhtf=hppadiffhtf
        ppadifflsv=hppadifflsv
        ppadiffltf=hppadiffltf

        appdv=happdv
        apdv=hapdv
        adv=hadv

        avroc=havroc
        apvroc=hapvroc

        amfi=hamfi
        apmfi=hapmfi
        appmfi=happmfi

        amdi=hamdi
        apmdi=hapmdi
        appmdi=happmdi

        amdm=hamdm
        apmdm=hapmdm
        appmdm=happmdm

        avar=havar
        apvar=hapvar
        appvar=happvar
        
        acor=hacor
        apcor=hapcor
        appcor=happcor

        pddiff=hpddiff
        ppddiff=hppddiff

        phdiff=hphdiff
        pphdiff=hpphdiff

        ptdiff=hptdiff
        pptdiff=hpptdiff

        clfvroc=hclfvroc
        clwmadiff=hclwmadiff

        clagain=hclagain
        
        cckey=[]
        for c2 in range(len(tnfv4)):
            cckey.append(ckey[tnfv4[c2]])
        "print('c2',cckey)"
        print('length=',len(cckey))
            
    if incnd==2:
        print("               ...........third cluster ..................")
        ccckey=[]
        for c3 in range(len(tnfv4)):
            ccckey.append(cckey[tnfv4[c3]])
        "print('c3',ccckey)"
        print('length=',len(ccckey))
            
    if incnd==3:
        print("               ...........fourth cluster ..................")
        cdaroc=fcdaroc
        cuproc=fcuproc
        cdownroc=fcdownroc
        cflagg=fcflagg

        pdaroc=fpdaroc
        puproc=fpuproc
        pdownroc=fpdownroc
        pflagg=fpflagg

        ppdaroc=fppdaroc
        ppuproc=fppuproc
        ppdownroc=fppdownroc
        ppflagg=fppflagg

        adiffhsv=fadiffhsv
        adiffhtf=fadiffhtf
        adifflsv=fadifflsv
        adiffltf=fadiffltf

        padiffhsv=fpadiffhsv
        padiffhtf=fpadiffhtf
        padifflsv=fpadifflsv
        padiffltf=fpadiffltf

        ppadiffhsv=fppadiffhsv
        ppadiffhtf=fppadiffhtf
        ppadifflsv=fppadifflsv
        ppadiffltf=fppadiffltf

        appdv=fappdv
        apdv=fapdv
        adv=fadv

        avroc=favroc
        apvroc=fapvroc

        amfi=famfi
        apmfi=fapmfi
        appmfi=fappmfi

        amdi=famdi
        apmdi=fapmdi
        appmdi=fappmdi

        amdm=famdm
        apmdm=fapmdm
        appmdm=fappmdm

        avar=favar
        apvar=fapvar
        appvar=fappvar
        
        acor=facor
        apcor=fapcor
        appcor=fappcor

        pddiff=fpddiff
        ppddiff=fppddiff

        phdiff=fphdiff
        pphdiff=fpphdiff

        ptdiff=fptdiff
        pptdiff=fpptdiff

        clfvroc=fclfvroc
        clwmadiff=fclwmadiff

        clagain=fclagain
        
        cccckey=[]
        for c3 in range(len(tnfv4)):
            cccckey.append(ccckey[tnfv4[c3]])
        "print('c4',cccckey)"
        print('length=',len(cccckey))

    if incnd==0 or incnd==2:
        'print(clustterrr)'
        clustst=[]
        fkey=[]
        for srt in range(len(tnfv4)):
            clustst.append(edst[tnfv4[srt]])
            clusted.append(endkeyss[tnfv4[srt]])
            

        if incnd==0:
            for z in range(28):
                for nll in range(lnn):
                    ky=tnfv4[nll]
                    if z==0:
                        inbtw.append(hrsi[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"rsi ",len(tnfv4))
                    elif z==1:
                        inbtw.append(hfastko[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"fastko ",len(tnfv4))
                    elif z==2:
                        inbtw.append(hfastkt[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"fastkt ",len(tnfv4))
                    elif z==3:
                        inbtw.append(hprsi[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"previous rsi ",len(tnfv4))
                    elif z==4:
                        inbtw.append(hpfastko[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"previous fastko ",len(tnfv4))
                    elif z==5:
                        inbtw.append(hpfastkt[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"previous fastkt ",len(tnfv4))

                inbtw=[]
                
        if incnd==2:
            for z in range(28):
                'for nll in range(lnn):'
                for nll in range(len(tnfv4)):
                    ky=tnfv4[nll]
                    if z==0:
                        inbtw.append(efvrsi[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"rsi ",len(tnfv4))
                    elif z==1:
                        inbtw.append(efastko[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"fastko ",len(tnfv4))
                    elif z==2:
                        inbtw.append(efastkt[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"fastkt ",len(tnfv4))
                    elif z==3:
                        inbtw.append(epfvrsi[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"previous rsi ",len(tnfv4))
                    elif z==4:
                        inbtw.append(epfastko[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"previous fastko ",len(tnfv4))
                    elif z==5:
                        inbtw.append(epfastkt[ky])
                        if nll==(lnn-1):
                            inbetween2(inbtw,"previous fastkt ",len(tnfv4))

                inbtw=[]

        if incnd==0:
            allcnd=[cndnlow,cndnhigh]
            wrt(cndnlow,cndnhigh,0)
            print('allcnd',allcnd)
            'get back'
            dlet=len(cndnlow)
            for dlttt in range(dlet):
                cndnlow.pop(0)
                cndnhigh.pop(0)

        if incnd==2:
            allcnd=[cndnlow,cndnhigh]
            wrt(cndnlow,cndnhigh,2)
            print('allcnd',allcnd)
            dlet=len(cndnlow)
            for dlttt in range(dlet):
                cndnlow.pop(0)
                cndnhigh.pop(0)        
            
            
        if incnd==0:
            forvthr(1,ckey,clustterrr,clustst,hroc,hwmadiffc,hdiffhsv,hdiffhtf,hdifflsv,hdiffltf,hpdiffhsv,hpdiffhtf,hpdifflsv,hpdiffltf,hppdiffhsv,hppdiffhtf,hppdifflsv,hppdiffltf,hppdv,hpdv,hdv,hvroc,hpvroc,hmfi,hpmfi,hppmfi,hmdi,hpmdi,hppmdi,hmdm,hpmdm,hppmdm,hvar,hpvar,hppvar,hcor,hpcor,hppcor,hopens,hcloses,hhighs,hlows,hpopens,hpcloses,hphighs,hplows,hppopens,hppcloses,hpphighs,hpplows)

        if incnd==2:    
            forvthr(3,ccckey,clustterrr,clustst,fvroc,wmadiffc,diffhsv,diffhtf,difflsv,diffltf,pdiffhsv,pdiffhtf,pdifflsv,pdiffltf,ppdiffhsv,ppdiffhtf,ppdifflsv,ppdiffltf,ppdv,pdv,dv,vroc,pvroc,mfi,pmfi,ppmfi,mdi,pmdi,ppmdi,mdm,pmdm,ppmdm,var,pvar,ppvar,cor,pcor,ppcor,opens,closes,highs,lows,popens,pcloses,phighs,plows,ppopens,ppcloses,pphighs,pplows)      
            
    if incnd==1 or incnd==3:
        gic=[]
        cndclst=[]
        skey=[]
        
        lnn=len(tnfv4)
            
        for z in range(60):
            for nll in range(lnn):
                
                ky=tnfv4[nll]    
                    
                if z==0:
                    inbtw.append(cdaroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"current body ",len(tnfv4))
                elif z==1:
                    inbtw.append(cuproc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"current head ",len(tnfv4))
                elif z==2:
                    inbtw.append(cdownroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"current tail ",len(tnfv4))
                elif z==3:
                    inbtw.append(pdaroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"previous body ",len(tnfv4))
                elif z==4:
                    inbtw.append(puproc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"previous head ",len(tnfv4))
                elif z==5:
                    inbtw.append(pdownroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"previous tail ",len(tnfv4))
                elif z==6:
                    inbtw.append(ppdaroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p previous body ",len(tnfv4))
                elif z==7:
                    inbtw.append(ppuproc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p previous head ",len(tnfv4))
                elif z==8:
                    inbtw.append(ppdownroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p previous tail ",len(tnfv4))
                elif z==9:
                    inbtw.append(clwmadiff[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"wmadiff ",len(tnfv4))
                elif z==10:
                    inbtw.append(clfvroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"fvroc ",len(tnfv4))
                elif z==11:
                    gic.append(clagain[ky])
                elif z==12:
                    inbtw.append(adiffhsv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"high n wmasv ",len(tnfv4))
                elif z==13:
                    inbtw.append(adiffhtf[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"high n wmatf ",len(tnfv4))
                elif z==14:
                    inbtw.append(adifflsv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"low n wmasv ",len(tnfv4))
                elif z==15:
                    inbtw.append(adiffltf[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"low n wmatf ",len(tnfv4))
                elif z==16:
                    inbtw.append(padiffhsv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p high n wmasv ",len(tnfv4))
                elif z==17:
                    inbtw.append(padiffhtf[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p high n wmatf ",len(tnfv4))
                elif z==18:
                    inbtw.append(padifflsv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p low n wmasv ",len(tnfv4))
                elif z==19:
                    inbtw.append(padiffltf[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p low n wmatf ",len(tnfv4))
                elif z==20:
                    inbtw.append(ppadiffhsv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"pp high n wmasv ",len(tnfv4))
                elif z==21:
                    inbtw.append(ppadiffhtf[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"pp high n wmatf ",len(tnfv4))
                elif z==22:
                    inbtw.append(ppadifflsv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"pp low n wmasv ",len(tnfv4))
                elif z==23:
                    inbtw.append(ppadiffltf[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"pp low n wmatf ",len(tnfv4))
                elif z==24:
                    inbtw.append(appdv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"pp div ",len(tnfv4))
                elif z==25:
                    inbtw.append(apdv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p div",len(tnfv4))
                elif z==26:
                    inbtw.append(adv[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"div ",len(tnfv4))
                elif z==27:
                    inbtw.append(avroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"vol roc ",len(tnfv4))
                elif z==28:
                    inbtw.append(apvroc[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p vol roc ",len(tnfv4))
                elif z==29:
                    inbtw.append(amfi[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"c mfi ",len(tnfv4))
                elif z==30:
                    inbtw.append(apmfi[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p mfi ",len(tnfv4))
                elif z==31:
                    inbtw.append(appmfi[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p mfi ",len(tnfv4))
                elif z==32:
                    inbtw.append(amdi[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"c mdi ",len(tnfv4))
                elif z==33:
                    inbtw.append(apmdi[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p mdi ",len(tnfv4))
                elif z==34:
                    inbtw.append(appmdi[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p mdi ",len(tnfv4))
                elif z==35:
                    inbtw.append(amdm[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"c mdm ",len(tnfv4))
                elif z==36:
                    inbtw.append(apmdm[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p mdm ",len(tnfv4))
                elif z==37:
                    inbtw.append(appmdm[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p mdm ",len(tnfv4))
                elif z==38:
                    inbtw.append(avar[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"c var ",len(tnfv4))
                elif z==39:
                    inbtw.append(apvar[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p var ",len(tnfv4))
                elif z==40:
                    inbtw.append(appvar[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p var ",len(tnfv4))
                elif z==41:
                    inbtw.append(acor[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"c cor ",len(tnfv4))
                elif z==42:
                    inbtw.append(apcor[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p cor ",len(tnfv4))
                elif z==43:
                    inbtw.append(appcor[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p cor ",len(tnfv4))
                elif z==44:
                    inbtw.append(pddiff[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p body diff ",len(tnfv4))
                elif z==45:
                    inbtw.append(ppddiff[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p body diff ",len(tnfv4))
                elif z==46:
                    inbtw.append(phdiff[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p up diff ",len(tnfv4))
                elif z==47:
                    inbtw.append(pphdiff[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p up diff ",len(tnfv4))
                elif z==48:
                    inbtw.append(ptdiff[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p tail diff ",len(tnfv4))
                elif z==49:
                    inbtw.append(pptdiff[ky])
                    if nll==(lnn-1):
                        inbetween2(inbtw,"p p tail diff ",len(tnfv4))
                       
                         
            inbtw=[]
            
        if incnd==1: 
            allcnd=[cndnlow,cndnhigh]
            print('allcnd',allcnd)
            wrt(cndnlow,cndnhigh,1)  
            dlet=len(cndnlow)
            for dlttt in range(dlet):
                cndnlow.pop(0)
                cndnhigh.pop(0)

        if incnd==3: 
            gainc=np.mean(gic)
            print('gain=',gainc)
            wrt(cndnlow,cndnhigh,3) 
            allcnd=[cndnlow,cndnhigh]
            print('allcnd',allcnd)
            dlet=len(cndnlow)
            for dlttt in range(dlet):
                cndnlow.pop(0)
                cndnhigh.pop(0)           
            
        if incnd==1:
            efvrsi=[]
            efastko=[]
            efastkt=[]
            epfvrsi=[]
            epfastko=[]
            epfastkt=[]
            
            for edln in range(len(cckey)):
                efvrsi.append(fvrsi[cckey[edln]])
                efastko.append(fastko[cckey[edln]])
                efastkt.append(fastkt[cckey[edln]])
                epfvrsi.append(pfvrsi[cckey[edln]])
                epfastko.append(pfastko[cckey[edln]])
                epfastkt.append(pfastkt[cckey[edln]])    

            'kmeann(2)'
            
            if clustterrr=='cluster 1':
                kmn(3,2)
            elif clustterrr=='cluster 2':
                kmn(3,2)
            elif clustterrr=='cluster 3':
                kmn(3,2)
            elif clustterrr=='cluster 4':
                kmn(3,2)
               


def kmeann(incnd):

    distortions = [] 
    inertias = [] 
    mapping1 = {} 
    mapping2 = {}
    
    if incnd==0:
        x1=np.array(hrsi)
        x2=np.array(hfastko)
        x3=np.array(hfastkt)
        x4=np.array(hprsi)
        x5=np.array(hpfastko)
        x6=np.array(hpfastkt)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6))).reshape(len(x1),6)
    
    if incnd==1:
        x1=np.array(cdaroc)
        x2=np.array(cuproc)
        x3=np.array(cdownroc)
        x4=np.array(pdaroc)
        x5=np.array(puproc)
        x6=np.array(pdownroc)
        x7=np.array(ppdaroc)
        x8=np.array(ppuproc)
        x9=np.array(ppdownroc)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6,x7,x8,x9))).reshape(len(x1),9)

    if incnd==2:
        x1=np.array(efvrsi)
        x2=np.array(efastko)
        x3=np.array(efastkt)
        x4=np.array(epfvrsi)
        x5=np.array(epfastko)
        x6=np.array(epfastkt)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6))).reshape(len(x1),6)

    if incnd==3:
        x1=np.array(cdaroc)
        x2=np.array(cuproc)
        x3=np.array(cdownroc)
        x4=np.array(pdaroc)
        x5=np.array(puproc)
        x6=np.array(pdownroc)
        x7=np.array(ppdaroc)
        x8=np.array(ppuproc)
        x9=np.array(ppdownroc)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6,x7,x8,x9))).reshape(len(x1),9)    
        
    
    'print(X)'
    
    K = range(1,10)

    b="cluster"
    for k in K:
        print(k)
        kmeanModel = KMeans(n_clusters=k).fit(X) 
        kmeanModel.fit(X)            
        
        distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 
                          'euclidean'),axis=1)) / X.shape[0]) 
        inertias.append(kmeanModel.inertia_) 
      
        mapping1[k] = sum(np.min(cdist(X, kmeanModel.cluster_centers_, 
                     'euclidean'),axis=1)) / X.shape[0] 
        mapping2[k] = kmeanModel.inertia_


    for key,val in mapping1.items(): 
        print(str(key)+' : '+str(val))

    plt.plot(K, distortions, 'bx-') 
    plt.xlabel('Values of K') 
    plt.ylabel('Distortion') 
    plt.title('The Elbow Method using Distortion') 
    plt.show()     


def kmn(k,incnd):

    bctz=[]
    bco=[]
    bctt=[]
    bcth=[]
    bctf=[]
    bcsx=[]
    bcsv=[]

    if incnd==0:
        x1=np.array(hrsi)
        x2=np.array(hfastko)
        x3=np.array(hfastkt)
        x4=np.array(hprsi)
        x5=np.array(hpfastko)
        x6=np.array(hpfastkt)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6))).reshape(len(x1),6)
    
    if incnd==1:
        x1=np.array(cdaroc)
        x2=np.array(cuproc)
        x3=np.array(cdownroc)
        x4=np.array(pdaroc)
        x5=np.array(puproc)
        x6=np.array(pdownroc)
        x7=np.array(ppdaroc)
        x8=np.array(ppuproc)
        x9=np.array(ppdownroc)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6,x7,x8,x9))).reshape(len(x1),9)

    if incnd==2:
        x1=np.array(efvrsi)
        x2=np.array(efastko)
        x3=np.array(efastkt)
        x4=np.array(epfvrsi)
        x5=np.array(epfastko)
        x6=np.array(epfastkt)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6))).reshape(len(x1),6)

    if incnd==3:
        x1=np.array(cdaroc)
        x2=np.array(cuproc)
        x3=np.array(cdownroc)
        x4=np.array(pdaroc)
        x5=np.array(puproc)
        x6=np.array(pdownroc)
        x7=np.array(ppdaroc)
        x8=np.array(ppuproc)
        x9=np.array(ppdownroc)
        X = np.array(list(zip(x1,x2,x3,x4,x5,x6,x7,x8,x9))).reshape(len(x1),9) 
    
    
    'print(X)'
    kmeanModel = KMeans(n_clusters=k).fit(X) 
    kmeanModel.fit(X)
    cluster_map =pd.DataFrame()
    cluster_map['cluster'] = kmeanModel.labels_
    "print(cluster_map[cluster_map.cluster == cr])"
    for cr in range (7):
                pr=0
                ln=len(cluster_map[cluster_map.cluster == cr])
                for pr in range (ln):
                    if cr==0:
                        bco.append(cluster_map[cluster_map.cluster == cr].iloc[pr].name)
                    elif cr==1:
                        bctz.append(cluster_map[cluster_map.cluster == cr].iloc[pr].name)
                    elif cr==2:
                        bctt.append(cluster_map[cluster_map.cluster == cr].iloc[pr].name)
                    elif cr==3:
                        bcth.append(cluster_map[cluster_map.cluster == cr].iloc[pr].name)
                    elif cr==4:
                        bctf.append(cluster_map[cluster_map.cluster == cr].iloc[pr].name)
                    elif cr==5:
                        bcsx.append(cluster_map[cluster_map.cluster == cr].iloc[pr].name)
                    elif cr==6:
                        bcsv.append(cluster_map[cluster_map.cluster == cr].iloc[pr].name)    

    if incnd==0:
        clusterdata(bco,"cluster 1",0)
        'print(bco)'
        clusterdata(bctz,"cluster 2",0)
        'print(bctz)'
        clusterdata(bctt,"cluster 3",0)
        'print(bctt)'
        clusterdata(bcth,"cluster 4",0)
        'print(bctt)'
        

    if incnd==1:
       clusterdata(bco,"cluster 1",1)
       'print(bco)'
       clusterdata(bctz,"cluster 2",1)
       'print(bctz)'
       clusterdata(bctt,"cluster 3",1)
       'print(bctt)'
       clusterdata(bcth,"cluster 4",1)
       'print(bcth)'
       

    if incnd==2:
        clusterdata(bco,"cluster 1",2)
        'print(bco)'
        clusterdata(bctz,"cluster 2",2)
        'print(bctz)'
        clusterdata(bctt,"cluster 3",2)
        'print(bctt)'
        
    if incnd==3:
       clusterdata(bco,"cluster 1",3)
       'print(bco)'
       clusterdata(bctz,"cluster 2",3)
       'print(bctz)'
         


def fechdata():
    
    global df
    global dft
    global startkeyss
    global endkeyss
    global edst
    global edgain
    global startdataa
    global enddataa
    global startspread
    global gainn

    crk=0
    pathr='FilteredCoinsDataV4/THETA/Filtered.xlsx'
    df = pd.read_excel (pathr, sheet_name='filtereddata')
    rows = len(df.axes[0])
    
    for r in range(rows):
        startt=int(df.loc[r][[0]])
        endd=int(df.loc[r][[1]])
        gainnn=float(df.loc[r][[5]])
        
        startkeyss.append(startt)
        endkeyss.append(endd)
        gainn.append(gainnn)

    pathsfv='CoinsDataV3/THETA/FiveMinData.xlsx' 
    dffv = pd.read_excel (pathsfv, sheet_name='data')

    pathshr='CoinsDataV3/THETA/HrData.xlsx' 
    dfhr = pd.read_excel (pathshr, sheet_name='data')
    
    st=len(startkeyss)
    '''
    print(startkeyss)
    print(endkeyss)
    '''
    for f in range(st):
        loccst=startkeyss[f]
        locced=endkeyss[f]
        startdataa[f]=dffv.loc[loccst]
        enddataa[f]=dffv.loc[locced]
        
        if dffv.loc[loccst][18]>3:

            fvstartdataa[f]=dffv.loc[loccst-1]
            pfvstartdataa[f]=dffv.loc[loccst-2]
            ppfvstartdataa[f]=dffv.loc[loccst-3]

            hkey=fvstartdataa[f][18]
            hstartdataa[f]=dfhr.loc[hkey-1]
            hpstartdataa[f]=dfhr.loc[hkey-2]
            hppstartdataa[f]=dfhr.loc[hkey-3]

            edst.append(loccst)
            edgain.append(gainn[f])
            opens.append(float(fvstartdataa[f][2]))
            closes.append(float(fvstartdataa[f][3]))
            highs.append(float(fvstartdataa[f][4]))
            lows.append(float(fvstartdataa[f][5]))
            fvrsi.append(float(fvstartdataa[f][6]))
            fastko.append(float(fvstartdataa[f][7]))
            fastkt.append(float(fvstartdataa[f][8]))
            wmasvdt.append(float(fvstartdataa[f][9]))
            wmatfdt.append(float(fvstartdataa[f][10]))
            cwmadiff=float(fvstartdataa[f][9])-float(fvstartdataa[f][10])
            wmadiffc.append(cwmadiff)
            fvroc.append(float(fvstartdataa[f][11]))

            
            popens.append(float(pfvstartdataa[f][2]))
            pcloses.append(float(pfvstartdataa[f][3]))
            phighs.append(float(pfvstartdataa[f][4]))
            plows.append(float(pfvstartdataa[f][5]))
            pfvrsi.append(float(pfvstartdataa[f][6]))
            pfastko.append(float(pfvstartdataa[f][7]))
            pfastkt.append(float(pfvstartdataa[f][8]))
            pwmasvdt.append(float(pfvstartdataa[f][9]))
            pwmatfdt.append(float(pfvstartdataa[f][10]))
            pcwmadiff=float(pfvstartdataa[f][9])-float(pfvstartdataa[f][10])
            pwmadiffc.append(pcwmadiff)
            pfvroc.append(float(pfvstartdataa[f][11]))

            
            ppopens.append(float(ppfvstartdataa[f][2]))
            ppcloses.append(float(ppfvstartdataa[f][3]))
            pphighs.append(float(ppfvstartdataa[f][4]))
            pplows.append(float(ppfvstartdataa[f][5]))
            ppfvrsi.append(float(ppfvstartdataa[f][6]))
            ppfastko.append(float(ppfvstartdataa[f][7]))
            ppfastkt.append(float(ppfvstartdataa[f][8]))
            ppwmasvdt.append(float(ppfvstartdataa[f][9]))
            ppwmatfdt.append(float(ppfvstartdataa[f][10]))
            ppcwmadiff=float(ppfvstartdataa[f][9])-float(ppfvstartdataa[f][10])
            ppwmadiffc.append(ppcwmadiff)
            ppfvroc.append(float(ppfvstartdataa[f][11]))

            sdiffhsv=float(fvstartdataa[f][9])-float(fvstartdataa[f][4])
            sdiffhtf=float(fvstartdataa[f][10])-float(fvstartdataa[f][4])

            sdifflsv=float(fvstartdataa[f][9])-float(fvstartdataa[f][5])
            sdiffltf=float(fvstartdataa[f][10])-float(fvstartdataa[f][5])

            psdiffhsv=float(pfvstartdataa[f][9])-float(pfvstartdataa[f][4])
            psdiffhtf=float(pfvstartdataa[f][10])-float(pfvstartdataa[f][4])

            psdifflsv=float(pfvstartdataa[f][9])-float(pfvstartdataa[f][5])
            psdiffltf=float(pfvstartdataa[f][10])-float(pfvstartdataa[f][5])

            ppsdiffhsv=float(ppfvstartdataa[f][9])-float(ppfvstartdataa[f][4])
            ppsdiffhtf=float(ppfvstartdataa[f][10])-float(ppfvstartdataa[f][4])

            ppsdifflsv=float(ppfvstartdataa[f][9])-float(ppfvstartdataa[f][5])
            ppsdiffltf=float(ppfvstartdataa[f][10])-float(ppfvstartdataa[f][5])

            diffhsv.append(sdiffhsv)
            diffhtf.append(sdiffhtf)
            difflsv.append(sdifflsv)
            diffltf.append(sdiffltf)

            pdiffhsv.append(psdiffhsv)
            pdiffhtf.append(psdiffhtf)
            pdifflsv.append(psdifflsv)
            pdiffltf.append(psdiffltf)

            ppdiffhsv.append(ppsdiffhsv)
            ppdiffhtf.append(ppsdiffhtf)
            ppdifflsv.append(ppsdifflsv)
            ppdiffltf.append(ppsdiffltf)

            sppdvh=float(ppfvstartdataa[f][4])*1000000
            sppdvl=float(ppfvstartdataa[f][5])*1000000
            spdvh=float(pfvstartdataa[f][4])*1000000
            spdvl=float(pfvstartdataa[f][5])*1000000
            sdvh=float(fvstartdataa[f][4])*1000000
            sdvl=float(fvstartdataa[f][5])*1000000

            nppdv=(((sppdvh+1)/(spdvl+1))-1)*100
            npdv=(((spdvh+1)/(sdvl+1))-1)*100
            ndv=(((sdvh+1)/(sdvl+1))-1)*100

            ppdv.append(nppdv)
            pdv.append(npdv)
            dv.append(ndv)

            vol=fvstartdataa[f][12]
            pvol=pfvstartdataa[f][12]
            ppvol=ppfvstartdataa[f][12]

            svroc=(((pvol+1)/(vol+1))-1)*100
            spvroc=(((ppvol+1)/(pvol+1))-1)*100

            vroc.append(svroc)
            pvroc.append(spvroc)

            mfi.append(fvstartdataa[f][13])
            pmfi.append(pfvstartdataa[f][13])
            ppmfi.append(ppfvstartdataa[f][13])

            mdi.append(fvstartdataa[f][14])
            pmdi.append(pfvstartdataa[f][14])
            ppmdi.append(ppfvstartdataa[f][14])
            
            mdm.append(fvstartdataa[f][15])
            pmdm.append(pfvstartdataa[f][15])
            ppmdm.append(ppfvstartdataa[f][15])
           
            var.append(fvstartdataa[f][16])
            pvar.append(pfvstartdataa[f][16])
            ppvar.append(ppfvstartdataa[f][16])
            
            cor.append(fvstartdataa[f][17])
            pcor.append(pfvstartdataa[f][17])
            ppcor.append(ppfvstartdataa[f][17])
            
            

            hopens.append(float(hstartdataa[f][2]))
            hcloses.append(float(hstartdataa[f][3]))
            hhighs.append(float(hstartdataa[f][4]))
            hlows.append(float(hstartdataa[f][5]))
            hrsi.append(float(hstartdataa[f][6]))
            hfastko.append(float(hstartdataa[f][7]))
            hfastkt.append(float(hstartdataa[f][8]))
            hwmasvdt.append(float(hstartdataa[f][9]))
            hwmatfdt.append(float(hstartdataa[f][10]))
            hcwmadiff=float(hstartdataa[f][9])-float(hstartdataa[f][10])
            hwmadiffc.append(hcwmadiff)
            hroc.append(float(hstartdataa[f][11]))

            hpopens.append(float(hpstartdataa[f][2]))
            hpcloses.append(float(hpstartdataa[f][3]))
            hphighs.append(float(hpstartdataa[f][4]))
            hplows.append(float(hpstartdataa[f][5]))
            hprsi.append(float(hpstartdataa[f][6]))
            hpfastko.append(float(hpstartdataa[f][7]))
            hpfastkt.append(float(hpstartdataa[f][8]))
            hpwmasvdt.append(float(hpstartdataa[f][9]))
            hpwmatfdt.append(float(hpstartdataa[f][10]))
            hpcwmadiff=float(hpstartdataa[f][9])-float(hpstartdataa[f][10])
            hpwmadiffc.append(hpcwmadiff)
            hproc.append(float(hpstartdataa[f][11]))

            hppopens.append(float(hppstartdataa[f][2]))
            hppcloses.append(float(hppstartdataa[f][3]))
            hpphighs.append(float(hppstartdataa[f][4]))
            hpplows.append(float(hppstartdataa[f][5]))
            hpprsi.append(float(hppstartdataa[f][6]))
            hppfastko.append(float(hppstartdataa[f][7]))
            hppfastkt.append(float(hppstartdataa[f][8]))
            hppwmasvdt.append(float(hppstartdataa[f][9]))
            hppwmatfdt.append(float(hppstartdataa[f][10]))
            hppcwmadiff=float(hppstartdataa[f][9])-float(hppstartdataa[f][10])
            hppwmadiffc.append(hppcwmadiff)
            hpproc.append(float(hppstartdataa[f][11]))

            hsdiffhsv=float(hstartdataa[f][9])-float(hstartdataa[f][4])
            hsdiffhtf=float(hstartdataa[f][10])-float(hstartdataa[f][4])

            hsdifflsv=float(hstartdataa[f][9])-float(hstartdataa[f][5])
            hsdiffltf=float(hstartdataa[f][10])-float(hstartdataa[f][5])

            hpsdiffhsv=float(hpstartdataa[f][9])-float(hpstartdataa[f][4])
            hpsdiffhtf=float(hpstartdataa[f][10])-float(hpstartdataa[f][4])

            hpsdifflsv=float(hpstartdataa[f][9])-float(hpstartdataa[f][5])
            hpsdiffltf=float(hpstartdataa[f][10])-float(hpstartdataa[f][5])

            hppsdiffhsv=float(hppstartdataa[f][9])-float(hppstartdataa[f][4])
            hppsdiffhtf=float(hppstartdataa[f][10])-float(hppstartdataa[f][4])

            hppsdifflsv=float(hppstartdataa[f][9])-float(hppstartdataa[f][5])
            hppsdiffltf=float(hppstartdataa[f][10])-float(hppstartdataa[f][5])

            hdiffhsv.append(hsdiffhsv)
            hdiffhtf.append(hsdiffhtf)
            hdifflsv.append(hsdifflsv)
            hdiffltf.append(hsdiffltf)

            hpdiffhsv.append(hpsdiffhsv)
            hpdiffhtf.append(hpsdiffhtf)
            hpdifflsv.append(hpsdifflsv)
            hpdiffltf.append(hpsdiffltf)

            hppdiffhsv.append(hppsdiffhsv)
            hppdiffhtf.append(hppsdiffhtf)
            hppdifflsv.append(hppsdifflsv)
            hppdiffltf.append(hppsdiffltf)

            hsppdvh=float(hppstartdataa[f][4])*1000000
            hsppdvl=float(hppstartdataa[f][5])*1000000
            hspdvh=float(hpstartdataa[f][4])*1000000
            hspdvl=float(hpstartdataa[f][5])*1000000
            hsdvh=float(hstartdataa[f][4])*1000000
            hsdvl=float(hstartdataa[f][5])*1000000

            hnppdv=(((hsppdvh+1)/(hspdvl+1))-1)*100
            hnpdv=(((hspdvh+1)/(hsdvl+1))-1)*100
            hndv=(((hsdvh+1)/(hsdvl+1))-1)*100

            hppdv.append(hnppdv)
            hpdv.append(hnpdv)
            hdv.append(hndv)

            hvol=hstartdataa[f][12]
            hpvol=hpstartdataa[f][12]
            hppvol=hppstartdataa[f][12]

            hsvroc=(((hpvol+1)/(hvol+1))-1)*100
            hspvroc=(((hppvol+1)/(hpvol+1))-1)*100

            hvroc.append(hsvroc)
            hpvroc.append(hspvroc)

            hmfi.append(hstartdataa[f][13])
            hpmfi.append(hpstartdataa[f][13])
            hppmfi.append(hppstartdataa[f][13])

            hmdi.append(hstartdataa[f][14])
            hpmdi.append(hpstartdataa[f][14])
            hppmdi.append(hppstartdataa[f][14])

            hmdm.append(hstartdataa[f][15])
            hpmdm.append(hpstartdataa[f][15])
            hppmdm.append(hppstartdataa[f][15])

            hvar.append(hstartdataa[f][16])
            hpvar.append(hpstartdataa[f][16])
            hppvar.append(hppstartdataa[f][16])

            hcor.append(hstartdataa[f][17])
            hpcor.append(hpstartdataa[f][17])
            hppcor.append(hppstartdataa[f][17])

    'kmeann(0)'
    kmn(4,0)


def inbetween2(inbtw,str,x):

    global cndnlow
    global cndnhigh

    

    textt=str
    '''
    for t in range(len(inbtw)):
        print(inbtw[t])
    '''    
    
    n=0


    for dell in range(len(intervs)):
        intervs.pop(dell)
        
    for fs in range(len(inbtw)):
        x=inbtw[fs]
        
        for sec in range(len(inbtw)):
            y=inbtw[sec]
            if x>y:
                highbnd=x
                lowbnd=y
            else:
                highbnd=y
                lowbnd=x
            cnter=0
            
            for thr in range(len(inbtw)):
                'if cnter<85:'
                if (cnter*100)/len(inbtw)<=98:    
                    if inbtw[thr]<=highbnd and inbtw[thr]>=lowbnd:
                        cnter=cnter+1
            if (cnter*100)/len(inbtw)>=98:
                hnldta=[highbnd,lowbnd]
                intervs[n]=hnldta
                n=n+1
                
    if len(intervs)>0:
        intervsdiff=intervs[0][0]-intervs[0][1]           
        for frt in range(len(intervs)):
             if(intervs[frt][0]-intervs[frt][1])<=intervsdiff:
                 low=intervs[frt][1]
                 high=intervs[frt][0]
                 intervsdiff=intervs[frt][0]-intervs[frt][1]
        cndnlow.append(low)
        cndnhigh.append(high)         
        print(textt,end=""),print(low,end=""),print("and",end=""),print(high)    


def forvthr(incnd,tptkys,str,clustst,rc,wdf,dhsv,dhtf,dlsv,dltf,pdhsv,pdhtf,pdlsv,pdltf,ppdhsv,ppdhtf,ppdlsv,ppdltf,cppdv,cpdv,cdv,vrc,pvrc,fi,pfi,ppfi,cmdi,cpmdi,cppmdi,cmdm,cpmdm,cppmdm,cvar,cpvar,cppvar,ccor,cpcor,cppcor,copens,ccloses,chighs,clows,cpopens,cpcloses,cphighs,cplows,cppopens,cppcloses,cpphighs,cpplows):

    global cdaroc
    global cuproc
    global cdownroc
    global cflagg

    global pdaroc
    global puproc
    global pdownroc
    global pflagg

    global ppdaroc
    global ppuproc
    global ppdownroc
    global ppflagg
    
    global tvls
    global ptvls
    global pptvls

    global diffhsv
    global diffhtf
    global difflsv
    global diffltf

    global pdiffhsv
    global pdiffhtf
    global pdifflsv
    global pdiffltf

    global ppdiffhsv
    global ppdiffhtf
    global ppdifflsv
    global ppdiffltf

    global adiffhsv
    global adiffhtf
    global adifflsv
    global adiffltf

    global padiffhsv
    global padiffhtf
    global padifflsv
    global padiffltf

    global ppadiffhsv
    global ppadiffhtf
    global ppadifflsv
    global ppadiffltf

    global appdv
    global apdv
    global adv

    global avroc
    global apvroc

    global amfi
    global apmfi
    global appmfi

    global amdi
    global apmdi
    global appmdi

    global amdm
    global apmdm
    global appmdm

    global avar
    global apvar
    global appvar
    
    global acor
    global apcor
    global appcor

    global pddiff
    global ppddiff

    global phdiff
    global pphdiff

    global ptdiff
    global pptdiff

    global clfvroc
    global clwmadiff

    global clagain

    global ahrsi

    
    global hcdaroc
    global hcuproc
    global hcdownroc
    global hcflagg

    global hpdaroc
    global hpuproc
    global hpdownroc
    global hpflagg

    global hppdaroc
    global hppuproc
    global hppdownroc
    global hppflagg

    global hadiffhsv
    global hadiffhtf
    global hadifflsv
    global hadiffltf

    global hpadiffhsv
    global hpadiffhtf
    global hpadifflsv
    global hpadiffltf

    global hppadiffhsv
    global hppadiffhtf
    global hppadifflsv
    global hppadiffltf

    global happdv
    global hapdv
    global hadv

    global havroc
    global hapvroc

    global hamfi
    global hapmfi
    global happmfi

    global hamdi
    global hapmdi
    global happmdi

    global hamdm
    global hapmdm
    global happmdm

    global havar
    global hapvar
    global happvar
        
    global hacor
    global hapcor
    global happcor

    global hpddiff
    global hppddiff

    global hphdiff
    global hpphdiff

    global hptdiff
    global hpptdiff

    global hclfvroc
    global hclwmadiff

    global hclagain 
    

    
    global fcdaroc
    global fcuproc
    global fcdownroc
    global fcflagg

    global fpdaroc
    global fpuproc
    global fpdownroc
    global fpflagg

    global fppdaroc
    global fppuproc
    global fppdownroc
    global fppflagg

    global fadiffhsv
    global fadiffhtf
    global fadifflsv
    global fadiffltf

    global fpadiffhsv
    global fpadiffhtf
    global fpadifflsv
    global fpadiffltf

    global fppadiffhsv
    global fppadiffhtf
    global fppadifflsv
    global fppadiffltf

    global fappdv
    global fapdv
    global fadv

    global favroc
    global fapvroc

    global famfi
    global fapmfi
    global fappmfi

    global famdi
    global fapmdi
    global fappmdi

    global famdm
    global fapmdm
    global fappmdm

    global favar
    global fapvar
    global fappvar
        
    global facor
    global fapcor
    global fappcor

    global fpddiff
    global fppddiff

    global fphdiff
    global fpphdiff

    global fptdiff
    global fpptdiff

    global fclfvroc
    global fclwmadiff

    global fclagain 

    
    

    cdaroc=[]
    cuproc=[]
    cdownroc=[]
    cflagg=[]

    pdaroc=[]
    puproc=[]
    pdownroc=[]
    pflagg=[]

    ppdaroc=[]
    ppuproc=[]
    ppdownroc=[]
    ppflagg=[]

    adiffhsv=[]
    adiffhtf=[]
    adifflsv=[]
    adiffltf=[]

    padiffhsv=[]
    padiffhtf=[]
    padifflsv=[]
    padiffltf=[]

    ppadiffhsv=[]
    ppadiffhtf=[]
    ppadifflsv=[]
    ppadiffltf=[]

    appdv=[]
    apdv=[]
    adv=[]

    avroc=[]
    apvroc=[]

    amfi=[]
    apmfi=[]
    appmfi=[]

    amdi=[]
    apmdi=[]
    appmdi=[]

    amdm=[]
    apmdm=[]
    appmdm=[]

    avar=[]
    apvar=[]
    appvar=[]
    
    acor=[]
    apcor=[]
    appcor=[]

    pddiff=[]
    ppddiff=[]

    phdiff=[]
    pphdiff=[]

    ptdiff=[]
    pptdiff=[]

    clfvroc=[]
    clwmadiff=[]

    clagain=[]
    
    ahrsi=[]

    clustterrr=str

    tpaths='CoinsDataV3/THETA/FiveMinData.xlsx' 
    tdft = pd.read_excel (tpaths, sheet_name='data')
    "print('opens',opens)"
    "print('len',len(opens))"
    for tp in range(len(tptkys)):

        ahrsi.append(hrsi[tptkys[tp]])

        clfvroc.append(rc[tptkys[tp]])
        clwmadiff.append(wdf[tptkys[tp]])

        clagain.append(edgain[tptkys[tp]])
        
        "print('key',tptkys[tp])"
        adiffhsv.append(dhsv[tptkys[tp]])
        adiffhtf.append(dhtf[tptkys[tp]])
        adifflsv.append(dlsv[tptkys[tp]])
        adiffltf.append(dltf[tptkys[tp]])

        padiffhsv.append(pdhsv[tptkys[tp]])
        padiffhtf.append(pdhtf[tptkys[tp]])
        padifflsv.append(pdlsv[tptkys[tp]])
        padiffltf.append(pdltf[tptkys[tp]])

        ppadiffhsv.append(ppdhsv[tptkys[tp]])
        ppadiffhtf.append(ppdhtf[tptkys[tp]])
        ppadifflsv.append(ppdlsv[tptkys[tp]])
        ppadiffltf.append(ppdltf[tptkys[tp]])

        appdv.append(cppdv[tptkys[tp]])
        apdv.append(cpdv[tptkys[tp]])
        adv.append(cdv[tptkys[tp]])

        avroc.append(vrc[tptkys[tp]])
        apvroc.append(pvrc[tptkys[tp]])

        amfi.append(fi[tptkys[tp]])
        apmfi.append(pfi[tptkys[tp]])
        appmfi.append(ppfi[tptkys[tp]])

        amdi.append(cmdi[tptkys[tp]])
        apmdi.append(cpmdi[tptkys[tp]])
        appmdi.append(cppmdi[tptkys[tp]])

        amdm.append(cmdm[tptkys[tp]])
        apmdm.append(cpmdm[tptkys[tp]])
        appmdm.append(cppmdm[tptkys[tp]])

        avar.append(var[tptkys[tp]])
        apvar.append(pvar[tptkys[tp]])
        appvar.append(ppvar[tptkys[tp]])
        
        acor.append(ccor[tptkys[tp]])
        apcor.append(cpcor[tptkys[tp]])
        appcor.append(cppcor[tptkys[tp]])
        
        #previous
        opn=float(copens[tptkys[tp]])*1000000
        cls=float(ccloses[tptkys[tp]])*1000000
        hgh=float(chighs[tptkys[tp]])*1000000
        lw=float(clows[tptkys[tp]])*1000000
        
        cdaroc.append((((opn+1)/(cls+1))-1)*100)
        cuproc.append((((hgh+1)/(opn+1))-1)*100)
        cdownroc.append((((cls+1)/(lw+1))-1)*100)
        if cls<opn:
            cflagg.append(0)
        elif cls>=opn:    
            cflagg.append(1)
            
        #previous previous
        popn=float(cpopens[tptkys[tp]])*1000000
        pcls=float(cpcloses[tptkys[tp]])*1000000
        phgh=float(cphighs[tptkys[tp]])*1000000
        plw=float(cplows[tptkys[tp]])*1000000
        
        pdaroc.append((((popn+1)/(pcls+1))-1)*100)
        puproc.append((((phgh+1)/(popn+1))-1)*100)
        pdownroc.append((((pcls+1)/(plw+1))-1)*100)
        if pcls<popn:
            pflagg.append(0)
        elif pcls>=popn:    
            pflagg.append(1)
            
        #previous previous previous
        ppopn=float(cppopens[tptkys[tp]])*1000000
        ppcls=float(cppcloses[tptkys[tp]])*1000000
        pphgh=float(cpphighs[tptkys[tp]])*1000000
        pplw=float(cpplows[tptkys[tp]])*1000000
        ppdaroc.append((((ppopn+1)/(ppcls+1))-1)*100)
        ppuproc.append((((pphgh+1)/(ppopn+1))-1)*100)
        ppdownroc.append((((ppcls+1)/(pplw+1))-1)*100)
        if ppcls<ppopn:
            ppflagg.append(0)
        elif ppcls>=ppopn:    
            ppflagg.append(1)
       
        pddiff.append(cdaroc[tp]-pdaroc[tp])
        ppddiff.append(pdaroc[tp]-ppdaroc[tp])

        phdiff.append(cuproc[tp]-puproc[tp])
        pphdiff.append(puproc[tp]-ppuproc[tp])

        ptdiff.append(cdownroc[tp]-pdownroc[tp])
        pptdiff.append(pdownroc[tp]-ppdownroc[tp])

        "configure for each cluster"
    '''
    print('a',cdaroc)
    print('b',cuproc)
    print('c',cdownroc)
    print('d',cflagg)
    '''
    if incnd==1:
        
        hcdaroc=cdaroc
        hcuproc=cuproc
        hcdownroc=cdownroc
        hcflagg=cflagg

        hpdaroc=pdaroc
        hpuproc=puproc
        hpdownroc=pdownroc
        hpflagg=pflagg

        hppdaroc=ppdaroc
        hppuproc=ppuproc
        hppdownroc=ppdownroc
        hppflagg=ppflagg

        hadiffhsv=adiffhsv
        hadiffhtf=adiffhtf
        hadifflsv=adifflsv
        hadiffltf=adiffltf

        hpadiffhsv=padiffhsv
        hpadiffhtf=padiffhtf
        hpadifflsv=padifflsv
        hpadiffltf=padiffltf

        hppadiffhsv=ppadiffhsv
        hppadiffhtf=ppadiffhtf
        hppadifflsv=ppadifflsv
        hppadiffltf=ppadiffltf

        happdv=appdv
        hapdv=apdv
        hadv=adv

        havroc=avroc
        hapvroc=apvroc

        hamfi=amfi
        hapmfi=apmfi
        happmfi=appmfi

        hamdi=amdi
        hapmdi=apmdi
        happmdi=appmdi

        hamdm=amdm
        hapmdm=apmdm
        happmdm=appmdm

        havar=avar
        hapvar=apvar
        happvar=appvar
        
        hacor=acor
        hapcor=apcor
        happcor=appcor

        hpddiff=pddiff
        hppddiff=ppddiff

        hphdiff=phdiff
        hpphdiff=pphdiff

        hptdiff=ptdiff
        hpptdiff=pptdiff

        hclfvroc=clfvroc
        hclwmadiff=clwmadiff

        hclagain=clagain

        'kmeann(1)'
        
        if clustterrr=='cluster 1':
            kmn(4,1)
        elif clustterrr=='cluster 2':
            kmn(4,1)
        elif clustterrr=='cluster 3':
            kmn(4,1)
        elif clustterrr=='cluster 4':
            kmn(4,1)    
        
        
    if incnd==3:
        
        fcdaroc=cdaroc
        fcuproc=cuproc
        fcdownroc=cdownroc
        fcflagg=cflagg

        fpdaroc=pdaroc
        fpuproc=puproc
        fpdownroc=pdownroc
        fpflagg=pflagg

        fppdaroc=ppdaroc
        fppuproc=ppuproc
        fppdownroc=ppdownroc
        fppflagg=ppflagg

        fadiffhsv=adiffhsv
        fadiffhtf=adiffhtf
        fadifflsv=adifflsv
        fadiffltf=adiffltf

        fpadiffhsv=padiffhsv
        fpadiffhtf=padiffhtf
        fpadifflsv=padifflsv
        fpadiffltf=padiffltf

        fppadiffhsv=ppadiffhsv
        fppadiffhtf=ppadiffhtf
        fppadifflsv=ppadifflsv
        fppadiffltf=ppadiffltf

        fappdv=appdv
        fapdv=apdv
        fadv=adv

        favroc=avroc
        fapvroc=apvroc

        famfi=amfi
        fapmfi=apmfi
        fappmfi=appmfi

        famdi=amdi
        fapmdi=apmdi
        fappmdi=appmdi

        famdm=amdm
        fapmdm=apmdm
        fappmdm=appmdm

        favar=avar
        fapvar=apvar
        fappvar=appvar
        
        facor=acor
        fapcor=apcor
        fappcor=appcor

        fpddiff=pddiff
        fppddiff=ppddiff

        fphdiff=phdiff
        fpphdiff=pphdiff

        fptdiff=ptdiff
        fpptdiff=pptdiff

        fclfvroc=clfvroc
        fclwmadiff=clwmadiff

        fclagain=clagain

        'kmeann(3)'
        
        if clustterrr=='cluster 1':
            kmn(2,3)
        elif clustterrr=='cluster 2':
            kmn(2,3)
        elif clustterrr=='cluster 3':
            kmn(2,3)
         
def wrt(cndnlow,cndnhigh,incnd):

    global cp1
    global cp2
    global cp3
    global cp4

    global c1p
    global c2p
    global c3p
    global c4p

    global gainc

    global cndn1
    
    print('low',cndnlow)
    
    if incnd==0:
        cndn1[cp1]=[[],[],c1p,4]
        for cnlw in range(len(cndnlow)):
            cndn1[cp1][0].append(cndnlow[cnlw])
            cndn1[cp1][1].append(cndnhigh[cnlw])
            
        c1p=c1p+4
        cp1=cp1+1
        
    if incnd==1:
        cndn2[cp2]=[[],[],c2p,3]
        for cn2w in range(len(cndnlow)):
            cndn2[cp2][0].append(cndnlow[cn2w])
            cndn2[cp2][1].append(cndnhigh[cn2w])
            
        c2p=c2p+3
        cp2=cp2+1
        
    if incnd==2:
        cndn3[cp3]=[[],[],c3p,2]
        for cn3w in range(len(cndnlow)):
            cndn3[cp3][0].append(cndnlow[cn3w])
            cndn3[cp3][1].append(cndnhigh[cn3w])
            
        c3p=c3p+2
        cp3=cp3+1
        
    if incnd==3:
        cndn4[cp4]=[[],[]]
        for cn4w in range(len(cndnlow)):
            cndn4[cp4][0].append(cndnlow[cn4w])
            cndn4[cp4][1].append(cndnhigh[cn4w])
            
        pnll[cp4]=[gainc,(gainc/2)] 
        cp4=cp4+1 
            
'''
(fvroc,wmadiffc,diffhsv,diffhtf,difflsv,diffltf,pdiffhsv,pdiffhtf,pdifflsv,pdiffltf,ppdiffhsv,ppdiffhtf,ppdifflsv,ppdiffltf,ppdv,pdv,dv,vroc,pvroc,mfi,pmfi,ppmfi,mdi,pmdi,ppmdi,mdm,pmdm,ppmdm,var,pvar,ppvar,cor,pcor,ppcor,opens,closes,highs,lows,popens,pcloses,phighs,plows,ppopens,ppcloses,pphighs,pplows

)

(hroc,hwmadiffc,hdiffhsv,hdiffhtf,hdifflsv,hdiffltf,hpdiffhsv,hpdiffhtf,hpdifflsv,hpdiffltf,hppdiffhsv,hppdiffhtf,hppdifflsv,hppdiffltf,hppdv,hpdv,hdv,hvroc,hpvroc,hmfi,hpmfi,hppmfi,hmdi,hpmdi,hppmdi,hmdm,hpmdm,ppmdm,hvar,hpvar,hppvar,hcor,hpcor,hppcor,hopens,hcloses,hhighs,hlows,hpopens,hpcloses,hphighs,hplows,hppopens,hppcloses,hpphighs,hpplows

)

(rc,wdf,dhsv,dhtf,dlsv,dltf,pdhsv,pdhtf,pdlsv,pdltf,ppdhsv,ppdhtf,ppdlsv,ppdltf,cppdv,cpdv,cdv,vrc,pvrc,fi,pfi,ppfi,cmdi,cpmdi,cppmdi,cmdm,cpmdm,cppmdm,cvar,cpvar,cppvar,ccor,cpcor,cppcor,copens,ccloses,chighs,clows,cpopens,cpcloses,cphighs,cplows,cppopens,cppcloses,cpphighs,cpplows

)

'''

fechdata()
print('cndn1=',cndn1)
print('cndn2=',cndn2)
print('cndn3=',cndn3)
print('cndn4=',cndn4)    
print('cndn=',pnll)


