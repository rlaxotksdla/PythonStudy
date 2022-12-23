import numpy as np #numpy를 사용하기위해선 Terminal에서 pip install numpy 명령어로 numpy를 인스톨해줘야한다


# temp = np.array() #이렇게 빈 array는 생성이 안된다
temp = np.array([1,2,3,4,5])
print(temp)
temp = np.zeros(4)
print(temp)
temp = np.ones(4)
print(temp)
temp = np.eye(4) #단위 행렬
print(temp)
temp = np.empty(4) #초기 무작위 데이터
print(temp)
temp = np.arange(5,10,2) # 한개넣으면 0부터 해당 갯수만큼, 두개넣으면 첫수~(마지막수-1)까지 한개씩, 3개넣으면 첫수~ (마지막수-1)까지 x단위로
print(temp)
temp = np.arange(3,13,3)
print(temp)


#배열 복사
#얕은 복사 - 주소값이 복사되므로 기존 배열의 값이 변경되면 복사한 배열의 값도 변경됨
arr = np.array([1,2,3])
new = arr
arr[0] = 3
print(arr)
print(new)

#깊은 복사 - 새로운 주소를 할당하여 배열 복사 기존 배열에 독립적임
arr = np.array([1,2,3])
new = arr.copy()  
arr[0] = 3
print(arr)
print(new)

#파이썬은 리스트가 기본 리스트와 배열의 가장 큰 차이점은 배열 내 값의 타입이 다달라도 되며 , 리스트끼리의 합연산, 선언 후의 값의 추가 특정값의 제거가 가능하다\
listprac=list()  #빈리스트
listprac=list(range(1,5,1)) #1부터 5미만까지 1씩 증가하는 list
print(listprac)
listprac=[89,10,30,25,98,76,56]
print(listprac[0]) #0부터
listprac=[89,"이름",30,25.5,'가격',76,56]
print(listprac) #타입이 달라도 됨
listprac.append(1000)
print(listprac) #값 추가
listprac=listprac+listprac #리스트 합연산
print(listprac)
listprac.remove(1000) #값 제거 중복값 있을 경우 앞에서부터 지움
print(listprac)
listprac[0]=9999 #값 변경
print(listprac)
listprac=[[1,2,3,4],[5,6,7,8],[9,10,11,12]] #2차원 리스트_매트릭스라고도 부름
print(listprac)
listprac=[[1,2,3,4]]*3 #2차원 리스트_매트릭스라고도 부름 이렇게 생성되면 리스트 내 리스트의 값이 얕은복사가되므로 for문을 사용해서 깊은복사를 해야함
listprac[0][0]=0
print(listprac)
listprac= [[1,2,3,4] for i in range(3)]
print(listprac)
listprac[0][0]=0
print(listprac)


def changeCalc():
  while True:
   try:
    price=int(input("물건의 가격은 얼마입니까?"))
    paid=int(input("얼마를 지불했습니까?"))
    moneyunit=[50000,10000,5000,1000,500,100,50,10]
    if paid-price<0:
     print("지불한 금액이 부족합니다.")
    elif paid==price:
     print("거스름돈이 없습니다.")
    else:
     difference=paid-price
     print("거스름돈은")
     for money in moneyunit:
         if int(difference/money)!=0:
          print(f'{money} : {int(difference/money)}개')
          difference=difference-money*(int(difference/money))
     print("입니다.")
    break
   except:
    print("숫자를 입력하세요.")
changeCalc()


#클래스 생성 및 호출 연습
class Calc(object):
    def __init__(self,price,paid):
        print("생성자 호출")
        self.price=price
        self.paid=paid
        

    def result(self): 
        while True:
            try:
                moneyunit=[50000,10000,5000,1000,500,100,50,10]
                if self.paid-self.price<0:
                    print("지불한 금액이 부족합니다.")
                elif self.paid==self.price:
                    print("거스름돈이 없습니다.")
                else:
                    difference=self.paid-self.price
                    print("거스름돈은")
                    for money in moneyunit:
                        if int(difference/money)!=0:
                            print(f'{money} : {int(difference/money)}개')
                            difference=difference-money*(int(difference/money))
                    print("입니다.")
                break
            except:
                print("숫자를 입력하세요.")
C1=Calc(10000, 32500)
C1.result()