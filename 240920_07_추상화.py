# 추상화 : 실체화가 되지 않는 부모로부터 상속받는 것
# 부모 클래스 내에 이름만 선언되고 구현부가 없는 추상 메서드를 포함
# 상속받은 클래스는 반드시 추상 메서드에 대해서 구현해줘야 함 (구현하지 않으면 오류 출력)

# 사용자 또는 프로그램 개발자가 연결되는 네트워크에 대한 구조를 몰라도 추상화를 통해 연결 기능을 제공할 수 있음을 보여주는 예제

from abc import * # abc라는 모듈 하위의 함수를 모두 import / 추상 클래스를 사용하기 위해

# 부모 클래스
class NetworkAdapter(metaclass = ABCMeta) : # 해당 클래스를 추상 클래스로 만들어줌
    @abstractmethod
    # 추상 메서드 삽입
    # 부모 클래스 내 이름만 선언, 구현부가 없음
    # 필요하다고 말만 함
    # 파이썬은 구현부가 없으면 자동으로 추상 메서드로 인지, JAVA는 키워드를 넣어줘야함
    def connect(self) :
        pass

# 상속받은 클래스 1
class WiFi(NetworkAdapter) : # NetworkAdapter에서 상속을 받음
    def __init__(self, company) : # 생성자
        self.company = company
    def connect(self) : # 상속받은 클래스에서 추상 메서드에 대해서 구현
        print(f"{self.company} Wi-Fi에 연결했습니다.")

# 상속받은 클래스 2
class FiveG(NetworkAdapter) :
    def __init__(self, company) : # 생성자
        self.company = company
    def connect(self) : # 상속받은 클래스에서 추상 메서드에 대해서 구현
        print(f"{self.company} 5G에 연결했습니다.")

# 상속받은 클래스 3
class Lte(NetworkAdapter) :
    def __init__(self, company) : # 생성자
        self.company = company
    def connect(self) : # 상속받은 클래스에서 추상 메서드에 대해서 구현
        print(f"{self.company} LTE에 연결했습니다.")

net = input("연결할 네트워크를 선택하세요. [1] Wi-Fi  [2] 5G  [3] LTE  :  ")

if net == "1" :
    adapter = WiFi("KT")
    adapter.connect()
elif net == "2" :
    adapter = FiveG("SKT")
    adapter.connect()
elif net == "3" :
    adapter = Lte("LGU+")
    adapter.connect()
else : print("연결 가능한 네트워크가 없습니다.")


# 다중 상속
# 인간으로서의 다중 상속 : 인간으로부터 직장인과 학생을 상속받음
# 개발자는 공부도 하고 일도 하는 특성이 있으므로 학생과 직장인으로부터 상속받음
# 파이썬에서는 다중 상속 가능 / C++의 경우에는 상속의 모호성이 발생함
# 다중 상속의 폐해 : 다이아몬드상속
# 인간 : 밥을 먹는다
# 학생 : 밥을 먹는다, 공부를 한다 (인간 상속)
# 직장인 : 밥을 먹는다, 일을 한다 (인간 상속)
# 개발자 : 밥을 먹는다, 공부를 한다 (학생 상속) / 밥을 먹는다, 일을 한다 (직장인 상속)
# > 개발자는 밥을 두번 먹어야 하는 문제

# 다중 상속 예제 / 파이썬에서는 정상 작동
"""
class Person :
    def __init__(self, eat):
        self.eat = eat
        print("인간입니다.")
    def set_eat(self):
        print(f"{self.eat} 밥을 먹습니다.")

class Student(Person):
    def __init__(self, eat, study):
        Person.__init__(self, eat)
        self.study = study
        print("학생입니다.")
    def set_study(self, study):
        self.study = study
        print("공부합니다.")

class Worker(Person):
    def __init__(self, eat, work):
        Person.__init__(self, eat)
        self.work = work
        print("직장인입니다.")
    def set_work(self, work):
        self.work = work
        print("일합니다.")
    
class Developer(Student, Worker):
    def __init__ (self, eat, study, work):
        Student.__init__(self, eat, study)
        Worker.__init__(self, eat, work)
        print("개발자 입니다.")

dev = Developer(1, 1, 1)
dev.eat = 200
dev.set_eat()
"""

