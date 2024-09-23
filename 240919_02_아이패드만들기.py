# 현재 시간 및 날짜 가져오는 내장 함수 사용
# 전역 변수 사용
# 시리얼넘버 : 제품의 고유번호이며 유일한 값
# enumerate(반복 개체-시퀀스 자료형, 시작값) : iterable(반복가능한 객체), start(인덱스의 시작값, 기본값은 0)
# if sel in map(str, range(1, len(options) + 1)): sel이 유효한 값인지 확인하는 조건문

"""
from datetime import datetime
import time # sleep함수를 사용하기 위해
make_cnt = 0 # 전역변수, 생산 대수를 구하기 위해 사용

# 공통 함수 만들기 : 유사한 함수의 반복적인 특성을 모아 함수 형태로 만듦
# 바뀌는 부분만 매개변수로 넣어줌 / 옵션에서 개수나 이름의 형태만 달라짐 ex) 색상, 사이즈, 용량, 셀룰러 등

def select_option(prompt, options) : # prompt는 화면에 찍히는 값
    while True : # 제대로 된 입력값이 들어올 때까지 무한 반복
        print(prompt) # 화면에 보여지는 값
        for idx, option in enumerate(options, start = 1) : # 시퀀스 자료형, 시작값
            print(f"[{idx}] {option}")
        sel = input("선택하세요 : ") # 화면에 위 프린트값 'print(f"[{idx}] {option}")'을 띄워 주고 선택하세요를 출력
        if sel in map(str, range(1, len(options) + 1)) : # 1부터 길이만큼(options 길이 + 1만큼) 돌게, map 값(문자)을 반환받으면 / 범위 체크
            return sel

def choice_pad() :
    return select_option("<< iPad Pro 구입하기 >> ", ("구입", "종료"))

def select_screen() :
    return select_option("모델. 원하는 사이즈를 선택하세요.", ("11 모델", "13 모델"))

def select_color() :
    return select_option("색상. 맘에 드는 색상을 선택하세요.", ("실버", "스페이스 블랙"))

def select_storage() :
    return select_option("저장 용량. 원하는 용량을 선택하세요.", ("256GB", "512GB", "1TB", "2TB"))

def select_display() :
    return select_option("디스플레이 글래스. 스탠다드 글래스 또는 Nano-texture 글래스를 선택하세요.", ("스탠다드 글래스", "Nano-texture 글래스"))

def select_network() :
    return select_option("연결성. 인터넷 연결 방식을 선택하세요.", ("Wi-Fi", "Wi-Fi + Cellular"))

def select_name_service() :
    sel = select_option("각인. 무료 각인 서비스로 나만의 iPad Pro 만들기.", ("각인 추가하기", "각인 없음"))
    if sel == "1" :
        return input("문구 입력 : ")
    return "없음"

def make_ipad(screen, color, storage, display, network, name_service) :
    global make_cnt # 외부의 값을 내부에서 변경
    make_cnt += 1 # 생산 대수, 만들어질때마다 1씩 더해짐

    # 선택한 옵션 출력 (튜플 사용)
    screen_options = ("", "11인치", "13인치")
    color_options = ("", "실버", "스페이스 블랙")
    storage_options = ("", "256GB", "512GB", "1TB", "2TB")
    display_options = ("", "스탠다드 글래스", "Nano-texture 글래스")
    network_options = ("", "Wi-Fi", "Wi-Fi + Cellular")

    # 시리얼 넘버 만들기
    # strftime(format, time_tuple) : time 튜플 구조의 timestamp 시간을 지정 포맷에 맞춰 출력
    # 포맷 : %Y(연도), %m(월), %d(일), %H(시간) 등

    serial_screen = "11" if screen == "1" else "13"
    serial_color = "SIL" if color == "1" else "SBL"
    serial_display = "STD" if display == "1" else "NTG"
    serial_network = "W" if network == "1" else "C"
    serial_date = datetime.today().strftime("%y%m%d")

    serial_number = f"iPad{serial_screen}{serial_color}{serial_display}{serial_network}{serial_date}{make_cnt}"

    # iPad 제작 진행 표시 (30초 동안 진행률 표시)
    print("\n아이패드 제작중...")

    for i in range(1, 31) :
      print(f"\r제작중... [{i * 100 // 30}%]", end="") # 진행률 표시
      time.sleep(1) # 1초 대기

    print("\n\niPad Pro가 출고되었습니다.")
    print("=" * 34)
    print(f"화면 크기 : {screen_options[int(screen)]}")
    print(f"제품 색상 : {color_options[int(color)]}")
    print(f"제품 용량 : {storage_options[int(storage)]}")
    print(f"디스플레이 글래스 : {display_options[int(display)]}")
    print(f"네트워크 : {network_options[int(network)]}")
    print(f"각인 : {name}")
    print(f"시리얼 넘버 : {serial_number}")
    print("=" * 34)

while True :
    if choice_pad() == "2" :
        print("iPad Pro 구입을 종료합니다.")
        break

    screen = select_screen()
    color = select_color()
    storage = select_storage()
    display = select_display()
    network = select_network()
    name = select_name_service()
    make_ipad(screen, color, storage, display, network, name)
"""
