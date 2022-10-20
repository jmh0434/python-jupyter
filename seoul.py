from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 크롤링 진행 함수
def seoul_shop(result): 
    wd = webdriver.Chrome('/Users/minhyuk/study/chromedriver') # 웹드라이버 경로

    for page in range(1, 6): # 1페이지부터 5페이지까지
        wd.get('https://thesool.com/front/publication/M000000058/list.do?page=%d&bbsId=A000000055&searchKey=&searchString=&searchCategory=' % page)
        time.sleep(3)
        try:
            link_list = wd.find_elements(By.CLASS_NAME, 'link') # link 요소 찾기
            for link in link_list[:-1]:
                link.click() # link 요소를 리스트에 담고 하나씩 꺼내서 클릭
                time.sleep(1)
                html = wd.page_source
                soup = BeautifulSoup(html, 'html.parser')
                shop_name = soup.select_one('div.body-title').string # 가게 이름
                print(shop_name)
                shop_info = soup.select('td.data') # 가게 정보
                shop_address = shop_info[0].string # 가게 주소
                print(shop_address) 
                shop_time = shop_info[1].string # 가게 운영시간
                print(shop_time)
                shop_phone = shop_info[2].string # 가게 전화번호
                print(shop_phone)
                shop_menu = shop_info[3].string # 가게 메뉴
                print(shop_menu)
                wd.find_element(By.CLASS_NAME, 'layer-close').click()
                time.sleep(1)
                result.append([shop_name]+[shop_address]+[shop_time]+[shop_phone]+[shop_menu]) # 한 리스트에 담기
        except:
            continue
    return

def main():
    result = []
    print('크롤링 진행 중')
    seoul_shop(result) 

    seoul_tbl = pd.DataFrame(result, columns=('name', 'address', 'time', 'phone', 'menu'))
    seoul_tbl.to_csv('./seoul.csv', encoding='utf-8', mode='w', index=True) # csv 파일로 변환

if __name__ == '__main__':
    main()