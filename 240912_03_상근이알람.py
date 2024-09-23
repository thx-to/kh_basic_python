# 상근이는 매일 아침 알람을 듣고 일어난다.
# 알람을 듣고 바로 일어나면 다행이겠지만,
# 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
# 상근이는 모든 방법을 동원해보았지만,
# 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
# 이런 상근이를 불쌍하게 보던 창영이는
# 자신이 사용하는 방법을 추천해 주었다.
# 바로 "45분 일찍 알람 설정하기" 이다.

# 45분 일찍 알람을 울리도록 하는 문제

# 입력 : 시간과 분, 24시간제
# 첫째 줄에 두 정수 H와 M이 주어진다.
# (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
# 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간
# H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다.
# 24시간 표현에서 하루의 시작은 0:0(자정)이고,
# 끝은 23:59(다음날 자정 1분 전)이다.
# 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

# 출력 : 첫째 줄에 상근이가 창영이의 방법을 사용할 때
# 설정해야 하는 알람 시간을 출력한다.
# 입력과 같은 형태로 출력

# HINT : 시간을 전부 분으로 환산해보자
# 분으로 환산한 시간이 45보다 작으면 시간(H)을 별도 계산 (00시의 경우)
# 계산된 시간에서 45분을 빼줌
# 다시 시간과 분으로 환산해서 출력

# 1 함수가없네..
"""
H,M = map(int, input("HH:MM : ").split(":"))
HM = H * 60
MM = HM + M
NMM = MM - 45
NH = NMM // 60
NM = NMM  % 60
print(NH,":",NM)
"""

# 2 재도전
"""
while True :
    H,M = map(int,input("HH:MM : ").split(":"))
    if 0 <= H <= 23 and 0 <= M <= 59:
        HM = H * 60 + M
        if HM < 45 :
            HM = 24 * 60 + M
        print(f"{(HM-45)//60}:{(HM-45)%60}")
        break
    else : print("시간을 잘못 입력하셨습니다.")
    continue
"""

# 3 해답
"""
h, m = map(int, input("시간 입력 : ").split(":"))
# 시간을 분으로 환산하기
calc_min = h * 60 + m # 입력받은 시간을 모두 분으로 환산
# 분으로 환산한 시간이 45보다 작으면 시간을 별도 계산
if calc_min < 45 :
    calc_min = 24 * 60 + m
# 45분을 빼줌
calc_min -= 45
# 다시 시간과 분으로 환산해 출력
print(f"{calc_min // 60}:{calc_min % 60}")
"""
