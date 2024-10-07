# 회원 가입을 위한 아이디 패스워드 입력 받기
id = input("ID 입력 : ")
if len(id) >= 8 :
    pw = input("PASSWORD 입력 : ")
    if len(pw) < 8 or len(pw) > 16 :
        print("PASSWORD는 8자리에서 16자리 사이여야 합니다.")
    elif pw.find(id) >= 0 : # 찾지 못한 경우는 -1 출력
        print("PASSWORD는 ID를 포함할 수 없습니다.")
    else :
        print(f"ID : {id}")
        print(f"PASSWORD : {pw}")
else :
    print("ID는 반드시 8자리 이상이어야 합니다.")