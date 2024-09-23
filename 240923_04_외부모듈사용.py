# 파이썬에서는 기본적으로 제공하는 표준 라이브러리 이외에도 다양한 외부 모듈을 제공함
# 기본으로 제공되는 것이 아니기 때문에 import하기 전에 먼저 pip install 해줘야 함
# 파이썬 커뮤니티에서 개발하고 공유하는 패키지로, 다양한 분야의 기능 제공
# 패키지 설치시 공백 기준으로 여러개 한번에 설치 가능 : pip install beautifulsoul4 requests
# 설치된 pip 리스트 확인 : pip list

# simple-colors : 파이썬에서 터미널에 출력되는 텍스트에 색상을 적용하는 간단한 기능을 제공하는 모듈
# 색상이 지정된 텍스트를 출력하여 가독성을 높이거나 시각적인 효과 추가 가능
# 패키지 설치 : pip install simple-colors
"""
from simple_colors import *

print(green('hello'))
print(green('hello', 'bold'))
print(green('hello', ['bold', 'underlined']))
"""

# Beautiful Soup : HTML 및 XML 파일에서 데이터를 추출하는 데 사용되는 파이썬 라이브러리
# 일반적으로 웹 스크래핑과 데이터 마이닝에 사용됨
# HTML 및 XML 파일의 구문 분석 및 탐색을 쉽게 할 수 있도록 하는 파서 라이브러리
# 파싱 : 원하는 정보를 추출하는 동작(행위) 자체를 이르는 말
# 웹 페이지의 태그 구조를 쉽게 파악하고 태그의 속성과 값을 추출할 수 있음
# 패키지 설치 : pip install beautifulsoup4

# Requests : 서버에 HTTP 요청을 보내고 응답을 받는 데 사용하는 라이브러리
# 이를 통해 웹 서버에 GET, POST, PUT, DELETE 등 다양한 유형의 HTTP 요청을 보내고 응답을 받을 수 있음
# 웹 서비스와 상호작용하는 간단한 API를 제공
# 파이썬 기반의 웹 개발에서 널리 사용됨
# 패키지 설치 : pip install requests

# weather.go.kr 사이트의 데이터를 Beautiful Soup으로 파싱하기
"""
import requests
from bs4 import BeautifulSoup
url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
print(soup)
"""

# 날씨 정보 가져오기 (기상청 전국 날씨 정보)
"""
import requests
from bs4 import BeautifulSoup

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

# HTTP GET 요청 / 사실상 주소창에 http~ 주소 치는건, http get 요청을 보낸 것임
response = requests.get(url)

# HTTP 파싱
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

for loc in soup.select("location"):
    print("도시 : ", loc.select_one("city").string)
    print("날씨 : ", loc.select_one("wf").string)
    print("최저기온 : ", loc.select_one("tmn").string)
    print("최고기온 : ", loc.select_one("tmx").string)
    print("-"*20)
"""

# Flask : 파이썬에서 웹 개발을 할 때 Django(장고) 또는 Flask(플라스크) 등의 모듈 사용
# Django는 매우 다양한 기능을 제공하는 웹 개발 프레임워크
# Flask는 웹 어플리케이션 개발을 위한 간결하고 유연한 도구
# Flask는 마이크로 프레임워크로 분류되며, 작고 간단한 핵심 기능을 제공하면서도 확장성과 유연성을 갖추고 있음
# 패키지 설치 : pip install flask

# 간단한 Flask 사용 예제
"""
from flask import Flask

app = Flask(__name__)

@app.route('/') # 웹 서버를 띄우고 루트 경로를 실행하면 이리로 진입
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
"""

# 정보 파싱하여 출력하기
"""
import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"

    return output

if __name__ == '__main__':
    app.run()
"""
