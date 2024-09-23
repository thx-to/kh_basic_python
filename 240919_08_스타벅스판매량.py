# 1) 파일 정상적으로 있는지 확인해보기
"""
file_name = "240919_08_스타벅스일일매출.txt"

with open(file_name, "r", encoding="utf-8") as file :
    for line in file :
        print(line, end = "")
"""

# 2) 전체 판매량과 일 평균 판매량 구하기
"""
file_name = "240919_08_스타벅스일일매출.txt"

with open(file_name, "r", encoding="utf-8") as file :
    header = file.readline() # 줄바꾸기 한줄기준
    header_list = header.split() # 공백기준으로 받아서 리스트 만들기

    espresso = [] # 빈 리스트(배열) 만들기
    americano = []
    latte = []
    cappuccino = []

    for line in file : # 파일에 돌려서 한줄씩 들어와지게
        data_list = line.split() # 라인을 한줄씩 읽어서 스플릿으로 쪼갬, 데이터리스트에 한줄로 넣음
        espresso.append(int(data_list[1])) # 0번은 날짜, 1번은 에스프레소
        americano.append(int(data_list[2]))
        latte.append(int(data_list[3]))
        cappuccino.append(int(data_list[4]))
        # with 키워드를 사용했기 때문에 이 지점에서 자동 close

print(f"{header_list[1]} 전체 판매량 : {sum(espresso)}, 일 평균 판매량 : {sum(espresso) / len(espresso)}")
print(f"{header_list[2]} 전체 판매량 : {sum(americano)}, 일 평균 판매량 : {sum(americano) / len(americano)}")
print(f"{header_list[3]} 전체 판매량 : {sum(latte)}, 일 평균 판매량 : {sum(latte) / len(latte)}")
print(f"{header_list[4]} 전체 판매량 : {sum(cappuccino)}, 일 평균 판매량 : {sum(cappuccino) / len(cappuccino)}")
"""