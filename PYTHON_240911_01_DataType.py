# 자료형 : 데이터를 저장하기 위해 미리 만들어진 데이터의 형태
# 값이 들어올 때 자료형이 결정됨
# 자료형은 3가지
# 문자열 자료형(파이썬에 '문자' 타입-형-은 존재하지 않음)
# 숫자 자료형(정수형과 실수형)
# Boolean 자료형(참과 거짓)

# 변수 : 자료형을 이용해 실제 데이터를 저장할 공간을 할당받는 것(RAM에)
# 변수에 값을 대입하는 연산자는 =(equal)
"""
a = b = c = 1 # 대입은 뒤에서부터 앞으로, 1을 c에 대입하고 c를 b에 대입하고 b를 a에 대입하여 a=1이 됨
print(a)
print(b)
print(c)
"""

"""
a, b, c = 1, True, "곰돌이" #a는 1에 대입, b는 true 대입, c는 곰돌이 대입
print(a)
print(b)
print(c)
"""

# 변수의 타입 확인 : type()
# int : integer
# str : string
# bool : boolean
"""
a, b, c = 1, True, "곰돌이"
print(type(a))
print(type(b))
print(type(c))
"""

# 문자열 : 문자로 이루어진 데이터의 집합 > 배열과 비슷함, 배열처럼 다뤄야 함
# "", '' > 한 라인에 대한 문자열 """ """, ''' ''' > 여러 라인에 대한 문자열

# 인덱싱 : 시퀀스 자료형(연속적인 것들)에서 특정 위치의 요소를 선택하는 작업
# 시퀀스 자료형은 리스트, 튜플, 문자열, input이 있음
# 인덱싱은 0부터 시작

# 슬라이싱 : 시퀀스 자료형에서 일부 데이터를 추출(잘라내기)하는 것
# 기본 주민등록번호 입력해서 성별 알아내기
"""
jumin = input("주민등록번호 입력 : ")
gender = jumin[7]
if gender == '1' or gender == '3' :
     print("남성입니다.")
else :
     print("여성입니다.")
"""

# 태어난 년도를 구하기 위해 슬라이싱
"""
jumin = input("주민등록번호 입력 : ")
gender = jumin[7]
year = jumin[0:2] # 0에서 2 미만, 0에서부터 시작되는 경우 0 생략 가능(year=jumin[:2])
year = int(year) # 형변환, 없으면 오류
if gender =='1' or gender =='2' :
    year += 1900
else :
    year += 2000

print(f"태어난 년도 : {year}")
"""

# 생일 출력 : 0720 > 7월 20일
"""
jumin = input("주민등록번호 입력 : ")
month = jumin[2:4]
day = jumin[4:6]
month = int(month)
day = int(day)
print(f"생일 : {month}월 {day}일")
"""

# 생년월일 및 주민등록번호 뒤 7자리 추출
"""
jumin = input("주민등록번호 입력 : ")
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[6:])
print("뒤 7자리 : " + jumin[-7:]) # -1은 맨 뒷자리
"""

# 문자열 예시
"""
life = "Life is too short, You need Python."
tmp = life[0] + life[1] + life[2] + life[3]
print(tmp)
"""

# 대소문자 바꾸기 : upper(), lower()
"""
a = 'Hello Python Program...'
print(a.upper())
print(a.lower())
"""

# 문자열 변경 : replace("기존 문자열", "바꿀 문자열")
"""
b = 'Hello Python Program...'
print(b.replace('Python','JavaScript'))
n_b = b.replace('Hello','Bye')
print(n_b)
"""

# 별도 존재(기본적으로 포함된) 함수와 내장(문자열 등에 포함=내부 메서드) 함수가 있음 (딱히 개념으로 정리된 건 아닌듯)
# 내장함수 / 내부 메서드는 '문자열.메서드'의 방식으로 타이핑하여 사용하는듯.. 하기예제참조

# 문자열에 포함된 문자 개수 세기 및 문자열 길이 구하기
# count() : 문자열 내장 메서드(함수)로, 문자열에 포함된 문자의 개수을 반환
# __len__() : 문자열 길이를 반환
# len() : 문자열 길이를 반환
"""
c = 'Hello Python Program'
print(c.count('l')) # 해당 문자열에서 매개변수로 전달한 문자/문자열의 개수 반환
print(len(c)) # 해당 문자열의 길이 반환 - 띄어쓰기 포함
print(c.__len__()) # 해당 문자열의 길이 반환 - 띄어쓰기 포함
"""

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 시작 인덱스 반환, 찾지 못하면 -1
# rfind() : 뒤에서부터 문자열을 찾음, 찾은 문자열의 인덱스는 앞에서부터 계산 (찾는건 뒤에서부터, 카운트는 앞에서부터)
# index() : 찾은 문자열의 시작 인덱스 반환, 찾지 못하면 ValueError 발생 및 종료
"""
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.__len__())
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))
print(phrase.find("나에게"))
new_phrase = phrase.replace("가장","나에게")
print(new_phrase)
"""

# index ValueError 발생 및 종료 예시
"""
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.index("나에게")) # 그대로 실행시 종료
"""

# 문자열 연산자 : +, *
"""
print("태양고" + "나희도") # 띄어쓰기 없이 출력
print("!" * 10) # 10회 반복 출력
list1 = [1] * 10 # 1이 10개인 리스트
print(list1)
list2 = [1*10] # 1*10이라는 숫자로 이루어진 리스트
print(list2)
"""

# 문자열 양옆의 공백제거 : strip()

d = "     문자열의 공백을 제거하겠습니다."
print(d)
print(d.strip())


# 형변환
# bool(값) : 값을 논리형으로 변환
# int(값) : 값을 정수형으로 변환
# float(값) : 값을 실수형으로 변환
# str(값) : 값을 문자열로 변환
