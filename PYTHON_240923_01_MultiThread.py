# 멀티스레드 : 하나의 Application 내에서 여러개의 일을 동시에 수행하는 것
# 스레드 : 하나의 프로세스 내에서 독립적으로 실행될 수 있는 작은 실행 단위
# 동시에 여러 작업 처리 가능
# 파이썬은 threading 모듈을 제공하여 스레드 생성 및 관리 가능

# 스레드 생성 절차
# 1) 모듈 임포트 import threading
# 2) 스레드로 실행할 함수 생성 def ~
# 3) 스레드로 객체를 생성하고 함수를 실행 thread = threading.Thread(target=my_function) / thread.start()
# 4) 필요에 따라 스레드가 종료될 때까지 대기 thread.join()

# 스레드로 게임 만들기 예시
# Unit을 상속받아서 Charactor 클래스 만들기
# 생성자를 통해 캐릭터의 능력 부여
# args = / 인자에 넘겨주는 인자가 한 개밖에 없는 경우에도 무조건 튜플을 만들어야 하기 때문에 (value,)와 같은 식으로 튜플을 만들어야 하는 부분을 눈여겨 봐두기

"""
# 시작 전 하단의 터미널 모드에서 pip 설치함 / pip install simple-colors / 터미널 모드에서 컬러를 지원
from simple_colors import * # 터미널 출력 시 컬러를 지원
# *은 '전부 다'를 의미함 / simple_colors에 있는걸 전부다 따옴

import threading # 멀티스레드를 지원하기 위함
import time # sleep()을 사용하기 위함 / 주어진 시간만큼 해당 스레드의 동작을 멈추는 것(일시정지)
import random # 난수 생성

class Unit : # 클래스 이름은 대문자로(파스칼표기법)
    def __init__(self, pp, mp, ph, mh, hp):
        self.pPower = pp  # Physical power 물리공격력
        self.mPower = mp  # Magical power 마법공격력
        self.pHit = ph  # 물리 적중률
        self.mHit = mh  # 마법 적중률
        self.hp = hp  # 체력
        self.isAlive = True  # 생사 여부

    def set_damage(self, damage): # 데미지 설정
        if self.hp > damage: # 체력이 더 크면
            self.hp -= damage # 데미지만큼 체력 깎임
            self.isAlive = True # 살아 있음
        else: # 체력이 더 작으면
            self.isAlive = False # 죽음

    def is_alive(self):
        return self.isAlive

class Character(Unit):  # Unit을 상속받아 캐릭터 클래스를 만듬
    def __init__(self, pp, mp, ph, mh, hp, um, job):
        super().__init__(pp, mp, ph, mh, hp)  # 부모의 생성자 호출
        self.ultimate = um  # 궁극기 특성 추가 / 부모 캐릭터에는 궁극기가 없었음
        self.job = job  # 직업 추가

# 위에는 데미지만 있었는데, 아래는 물리공격, 마법공격, 궁극기 등 공격 기능 추가

    def p_attack(self):  # 물리 공격
        return self.pPower * self.pHit # class Unit

    def m_attack(self):  # 마법 공격
        return self.mPower * self.mHit # class Unit

    def attack_ultra(self):  # 궁극기
        return self.ultimate # class Character(Unit)


# 스레드에서 실행할 함수

def wizard_th(): # 마법사 스레드 (마법사 / 전사 두개 만든다고 가정)
    print(f"{wizard.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1) # 스레드를 시작하기 위해 잠시 쉬고 가라고 임의로 설정함
    while True: # 둘 중에 한명이 죽을때까지 무한 반복
        time.sleep(5) # 한번 공격하고 5초 이따가 다시 공격 / 공격 호흡(흐름)이 너무 빠르지 않게 임의로 설정
        if not warrior.is_alive() or not wizard.is_alive(): # 둘 중에 하나가 죽으면
            break # 멈춰
        perform_attack(wizard, warrior)


def perform_attack(attacker, defender): # 공격 / 방어
    val = random.choice(["physical", "magical"]) # 물리공격, 마법공격 중 랜덤으로 하나 나감, 랜덤 게임 / val 값은 둘중에 하나
    ul = random.randrange(0, 18)

    if val == "physical": # 물리공격
        damage = attacker.p_attack()
        print(f"{blue('물리공격')} >> {defender.job}에게 {yellow(f'{damage:.2f}')} 데미지를 입혔습니다.")
    else: # 마법공격
        damage = attacker.m_attack()
        print(f"{yellow('마법공격')} >> {defender.job}에게 {yellow(f'{damage:.2f}')} 데미지를 입혔습니다.")

    defender.set_damage(damage)
    print_status(defender)

    if ul == 1:
        damage = attacker.attack_ultra()
        print(f"{red('궁극기 발동')} >> {defender.job}에게 {red(f'{damage:.2f}')} 데미지를 입혔습니다.")
        defender.set_damage(damage)
        print_status(defender)


def print_status(character):
    if character.is_alive():
        print(f"남아 있는 {green(character.job)}의 체력은 {blue(f'{character.hp:.2f}')} 입니다.")
    else:
        print(f"{green(character.job)}가 죽었습니다. 게임을 종료 합니다.")


# 메인 영역
if __name__ == "__main__":  # main thread 흐름을 타는 시작점 / entry point

    name1 = input("전사는 강력한 체력의 물리공격형 캐릭터 (이름 입력) : ")
    name2 = input("마법사는 강력한 마법 공격형 캐릭터 (이름 입력) : ")

    warrior = Character(8, 2, 0.8, 0.5, 150, 40, name1)  # 물공, 마공, 물적, 마적, 체력, 궁극기
    wizard = Character(2, 20, 0.5, 0.9, 60, 55, name2)  # 물공, 마공, 물적, 마적, 체력, 궁극기

    x = threading.Thread(target=wizard_th)
    print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    x.start()  # 서브 스레드 시작

    while True:
        time.sleep(5)
        if not warrior.is_alive() or not wizard.is_alive():
            break
        perform_attack(warrior, wizard)
"""

# 스레드 동기화 : 여러 스레드가 동일한 자원에 접근할 때 발생할 수 있는 문제를 해결하기 위해 동기화 필요
# threading 모듈은 여러 도구 제공, 그 중 하나가 Lock 객체
"""
import threading

lock = threading.Lock()
shared_resource = 0

def increment():
    global shared_resource
    for _ in range(100000):
        lock.acquire()
        shared_resource += 1
        lock.release()

# 두 개의 쓰레드를 생성
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# 쓰레드 시작
thread1.start()
thread2.start()

# 쓰레드가 종료될 때까지 기다림
thread1.join()
thread2.join()

print(shared_resource)
"""