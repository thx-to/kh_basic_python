# 예외 처리(exception handling) : 프로그래밍 중 발생하는 여러 가지 오류 상황이 발생할 가능성이 있는 경우에 대해 실행
# try ~ exception을 통해 프로그램의 흐름을 변경

# 1) 문법 오류 : 파이썬에서 제공하는 문법적인 기능을 잘못 사용하는 경우
# 2) 예외 상황(exceptions) : 프로그램 작성 후 실행 도중에 발생하는 여러가지 상황에 대한 것
# 실행 도중에 오류가 발생하게 되면 프로그램이 중지되는 등의 심각한 문제가 발생할 수 있음

# 기본 예외 처리
# 1) 조건문 사용
# 2) try 구문 사용

# try except 구문
# 예외가 발생하는 모든 경우에 대해서 조건문으로 처리하기는 매우 어렵거나 불가능
# 예외가 발생하면 프로그램이 비정상적으로 종료될 수 있지만, 예외처리를 통해 이러한 상황 관리
# try : 예외할 가능성이 있는 코드
# except : 예외가 발생했을 때 실행할 코드
# else : 예외가 발생하지 않았을 때 실행할 코드
# finally : 무조건 실행하는 코드

# 작업을 명령한 파일이 없는 경우 예시
# score.text라는 파일이 없어서 오류 발생
"""
score_file = open("score.text", "r", encoding="utf-8")
print(score_file.read())
score.file.close()
"""

# try 구문으로 예외 처리 1) 파일이 없는 경우 pass (오류 회피하기)
"""
try :
    score_file = open("score.text", "r", encoding="utf-8")
    print(score_file.read())
    score.file.close()
except FileNotFoundError :
    pass
"""

# try 구문으로 예외 처리 2) 파일 이름 입력 후 해당 파일이 없으면 파일이 없다는 문구 출력
"""
try :
    file_name = input("파일 이름 입력 : ")
    score_file = open("score.text", "r", encoding="utf-8")
    print(score_file.read())
    score.file.close()
   
except FileNotFoundError:
    print("파일이 없습니다. 파일 확인 후 다시 진행해 주세요.")
"""

# 나눗셈 계산기 만들기 1) 기본
"""
print("나눗셈 계산기 입니다.")
num1 = int(input("첫번째 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력 : "))
print(f"{num1} / {num2} = {num1 / num2}")
"""

# 나눗셈 계산기 만들기 2) try except 구문 활용
"""
try :
    print("나눗셈 계산기 입니다.")
    num1 = int(input("첫번째 숫자 입력 : "))
    num2 = int(input("두번째 숫자 입력 : "))
    print(f"{num1} / {num2} = {num1 / num2}")
except ValueError :
    print("Error!!! 숫자만 입력하세요.")
except ZeroDivisionError :
    print("나눗셈은 0으로 나눌 수 없습니다.")
else :
    print("정상 처리되었습니다.")
finally :
    print("프로그램 실행 완료!!")
"""

# 나눗셈 계산기 만들기 3) while True로 정상 실행까지 반복
"""
while True : 
    try:
        print("나눗셈 계산기 입니다.")
        num1 = int(input("첫번째 숫자 입력 : "))
        num2 = int(input("두번째 숫자 입력 : "))
        print(f"{num1} / {num2} = {num1 / num2}:.2f")
        break
    except ValueError:
        print("Error!!! 숫자만 입력하세요.")
    except ZeroDivisionError:
        print("나눗셈은 0으로 나눌 수 없습니다.")
    except Exception:
        print(err)
    else:
        print("정상 처리되었습니다.")
    finally:
        print("프로그램 실행 완료!!")
print("프로그램 종료")
"""

