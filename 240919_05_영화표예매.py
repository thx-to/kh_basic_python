# 함수로 영화표 예매하기
# 사용자로부터 좌석번호를 입력받아 예매하는 시스템, 좌석은 10개
# 예매가 완료되면 해당 좌석값을 1로 변경 (초기값은 0)
# 이미 예매가 완료된 좌석은 재구매 불가
# 좌석당 가격은 12,000원
# 프로그램 종료시 매출액을 출력

"""
seat = [0] * 10 # 0으로 초기화된 10개의 리스트 생성
PRICE = 12000 # 파이썬에는 상수가 없는데 상수처럼(고정된 값) 보이게 하려고 대문자로 넣어봄.. (의미없음)

def print_seat() :
    for e in seat :
        if e == 0 :
            print("[ ]", end = " ") # 좌석을 보여주고 공백을 하나 넣음
        else :
            print("[V]", end = " ")
    print()

# 이부분은 입력예제쪽 참고 (12시간제 변경)
def select_seat() :
    print_seat() # 현재 상태를 한번 보여주고
    seat_num = int(input("좌석번호 입력 : ")) - 1 # 사용자의 입력은 1부터, 리스트의 인덱스는 0부터 시작되기 때문에 1을 빼야 인덱스 숫자와 맞아짐
    if seat[seat_num] == 0 : # 아직 예약되지 않은 좌석 / 0이면
        seat[seat_num] = 1 # 예약이 안된 좌석이므로 예약 진행 / (해당 인덱스에 대한 리스트값을) 1로 만들고
        print_seat() # 예약 성공시 결과 출력 / 체크표시 출력
    else :
        print("이미 선점된 좌석입니다.")

def total_account() :
    cnt = 0 # 판매된 좌석 개수를 누적
    for e in seat :
        if e == 1 :
            cnt += 1
    return PRICE * cnt # 티켓 가격 * 판매 좌석 수

while True :
    print("[1] 예매하기")
    print("[2] 종료하기")
    sel = int(input("메뉴 선택 : "))
    if sel == 1 :
        select_seat()
    else :
        print(f"총 매출액 : {total_account()}")
        break
"""