# 파일 입/출력 : 파일을 읽고 쓰는 동작
# 파일을 읽거나 쓰기 위해서는 우선 파일을 open해야 함
# 작업 완료 후 반드시 close해야 함 (with 키워드 사용시 생략 가능)

# 파일 객체 = open(파일명, 파일모드, 인코딩)
# utf-8은 한글 깨짐 방지를 위한 인코딩

# 파일모드 w = wt (write text, 텍스트 형태로 쓰는 것)
# w = write / r = read / a = append (파일의 마지막에 새로운 내용을 추가)
# t = text / b = binary

# 파일 쓰기 예시
"""
score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 55", file = score_file) # print 함수를 사용해 파일에 쓰기
print("영어 : 70", file = score_file)
score_file.write("국어 : 90" + "\n") # 줄바꿈 문자를 넣어 줘야 함
score_file.write("과학 : 87" + "\n")
score_file.close() # open한 파일은 반드시 닫아줘야 함
"""

# 파일 읽기 예시 1) read
# read() : 파일 내 모든 내용을 읽어 하나의 문자열로 반환
"""
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()
"""

# 파일 읽기 예시 2) readline, while True : 더 이상 읽을 라인이 없을때까지 반복 수행하기 위해서
# readline() : 해당 파일의 내용을 한 라인씩 읽어들여 문자열로 반환, 파일의 끝(EOF)에 도달하여 더 이상 가져올 라인이 없는 경우에는 None 반환
"""
score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline() # score_file이라는 파일 객체에서 한줄씩 라인을 읽어들임
    if not line: break # 읽을 게 없으면 탈출
    print(line, end="") # 아니면 라인 출력 / 어차피 한줄씩 되어 있어서 줄바꿈이 되어 있는 상태라 end에 ""로 넣어줌
score_file.close()
"""

# 파일 읽기 예시 3) readlines
# readlines() : 해당 파일의 모든 라인을 순서대로 읽어들여 각각의 라인을 하나의 요소로 저장하는 하나의 리스트를 반환
"""
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
"""

# with 키워드 : close() 메서드를 불러주지 않아도 구문이 종료될 때 자동으로 닫아 주는 기능
# 뒤에 as 하고 파일 전체를 이르는 말이 필요함
# 코드가 엄청 길어질 경우에 유용함
"""
with open("score.txt", "r", encoding="utf8") as score_file :
    lines = score_file.readlines()
    for line in lines :
        print(line, end="")
# 이 지점에서 자동으로 close() 함수 호출
"""

# pickle : 파이썬 객체를 직렬화(serialize) / 역직렬화(deserialize)하기 위한 모듈
# 파이썬 객체를 파일에 저장하거나 네트워크를 통해 전송할 수 있음
# 객체를 이진 형식으로 저장하며, 나중에 필요할 때 원래의 상태로 복원할 수 있음


# 객체를 직렬화하여 파일에 저장하기
# 바이너리 파일로 바꿀거라(wb) utf를 안넣어줘도 됨
# 읽을 수 없는 data.pickle 파일이 만들어짐
"""
import pickle

data = {"name": "팜하니", "age": 21, "addr": "서울시 강남구"}
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file) # .dump 해당 객체를 파일에 직렬화해서 쓰게 하는 문법
"""

# 파일에서 객체를 역직렬화하여 복원하기
"""
import pickle

with open('data.pickle', 'rb') as file:
    restored_data = pickle.load(file) # 파일 자체에서 객체를 역직렬화
print(restored_data)  # {"name": "팜하니", "age": 21, "addr": "서울시 강남구"}
"""

