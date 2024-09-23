# 외장함수 : import 해서 사용하는 함수, 별도의 모듈 설치 필요 없이 파이썬에서 기본으로 제공 (무거워지지 않게 필요하면 import 해서 사용)
# import 해서 사용하는 함수는 외장함수 이외에도 외부 모듈이 있음
# 랜덤함수 : 지정한 범위 내에서 임의의 숫자를 만들어 내는 것

"""
import random
rand = random.randint(0,4)# 0 ~ 4
print(rand)
"""

"""
import random
rand = random.randrange(1,2) #1부터 2미만 -> 1
print(rand)
"""

"""
import random
for i in range(10) :
    rand = random.randint(0, 4) # 0 ~ 4 까지의 임의의 값을 생성
    print(rand, end=" ")
print()
"""

"""
import random
for i in range(30) :
    rand = random.randrange(0, 10) # 0 ~ 10 미만, start는 0이라서 생략 가능 (randrange(10))
    print(rand, end=" ")
print()
"""

# 중복되지 않는 로또 번호 생성 : 1 ~ 45 사이의 임의의 수 6개
# 리스트를 사용하고, 리스트 내에 임의로 생성한 번호가 있으면 추가하면 안됨
# if rand not in list :

# 해보려고 한거.. 리스트는 가지도 못함
"""
import random
for i in range(6) :
    rand = random.randrange(1, 46)
    print(rand, end=" ")
print()
"""

# 답 1) while True
"""
import random
print("로또 번호 자동 생성 : ", end="")
lotto = []
while True :
    rand = random.randrange(1, 46)  # 1 ~ 45
    if rand not in lotto :
        lotto.append(rand)
    if len(lotto) == 6 : break # while문은 반복이기 때문에 탈출조건을 넣어줌
print(lotto)
"""

# 답 2) while
"""
import random
print("로또 번호 자동 생성 : ", end="")
lotto = []
while len(lotto) <= 6 :
    rand = random.randrange(1, 46)  # 1 ~ 45
    if rand not in lotto :
        lotto.append(rand)
print(lotto)
"""

# 답 3) 더 줄여보기 / 중복 체크 제외 : 집합을 썼기 때문에 중복 체크 없이도 중복 안됨
"""
import random
lotto = set() # set은 집합 / 중복 제어 가능
while len(lotto) <= 6 :
    rand = random.randrange(1, 46)
    lotto.add(rand)
print(lotto)
"""

