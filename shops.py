from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/minhyuk/study/chromedriver')
driver.implicitly_wait(3)
driver.get('https://thesool.com/front/publication/M000000058/list.do?page=1&bbsId=A000000055&searchKey=&searchString=&searchCategory=')
driver.find_element(By.CLASS_NAME, 'link').click()
html = driver.page_source
soup1 = BeautifulSoup(html, 'html.parser')

# #print(soup1.prettify())
# print('-------------------------')
# shop_name = soup1.select_one('div.body-title').text
# shop_address = soup1.select("div.body-table>table>tbody>tr>td.data")

# print('가게명: ',shop_name)
# for i in shop_address:
#     print(i.string)
