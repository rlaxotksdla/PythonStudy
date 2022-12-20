import string
import random

def randomName():
  letters_set = string.ascii_letters
  # print(letters_set)
  random_list = random.sample(letters_set,10)
  # print(random_list)
  result = ''.join(random_list)
  # print(result)
  return result

class Calculator:
    def __init__(self,namedata):
     self.power=False
     self.batteryMax=10
     self.battery=5
     self.name=""
     if namedata=="":          #이부분 원래는 Calculator()이렇게 호출하고 싶었는데 안되서 ""로 바꿈 자바는 오버로딩 이용해서 매개변수 입력안하고도 생성이가능한데 아직 방법을 못찾음 ㅠ 처음에 매개변수 이름을 안주고 나중에 메소드로 이름 입력하게 할수는있지만..
        print("계산기의 이름이 지정되지 않았습니다. 랜덤으로 생성됩니다.") 
        self.name=randomName()
        print(f'생성된 이름은 {self.name} 입니다.')
        
     else:
        self.name=namedata
        print(f'계산기가 생성되었습니다. 이름은 {self.name} 입니다.')
    def calcName(self):
      return self.name
    def newName(self,newname):
      self.name=newname
      print(f'계산기의 새로운 이름은 {self.name} 입니다.')
    def powerOn(self):
      if self.power and self.battery>0:
        print("전원이 이미 켜져있습니다.")
      elif self.battery<=0:
        print("배터리가 없습니다.")
      else:
        print("전원을 켰습니다.")
        self.power=True
    
    def powerOff(self):
      if self.power:
        print("전원을 종료합니다.")
        self.power=False
      else:
        print("전원이 이미 꺼져있습니다.")
    def charge(self):
      print("배터리를 충전하였습니다.")
      self.battery=self.batteryMax
    def batteryCheck(self):
      print(f'현재 배터리는 {int(self.battery/self.batteryMax*100)}% 입니다.')
    def add(self,num1,num2):
      if self.power and self.battery>0:
        self.battery=self.battery-1
        print(f'계산 결과는 {num1+num2}입니다. 결과값이 반환됩니다.')
        return num1+num2
      elif self.battery<=0:
        print("배터리가 없습니다.")
        if self.power:
         self.powerOff()
      else:
        print("먼저 전원을 켜주세요.")
    def multiple(self,num1,num2):
      if self.power and self.battery>0:
        self.battery=self.battery-1
        print(f'계산 결과는 {num1*num2}입니다. 결과값이 반환됩니다.')
        return num1*num2
      elif self.battery<=0:
        print("배터리가 없습니다.")
        if self.power:
         self.powerOff()
      else:
        print("먼저 전원을 켜주세요.")
    def divide(self,num1,num2):
      if self.power and self.battery>0:
        self.battery=self.battery-1
        print(f'계산 결과는 {num1/num2}입니다. 결과값이 반환됩니다.')
        return num1/num2
      elif self.battery<=0:
        print("배터리가 없습니다.")
        if self.power:
         self.powerOff()
      else:
        print("먼저 전원을 켜주세요.")
    def sum(self,*nums):
      if self.power and self.battery>0:
        self.battery=self.battery-1
        sumdata=0
        for i in nums:
          sumdata=sumdata+i
        print(f'계산 결과는 {sumdata}입니다. 결과값이 반환됩니다.')
        return sumdata
      elif self.battery<=0:
        print("배터리가 없습니다.")
        if self.power:
         self.powerOff()
      else:
        print("먼저 전원을 켜주세요.")
      
