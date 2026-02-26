from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://the-internet.herokuapp.com/checkboxes"

def set_checked(checkbox, desired: bool):
    """确保 checkbox 达到 desired 状态（True=勾选，False=不勾选）"""
    if checkbox.is_selected() != desired:
        checkbox.click()

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get(URL)

    # 等到页面上至少出现 2 个复选框（这个页面就是两个）
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")) >= 2)

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    cb1, cb2 = checkboxes[0], checkboxes[1]

    # 1) 打印初始状态
    print("before:", cb1.is_selected(), cb2.is_selected())

    # 2) 设置目标状态：checkbox1 勾选，checkbox2 不勾选
    set_checked(cb1, True)
    set_checked(cb2, False)

    # 3) 断言最终状态
    print("after: ", cb1.is_selected(), cb2.is_selected())
    assert cb1.is_selected() is True, "checkbox1 should be checked"
    assert cb2.is_selected() is False, "checkbox2 should be unchecked"

    driver.quit()

if __name__ == "__main__":
    main()
