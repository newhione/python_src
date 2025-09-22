#pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'https://www.google.com/?hl=ko'
time.sleep(3) # 약 3초 페이지 로드 될 때까지 기다리기

#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url)
print('브라우저가 성공적으로 열렸습니다.')
# driver.quit()
# 검색창 요소 찾기(id가 'ipt_keyword_recruit'인 input 태그를 찾음)
search_input =driver.find_element(By.CLASS_NAME, 'gLFyf')
# 검색창에 파이썬 입력
search_input.send_keys('파이썬')
#  Enter키 누르기
search_input.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
