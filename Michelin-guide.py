from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#設定Chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="C:\python\chromedriver.exe"
#建立 driver物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)

# 連線到 Michelin Guide Sustainable Gastronomy 頁面
driver.get("https://guide.michelin.com/en/restaurants/sustainable_gastronomy")

# 使用 class name 定位所有符合條件的元素
restaurant_name_elements = driver.find_elements(By.CLASS_NAME, "card__menu-content--title")

for restaurant_name_element in restaurant_name_elements:
    restaurant_name = restaurant_name_element.text
    print(restaurant_name)

# 確保瀏覽器有足夠的時間完成操作
time.sleep(10)

driver.quit()





# tags=driver.find_elements(By.CLASS_NAME,"col order-2 order-lg-1 mb-lg-0 mt-1 mt-lg-0") #抓很多個標籤要加s(BY搜尋 class 屬性是 title 的所有標籤)

# for tag in tags:
#     print(tag.text) #印出來後為一個列表，包含所有標籤的資訊，逐一取得列表內部的每一個標籤，並取得標籤內部的文字

# #取得上一頁的文章標題(概念：根據超連結的內文來搜尋取得標籤命名為(link)，再模擬使用者的點擊)
# link=driver.find_element(By.LINK_TEXT,"‹ 上頁") #只要蒐集"上頁"，只有一個標籤
# link.click()  # 模擬使用者點擊(上一頁)連結標籤
# tags=driver.find_elements(By.CLASS_NAME,"title") #抓很多個標籤要加s(BY搜尋 class 屬性是 title 的所有標籤)
# for tag in tags:
#  print(tag.text) #印出來後為一個列表，包含所有標籤的資訊，逐一取得列表內部的每一個標籤，並取得標籤內部的文字
