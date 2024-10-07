# 재귀함수 : 함수 내에서 자기 자신을 호출하는 구조
# 호출될 때는 아무 일도 안하고, 호출 되어서 return문을 만났을 때 되돌아나오면서 값을 계산함
# 길찾기 등의 알고리즘에서 많이 사용(정렬, 검색 등), 효율적인 정렬 알고리즘에서도 사용됨

# 1 ~ n까지의 합을 구하는 여러가지 방법 (for문, while문, 재귀함수)

# 1) for문 사용
"""
def for_sum(n) :
    s = 0
    for i in range(1, n + 1) : # 1부터 n까지의 합을 구함
        s += i
    return s

num = int(input("정수 입력 : "))
print(for_sum(num)) # 함수 호출해서 리턴값이 이쪽으로 옴
"""

# 2) while문 사용
"""
def while_sum(n) :
    s = 0
    while n :
        s += n
        n -= 1
    return s
    
num = int(input("정수 입력 : "))
print(while_sum(num))
"""

# 3) while True문 사용
"""
def while_sum(n):
    s = 0
    while True:
        s += n
        n -= 1
        if n == 0: break
    return s

num = int(input("정수 입력 : "))
print(while_sum(num))
"""

# 4) 재귀함수 사용
# 불려질 때는 아무 것도 안함 / 리턴문이나 종료 조건 필요
# 불릴때는 아무 것도 안하고, 돌아오면서 n값을 더해나가는 구조
"""
def recursive_sum(n) :
    if n == 1 : return 1
    return n + recursive_sum(n - 1)

num = int(input("정수 입력 : "))
print(recursive_sum(num))
"""

# 람다 : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현한 것 / 익명의 함수를 만드는 방식
# 파이썬에서는 람다함수를 통해 이름 없는 함수를 만들 수 있음
# JAVA는 람다가 있는데 사용하기가 불편함 / JAVA는 함수가 없어서(함수가 독립적으로 만들어질 수 없고 항상 클래스 내에 들어가야 하기 때문) 클래스를 만들어줘야 함, 클래스 만들기 불편하니까 인터페이스 사용

# lambda 이해하기
# "square = lambda x : x * x" < 이런 형식이라면, square라는 객체가 lambda의 역할을 해줌
# 함수 이름은 아니고, 변수인데 함수의 형태를 대입받은 것 > def 하지 않아도 됨
# 굳이 이렇게 써야 하는가? 그냥 lambda x : x * x 의 형태면 안되는지?
# 원래 함수가 와야 하는 자린데, 함수를 사용하려면 외부에서 선언하고 이름을 지어줘야 함
# 한번 쓰고 버릴건데 굳이 이름까지 써 줘야 하나? > lambda함수를 만들어냄
# 넣을 수 있는건 한줄짜리밖에 안됨
# 익명의 함수를 만드는 것 > 최근 많이 쓰임

# 함수와 람다 비교
"""
def add(a, b) : # add라는 함수를 만들어줌
    return a + b
print(add(1, 2)) # add 함수 사용
print((lambda a, b : a + b)(1, 2)) # lambda 사용
"""

# filter()함수와 map()함수 : 함수를 매개변수로 전달하는 대표적인 표준함수
# filter(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴값이 True인 것으로 새로운 리스트 구성
# map(함수, 리스트) : 리스트의 요소를 함수에 넣고 새로운 리스트를 구성

# 함수의 매개변수로 함수를 전달(1급 고차함수)하는 법

# 1) 함수 선언해서 불러오기
"""
def power(n) :
    return n * n # 제곱을 만들어주는 함수로 설정
in_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pow_val = list(map(power, in_val)) # in_val을 파워로 바꿔서, 다시 리스트를 씌움
print(pow_val)
"""

# 2) lambda 변수 정의해서 넣기
"""
square = lambda x : x * x # 이름이 없는 함수의 형태
in_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pow_val = list(map(square, in_val)) # lambda 함수를 직접 넣어도 됨
print(pow_val)
"""

# 3) lambda 직접 넣기
"""
in_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pow_val = list(map(lambda x : x * x, in_val)) # lambda 함수를 직접 넣어도 됨
print(pow_val)
"""
