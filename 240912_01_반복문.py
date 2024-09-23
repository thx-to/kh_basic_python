# 반복문 : 조건이 참인 동아 반복 수행
# while문, for문
# while문 : 조건식이 들어가고 참인 동안 조건식 반복
# while문은 주로 횟수가 정해지지 않은 반복적인 수행을 할 때 사용
# while True나 while 1(literal 상수)같이 고정일 때 반드시 exit을 넣어줘야 함(break) - for문도 마찬가지로 반복문을 빠져나갈 때는 탈출조건이 있어야 함
# while True를 하는 경우 : 몇 번 넣어야할 지 모를 때(횟수가 정해지지 않았을 때)
# while문에서 JAVA는 while  n > 0 이런식으로, 0보다 크냐 아니냐로 기재 / 나머지 언어는 while n : 으로, 참이냐 거짓이냐로 기재


# while문 예제
"""
n = int(input("정수 입력 : "))
sum = 0 # 값을 누적하기 위한 변수 / 값을 누적하기 위한 변수는 반드시 초기값을 넣어 줘야 함
while n : # 0이 아닌 모든 값은 참으로 간주 (JAVA 제외)
    sum += n # 10을 입력했을 경우, 1씩 빼서 모두 더함 / 10 + 9 + 8 + ... + 1 = 55
    n -= 1 # n = n - 1 , n값이 참인 동안 계속 반복, 거짓이면 중단
print(sum)
"""

# for문으로 바꾼 예제
"""
n = int(input("정수 입력 : "))
sum = 0 # 초기화해주기
for i in range(1, n+1) : # 범위 기반(range)의 for문 (일정한 크기만큼 돌려줌)
    sum += i
print(sum)
"""

# while True 예제
"""
while True :
    age = int(input("나이를 입력하세요 : "))
    if 0 <= age <= 200 : break # 정상적인 입력이므로 반복문 탈출
    print("나이를 잘못 입력하셨습니다.") # if문이지만 어차피 break가 걸려 있기 때문에 else 생략 가능 / 맞을 경우 위에서 빠져나감
print(f"당신의 나이는 {age}입니다.")
"""

# 어제의 조건문 수정
# 성적을 입력 받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력했다고 표기
# 성적은 0 ~ 100
# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C
# 60점 이상이면 D
# 나머지는 F
# 성적이 잘못 입력된 경우 다시 입력하게 수정
"""
while True :
    score = int(input("성적 입력 : "))
    if 0 <= score <= 100 :
      if score >= 90 : print("A")
      elif score >= 80 : print("B")
      elif score >= 70 : print("C")
      elif score >= 60 : print("D")
      else : print("F")
      break # 올바른 점수 입력했을 경우 탈출
    else : print("잘못 입력하셨습니다.")
    continue # 반복문으로 되돌아감
"""

# for문 : 정해진 범위만큼을 반복 수행할 때 효과적
# for문은 while문보다 조금 더 직관적
# for 요소 in 시퀀스(리스트, 튜플, 문자열, input, stream 등 연속된 자료형은 다 올 수 있음) : 시퀀스 자료에 대한 자동 순회 / 자료(시퀀스) 안에 있는 값들을 처음부터 끝까지 자동 순회하면서 요소 값을 꺼냄
# for 인덱스 in range(시작값, 종료값, 증감값) :
# for문도 매개변수 3개 설정 가능(시작값, 종료값, 증감값)
# 0부터 시작하면 시작값 생략 가능, 1씩 증가하면 증감값도 생략 가능 / 매개변수가 1개라면 종료값

# for 요소 in 시퀀스 예문 1
"""
fruits = ["apple", "banana", "cherry"] # 리스트형 자료형으로 대괄호 사용
for fruits in fruits : # fruits라는 시퀀스형 자료형에서 fruits라는 요소값들을 꺼냄
    print(fruits)
"""

# for 요소 in 시퀀스 예문 2
"""
name = "쿵쿵쿵"
for e in name :
    print(e, end="-")
"""

# for 요소 in 시퀀스 예문 3
"""
for e in input("문자열 입력 : ") :
    print(e, end="-")
"""

# for 인덱스 in range 예문 1
"""
n = int(input("정수 값 입력 : "))
sum = 0
for i in range(1, n + 1, 1) :
    sum += i
print(sum)
"""

# for 인덱스 in range 예문 1-1
"""
n = int(input("정수 값 입력 : "))
sum = 0
for i in range(n + 1) : # 예문 1과 같으나 시작값이 0, 증감값이 1이라 각각 생략하여 매개변수는 종료값 1개만 남김
    sum += i
print(sum)
"""

# 이중 for문 사용하기
"""
n = int(input("정수 입력 : "))
for i in range(n) : # 0에서 n 미만까지 돈다
    for j in range(n) : # i가 0일때부터 n일때까지 j가 각각 n번씩 돌아가므로 결국 i=j=n으로, n*n개의 별이 찍힘
        print("*", end = " ")
"""

# n값씩 줄바꿈 행렬표시
"""
n = int(input("정수 입력 : "))
for i in range(n) :
    print(f"i={i}", end=" ") # 이해하기 쉽도록 별 왼쪽에 i=n 형식으로 표시하게 함(편의상)
    for j in range(n) :
        print("*", end=" ") # j의 별은 띄어쓰기로 구분
    print() # 줄바꿈 / 다시 위로 돌아가서 이전 i값 + 1값으로 j 순회 / i값이 한번 바뀌려면(+1) 내부 for문이 한바퀴 돌아야함
"""

# 2중 for문 구구단 찍기
"""
for i in range(2, 10) :
    for j in range(1, 10) :
        print(f"{i} X {j} = {i * j}")
    print()
"""

# 단 구분 넣어주기(나중에 참고만 하라공..)
"""
for i in range(2, 10) :
    for j in range(1, 10) :
        print(f"{i} X {j} = {i * j}")
    print("-"*10)
"""

# 제어문 : break, continue
# break : 반복문을 탈출할 때 사용
# continue : 아래의 문장을 수행하지 않고 반복문의 조건식으로 다시 이동 / 이 때, 해당 루틴은 수행된 것으로 간주됨)

# 홀수 찍기
"""
n = int(input("정수 입력 : "))
for i in range(n) :
    if i % 2 == 0 : continue # 2로 나눈 나머지가 0일 경우 pass / 해당 수보다 작은 홀수만 찍히게 됨
    print(i)
"""

# 반복문을 반대로(역순으로) 수행하기
"""
n = int(input("정수 입력 : "))
for i in range(n, 0 - 1, -1) : # 초기값은 0부터 시작, 0까지 찍기(0까지 찍으려면 0-1을 해야 함, 1씩 작아지게 / 순서대로라서 그 다음 숫자까지 기입 / 0은 생략 가능 '-1'로만 표기해도 같은 값 출력
    print(f"인덱스 : {i}")
"""

# for문으로 알파벳 출력하기
# 기존 알파벳 등 일부 사용 문자들만 있던 코드가 ASCII 코드 + 추후에 중문, 한글 등 각국의 언어를 추가한 게 유니코드
# 유니코드의 첫 부분은 아스키코드와 같음
# chr() : 유니코드를 입력받아 그 코드에 해당하는 문자를 출력
# ord() : 문자의 유니코드 값을 돌려주는 함수
# 코드 2가지정도는 외우면 좋음 / A=65, a=97 / 대문자가 앞에 있음

# 1) A부터 Z까지의 코드값 출력해보기
"""
for i in range(ord("A"), ord("Z") + 1) :
    print(i, end=" ")
"""

# 2) 해당 코드값을 다시 알파벳으로 변환하기
"""
for i in range(ord("A"), ord("Z") + 1) :
    print(chr(i), end=" ")
"""

# for i in range(2,10)
# 순서 : i=2*j=1, i=2*j=2, ..., i=9*j=10
# print문의 end 매개변수에는 줄바꿈 문자 \n이 기본값으로 설정
"""
for i in range(2,10) : # 2에서부터 9까지의 숫자가 차례대로 i에 대입된다.
  for j in range(1,10) : # 1에서부터 9까지의 숫자가 차례대로 j에 대입된다.
      print(i * j, end=" ")
  print(" ")
"""


"""
def prime_func(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0 : is_prime = False
    if is_prime : return n
    else: return 0

n = int(input("정수 입력 : "))
sum = 0
for i in range(2, n) :
    sum += prime_func(i)
print(sum)
"""

