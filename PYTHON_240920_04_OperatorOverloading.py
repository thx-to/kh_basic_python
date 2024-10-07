# 연산자 오버로딩 : 내장 연산자들을 사용자 정의 클래스에 대해 다르게 동작하도록 재정의하는 것
# 연산자의 기본 기능을 사용자가 정의할 수 있게 하는 것
# 사용자 정의 객체에 대한 연산을 직관적이고 편리하게 처리 가능
# 오버로딩 : 상황에 맞는 메서드를 자동으로 불러오는 것

# 파이썬(동적타입언어)은 오버로딩은 없고 연산자 오버로딩은 있음
# Java(정적타입언어)는 오버로딩은 있고 연산자 오버로딩은 없음
# C++(정적타입언어)은 오버로딩도 있고 연산자 오버로딩도 있음
"""
def over_sum(x, y) :
    return x + y

print(over_sum(100, 200)) # 정수타입으로 연산 / 정수연산자로 동작
print(over_sum(1.11, 2.11)) # 실수타입으로 연산 / 실수연산자로 동작
print(over_sum("킴민지", "팜하니")) # 문자열 연산 (문자열을 이어주는 연산)
"""

# 좌변과 우변에 객체가 오면 객체끼리도 연산이 될까?
# 기본 기능으로는 안되는데, 연산자 오버로딩으로 만들어낼 수 있음

# 연산자 오버로딩 종류
# __add__(self, other) : + 연산자 대응, 객체끼리의 덧셈 연산 정의
# __sub__(self, other) : - 연산자 대응, 객체끼리의 뺄셈 연산 정의
# __mul__(self, other) : * 연산자 대응, 객체끼리의 곱셈 연산 정의
# __div__(self, other) : / 연산자 대응, 객체끼리의 나눗셈 연산 정의
# __eq__(self, other) : == 연산자 대응, 객체의 동등성 비교 정의
"""
class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __add__(self, other) :
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other) :
        return Vector2D(self.x - other.x, self.y - other.y)

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

# + 연산자가 __add__ 메서드 호출
# 좌변과 우변에 Vector2D라는 객체가 올 때만 동작
# v1은 self, 자기 자신 / v2는 other, 객체로 봄
v3 = v1 + v2

print(v3.x, v3.y)

v4 = 12 + 13 # 정수값 / 객체가 더해진 게 아님
print(v4)
"""

# 파이썬 연산자 오버로딩은 하나밖에 못만듦, 아래와 같이 연산시 오류출력
# 자바에서는 동작
"""
v5 = v1 + 12
print(v5)
"""


