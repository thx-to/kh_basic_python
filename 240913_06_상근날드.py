# 입력 1 : 햄버거 가격 3개
# 입력 2 : 음료 가격 2개
# 출력 : 세트 메뉴 가격 = 햄버거 3개 중 가장 싼 것 + 음료 2개 중 가장 싼 것 - 50원
# 입력 예제 : 1000 1500 3000 1200 750 / 5개를 연속해서 입력, 구분은 띄어쓰기
# 출력 예제 : 세트 메뉴 가격 : 1700원

# 풀어보기 / 출력은 맞다
"""
price = list(map(int, input("햄버거 3개와 음료 2개 가격을 입력하세요 : ").split()))
hamburger = (price[0:3])
min_hamburger = min(hamburger)
beverage = (price[3:5])
min_beverage = min(beverage)
print(f"세트 가격은 {min_hamburger + min_beverage - 50}원 입니다.")
"""

# 줄여서 다시 풀어보기 / 해답이랑 비슷해졌다 ^^..
"""
price = list(map(int, input("햄버거 3개와 음료 2개 가격을 입력하세요 : ").split()))
min_hamburger = min(price[0:3])
min_beverage = min(price[3:5])
print(f"세트 가격은 {min_hamburger + min_beverage - 50}원 입니다.")
"""

# 쉬운 해답
"""
ls = list(map(int, input("입력 : ").split()))
min_burger = min(ls[:3])
min_drink = min(ls[3:5])
print(f"세트 가격 : {min_burger + min_drink - 50}")
"""

# 다르게 풀기 / 이거 이해하고 응용하는게 더 중요함
"""
ls = list(map(int, input("입력 : ").split()))
min_burger = ls[0] # 기준값 정하기 / 0번째값이 더 쌀수도 있고 안쌀수도있으니까 / 정해놓고 for문 돌리기
min_drink = ls[3]
for i in range(len(ls)) :
    if i < 3 and min_burger > ls[i] : # 리스트 인덱스 3번째까지의 요소 중에 민버거보다 작으면
        min_burger = ls[i] # 그럼 가장 작은 가격이니까 그걸 i로 한다
    if i > 2 and min_drink > ls[i] : # 리스트 인덱스 4번째부터의 요소 중에 민드링크보다 작으면
        min_drink = ls[i] # 가장 작은 가격이니까 그걸 i로 한다
print(f"세트 가격 : {min_burger + min_drink - 50}")
"""