# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
# 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
# for 문을 사용
# islower() : 소문자면 True, 아니면 False

# 앞에서 나온 대소문자 바꾸기 예제 : upper(), lower()
"""
a = 'Hello Python Program...'
print(a.upper())
print(a.lower())
"""

# 직접해보기
"""
word=input("단어 입력 : ")
for i in range(0, count())
    print
"""

# 해설
# index가 아니고 element라서 for 'e'
# input은 시퀀스라서 바로 넣을 수 있음
"""
rst = ""
for e in input("입력 : ") :
    if e.islower() :
        rst += e.upper()
    else :
        rst += e.lower()
print(rst)
"""