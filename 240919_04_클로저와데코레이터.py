# 클로저 : 함수 안에 내부 함수를 구현하는 것
# 함수와 함수 사이에 내부 변수(함수 내부 변수)를 넣고 그 안에 함수를 넣을 수 있음
# 내부 함수가 외부 함수에 있는 변수값을 사용하기 위해 사용
# 결국 클래스 문법과 같아짐
# 함수에서 클래스의 변수를 사용하는 형태로 사용
# 객체마다 상태값을 저장, 각각의 변수는 따로 움직임 > 요 형태와 비슷하게 만드는 게 클로저
# 클로저를 쓸 것 같으면 객체지향 문법을 쓰는게 더 나아서.. 실무에서 잘 쓰이지는 않음
# 객체지향언어에서 생성된 객체 내부의 메서드가 필드를 참조하는 것과 유사한 개념
# 클로저 사용 예시
"""
def calc() :
    a = 3
    b = 5
    def mul_add(x) : # 함수 안에 함수를 또 넣을 수 있음
        return a * x + b # x값이 a값에도 영향을 받고 b값에도 영향을 받음
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))
"""

# 클로저로 callback 기능 구현해보기
# callback : 특정 버튼을 눌렀을 때 특정 기능 수행 / 특정한 이벤트를 눌러줬을 때 해당하는 함수를 불러주는 것
# ex) 아이폰에서 사진 어플 아이콘을 누르면 사진 어플 실행 (감시하는 역할은 event handler)
"""
import time

def perform_operation(x, y, callback) : # x, y는 일반 변수, callback은 함수를 넣는 부분
    result = 0 # result에 perform_operation에 있는 내부 변수가 전달됨
    for i in range(x) : # x값(현재 함수에서는 10)만큼 대기 이후 callback 함수 호출
        result += i + x + y
        time.sleep(1) # 1초를 기다리고
    callback(result) # 콜백 함수 호출, 클로저의 역할을 해줌 / 변수값이 바뀌어서 callback에 영향을 미침

# callback 함수 만들기(정의)
def callback_function(result) :
    print(f"Opertion result is : {result}")

# callback 함수 불러오기
# perform_opertion 함수를 호출하면서 callback 함수를 전달
perform_operation(10, 20, callback_function)
"""

# 데코레이터 : 함수의 앞뒤에 기능을 추가할 때 사용

# 데코레이터 호출 방법 1)
"""
import datetime

def datetime_deco(func) :
    def decorated() :
        print(datetime.datetime.now()) # 현재 시간에 대한 부분 출력
        func() # func 호출 : 매개변수로 함수를 전달하는 형태
        print(datetime.datetime.now()) # 위 시간과 현재 시간까지의 차이로 함수 실행 시간(경과 시간)을 구함
    return decorated # 반환

@datetime_deco # @는 파이썬에서 데코레이터를 적용하는 기호
def for_sum():
    sum = 0
    for i in range(1, 100000):
        sum += i
    print(sum)

for_sum()
"""

# 데코레이터 호출 방법 2)
"""
import datetime

def datetime_deco(func) :
    def decorated() :
        print(datetime.datetime.now()) # 현재 시간에 대한 부분 출력
        func() # func 호출 : 매개변수로 함수를 전달하는 형태
        print(datetime.datetime.now()) # 위 시간과 현재 시간까지의 차이로 함수 실행 시간(경과 시간)을 구함
    return decorated # 반환

@datetime_deco # @는 파이썬에서 데코레이터를 적용하는 기호
def for_sum():
    sum = 0
    for i in range(1, 100000):
        sum += i
    print(sum)

test = datetime_deco(for_sum)
test()
"""
