# 각 사이트의 비밀번호 만들기
# 규칙1 : http://naver.com에서 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자에 포함된 'o' 개수 + 글자에 포함된 'k' 개수 + '!' + 자신의 이니셜

# 기본 풀이
"""
url = input("사이트 : ")
my_str = url.replace("http://","") # 규칙1 적용 : 입력받은 문자열에서 http 영문자 잘라내기
my_str = my_str[:my_str.index(".")] # 규칙2 적용 : 0에서부터 .의 인덱스 미만까지 슬라이싱
pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "koong"
print("비밀번호 : " + pwd)
"""

# 파일로 저장하기
"""
file_name = "password.txt"
f = open(file_name, "wt")
while True :
    url = input("사이트 : ")
    if url == "exit" : break
    my_str = url.replace("http://","")
    my_str = my_str[:my_str.index(".")]
    pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "koong"
    f.write(pwd+"\n")
f.close()
"""