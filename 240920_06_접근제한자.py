# 접근제한자 : 클래스 내부에 선언된 변수에 대한 접근을 제한하는 것
# 외부에서 내부 변수에 접근하고자 할 때, 지정된 게터와 세터 메서드를 통해서만 접근하도록 하는 것
# 파이썬은 자바의 private과 같은 엄격한 접근 제한자가 없음
# 네이밍 컨벤션과 관례를 사용하여 속성과 메서드의 가시성을 관리
# public : 기본값, 변수명 앞에 아무것도 붙이지 않음, 아무데서나 접근 가능
# protected : _변수명, 외부에서 접근 가능하지만 보호됨, 같은 클래스거나 상속관계가 존재하면 접근 가능
# private : __변수명, 클래스 외부에서 직접 접근 불가, 같은 클래스에서만 접근 가능
"""
class TV:
    cnt = 0 # 클래스 맴버
    def __init__(self, name, isOn, channel, volume):
        self.__name = name # 언더바 2개 : private (클래스 내부에서만 접근 가능)
        self.__isOn = isOn
        self.__channel = channel
        self.__volume = volume
        TV.cnt += 1
    def set_on(self, isOn):
        self.__isOn = isOn
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.__channel = cnl
        else :
            print("채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.__volume = vol
    def get_on(self):
        return self.__isOn
    def get_channel(self):
        return self.__channel
    def get_volume(self):
        return self.__volume
    def view_tv(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.__name}")
        print(f"전원 : {power[self.__isOn]}")
        print(f"채널 : {self.__channel}")
        print(f"볼륨 : {self.__volume}")


lg_tv = TV("LG", True, 10, 20)
sam_tv = TV("LG", True, 10, 20)

lg_tv.__name = "SAMSUNG" # 오류는 아니지만 변경은 안됨
lg_tv.__isOn = False # 오류는 아니지만 변경은 안됨
lg_tv.set_channel(999)
lg_tv.view_tv()
print(TV.cnt)
"""