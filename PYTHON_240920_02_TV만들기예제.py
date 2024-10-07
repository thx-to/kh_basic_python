# TV 만들기
# 클래스를 만들기 위해서는 생성자가 필요
# 생성자 : 클래스가 객체로 만들어질 때 자동으로 호출됨, 내부의 인스턴스 변수를 초기화하는 목적(객체의 초기값 지정)
# __init__() : 생성자 키워드
# self : 자신의 객체를 가리키는 포인터 (객체 자신을 참조하는 매개변수), 인스턴스 내의 속성에 접근하고 수정하는 데 사용됨


class Television : # 클래스를 만들기 위한 기본적인 동작 정의 / 클래스 변수
    def __init__(self, name, is_on, channel, volume) : # 생성자, 객체를 만들 때 같이 만들어지는 것들은 여기 넣어야 함 / 인스턴스 변수
        self.name = name # 인스턴스 변수를 생성하고 생성자의 매개변수를 통해 초기값을 입력받음
        self.is_on = is_on # TV의 전원 ON/OFF 상태 표시
        self.channel = channel # 채널 정보
        self.volume = volume # 볼륨 정보

    def set_on(self, is_on) : # 세터 메서드, 전원을 ON/OFF하는 세터 메서드(내부에 있는 변수값을 바꾸기 위한 메서드)
        self.is_on = is_on
    def set_channel(self, cnl) : # 채널을 변경하는 세터 메서드
        self.channel = cnl
    def set_volume(self, vol) : # 볼륨을 조절하는 세터 메서드
        self.volume = vol

    def get_on(self) : # 게터 메서드, 수업 중 실습에서는 사용하지 않음
        return self.is_on
    def get_channel(self) :
        return self.channel
    def get_volume(self) :
        return self.volume

    def tv_info(self) :
        power = ("OFF", "ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv = Television("우리집TV", False, 10, 10) # TV이름, 전원상태, 채널, 볼륨 / 위 생성자의 순서
samsung_tv = Television("시골집TV", False, 20, 20) # 여러개 찍어낼 수 있음

lg_tv.set_on(True)
lg_tv.set_volume(50)
lg_tv.set_channel(59)
lg_tv.tv_info()
samsung_tv.tv_info()



# 캡슐화를 위해 게터/세터 메서드 사용했지만, 게터 세터 없이도 아래와 같이 설정 가능
# 접근 제한, 볼륨이 10000이 되면 위험함.. (고막이나가거나 TV가터지거나)
"""
lg_tv.volume = 10000
lg_tv.tv_info()
"""

# 이렇게 되지 않게 하기 위해 볼륨 최대값을 지정함
# 아래 볼륨 지정 부분에 if문으로 접근제한을 넣어줌
"""
def set_volume(self, vol):  # 볼륨을 조절하는 세터 메서드
    if 0 <= vol <= 100 :
        self.volume = vol
    else :
        print("볼륨값 허용 범위를 벗어났습니다.")
"""