# 날짜와 시간 관련 함수

# datetime 모듈에서 datetime 함수를 가져옴
"""
from datetime import datetime
print(datetime.today())
"""

# 이렇게 하면 datetime 모듈만 가져온 거
# 출력시 datetime 모듈의 datetime 함수임을 추가 기재해야함
"""
import datetime
print(datetime.datetime.today())
"""

# month랑 hour에만 소괄호가 붙지 않는 이유를 생각해보니
# month랑 hour는 숫자로만 표시돼서 int가 필요함
# date 표시형식은 2024-09-13 형식 / time 표시형식은 10:45:55.628910 형식
"""
from datetime import datetime
print(datetime.today())
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)
print(datetime.today().date())
print(datetime.today().time())
"""

# 달력 모듈
"""
import calendar
print(calendar.calendar(2024))
print(calendar.calendar(2024, m=4))
print(calendar.month(2024,9))
print(calendar.monthrange(2024,9))
"""

# math 모듈 : 수학 관련 기능 처리
"""
import math
print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.ceil(1.000000001)) # 소숫점 이하 올림
print(math.floor(1.99999999)) # 소숫점 이하 내림
print(math.pi)
"""

# log 함수 궁금해서 찾아봄
"""
import math

# 밑이 2인 로그함수 표시 : log2(n)
print(math.log2(5))

# 밑이 10인 상용로그함수 표시 : log10(n)
print(math.log10(5))

# 밑이 e인 로그함수(자연로그) 표시 : log(math.e(n))=log(n)
print(math.log(math.e))
print(math.log(5))

# 밑이 n인 로그함수 표시 : log(n, 밑)
print(math.log(1,5))
print(math.log(1,5)) # 이런식으로 n에 밑 대입, 밑이 5인 로그함수의 경우
"""