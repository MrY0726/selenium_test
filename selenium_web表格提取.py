from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/tables"

driver = webdriver.Edge()   # 或 webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    # 找到 table1 的所有行
    rows = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "#table1 tbody tr")
    ))

    table_data = []
    for r in rows:
        # 每一行里找所有单元格 td
        tds = r.find_elements(By.TAG_NAME, "td")
        row_texts = [td.text for td in tds]   # 一行的文本列表
        table_data.append(row_texts)

##table_data = [[], [], []]
    print("二维数组 table_data：")
    for row in table_data:
        print(row)

finally:
    driver.quit()




#table1 > tbody > tr:nth-child(1)	
#table1
#table1 > tbody