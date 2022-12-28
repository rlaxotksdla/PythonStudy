# try:
#   문장1
#   문장2
# except:
#   예외처리
# else:
#   예외가 없으면 실행되는 구절
# finally:
#   마지막에 항상 수행


def calc(values):
    sum = None
    # try...except...else
    try:
       sum = values[0] + values[1] + values[2]
    except IndexError as err:  #자바의 다중 예외처리 여기도 순서가 중요함
        print('인덱스에러')
    except Exception as err:
        print(str(err))
    else:
        print('에러없음')
    finally:
        print(sum)
 
# 테스트
calc([1, 2, 3, 6]) # 출력: 에러없음, 6
calc([1, 2])       # 출력: 인덱스에러, None


def calc(values):
    sum = None
    try:
       sum = values[0] + values[1] + values[2]
    except (IndexError, ValueError):  #자바의 멀티 예외 처리와 동일
        print('오류발생')
 
    print(sum)



    # pass 를 사용한 예제
try:
   check()
except FileExistsError:
    pass           #pass를 사용하면 해당 예외를 무시한다.
 
# raise 를 사용한 예
if total < 0:
    raise #이렇게 쓰면 발생한 예외 종류를 그대로 던진다(자바의 throws 개념)
    raise Exception('Total Error') #이렇게 쓰면 발생한예외 종류를 Exception 종류로 메세지와함께 던진다