# 다형성이란 부모가 물려준 특성을 재정의하여 사용하는 것을 의미
# 메서드 오버로딩 / 메서드 오버라이딩

# 오버로딩 : 파이썬에서 지원하지 않음 (메서드 이름은 동일하고 매개변수의 개수나 타입으로 구분)
# 파이썬에 오버로딩이 없는 이유
"""
def over_sum(x, y, z) :
    return x + y + z
# 자바에서 아래와 같이 구현하면 오류, 자바는 x, y, z 타입이 정해져 있어야 함 > 오버로딩이 필요함
print(over_sum(1, 2, 3)) # 정수에 대한 덧셈, 정수가 동적 타입의 변수에 대입되어 x, y, z가 정수가 되어버림
print(over_sum(1.1, 2.2, 3.3)) # 실수에 대한 덧셈, 실수가 동적 타입의 변수에 대입되어 x, y, z가 실수가 되어버림
print(over_sum("팜하니", "킴민지", "모다니")) # 문자열 덧셈까지도 가능 / 파이썬은 이미 값이 들어갈 때 동작을 해버림
"""

# 오버라이딩 : 부모가 물려준 특성을 재정의하는 것
# TV 설정 오버라이딩 예제
"""
class PrototypeTv : # 상속을 주기 위해서 부모클래스 임의로 생성해봄 / 파스칼표기법
    def __init__(self, is_on, channel, volume) : # 기본 부모의 생성자를 만듦
        self.is_on = is_on
        self.channel = channel
        self.volume = volume

    def set_on(self, is_on) :
        self.is_on = is_on # ON/OFF 두개만 있어서 이렇게 씀
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.channel = cnl
            print(f"채널을 {cnl}로 변경합니다.")
        else :
            print(f"채널 범위를 벗어났습니다.")
    def set_volume(self, vol) :
        self.volume = vol

    def get_on(self) :
        return self.is_on
    def get_channel(self) :
        return self.channel
    def get_volume(self) :
        return self.volume
        
class ProductTv(PrototypeTv) : # PrototypeTv를 상속받아서 ProductTv 클래스를 만듦
    def set_channel(self, cnl) : # 오버라이딩 / 파이썬은 오버라이딩 관계가 성립하는지를 체크할 수 있는 기능이 없음 / 이름이 같으면 오버라이딩 관계인 것으로 파악할 것
        if 0 < cnl < 2000 : # 부모가 물려준 채널 설정 기능을 변경함
            self.channel = cnl
            print(f"채널을 {cnl}로 변경합니다.")
        else :
            print(f"채널 범위를 벗어났습니다.")

lg_tv = ProductTv(False, 20, 20)
lg_tv.set_channel(1500)
lg_tv.set_channel(3000)
"""