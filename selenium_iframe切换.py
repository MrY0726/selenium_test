from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/iframe"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    # 1) 等到 iframe 出现，并切进去
    iframe = wait.until(EC.presence_of_element_located((By.ID, "mce_0_ifr")))
    driver.switch_to.frame(iframe)

    # 2) 在 iframe 里找到编辑区（这是 TinyMCE 的编辑 body）
    body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    body.clear()
    body.send_keys("Hello from Selenium!")

    # 3) 切回主页面（很重要！）
    driver.switch_to.default_content()

    # 4) 读取页面标题
    title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
    print("page title:", title)

finally:
    driver.quit()
