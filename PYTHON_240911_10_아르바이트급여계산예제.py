# 주/야간 근무시간을 입력받아 아르바이트 급여 계산하기
# 주간 근무 시급 : 9860원
# 야간 근무 시급 : 주간 근무 시급 * 1.5배
# [입력] 주간 근무 [1], 야간 근무 [2] 를 입력하세요 :
# [입력] 근무 시간을 입력하세요 :
# [출력] print(f"{근무시간}시간 동안 근무한 {근무타입문자열} 급여는 {급여}원 입니다.)

type = int(input("주간 근무 [1], 야간 근무[2]를 입력하세요 : "))
hour = int(input("근무 시간을 입력하세요 : "))
payperhour = 9860
if type == 1 :
    pay = hour * payperhour
else :
    pay = hour * payperhour * 1.5
type_str = type == 1 and "주간" or "야간"
pay_str = f"{pay:,.0f}" # 기존 :.0f는 소숫점 표시 하지 않게, 사이에 ,는 천자리 표시 - 챗GPT 팁임..
print(f"{hour}시간동안 근무한 {type_str} 급여는 {pay_str}원 입니다.")