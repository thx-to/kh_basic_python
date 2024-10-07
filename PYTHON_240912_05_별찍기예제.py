# 만약 입력이 5라면, 아래와 같이 별찍기가 이루어지게
# *
# **
# ***
# ****
# *****

# 노력해본거
"""
n = int(input("숫자 입력 : "))
for i in range(1,n+1) :
    print(f"i={i}")
    for j in range(n) :
        print("*", end=" ")
        if j % n == 0: print()
    print()
"""

# 답
"""
n = int(input("입력 : "))
for i in range(n) : # 행의 개수를 결정
    for j in range(i+1) : # j가 별을 찍어주는 애, 여기에서 range의 범위가 별의 개수 / 따라서 요 range가 이 코드의 핵심 / 0번째는 별이 한개, 1번째는 두개 이런식으로 i+1만큼 별을 찍는거..
        print("*", end="")
    print() # 행의 개수 출력
"""