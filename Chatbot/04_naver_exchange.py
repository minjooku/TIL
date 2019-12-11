# 네이버 금융 - 시장 지표 - 원달러 환율 가져오기 
#0. 관련 모듈 import
#1. 문자열 형태로 문서 가져오기
#2. BeautifulSoup클래스 객체 받기
#3. 원하는 선택자 내용 가져오기 
#4. 결과물 출력

import requests
from bs4 import BeautifulSoup



url='https://finance.naver.com/marketindex/'

html = requests.get(url).text


soup=BeautifulSoup(html,'html.parser')

exchange=soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(exchange)
