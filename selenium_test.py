from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
import time

# 获取当前时间的毫秒级时间戳，输出示例: 1700000000000 (13位数字)
timestamp_milliseconds = int(time.time() * 1000)

URL = "https://tool.lu/timestamp/"
driver = webdriver.Edge()
wait = WebDriverWait(driver, 3)

try:
    driver.get(URL)
    ###填入时间戳
    times = driver.find_element(By.CSS_SELECTOR, "#jsTimestamp")
    times.clear()
    times.send_keys(timestamp_milliseconds)
    ##切换毫秒模式
     #等待下拉框出现，并用 Select 包装（Select 专门用来操作 <select> 下拉框）
    dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div:nth-child(2) > div > div.mb-8 > div > div:nth-child(1) > select")))
    sel = Select(dropdown)
    sel.select_by_value("ms")
    ##点击转换
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div > div:nth-child(2) > div:nth-child(2) > div > div.mb-8 > div > div:nth-child(2) > button"))).click()  
    ##查看结果
    Datetime = driver.find_element(By.CSS_SELECTOR, "#jsDatetime").get_attribute("value")
    print(f"时间戳:{timestamp_milliseconds},转化为日期时间为:{Datetime}")
    assert "2026" in Datetime
    print("测试通过！")

except Exception as e:
    print(f"出现错误: {e}")
    
finally:
    driver.quit()
