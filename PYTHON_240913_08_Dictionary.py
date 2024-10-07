# 딕셔너리 : 키로 값을 찾는 것
# 리스트, 튜플은 정수인 인덱스를 가지고 순차적으로 각 요소에 접근
# 딕셔너리는 '사전'과 같이 별도의 키를 통해 각 요소에 접근할 수 있도록 만들어진 데이터 타입
# 키는 중복되지 않는 고유한 값
# 다른 언어(C++, JAVA)에서는 같은 개념을 Map이라고 부름

# 딕셔너리 선언은 중괄호 {}
# 각 요소는 쉼표 , 로 구분
# 키와 값은 콜론 : 으로 구분
# 통신 등에서 정보를 주고받을 때 사용
# 제이슨 방식인 자바스크립트의 '객체' 개념과 같음(키와 밸류)
# 제이슨 방식의 데이터가 들어오면 파이썬에서 딕셔너리의 키와 밸류로 받아내야 함
"""
coffee_menu = {"Americano":2500, "Espresso":2500, "Latte":4000, "Moca":4500}
food_menu = {"Cake":5000, "Bakery":6000}
print(coffee_menu)
print(food_menu)
print(coffee_menu["Espresso"]) # 키로 값 확인하기
print(coffee_menu.get("Espresso")) # get(키) 함수로 값 확인하기
"""

# 값 추가, 삭제, 키 존재 여부 확인
"""
coffee_menu = {"Americano":2500, "Espresso":2500, "Latte":4000, "Moca":4500}
food_menu = {"Cake":5000, "Bakery":6000}
food_menu["Icecream"] = 5000 # 새로운 키와 값 추가
del coffee_menu["Latte"] # 해당 명령으로 아이템(키와 값) 삭제 / 자바에서는 엔티티라고 부름(아이템)
print(coffee_menu)
print(food_menu)

if "Bakery" in food_menu :# Bakery라는 키가 food_menu에 있으면
    print(food_menu["Bakery"])
else :
    print("해당 메뉴가 없습니다.")
"""

# update() 함수 : 딕셔너리의 데이터를 한꺼번에 변경할 때 사용
"""
coffee_menu = {"Americano":2500, "Espresso":2500, "Latte":4000, "Moca":4500}
print(coffee_menu)
coffee_menu.update({"Americano":3000, "Espresso":2800, "Latte":5000, "Moca":7000})
print(coffee_menu)
"""

# 정보 얻기 : keys(), values(), items()
# keys는 키만 반환
# values는 값만 반환
# items는 아이템(키와 값) 반환
"""
dict_lang = {"JAVA":99, "JAVASCRIPT":80, "PHYTHON":92, "C++":89}
print(dict_lang.keys())
print(dict_lang.values())
print(dict_lang.items())
"""