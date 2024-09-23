# 함수 : 코드의 특정 블럭을 하나의 이름으로 묶는 것
# 코드의 재사용성을 높이고 가독성을 향상시킴

# 함수는 매개변수 및 반환값을 가질 수 있음 (없어도 됨)
# 식별자는 스네이크 표기법(소문자 및 언더바)으로 작성
# 식별자 뒤에 소괄호()가 있음 - 매개변수를 넣는 부분
# 일반적으로 매개변수의 개수와 함수 호출 인자의 개수가 일치해야 함
# 일치하지 않아도 되는 경우 : default 매개변수 사용시, 튜플 형태로 지정시
# 매개변수(Parameter) : 함수 정의시 지정한 변수
# 가변 매개변수 : 매개변수를 원하는만큼 받을 수 있는 함수 (Java에도 있음)
# 기본 매개변수 : 매개변수에 값을 넣지 않으면 기본값으로 들어감 (Java에는 없음)
# 인자(Argument) : 함수 호출시 실제로 넘겨주는 값
# 리턴값 : 함수를 수행하고 결과값 반환 (호출한 위치로)

# def 키워드를 사용해서 정의 (파이썬의 특징, 다른 많은 언어들은 키워드를 사용하지 않음)
# Java, C++는 키워드가 없고 반환 타입에 대한 데이터형이 있음
# Javascript는 Function이라는 키워드 사용

# 호출 : 함수를 실행하는 행위 / 호출하지 않으면 함수는 실행되지 않는 코드
# 여러 함수를 쭉 선언해두고 필요할 때 불러서 씀
# 함수 선언구 내에는 들여쓰기를 해서 내부에 내용 써야 함

# 함수의 반복호출
# 반복호출을 하기 위한 함수 만들어보기 예제 1) 네임카드 만들기
# 매개변수는 존재하고 반환값은 없는 함수 선언
"""
def name_card(name, addr, phone, position) : # 함수를 선언하고 매개변수로 4개의 값을 입력받음
    print(f"{position} : {name}")
    print(f"전화번호 : {phone}")
    print(f"주소 : {addr}")
    print("="*30)

# 함수 호출해주기, 하나만 호출했을 때는 크게 의미 없지만 여러개 호출시 간편함
name_card("팜하니", "서울시 강남구 역삼동", "010-0000-0000", "Angel")
name_card("킴민지", "서울시 강남구 삼성동", "010-1111-1111", "Leader")
name_card("모다니", "서울시 강남구 신사동", "010-2222-2222", "Sunflower")
"""

# 반복호출을 하기 위한 함수 만들어보기 예제 2) 은행 계좌 개설하기
# 매개변수와 반환값이 모두 있는 함수 선언
"""
def open_account(name) :
    print(f"{name}님의 계좌를 개설하였습니다.")
    return name # 반환값을 안받아도 되기 때문에 생략 가능 (아래 호출에서 입력값을 받아 넣어줌 input)

def deposit(balance, in_val) : # 잔액과 입금 금액을 매개변수로 전달받음
    print(f"{in_val}원이 입금되었습니다. 잔액은 {balance + in_val}원 입니다.")
    return balance + in_val # 기존 잔액에서 입금 금액을 더해서 반환

def withdraw(balance, out_val) : # 잔액과 출금 금액을 매개변수로 전달받음
    if balance >= out_val : # 출금 금액이 기존 잔액보다 큰 경우에만 출금 가능
        print(f"{out_val}원이 출금되었습니다. 잔액은 {balance - out_val}원 입니다.")
        return balance - out_val
    else : # 잔액이 부족한 경우
        print(f"출금을 실패했습니다. 잔액은 {balance}원 입니다.")
        return balance

# 함수 호출해주기
balance = 0 # 외부에서 선언한 변수 / 잔액 0원으로 초기화
name = input("계좌를 개설할 이름을 입력하세요 : ")
name = open_account(name) # 인자값으로 입력한 이름을 반환값으로 되돌려받음
# 잔액 0원인 상태에서 1000원 입금
balance = deposit(balance, 1000) # 외부에서 선언한 잔액을 인자값으로 전달, 입금액을 인자값으로 전달
balance = deposit(balance, 2000) # 2000원 더 입금함, 전체 입금 금액 3000원
balance = withdraw(balance, 500) # 500원 출금함
# 잔액 출력해보기
print(f"{name}의 잔액은 {balance}원 입니다.")
"""

# 계속 업데이트되는 잔액 부분이 함수에서는 계속 신경써줘야하는데 클래스를 사용하면 간편하게 해결 가능
# 클래스형태의 객체로 만든다면 상태값을 저장할 수 있음
# 클래스의 메서드와 필드(변수값)으로, 이전값을 저장할 수 있음 ex) TV 껐다 켜도 음량이 이전 상태로 저장되어 0부터 시작되지 않음
# 클래스 심화예제
"""
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        print(f"{self.name}님의 계좌가 개설 되었습니다.")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} 입금 되었습니다. 잔액은 {self.balance}입니다.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"출금 되었습니다. 잔액은 {self.balance}입니다.")
        else:
            print(f"출금이 실패 했습니다. 잔액은 {self.balance}입니다.")

# 사용 예시
account = BankAccount("팜하니")
account.deposit(1000)
account.withdraw(500)
print(f"{account.name}의 잔액은 {account.balance}입니다.")
"""

# 기본값 인자 : 함수 선언 시 매개변수에 대한 기본값을 정의
# 기본값을 정의할 수 있는 언어가 많지 않음 : 파이썬, C++ 가능 / Java, C, Javascript는 기본값 인자가 없음 / Java는 오버로딩과 겹침
# 매개변수에 기본값이 정의되어 있는 경우 호출시 인자값을 넣지 않으면 기본값 호출
"""
def profile(name, grade = 2, age = 18, school = "태양고등학교") :
    print(f"이름 : {name}, 학교 : {school}, 학년 : {grade}, 나이 : {age}")

# 함수 호출
# name은 기본값(default 매개변수)이 정의되지 않았으므로(기본값 인자가 아니므로) 넣지 않으면 오류 출력
profile("나희도")
profile("고유림")
# profile에 정의된 순서대로 왼쪽부터 채워지거나 비워짐
# print는 그냥 우리가 출력으로 지정한 순서라서 의미없음
# 아래 출력값의 순서 확인
profile("백이진", None, 22)
"""

# 가변 매개변수 : 함수의 매개변수 앞에 *별을 붙여주면, 함수의 매개 변수(인자값으로)를 몇개를 입력하든 함수 내에서 튜플로 인식하여 처리 가능
# Java에도 있고 파이썬에도 있고 C++에도 있고 C는 없음 / 사용하는 방식은 다름
# * : '전부 다'를 의미한다고 생각하면 좋을 듯 (터미널 등 명령에서도 많이 쓰임) / 모든 걸 다 받아들이겠다
# 패킹과 언패킹 개념 활용

# 무수히 많은 lang을 받아서 튜플(시퀀스형 데이터)로 인식하겠다.
# 왜 리스트가 아니고 튜플일까? 전달받은 값이 바뀌면 안되기 때문(이뮤터블)
"""
def profile(name, age, *lang) :
    print(f"이름 : {name}, 나이 : {age}", end = " ") # end는 출력 이후에 뭐 할건지 결정
    for e in lang : # 향상된 for문 , lang에 대한 시퀀스형 데이터를 for문으로 출력하겠다
        print(e, end = " ")
    print()

profile("팜하니", 21, "Python", "Java", "C", "C++", "React", "Kotlin", "Swift")
profile("킴민지", 21, "Python", "Java")
"""

# 지역변수, 전역변수 : 파이썬에서만 특징적으로 다룸, 지금은 대부분의 언어가 다 같아짐
# 대부분의 언어는 블록스코프를 기반으로 변수의 생명주기를 관리
# 블록 : 중괄호 / 블록스코프 기반의 변수 생명주기 관리 : 중괄호 안에서 선언시 중괄호를 벗어나면 소멸함
# 파이썬은 함수스코프 기반의 언어로 외부에서 선언한 변수의 값을 함수 내에서 변경하기 위해서는 global 키워드를 사용해야 함

# 예제) 펜싱 경기, 준비된 칼 10자루에서 시합에 참여하는 학생 수를 입력하여 남아 있는 칼이 얼마인지를 지역변수/전역변수를 사용하여 구현
# 매개변수의 이름과 아규먼트의 이름이 같을 필요는 없음, 변수 자체가 넘어가는게 아니고 변수에 들어가는 값만 들어감
# call by value = 값에 의한 호출
# 'knife -= player' = 'knife = knife - player'

# 전역변수 사용 예시
"""
knife = 10 # 실제 게임에 사용할 칼을 10자루 준비

def game(player) :
    global knife # 전역변수 사용 / 외부 선언 함수를 내부에서 사용하겠다 / knife = 10을 내부에서 바꾼다
    knife -= player # knife = knife - player, 플레이어가 게임에 참여하면 칼이 없어짐(사용하기 때문에)
    print(f"남아 있는 칼은 {knife}자루 입니다.")

in_val = int(input("경기에 참여하는 선수의 수 입력 : "))
game(in_val)
"""

# 지역변수 사용 예시
"""
knife = 10 # 실제 게임에 사용할 칼을 10자루 준비

def game(knife, player) : # 지역변수를 사용, 매개변수를 2개 입력
    knife -= player
    print(f"남아 있는 칼은 {knife}자루 입니다.")

in_val = int(input("경기에 참여하는 선수의 수 입력 : "))
game(knife, in_val) # 매개변수 2개 입력
"""

# 함수 예제) 키를 입력받아 표준체중 구하기
# 키는 cm 단위로 입력받음
# 체중에 대한 출력은 소수점 2자리까지 출력 (반올림 함수 사용)
# round(값, 원하는 소수점 자리수) : 소수점 자리수에서 반올림 / 2라고 입력하면 3에서 반올림해서 2까지 출력
# 남자 표준체중 : 키(m) * 키(m) * 22
# 여자 표준체중 : 키(m) * 키(m) * 21

# 기본답안
"""
def std_weight(height, gender) : # standard weight, 남녀 표준체중이 다르니까 키와 성별을 입력받음
    hm = height / 100 # 입력받은 cm 키를 m 단위로 변경
    if gender == "남" :
        return hm * hm * 22
    else :
        return hm * hm * 21

height = int(input("키 입력 : "))
gender = input("성별(남/여) : ")
weight = round(std_weight(height, gender), 2)
print(f"키 {height}cm {gender}성의 표준체중은 {weight}kg 입니다.")
"""

# 배리에이션
"""
def std_weight(height, gender) : # standard weight, 남녀 표준체중이 다르니까 키와 성별을 입력받음
    hm = height / 100 # 입력받은 cm 키를 m 단위로 변경
    if gender == "1" :
        return hm * hm * 22
    else :
        return hm * hm * 21

h = int(input("키 입력 : ")) # 위 매개변수와 / 본 아규먼트의 변수 이름이 같을 필요는 없음, 위에는 height, 아래는 h로 설정
g = int(input("성별 [1] 남성 [2] 여성 : ")) # 변수 자체가 넘어가는게 아니고 변수에 들어가는 값만 들어감
weight = round(std_weight(h, g), 2)
gender_str = "", "남성", "여성"
print(f"키 {h}cm {gender_str[g]}의 표준체중은 {weight}kg 입니다.") # 성별 표기를 위해 변수 하나를 더 넣어줌
"""

