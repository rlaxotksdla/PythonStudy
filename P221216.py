import random


#파이썬에는 switch 메소드가 없으므로 구현을 새로함
def switchExample():
    dicenum=random.randrange(1,6)
    print(dicenum)
    switch(dicenum)

def switch(key):
  num = {
    1 : "'1'이(가) 나왔습니다.",
    2 : "'2'이(가) 나왔습니다.",
    3 : "'3'이(가) 나왔습니다.",
    4 : "'4'이(가) 나왔습니다.",
    5 : "'5'이(가) 나왔습니다.",
    6 : "'6'이(가) 나왔습니다."
    }.get(key, "나올 수 없는 숫자")
  print(num)

switchExample()

def guguExample():
    a=range(2,10)
    b=range(1,10)
    for i in a:
        print(f'{i} 단 입니다.')
        for j in b:
            print(f'{i} X {j} = {i*j}')
        print()  
         
guguExample()


def whileExample():
    speed=0
    inputdata=None
    while inputdata!="3": #input을 통해 입력받은값은 문자열타입
     inputdata=input("---------------------\n1.증속 | 2.감속 | 3.중지\n---------------------\n 선택 : ")
     if inputdata=="1":
        speed=speed+1
        print(f'속도를 증가시킵니다. \n현재속도 : {speed}')
     elif inputdata=="2":
        speed=speed-1
        print(f'속도를 감소시킵니다. \n현재속도 : {speed}')
    print("프로그램을 종료합니다.")
whileExample()


def scannerDIY():
 count=0
 while True:
    try:
      maxNumber=int(input("최대 숫자를 입력하세요.\n>>"))
      if maxNumber>1:
        chosenNumber=int(input(f'뽑고싶은 숫자를 입력하세요.\n  범위 : 1~{maxNumber} \n>>'))
        if 1 <=chosenNumber<=maxNumber:
            number=0
            while number!=chosenNumber:
               number= random.randrange(1,maxNumber)
               count=count+1
               print(f'{count}번째 시도 : {number}를 뽑았다!')
            break
        else :
            print('\033[91m범위 내의 숫자를 입력하세요.\033[0m')

      else:
        print("1보다 큰 수를 입력하세요")
    except:
     print('\033[91m숫자를 입력하세요.\033[0m')
     continue
 print(f'\033[92m정수 1부터 {maxNumber}까지 랜덤으로 추출했을때 {count}번째에서 {chosenNumber}이 나왔어!\033[0m')
scannerDIY()