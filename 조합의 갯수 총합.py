from itertools import *
import random
Number=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
            26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45])
printlist=list(combinations(Number,6))
printlist2=set(printlist)
QQQ=set([1,2,3,4,5,6,7,8,9])
WWW=set([10,11,12,13,14,15,16,17,18,19])
ZZZ=set([21,22,23,24,25,26,27,28,29,20])
SSS=set([31,32,33,34,35,36,37,38,39,30])
QWERR=set([30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45])
ST=0
AT=0
AT120=0
AT140=0
AT160=0
AT180=0
AT200=0
WT=0
WT220=0
WT240=0
BT=0
import sys
for printlist1 in printlist2:
    i=set(printlist1)
    if len(i&QQQ)<4 and len(i&WWW)<4 and len(i&ZZZ)<4 and len(i&QWERR)<4:
            if sum(i)<100:
                ST +=1
            elif 200>sum(i)>=100:
                AT +=1
                if 120>sum(i)>=100:
                    AT120 +=1
                elif 140>sum(i)>=120:
                    AT140 +=1
                elif 160>sum(i)>=140:
                    AT160 +=1
                elif 180>sum(i)>=160:
                    AT180 +=1
                elif 200>sum(i)>=180:
                    AT200 +=1
            elif 240>sum(i)>=200:
                WT +=1
                if 220>sum(i)>=200:
                    WT220 +=1
                elif 240>sum(i)>=220:
                    WT240 +=1
            elif sum(i)>240:
                BT +=1
print("90% 로또번호 조합의 합")
print("100미만 : ",ST)
print("100~120 : ",AT120)
print("120~140 : ",AT140)
print("140~160 : ",AT160)
print("160~180 : ",AT180)
print("180~200 : ",AT200)
print("200~240 : ",WT)
print("240이상 : ",BT)
print("[그외>=100~180]")
print(ST+WT+BT+AT200 >= AT120+AT140+AT180)
print("[(100~180)/그외]")
print((AT120+AT140+AT180) / (ST+WT+BT+AT200))
print("[그외>=120~180]")
print(ST+WT+BT+AT200+AT120 >= AT140+AT180+AT160)
print("[(120~180)/그외]")
print( (AT140+AT180+AT160) / (ST+WT+BT+AT200+AT120))
