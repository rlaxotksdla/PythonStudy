import sys #sys.argv 입력값을 받기위해 import해야함
'''파이썬은 자바와 다르게 변수 형식 선언 안함
'''
a=1
b=5
result1=a+b
result2=a*b
result3=a/b
result4= a==b
if result4:
    result4="네"
else:
    result4="아니요"
print("화면에 문자열 출력하기 = 221213")
#print("변수 연산 결과 출력하기 \n a + b = " + result1 +"\n a * b= " + result2 + "\n a / b = " +result3+ "\n a와 b는 같나요? : " + result4 )
print("화면에 sys.argv 입력값 출력하기 - " ,sys.argv[1],",",sys.argv[2]) #python P221213.py 1 2
print("변수 연산 결과 출력하기 \n a + b = " , result1 ,"\n a * b= ",  result2 , "\n a / b = ", result3 ,"\n a와 b는 같나요? : ",  result4 )

