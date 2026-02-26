from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    driver.get(URL)

    # 点击 Start
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))).click()

    # 等待 “Hello World!” 出现（finish div 变为可见）
    finish = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    text = finish.text

    print("result:", text)
    assert "Hello World!" in text

finally:
    driver.quit()



#start > button