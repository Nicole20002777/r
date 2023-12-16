# 載入 selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.common.keys import Keys
import time

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "C:\python\chromedriver.exe"

# 建立 driver 物件實體，用程式操作瀏覽器運作
options.add_argument('headless')
options.add_argument("--disable-web-security")
options.add_argument("--disable-site-isolation-trials")
driver = webdriver.Chrome(options=options)

# 連線到 TripAdvisor
driver.get("https://www.tripadvisor.com/Restaurant_Review-g1224250-d11913607-Reviews-PRU_Restaurant-Choeng_Thale_Thalang_District_Phuket.html")

# 使用 WebDriverWait 等待 "more" 按鈕載入，增加等待時間
wait = WebDriverWait(driver, 30)  

# 等待評論元素載入
wait = WebDriverWait(driver, 60)
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "noQuotes"))) 
    
    # 載入 more 按鈕
    time.sleep(5)
    
    # 尋找 more 按鈕
    more_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.taLnk.ulBlueLinks')))

    # 點擊所有 more 按鈕
    for button in more_buttons:
        try:
            button.click()
        except:
            pass

except TimeoutException as ex:
    print("TimeoutException:", ex)

# 模擬按下 PageDown 鍵，滾動頁面
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

# 使用 WebDriverWait 等待 "more" 按鈕載入
wait = WebDriverWait(driver, 10)
more_buttons = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.taLnk.ulBlueLinks')))

# 獲取留言的星等
star_rating_tags = driver.find_elements(By.CSS_SELECTOR, 'span.ui_bubble_rating')
star_ratings = []

for star_rating_tag in star_rating_tags:
    class_value = star_rating_tag.get_attribute("class")
    # 從 class_value 中提取星等數字
    star_rating = int(class_value.split("_")[-1])
    star_ratings.append(star_rating)

review_elements = driver.find_elements(By.CSS_SELECTOR, 'div.prw_rup.prw_reviews_text_summary_hsx')

# 取得留言的標題、內容和時間、評論者姓名、所在地
title_tags = driver.find_elements(By.CLASS_NAME, "noQuotes")
content_tags = driver.find_elements(By.CLASS_NAME, "partial_entry")
date_tags = driver.find_elements(By.CSS_SELECTOR, 'span.ratingDate')
name_tags = driver.find_elements(By.CLASS_NAME, 'info_text')
location_tags = driver.find_elements(By.CLASS_NAME, 'userLoc')

# 建立用來儲存資料的列表
titles = []
contents = []
dates = []
names = []
locations = []
ratings = []


# 迭代所有星等元素的標籤
for star_rating_tag in star_rating_tags:
    class_value = star_rating_tag.get_attribute("class")
    # 從 class_value 中提取星等數字
    star_rating = int(class_value.split("_")[-1]) // 10  # 除以10取整數部分，例如：40 → 4, 50 → 5
    ratings.append(star_rating)  # 將星等數字轉換為浮點數並除以10，然後存入列表

# 逐一處理每個評論
for i in range(len(title_tags)):
    title = title_tags[i].text
    content = content_tags[i].text
    date = date_tags[i].text
    name = name_tags[i].text
    rating = ratings[i]


    # 將資料附加到對應的列表中
    titles.append(title)
    contents.append(content)
    dates.append(date)
    names.append(name)
    ratings.append(rating)

    # 印出評論標題、內容和時間（可選步驟，用於檢查）
    print(f"Title: {title}")
    print(f"Content: {content}")
    print(f"Time: {date}")
    print(f"Star Rating: {rating}")
    print(f"Name: {name}")
    print("-" * 50)

    # 逐一處理每個評論，只處理奇數索引位置的元素
for i in range(1, len(review_elements), 2):
    content = review_elements[i].find_element(By.CLASS_NAME, 'partial_entry').text.strip()
    print(f"Customer Review {i // 2 + 1}: {content}")


# 關閉瀏覽器
driver.close()
