# 달력(양력)은 지구가 태양을 공전하는 시간을 기준으로 작성
# 양력에서의 1년은 지구가 태양을 1바퀴 도는데 걸리는 시간
# 시간은 365일+1/4일만큼 걸린다.

# 윤년의 조건
# 연도가 4로 나누어떨어진다.
# 100으로 나누어 떨어지면 연도는 윤년이 아니다.
# 400으로 나누어 떨어지면 윤년이다.

"""
if 조건문 :
print(f"참인 경우")
else :
print(f"거짓인 경우")
"""
year=int(input("연도를 입력하세요 : "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print(f"{year}년은 윤년입니다.")
else :
    print(f"{year}년은 윤년이 아닙니다.")