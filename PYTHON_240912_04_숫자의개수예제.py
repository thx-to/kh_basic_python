# 실습 1

# 자연수 A, B, C
# A = 150, B = 266, C = 427 이라면, A X B X C = 150 X 266 X 427 = 17037300
# 등장하는 숫자(0 ~ 9)의 개수를 세는 문제
# Hint : 범위 기반 for문 사용, count("찾고자 하는 문자")

# 못하겟당.ㅎ...
"""
a,b,c = map(int,input("자연수 a,b,c를 입력하세요 : ").split(","))
cal = a*b*c
for i in range(1,) :
print(cal)
"""

# 답
"""
a,b,c = map(int, input("정수 입력 : ").split()) # 숫자를 공백 기준으로 입력 받음
print(a * b * c)
cal = str(a * b * c) # 계산된 값을 문자열로 바꿈(str) 개수 세기 위해
for i in range(10) : # 10이라고 넣어야  0 ~ 9 까지의 숫자 범위를 수행
    print(cal.count(str(i))) # 0이라는 문자를 찾아달라는 말
"""

# 실습 2

# 문자열 반전, 문자열을 입력받아 문자열 반전 출력
# ex) ABCDEF > FEDCBA

# 못해..
"""
TEXT = str(input("문자열 입력 : "))
for i in range(1,0-1,-1) :
    print(f"{i}")
"""

# 답
"""
in_str = input("문자열 입력 : ")
for i in range(len(in_str)-1,-1,-1) : # len : 시퀀스 데이터의 문자 개수를 반환 / 거꾸로 찍어야해서 마지막 인덱스를 시작값으로 설정 / ABCDEF라면 길이는 6인데 인덱스는 5(0에서 시작하니까) 전체 길이에서 1을 빼야지 마지막 인덱스가 됨
    print(in_str[i], end="")
"""

# 답 2 (파이썬에서만 통하는 문법)
"""
in_str = input("문자열 입력 : ")
reverse_str = in_str[::-1] # : 처음부터 : 마지막까지
print(reverse_str)
"""