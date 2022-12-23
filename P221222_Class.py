#파이썬에서 접근제한자로 작동하는것은 실제로 없으나
#상호간의 약속으로 언더 스코어를 쓴다
#아무표시없는것은 public 메소드와 변수 앞에 _하나는 protected , __두개는 private로 사용권장한다.

class Class:
  ACA_NAME="서울학원" #Java에서는 final static private으로 초기 변수값에 직접 접근을 막았지만 파이썬은 대문자를 통해 상호약속하여 표시하고 우회하여 Class에 변수를 할당하여 막는 방법이 있다. 
  address="미등록"
  acanumber="미등록"
  classList=list()
  Students=list()
  def __init__(self,roomNameData,roomNumbData):
    self.ROOM_NAME=roomNameData
    self.ROOM_NUMBER=roomNumbData
    self.teacher="미배정"
    self.classAdd()
  def classAdd(self):
    Class.classList.append(f'반 번호 : {self.ROOM_NUMBER}, 반 이름 : {self.ROOM_NAME} ')
    print(f'{self.ROOM_NUMBER}호의 반이 생성되었습니다.')
  @staticmethod
  def setAddress(adressData):
    Class.address=adressData
    print("학원 주소가 등록되었습니다.")
  @staticmethod
  def getAddress():
    return Class.address
  @staticmethod
  def setAcaNumber(acanumberData):
    Class.acanumber=acanumberData
    print("학원 연락처가 등록되었습니다.")
  @staticmethod
  def getAcaNumber():
    return Class.acanumber
  def getRoomNumber(self):
    return self.ROOM_NUMBER
  def getRoomName(self):
    return self.ROOM_NAME
  def getTeacher(self):
    return self.teacher
  def setTeacher(self,teacherName):
    self.teacher=teacherName
    print(f'{this.roomNumber}호에 교사 {self.teacher}이(가) 배정되었습니다.')
  def addStudent(self,nameInput,ageInput):
    self.Students.append(f'이름 : {nameInput}, 나이 : {ageInput}세')
    print(f'{self.ROOM_NUMBER}호에 {nameInput} 학생이 등록되었습니다.')
  def removeAllStudents(self):
    self.Students.clear()
  def printStudentList(self):
    print(f'{self.ROOM_NUMBER}호의 학생 목록입니다.')
    for Student in self.Students:
      print(Student)
  @staticmethod
  def printAcaInfo():
    print(f'-학원 정보-\n이름 : {Class.ACA_NAME}\n주소 : {Class.address}\n번호 : {Class.acanumber}')
  def printClassInfo(self):
    print(f'{self.ROOM_NUMBER}호의 반 정보입니다.\n반 이름 : {self.ROOM_NAME}\n인원 : {len(self.Students)}명')
  @staticmethod
  def printClassList():
    print(f'현재 {Class.ACA_NAME}의 총 {len(Class.classList)}개의 반 리스트 입니다.')
    for classinfo in Class.classList:
      print(classinfo)
  
a=Class("501호",501)
print(a.ACA_NAME)
print(a.teacher)
print(Class.classList[0])
Class.address="서울-------"
print(Class.getAddress())
a.addStudent("asdf", 124)
a.addStudent("asdf", 124)
a.addStudent("asdf", 124)
a.printStudentList()
Class.printAcaInfo()    
#    public static void printClassList() {//Class자체에서 호출할 용도이므로 static
# 	   System.out.println("현재 "+ acaname+"의 총 "+J221222_Class.classList.size()+ "개의 반 리스트 입니다.");
# 	   for(J221222_Class classlist : classList) {
# 	   System.out.println("반 이름 : "+classlist.roomName+", 반 번호 : "+classlist.roomNumber+", 인원 : "+classlist.students.size()+"명"+", 교사 : "+classlist.teacher);
# 	   }
#    }
#    public static void removeClass(J221222_Class cls) { //메소드에 클래스인자를 넣어 해당 클래스를 제거, 당연하게 classList에서도 제거
# 	   classList.remove(cls);
# 	   System.err.println(Class.roomNumber+"호의 데이터를 삭제합니다.");
# 	   cls=null;
#    }
   
# }

# class Student{
#      final int age;
#      final String name;
#     public Student(String nameInput,int ageInput) {
#     	this.name=nameInput;
#     	this.age=ageInput;
#     }
# }


