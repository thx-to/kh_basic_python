# 행사 안내 메일 내용 자동 작성하기
# 이름 : 백이진
# 행사내용 : 현대 자동차 신차 발표회
# 일시 : 20220301 (연속해서 입력)
# 시간 :  14
# 한파의 연속인 1월 입니다.
# 봄을 기다리는 2월 입니다.
# 봄의 기운이 느껴지는 3월 입니다.
# 새싹이 피어나는 4월 입니다.
# 계절의 여왕 5월 입니다.
# 활동하기 좋은 6월 입니다.
# 휴가가 기다려지는 7월 입니다.
# 무더운 8월 입니다.
# 선선한 9월 입니다.
# 천고마비의 계절 10월 입니다.
# 쓸쓸한 늦가을 11월 입니다.
# 올 한해의 마무리 12월 입니다.

name = input("이름 : ")
event = input("제목 : ")
date = input("날짜 : ") # 240911
time = input("시간 : ") # 24시간제

# 입력받은 date에서 월 정보 추출
#elif는 else if

month = date[4:6]

greeting = ""
if month == "01" :
    greeting = "한파의 연속인 1월입니다."
elif month =="02" :
    greeting = "봄을 기다리는 2월입니다."
elif month =="03" :
    greeting = "봄의 기운이 느껴지는 3월입니다."
elif month =="04" :
    greeting = "새싹이 피어나는 4월입니다."
elif month =="05" :
    greeting = "계절의 여왕 5월입니다."
elif month =="06" :
    greeting = "활동하기 좋은 6월입니다."
elif month =="07" :
    greeting = "휴가가 기다려지는 7월입니다."
elif month =="08" :
    greeting = "무더운 8월입니다."
elif month =="09" :
    greeting = "선선한 9월입니다."
elif month =="10" :
    greeting = "천고마비의 계절 10월입니다."
elif month =="11" :
    greeting = "쓸쓸한 늦가을 11월입니다."
elif month =="12" :
    greeting = "올 한해의 마무리 12월입니다."
else :
    print("월 정보가 잘못 입력되었습니다.")

print(f"{name}님,")
print(greeting)
print(f"아래의 일정으로 {event}를 진행하고자 하니, 자리를 빛내 주시기 바랍니다.")
print("="*7, "행사 안내", "="*7)
print("내용: " + event)
print(f"날짜 : {date[:4]}년 {date[4:6]}월 {date[6:8]}일")
time = int(time)
if time > 12 :
    time-=12
    print(f"시간 : 오후 {time}시")
else :
    print(f"시간 : 오전 {time}시")
