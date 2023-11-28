# lotto
로또번호를 추론할 수 있을거라는 생각에 도전한 프로그램  
(A program that challenged the idea that korean lottery numbers could be deduced.)
## 1. 조합의 갯수 총합.py
이 파일은 모든 경우의 수를 개산하여 번호의 합을 계산함  
(This file calculates the sum of the numbers by estimating the numbers in all cases.)
![image](https://github.com/JSHTIRED/lotto/assets/143377935/9019a759-5c68-4035-94dc-a3d7e0a3f0cd)

## 2. 로또 번호 생성 검증프로그램.py
이 파일은 로또번호를 자체적으로 생성하는 방법과 해당방법으로 제작시 결과를 검증하는 프로그램  
(This file contains a method for generating lottery numbers on its own and a program that verifies the results when produced using that method.)
```py
while True:
    TA=random.sample(number,6)
    AT=set(TA)
    if 생성조건 :
        A=set(AT)
        break
    else:
        continue
```
![image](https://github.com/JSHTIRED/lotto/assets/143377935/4c295211-00b2-439e-9586-ff58d59d217c)

## 3. 프로그램 결과 검증.py
프로그램 결과 검증은 생성된 번호들의 경우의 수 전체를 당첨번호와 비교하여 모든 경우를 실행시 결과에 대한 결과를 보여줌  
(Program result verification compares the total number of generated numbers with the winning number and shows the results when all cases are executed.)
![image](https://github.com/JSHTIRED/lotto/assets/143377935/bd7cec3e-19e0-44c4-9c9b-0fb79881b8f5)

---

