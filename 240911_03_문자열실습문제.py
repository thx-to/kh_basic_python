# 2개의 문자열을 포인터 변수 s와 k에, 양의 정수를 정수형 변수
# n에 각각 전달받아 s 문자열의 뒤 부분에 n개 문자를 k 문자열 앞에 끼워 넣는 코드 작성
# 예) s : seoul / k : korea / n : 2 / result : ulkorea

# 내가해본거
"""
s = input("포인터 변수 s를 입력하세요 : ")
k = input("포인터 변수 k을 입력하세요 : ")
n = int(input("양의 정수 n을 입력하세요 : "))
result = s[-n:] + k
print(result)
"""

# 해설1
"""
s = input("s : ")
k = input("k : ")
n = int(input("n: "))
print(s[-n:] + k)
"""

# 해설2
"""
s = input("s : ")
k = input("k : ")
n = int(input("n : "))
pos = len(s) - n # pos : position
print(s[pos:] + k)
"""