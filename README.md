# lotto
---로또번호를 추론할 수 있을거라는 생각에 도전한 프로그램---

## 1. 조합의 갯수 총합.py
이 파일은 모든 경우의 수를 개산하여 번호의 합을 계산함  
![image](https://github.com/JSHTIRED/lotto/assets/143377935/9019a759-5c68-4035-94dc-a3d7e0a3f0cd)

## 2. 로또 번호 생성 검증프로그램.py
이 파일은 로또번호를 자체적으로 생성하는 방법과 해당방법으로 제작시 결과를 검증하는 프로그램
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

## 3. 프로그램 결과 검증은 생성된 번호들의 경우의 수 전체를 당첨번호와 비교하여 모든 경우를 실행시 결과에 대한 결과를 보여줌

---

