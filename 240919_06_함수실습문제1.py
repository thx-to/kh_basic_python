# 입력 받은 수 미만의 소수의 합 구하기
# 소수 : 1과 자기 자신을 제외하고 나누어지지 않는 수
# ex) 12 입력시, 12 미만의 소수는 2, 3, 5, 7, 11 > 다 더하면 28
# HINT : 소수인지 아닌지 판별하는 함수를 만들기
# 반복호출을 해야 하기 때문에 함수로 돌리는게 효율적임
# 함수 사용하지 않고 이중 for문 등 사용해서 구현하는 것도 가능
# 강사님이 이전에 면접때 출제했는데, 아무도 못맞춤.. 한명만 JAVASCRIPT로 도전만하고 성공은못함

# 해보려고한거
"""
def prime_func(n) :
    for i in range(2, n) :
        if n % i != 0 :
            print(sum(i))
            pass
        else:
            return "소수가 아닙니다."

while True :
    n = int(input("정수를 입력하세요 : "))
    if n == prime_func :
        print(sum(i))
    else :
        print("소수가 없습니다.")
"""

# 1단계) 소수를 판별할 수 있는 함수 만들기
"""
def prime_func(n) :
    for i in range(2, n) :  # 1과 자기 자신을 제외
        if n % i == 0 : return False
    return True

num = int(input("정수 입력 : "))
is_prime = prime_func(num)
if is_prime : print("소수입니다.")
else : print("소수가 아닙니다.")
"""

# 2단계) 소수의 합을 구하기 위한 변수 만들기
"""
def prime_func(n) :
    is_prime = True
    for i in range(2, n) : # 1과 자기 자신을 제외
        if n % i == 0 : is_prime = False
    if is_prime : return n # 입력받은 값을 그대로 되돌려줌 / 2인 경우
    else : return 0 # 소수의 합이니까, 소수가 아닌 건 다 걸러버림

num = int(input("정수 입력 : "))
prime_sum = 0
for i in range(2, num) : # 2부터 자기 자신 미만까지 func을 다 불러옴
    prime_sum += prime_func(i)
print(prime_sum)
"""