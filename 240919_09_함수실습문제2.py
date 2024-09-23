# 두번째 수 찾기
# 입력 : 1 2 3 4 5 6 7 8 3 4 5 6 7 8
# 찾을 수 : 3
# 해당 수의 위치를 반환 : 인덱스가 아님(0부터 시작하지 않음), 9번째
# 찾지 못하면 -1을 반환
# 함수 사용

# HINT)
# def second_find(ls, n) :
# pass
# 정수값에 대한 리스트 입력 생성
# 찾을 수를 입력받기
# 결과 출력하기

# 해보기
"""
def second_find(ls, n) :
    pass

num = list(map(int, input("정수값 리스트 입력 : ").split()))
find = int(input("찾을 수 입력 : "))
print(second_find(ls, find)) # 출력값을 생각을 아예 못했음
"""

# 강사님따라가보기
"""
def second_find(ls, n) :
    cnt = 0 # 몇번 등장했는지 카운트 / 0이면 한번 등장한거
    for i in range(len(ls)) :
        if ls[i] == n : # 몇번쨰인지는 i값(인덱스)로
            if cnt > 0 : return i + 1 # cnt값이 처음에는 0이었는데 0보다 크면 i + 1을 반환
            else : cnt += 1 # 0일때는 리턴 안하고 카운트만 1 더해서 한바퀴 더 돌아 / 첫번째 값을 만나면 skip, 두번째 값을 만나면 return
    return -1 # 실제 순서에서 1 빼줘야 인덱스

ls = list(map(int, input("정수값 리스트 : ").split())) # 정수값에 대한 리스트 입력
find = int(input("찾을 수 입력 : ")) # 찾을 수 입력
print(second_find(ls, find)) # 결과 출력
"""

