import sys
import random

# 파이썬 문자열 비교연산자
# 완전 일치 : == !=
# 부분 일치 : in not in
# 전방 일치 : startswith
# 후방 일치 : endswith
A = "501"
B = "501"
C = "50"
D = "2"
print(A == B)
print(A != C)
print(C in A)
print(D not in A)
print(A.startswith(C))
print(A.endswith(D))

# 증감연산자 ++, -- 없음   i+=1,i-=1 이렇게 써야함

# 	    산술 연산자(+,-,*,/,%)
# 	     덧셈 연산
# 	     뺄셈 연산
# 	     곱셈 연산
# 	     오른쪽 피연산자로 좌측 피연산자로 나눗셈 연산
# 	     오른쪽 피연산자로 좌측 피연산자로 나눈 나머지를 구하는 연산
#        Java 에선 거듭제곱이 Math.pow(a,b)로 쓰이지만 파이썬에선 a**b로 표현

# a=True print(!a) Java에 있는 논리부정 연산자 없음


# 	    비트 연산자(&, |, ^, ~ , >>, <<)
#       파이썬은 타입 선언이 없기때문에 비트연산을 위해서는 bin()를 사용한다.
#       표현의 차이만 있을뿐 각 연산자의 역할은 같다
x = 0b0110
y = 0b1010

print(bin(x | y), x | y)
print(bin(x & y), x & y)
print(bin(x ^ y), x ^ y)
print(bin(x << 1), x << 1)
print(bin(y >> 1), y >> 1)
print(bin(~x), ~x)


#    파이썬은 오버플로우가 발생하지 않는다.
a = 2000000000
b = 2000000000
print(a*b)
#  NaN과 Infinity 연산 Java에선 try, catch 로 예외처리하였으나 파이썬에는 try except로 가능
try:
    print(1/0)
    print(1 % 0)
except:
    print("예외가 발생하였습니다.")

# 	   삼항 연산자 자바 [condition] ? [true_value] : [false_value]
#                파이썬 [true_value] if [condition] else [false_value]
aa = 0
bb = 1 if aa == 0 else aa
print(f'{aa=} {bb=}')  # aa=0 bb=1
aa = 60
bb = 1 if aa == 0 else aa
print(f'{aa=} {bb=}')  # aa=60 bb=60

per = random.randrange(1, 50)
print(per)
if per <= 10:
    print("1등급입니다.")
elif per <= 20:
    print("2등급입니다.")
#파이썬도 마찬가지로 순서대로 진행하므로 아래처럼 elif 순서를 잘못 지정하면 일부조건이 누락될 수 있음
elif per <= 40:          #이런 조건부분을 30<per<=40 으로 수정가능함 자바는 안됨 자바는  30<per && per<=40 
    print("4등급입니다.")

elif per <= 30:
    print("3등급입니다.")

else:
    print("5등급입니다.")
