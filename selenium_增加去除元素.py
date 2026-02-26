from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/add_remove_elements/"

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    # 1) 找到 Add Element 按钮并点击 3 次
    add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#content button")))
    for _ in range(3):
        add_btn.click()

    # 2) 统计 Delete 按钮数量（这些按钮的 class 固定是 added-manually）
    deletes = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
    print("delete buttons:", len(deletes))
    assert len(deletes) == 3

    # 3) 删除一个
    deletes[0].click()

    # 4) 再统计一次
    deletes2 = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
    print("after delete:", len(deletes2))
    assert len(deletes2) == 2

finally:
    driver.quit()


#content > div > button
#elements > button:nth-child(1)