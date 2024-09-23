# 커피 메뉴 만들기
# [1] 메뉴 보기 [2] 카테고리 조회 [3] 메뉴 조회 [4] 메뉴 추가 [5] 메뉴 삭제 [6] 종료
# 기본 메뉴 만들기
# 딕셔너리에 키, 밸류 이외에 다른 객체를 넣을 수도 있음
# 딕셔너리에 키는 중복될 수 없음
# 카테고리별 조회 추가하기


"""
# 메뉴 생성
menu = {
    "Americano":["Coffee", 2000, "기본 커피 입니다."],
    "Espresso":["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}

# [1] 메뉴 보기 1) 메뉴의 키값으로 돌리기
"""
def print_menu() :
    for key in menu : # menu를 자동순회하면서 key값을 뽑아내 (메뉴에서 키값을 받자)
        print(f"{key} : {menu[key]}")
"""

# [1] 메뉴 보기 2) 아이템 세트로 돌리기

def print_menu() :
    for key, value in menu.items() : # for문에서 뒤에 items 넣으면 앞에 key/value 모두 넣어줘야 함 / 출력이 둘 다 되니까
        print(f"{key} : {value}")


# [2] 카테고리 조회

def get_category(cate) :
    for key, value in menu.items() :
        if cate == value[0] :
            print(key, value[0], value[1], value[2])
        else :
            print("찾는 카테고리가 없습니다.")


# [3] 메뉴 조회(개별 메뉴)

def get_menu(key) :  # key값을 전달받으면 해당하는 커피 이름에 대한 값만 조회
    if key in menu : # 해당하는 key값이 in이면(메뉴에 있으면)
        print(menu[key]) # 메뉴에 대해서 key값을 넣어줌
    else :
        print("찾는 메뉴가 없습니다.")# 아니면 출력될 문구


# [4] 메뉴 추가

def add_menu(key, cate, price, desc) : #key, 분류, 가격, 설명
    if key not in menu : # 해당 key값이 menu에 not in(없으면)이면 추가한다. 해당 key값을 가진 메뉴가 없으면!
        menu[key] = [cate, price, desc] # 하나의 키 값에 카테고리, 가격, 설명부분 추가
        print(f"{key} 메뉴가 추가되었습니다.")
    else :
        print("메뉴가 이미 존재합니다.")


# [5] 메뉴 삭제

def del_menu(key) :
    if key in menu : # 메뉴에 키가 있으면
        del menu[key] # 해당하는 키를 지워줌
        print(f"{key} 메뉴가 삭제되었습니다.")


while True :
    print("메뉴를 선택하세요 : ")
    sel = input("[1] 메뉴 보기 [2] 카테고리 조회 [3] 메뉴 조회 [4] 메뉴 추가 [5] 메뉴 삭제 [6] 종료 : ") # select라는 변수를 만들어줌
    if sel == "1" : # sel 값을 비교해줌 / 1을 불러주면
        print_menu()
    elif sel == "2" :
        key = input("조회할 카테고리 입력 : ")
        get_category(key)
    elif sel == "3" :
        key = input("조회할 메뉴 입력 : ") # 메뉴 이름을 넣어줘야 키값이 동작
        get_menu(key)
    elif sel == "4" :
        key = input("추가할 메뉴 입력 : ") # 추가하고자 하는 메뉴 이름 입력
        cate = input("분류 입력 : ")
        price = int(input("가격 입력 : "))
        desc = input("설명 입력 : ")
        add_menu(key, cate, price, desc)
    elif sel == "5" :
        key = input("삭제할 메뉴 입력 : ")
        del_menu(key)
    elif sel == "6" :
        print("종료합니다.")
        break
    else :
        print("잘못된 입력입니다.")

"""
