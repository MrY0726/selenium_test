from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

def main():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    # 1) 输入账号密码
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    # 2) 点击登录
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 3) 断言/打印提示信息（成功会包含 “You logged into a secure area!”）
    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    print("flash:", flash)

    # 4) 可选：点击退出（练习登出）
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

    driver.quit()

if __name__ == "__main__":
    main()
