# 무작위 수를 공백 기준으로 입력받아 홀수와 짝수로 리스트에 나누어 담아 출력

# 해보려고한거 / 택도없었음 리스트 인풋으로 받는것도 모름
"""
list = []
number = int(input("무작위 수를 입력하세요 : ").split())
list.append(number)
print(list)
"""

# 해답
"""
number = list(map(int, input("입력 : ").split())) # 리스트가 바깥
odd = [] # 홀수 리스트 생성
even = [] # 짝수 리스트 생성
for e in number : # number에서 e를 찾음
    if e % 2 == 0 : even.append(e) # e를 2로 나눈 나머지가 0이면 짝수 리스트에 추가
    else : odd.append(e) # 아니면 홀수 리스트에 추가
print(f"홀수 : {odd}") # 홀수 리스트 출력
print(f"짝수 : {even}") # 짝수 리스트 출력
"""

# 조금 더 간단하게
# filter : 조건에 맞는 것만 골라냄 (결과가 참인 것)
# filter도 map과 똑같이 앞에는 함수가 들어가고 뒤에는 수행 데이터가 들어감
# 10개의 리스트를 넣으면 0개가 반환될 수도, 10개가 반환될 수도 있음 (조건에 맞는 것)
# 앞자리는 원래 조건식(함수)이 들어가야 할 자리
# lambda : 1회성 함수를 만들어줌 > 함수 자리에 넣음
# lambda 매개변수 : 표현식 > 요 형태로 입력 # 뒤에 ,~ 이건 범위인듯
# 여기서 x : x % 2 == 1 이라는 함수를 만들어줌 / 콜론 앞 x가 매개변수
"""
number = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda x: x % 2 == 1, number))
even = list(filter(lambda x: x % 2 == 0, number))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")
"""