# 모듈과패키지 이름에 숫자 및 언더바가 많이 들어있어서 정상 작동 안됨
# 모듈과패키지 파일을 '모듈과패키지.py' 으로 변경해서 사용

"""
# import 모듈이름 : 전체를 가져올 때 (모듈이 포함된 경로 표시 필요)
import 모듈과패키지
print(모듈과패키지.add(100, 200))
print(모듈과패키지.sub(200, 20))

get_pwd = 모듈과패키지.password("http://naver.com")
print(get_pwd)

# from 모듈이름 import 모듈함수 : 모듈 파일에서 특정 함수만 가져올 때
from 모듈과패키지 import add, sub, password
print(add(100, 200))
print(sub(200, 20))

get_pwd = password("http://naver.com")
print(get_pwd)


if __name__ == "__main()__" :
    print(add(1, 4))
    print(sub(4, 2))
"""