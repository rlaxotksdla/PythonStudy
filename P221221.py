#인스턴스별로 존재하는 변수를 인스턴스 변수, 클래스에 속한 변수는 클래스변수 구분
class Simple:
    cv=20 #클래스 변수
    count=0 # Simple 클래스 변수, 생성된 객체의 수를 저장하기 위한 변수
    def __init__(self):
        Simple().count +=1
        self.iv =10 # 인스턴스 변수, 객채별로 존재
    def get_count(self):
        return Simple.count
s= Simple()
print(s.iv) #10 / 인스턴스 변수는 객체를 통해 접근 가능
print(Simple().cv) #20 /클래스 변수는 클래스 이름 또는 객체를 통해 접근 가능
print(s.cv)

def main():
    s1=Simple() #s1  생성
    print(s1.get_count()) #1
    s2=Simple() #s2  생성
    print(s2.get_count()) #2
    s3=Simple() #s1  생성
    print(s3.get_count()) #3

    #하나의 클래스 변수를 3개의 인스턴스로 접근(어떤 인스턴스로든 접근 가능)
    print(s1.get_count()) #3
    print(s2.get_count()) #3
    print(s3.get_count()) #3
    #클래스명으로 get_count() 접근 불가 (self)처리가 안됨 대신 인자를 객체로 전달하면 가능
    print(Simple.get_count(s1)) #3
    print(Simple.get_count(s2)) #3
    print(Simple.get_count(s3)) #3
    #https://goodthings4me.tistory.com/66