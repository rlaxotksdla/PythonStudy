class GrandParent:
 def __init__(self):
  self.grandParentValue="GrandParentValue"
 @staticmethod        #static 메소드로 self를 없앨수 있고 당연히 self 인자를 넣지못하므로 고정적인 메소드로만 사용할때 
 def grandParentMethod():
    print("상속 받은 GrandParent의 메소드가 호출되었습니다.")



class Friend:
 friendValue="Empty"
 def __init__(self):
  self.friendValue="Friendvalue"
 @classmethod
 def friendMethod(cls): #class메소드로 cls자체를 인자로 넣어 클래스의 변수를 바꿀수있다. 
    cls.friendValue="Friendvalue + ClassMethod"
    print("상속 받은 Friend의 메소드가 호출되었습니다.")


class Parent(GrandParent):
 def __init__(self):
  super().__init__()
  self.parentValue="ParentValue"
 def ParentMethod(self): #일반 메소드로 인스턴스의 변수를 바꿀수있다.
    self.parentValue="ParentValue + NormalMethod"
    print("상속 받은 Parent의 메소드가 호출되었습니다.")

class Child(Parent, Friend): #Java에서는 클래스 상속은 한개밖에 안되지만 파이썬은 무한대로 가능
 def __init__(self):        #다중 상속시 상속받은 클래스의 생성자를 모두 실행해줘야한다
  Parent.__init__(self)
  Friend.__init__(self)
  self.childValue="ChildValue"

class P221222:
 child=Child()
 print(child.grandParentValue) #Java처럼 부모의 부모 클래스 변수의 접근 가능
 print(child.friendValue) #다중 상속 받은곳의 변수도 당연히 접근 가능

#메소드도 당연히 전부 접근가능
 child.friendMethod()
 print(Child.friendValue)
 child.ParentMethod()
 print(child.parentValue)
 child.grandParentMethod()
