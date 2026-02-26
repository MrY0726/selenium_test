from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/windows"

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    # 1) 记录当前窗口
    main_handle = driver.current_window_handle
    print("main handle:", main_handle)

    # 2) 点击打开新窗口
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here"))).click()

    # 3) 等待新窗口出现（窗口数量变成 2）
    wait.until(lambda d: len(d.window_handles) == 2)

    # 4) 找到新窗口句柄并切换
    new_handle = [h for h in driver.window_handles if h != main_handle][0]
    driver.switch_to.window(new_handle)

    # 5) 读取新窗口内容
    h3 = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
    print("new window h3:", h3)
    assert "New Window" in h3

    # 6) 关闭新窗口，切回主窗口
    driver.close()
    driver.switch_to.window(main_handle)

    # 7) 主窗口标题打印一下
    print("back to main, title:", driver.title)

finally:
    driver.quit()



#content > div > a