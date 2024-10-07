# 기본 별찍기

# 강사님
"""
n = int(input("입력 : "))
for i in range(n) : # 행의 개수를 결정
    for j in range(i+1) : # j가 별을 찍어주는 애, 여기에서 range의 범위가 별의 개수 / 따라서 요 range가 이 코드의 핵심 / 0번째는 별이 한개, 1번째는 두개 이런식으로 i+1만큼 별을 찍는거..
        print("*", end="")
    print() # 행의 개수 출력
"""

# 쉬운버전
"""
N = int(input())
for i in range(1, N+1) :
    print("*" * i)
"""


# 기본 별찍기 우측정렬
"""
N = int(input())
for i in range(1, N+1) :
    print(" "*(N-1)+"*"*i)
"""


# 역순 별찍기

# 강사님
"""
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()
"""


# 역순 별찍기 우측정렬

# 강사님
"""
n = int(input())
for i in range(n):
    for k in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end="")
    print()
"""