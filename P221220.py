from P221220_Calculator import Calculator  #자바는 파일명과 클래스명 일치시켜야하지만 파이썬은 from 파일명(확장자 제외) import 클래스명으로 사용가능 방법은 여러가지가 있음
'''from 및import 문을 사용하여 다른 파일에서 Python 가져 오기 클래스
import 및as 문을 사용하여 다른 파일에서 Python 가져 오기 클래스
sys.path.insert()메서드를 사용하여 다른 파일에서 Python 가져 오기 클래스'''  

cal =Calculator('이름')
cal.newName("새로운이름")
cal.powerOn()
cal.add(5,10)
cal.multiple(5,5)
cal.divide(5,7)
cal.sum(89,10,30,25,98,76,56)
cal.batteryCheck()
cal.divide(5,7)
cal.divide(5,7)
cal.divide(5,7)
cal.batteryCheck()
cal.powerOn()
cal.charge()
cal.batteryCheck()