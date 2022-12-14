#인스턴스별로 존재하는 변수를 인스턴스 변수, 클래스에 속한 변수는 클래스변수 구분
class Simple:
    cv=20 #클래스 변수
    count=0 # Simple 클래스 변수, 생성된 객체의 수를 저장하기 위한 변수
    def __init__(self):
        Simple.count +=1
        self.iv =10 # 인스턴스 변수, 객채별로 존재
    def get_count(self):
        return Simple.count
    @staticmethod
    def sm_get_count(): # 매개변수 self가 없이 만들면 static 메소드
        print('static method')
        return Simple.count
    @classmethod
    def cls_get_count(cls): #매개변수에 cls를 기입하면 class 메소드
        print('class method')
        return cls.count
# s= Simple()
# print(s.iv) #10 / 인스턴스 변수는 객체를 통해 접근 가능
# print(Simple().cv) #20 /클래스 변수는 클래스 이름 또는 객체를 통해 접근 가능
# print(s.cv)

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
    #static 메소드 호출
    print(Simple.sm_get_count()) # static method , 3
    #class메소드 호출
    print(Simple.cls_get_count()) # class method , 3
main()

# static과 class 차이 
class Animal:
    language='울음소리'
    def __init__(self):
        self.sound='동물 울음소리 : '+self.language

    @classmethod
    def cls_language(cls): # class 메소드
        return cls()

    @staticmethod
    def sm_language(): # static 메소드
        return Animal()
        
    def show(self):
        return self.sound
        
class Dog(Animal):
    language='멍멍'

a= Animal.cls_language() # class 메소드 호출해서 class 자체를 리턴받기 가능
b= Animal.sm_language() # static 메소드 호출해서 Animal() 클래스 리턴
print(a.show()) # 동물 울음소리 : 울음소리 / 부모클래스의 속성 값
print(b.show()) # 동물 울음소리 : 울음소리 / 부모클래스의 속성 값
c= Dog.cls_language() 
d= Dog.sm_language()
print(c.show()) #동물 울음소리 : 멍멍 / dog cls가 매개변수역할을 해서 들어가서 생성자에 들어감 __int__(dog)
print(d.show()) #동물 울음소리 : 울음소리 / 무슨 클래스에서 .호출을 하든 Animal()클래스가 반환되므로__int__(Animal)


