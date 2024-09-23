# 표준 입출력 : 콘솔 입출력을 의미
# [] 대괄호 : 리스트를 표시할 때 사용
# {} 중괄호 : 딕셔너리를 표시할 때 사용
# () 소괄호 : 함수의 인수를 표시할 때, 튜플을 할 때 사용
# 파이썬에서 데이터를 출력하는 방식은 리스트, 딕셔너리밖에 없음(튜플도 리스트에 포함)
# 자바는 여러 방식이 있지만, 파이썬은 그 두가지가 너무 강력해서 다른 필요가 없음

# print() : 화면 출력을 위한 함수
print(36) # 정수 값 출력
print("문자열") # 문자열 출력
print([1,2,3]) # 리스트 출력
print("파이썬") # '파이썬' 문자열 출력
print("파"+"이"+"썬") # 플러스 + : 문자열을 이어주는 연산
print("파","이","썬") # 콤마 , : 구분자를 의미, 구분자의 기본값은 공백
print("파","이","썬", sep="")
print("파""이""썬") #

# 이스케이프 문자 : 출력 구간의 흐름을 제어
# 따라서 그냥 넣으면 안되고 출력 구간(따옴표) 안에 넣어줘야 함
# 이스케이프 문자는 모든 언어의 공통사항
# 이스케이프 문자 사용은 앞에 백슬래시(back slash, \) 사용
# \n : New Line, 줄바꿈
# \t : Tab, 탭
# \b : Backpace, 백스페이스
# \r : Carriage Return, 커서를 맨 앞으로 돌림
print("파이썬줄바꿈1","\n") # 이렇게 하면 두줄 바꿈, 기본적으로 end가 포함되어 있음
print("파이썬줄바꿈2","\n","\n",end="\n") # 이렇게 하면 세줄 바꿈
print("파이썬줄바꿈3","\n", end="")
# 기본값이 sep은 띄어쓰기, end는 줄바꿈, split은 공백
print("Banana\b")
print("Banana\rApple")
print("Banana","Apple",sep="*")

year = 2024 # 종속값 설정
month = 9 # 종속값 설정
day = 10 # 종속값 설정
print(f"{year}",f"{month}",f"{day}",sep="-")
print(year,month,day,sep="-")


# 퍼센테이지 차는 \r 이스케이프 문자 예시
"""
import time
for i in range(1,101): # 1에서 101 미만
    time.sleep(1)
    print(f"\r{i}%",end="")
"""

# 출력 스타일 정리 값 예시
name = "쿵"
age = 12
gender = "여"
job = "개발자"
addr = "서울특별시"

# 서식지정자 스타일 (C언어 방법, %방식, 문자는 s타입 / 숫자는 d타입)
print("======== 서식 지정자 스타일 ========")
print("이름 : %s\n성별 : %s"%(name,gender))
print("나이 : %d"%age)
print("주소 : %s"%addr)


# 파이썬 올드 스타일
print("======== 파이썬 올드 스타일 ========")
print("이름 : {}\n성별 : {}".format(name,gender))
print("주소 : {}".format(addr))


# 파이썬 현재 스타일, f는 포맷을 지정 / f스트링을 쓰겠다.
print("======== 파이썬 현재 스타일 ========")
print(f"이름 : {name}\n성별 : {gender}")
print(f"주소 : {addr}")

# 문자열 연결 연산자 사용 방식
# 문자열 연결 연산자이기 때문에, 숫자로 표시되는 나이는 문자열이 아니어서 오류
# 숫자 출력의 경우 형을 바꿔주는 str로 입력
print("======== 문자열 연결 연산자 사용 방식 ========")
print("이름 : " + name)
print("나이 : " + str(age))

# 정렬 가이드 값 예시
num1 = 10
num2 = 100
num3 = 1000
num4 = 10000
num5 = 3.1415924898617893
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

# 가이드 | 로 알아보기 쉽게 정리
print(f"|{num1}|")
print(f"|{num2}|")
print(f"|{num3}|")
print(f"|{num4}|")

# 콜론 : 뒤 숫자는 해당 숫자의 값만큼 우측 정렬로 출력, :>와 동일(:=>:, 우측 정렬이 기본)
print(f"|{num1:5}|")
print(f"|{num2:5}|")
print(f"|{num3:5}|")
print(f"|{num4:5}|")

# 콜론 : 뒤 ^ + 숫자는 해당 숫자의 값만큼 중앙 정렬로 출력
print(f"|{num1:^5}|")
print(f"|{num2:^5}|")
print(f"|{num3:^5}|")
print(f"|{num4:^5}|")

# 콜론 : 뒤 < + 숫자는 해당 숫자의 값만큼 좌측 정렬로 출력
print(f"|{num1:<5}|")
print(f"|{num2:<5}|")
print(f"|{num3:<5}|")
print(f"|{num4:<5}|")

# 콜론 : 뒤 . + 숫자 + f는 해당 숫자만큼의 소수점까지 출력
print(f"{num5:.3f}")