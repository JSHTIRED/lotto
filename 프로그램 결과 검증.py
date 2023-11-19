from itertools import *
import random
Number=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
            26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45])
number=list(Number)
TTT=set([1,2,3,4,5])
YYY=set([6,7,8,9,10])
RRR=set([11,12,13,14,10])
XXX=set([16,17,18,19,15])
PPP=set([21,22,23,24,20])
LLL=set([26,27,28,29,25])
OOO=set([31,32,33,34,30])
KKK=set([36,37,38,39,35])
III=set([40,41,42,43,44,45])
QQQ=set([1,2,3,4,5,6,7,8,9])
WWW=set([10,11,12,13,14,15,16,17,18,19])
ZZZ=set([21,22,23,24,25,26,27,28,29,20])
SSS=set([31,32,33,34,35,36,37,38,39,30])
QWERR=set([30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45])
# 기존 숫자 5단위와 10단위
asd=set([5,10,15,20,25,30,35,40,45])
asg=set([3,6,9,12,15,18,21,24,27,30,33,36,39,42,45])
ash=set([4,8,12,16,20,24,28,32,36,40,44])
asj=set([6,12,18,24,30,36,42])
ask=set([7,14,21,28,35,42])
asl=set([8,16,24,32,40])
asq=set([9,18,27,36,45])
UND=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
# 배수들
while True:
    TA=random.sample(number,6)
    AT=set(TA)
    if len(AT&QQQ)<3 and len(AT&WWW)<3 and len(AT&ZZZ)<3 and len(AT&QWERR)<3:
        TW=set(AT)
        break
    else:
        continue

# 랜덤 번호 추출
RR=set([6,18,28,30,32,38])
A=set([16,18,20,23,32,43])
B=set([1,2,11,21,30,35])
C=set([3,6,14,22,30,41])
D=set([1,10,18,22,28,31])
E=set([4,7,19,26,33,35])

F=set([7,10,19,23,28,33])
G=set([6,11,16,19,21,32])
H=set([3,18,19,23,32,45])
T=set([3,6,9,18,22,35])
J=set([3,6,22,23,24,38])

K=set([20,31,32,40,41,45])
L=set([4,24,27,35,37,45])
M=set([3,10,24,33,38,45])
N=set([7,10,22,25,34,40])
O=set([11,23,25,30,32,40])

P=set([8,13,19,27,40,45])
Q=set([13,20,24,32,36,45])
R=set([4,7,12,14,22,33])
S=set([14,19,27,28,30,45])
RE10=set([22,26,29,30,34,45])
RE9=set([5,17,26,27,35,38])
RE8=set([21,26,30,32,33,35])
RE7=set([6,12,31,35,38,43])
RE6=set([3,5,13,20,21,37])
RE5=set([6,12,17,21,32,39])
RE4=set([2,20,33,40,42,44])
RE3=set([7,16,25,29,35,36])
RE2=set([6,14,15,19,21,41])
RE1=set([12,17,20,26,28,36])
#과거의 결과

past5=RR|A|B|C|D
bbb=(Number-past5)
BBB=set(bbb)
#최근 5회차 미출현 번호
past10=past5|E|F|G|H|T
ddd=(Number-past10)
DDD=set(ddd)
#최근 10회차 미출현 번호
past15=past10|J|K|L|M|N
fff=(Number-past15)
FFF=set(fff)
#최근 15회 미출현 번호
past20=past15|O|P|Q|R|S
hhh=(Number-past20)
HHH=set(hhh)
#최근 20회 미출현 번호

MMS=set([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44])
printlist=list(combinations(Number,6))
# 로또가 될 수 있는 모든 경우의 수
printlist2=set(printlist)
UO=0
YO=0
KO=0
TO=0
SO=0

import sys
for I in printlist2:
        i=set(I)
        if 0<len(i&RR)<=2 and len(i&A)<3 and len(i&B)<3 and len(i&C)<3 and len(i&D)<3 and len(i&
        E)<3 and len(i&F)<3 and len(i&G)<3 and len(i&H)<3 and len(i&T)<3 and len(i&J)<3 and len(i&
        K)<3 and len(i&L)<3 and len(i&M)<3 and len(i&N)<3 and len(i&O)<4 and len(i&P)<4 and len(i&Q)<4 and len(i&R)<4 and len(i&
        S)<4 and len(i&RE1)<4 and len(i&RE2)<4 and len(i&
        RE3)<4 and len(i&RE5)<4 and len(i&RE6)<4 and len(i&RE7)<4 and len(i&RE8)<4 and len(i&RE9)<4 and len(i&
        RE10)<4 and 4<=(len(i&RE1)+len(i&RE2)+len(i&RE3)+len(i&RE4)+len(i&RE5))<=7 and 4<=(len(i&RE6)+len(i&RE7)+len(i&RE8)+len(i&RE9)+
        len(i&RE10))<=7  and 6<=(len(i&
        RE1)+len(i&RE2)+len(i&RE3)+len(i&RE4)+len(i&RE5)+len(i&RE6)+len(i&RE7)+len(i&RE8)+len(i&RE9)+len(i&RE10))<=10 and len(i&
        TTT)<=2 and len(i&YYY)<=2 and len(i&RRR)<=2 and len(i&XXX)<=2 and len(i&PPP)<=2 and len(i&LLL)<=2 and len(i&OOO)<=2 and len(i&
        KKK)<2 and len(i&III)<2 and len(i&QQQ)<3 and len(i&WWW)<3 and len(i&ZZZ)<3 and len(i&QWERR)<3 and 2<=len(i&UND)<=4 and len(i&
        asd)<3 and len(i&asg)<3 and len(i&ash)<3 and len(i&asj)<3 and len(i&ask)<3 and len(i&
        asl)<3 and len(i&asq)<3 and 16.67<=(sum(i)/6)<=30 and 4<=(len(i&RR)+len(i&A)+len(i&B)+len(i&C)+len(i&D))<=6 and 6<(len(i&
        RR)+len(i&A)+len(i&B)+len(i&C)+len(i&D)+len(i&E)+len(i&F)+len(i&G)+len(i&H)+len(i&T))<=9 and 9<(len(i&
        RR)+len(i&A)+len(i&B)+len(i&C)+len(i&D)+len(i&E)+len(i&F)+len(i&G)+len(i&H)+len(i&T)+len(i&J)+len(i&
        K)+len(i&L)+len(i&M)+len(i&N))<=13 and 15<(len(i&RR)+len(i&A)+len(i&B)+len(i&C)+len(i&D)+len(i&E)+len(i&
        F)+len(i&G)+len(i&H)+len(i&T)+len(i&J)+len(i&K)+len(i&L)+len(i&M)+len(i&N)+len(i&O)+len(i&P)+len(i&
        Q)+len(i&R)+len(i&S))<=20 and 2<=len(i&BBB)<=3 and 1<=len(i&DDD)<=2 and 2<=len(i&MMS)<=4 and len(i&FFF)<2 and len(i&HHH)<2:
        # 로또번호 추출 방법
            UO+=1
            # 조건을 만족하는 경우의 수
            if len(i&TW)==3:
                #5등은 3개 공통
                YO+=1
                #5등 당첨 수
            elif len(i&TW)==4:
                #4등은 4개의 수 동일
                KO+=1
                #4등 당첨수
            elif len(i&TW)==5:
                #3등은 5개의 수 동일
                TO+=1
                #3등 당첨수
            elif len(i&TW)==6:
                SO+=1
                #1등
        else:
            continue
SOM=SO*1000000
#1등 10억원 가정
TOM=TO*1000
#3등 100만원 가정
KOM=KO*50
#4등 5만원
YOM=YO*5
#5등 5천원
ANS=YOM+KOM+TOM+SOM-UO
# 당첨금 - 지불금액
RESU=ANS/10
# 만원 단위로 통일
if 1<=ANS:
    print("승리")
elif ANS==0:
    print("평균")
elif ANS<0:
    print("패배")
print(TW)
print("전체 경우의 수" + str(UO) + "개:" + str(UO/10) + "만원")
print("1등" + str(SO)+ "개" + str(SOM*10)+ "억원" )
print("3등" + str(TO)+ "개" + str(TO)+ "백만원" )
print("4등" + str(KO)+ "개" + str(KO*5)+ "만원" )
print("5등" + str(YO)+ "개" + str(YO/2)+ "만원" )
print("당첨 총합" + str((ANS+UO)/10) + "만원")
print("손익 총합" + str(RESU) + "만원")