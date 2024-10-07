# 제어문 : 조건문과 반복문의 의미
"""
num = int(input("정수값 입력 : "))
if num >= 0 :
    print(f"{num}은 양수입니다.")
else :
    print(f"{num}은 음수입니다.")

if num > 100 :
    print(f"{num}은 100보다 커요")
elif num < 100 :
    print(f"{num}은 100보다 작아요")
else :
    print(f"{num}운 100과 같아요")
"""

# 실습문제
# 성적을 입력 받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력했다고 표기
# 성적은 0 ~ 100
# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C
# 60점 이상이면 D
# 나머지는 F


# 다예풀이
"""
score = int(input("성적을 입력하세요 : "))
if score < 0 or score > 100 :
    print(f"성적을 잘못 입력했습니다.")
elif score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")
"""

# 선생님(중첩if)
"""
score = int(input("성적 입력 : "))
if 0 <= score <= 100 :
    if score >= 90 : print("A")
    elif score >= 80 : print("B")
    elif score >= 70 : print("C")
    elif score >= 60 : print("D")
    elif score >= 0 : print("F")
else : print("잘못 입력하셨습니다.")
"""

# 세자리 정수를 입력받아 100의 자리, 10의 자리, 1의 자리로 나누어 담고
# 이 중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if ~ else 문으로 값 비교
# ex) 456일 때, a=4, b=5, c=6으로 c가 제일 큼
"""
num = int(input("세자리 정수 입력 : "))
a = num // 100
b = num % 100 // 10
c = num % 10
if a > b :
    if a > c : print(a)
    else : print(c)
else :
    if b > c : print(b)
    else : print(c)
"""

