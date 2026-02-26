import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/infinite_scroll"

driver = webdriver.Edge()

try:
    driver.get(URL)

    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   ##滚动到最底部，加载出所有内容
        time.sleep(0.8)  # 这个页面就是靠加载，练习可用，真实项目更推荐显式等待
        blocks = driver.find_elements(By.CSS_SELECTOR, ".jscroll-added")
        print(f"scroll {i+1}, blocks:", len(blocks))

finally:
    driver.quit()


#content > div > div > div > div