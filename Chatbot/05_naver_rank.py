import requests
from datetime import datetime
from bs4 import BeautifulSoup
url='https://www.naver.com/'
html=requests.get(url).text
soup=BeautifulSoup(html,'html.parser')
names=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')


print(f'{datetime.now()}기준 시간 검색어')

for name in names:
    print(name.text)
