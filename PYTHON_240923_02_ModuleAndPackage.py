# 모듈(Module) : 파이썬 코드를 포함하는 파일(.py)
# 함수, 클래스, 변수 등을 포함할 수 있으며, 다른 파이썬 파일에서 임포트하여 사용 가능
# 코드의 재사용성을 높이고 네임스페이스를 구분하여 코드 관리를 용이하게 함

# 패키지(Package) : 모듈의 집합, 여러 모듈을 포함하는 디렉토리
# 코드의 구조화, 재사용성 및 네임스페이스 관리를 위해 사용
# 프로젝트의 규모가 커질 때 모듈을 조직화하고 명확한 계층 구조를 가질 수 있도록 도와줌
# 파이썬은 폴더 구조로 되어 있으며, 디렉토리와 모듈로 구성됨
# __init__.py 라는 특별한 파일을 포함하여 디렉토리를 패키지로 식별
# __init__.py 파일은 패키지를 초기화하는 코드를 넣을 수도 있고 아무 코드 없는 빈 파일일 수도 있음

# 모듈 사용의 기본
# import 모듈이름 : 전체를 가져올 때 (모듈이 포함된 경로 표시 필요)
# 모듈 가져오기
"""
import math # math 모듈을 import
print(math.sin(1))
print(math.cos(1))
"""

# from 구문 : 많은 변수와 함수가 포함된 모듈 전체에서 필요한 일부만 사용
# from 모듈이름 import 모듈함수 : 모듈 파일에서 특정 함수만 가져올 때
# 모듈 내부 함수만 가져오기
"""
from math import sin, cos
print(sin(1))
print(cos(1))
"""

# 모듈 내부 함수 전체 가져오기
"""
from math import *
print(sin(1))
print(cos(1))
"""

# as 구문 : 모듈을 가져올 때 이름 충돌이 발생하는 경우, 긴 이름을 간결하게 사용하고 싶은 경우 등 모듈 이름을 변경하여 사용할 수 있게 하는 구문
# 모듈을 다름 이름으로 사용하기 (모듈 이름을 바꿔 사용하기)
"""
import math as m
print(m.sin(1))
print(m.cos(1))
"""

# sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈
# 명령 매개변수를 받을 때 많이 사용
"""
import sys
print("명령줄 인수 : ", sys.argv) # 명령줄 인수 출력
print("실행 경로 : ", sys.path[0]) # 스크립트 실행 경로
sys.stdout.write("Hello, World!\n") # 표준 출력
sys.stderr.write("Error Occurred!\n") # 표준 오류 출력
sys.exit(0) # 프로그램 종료
"""

# os 모듈 : 파이썬의 표준 라이브러리로, 운영체제와 상호작용하기 위한 기능을 제공
# 파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등 다양한 운영체제 관련 작업 수행 가능
"""
import os

# 현재 작업 디렉토리
cwd = os.getcwd()
print("현재 작업 디렉토리 : ", cwd)

# 디렉토리 생성
os.mkdir("mydir")

# 파일 또는 디렉토리 존재 여부 확인
is_file = os.path.isfile("myfile.txt")
is_dir = os.path.isdir("mydir")
print("myfile.txt는 파일인가?", is_file)
print("mydir은 디렉토리인가?", is_dir)

# 시스템 명령 실행 (OS에 따라 다름, cmd)
# os.system("ls -l") # 윈도우라서 안먹음 - 유닉스 계열의 mac에서는 먹음
os.system("dir") # 윈도우에서 먹음
"""

# 모듈 만들기
# 모듈 함수 만들기
# __name__ == "__main__" 현재 파일이 엔트리 포인트인지 확인할 때 사용
# 다른 파일이나 인터프리터 터미널로 접속할 때는 해당 조건이 거짓이 되어 수행되지 않음
"""
def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

# PYTHON_240911_02_비밀번호만들기예제.py 파일 참고
def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "koong" + "2024"
    return password

if __name__ == "__main__" :
    print(add(1, 4))
    print(sub(4, 2))
"""