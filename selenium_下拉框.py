from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/dropdown"

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    # 1) 等待下拉框出现，并用 Select 包装（Select 专门用来操作 <select> 下拉框）
    dropdown = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    sel = Select(dropdown)
    # 2) 选择 value="2" 的选项（比按文字 "Option 2" 更稳，避免翻译影响）
    sel.select_by_value("2")

    # 3) 打印当前选中项（text 是页面显示文字，value 是 option 的 value 属性）
    chosen = sel.first_selected_option
    print("selected text:", chosen.text)
    print("selected value:", chosen.get_attribute("value"))

    # 4) 断言：确认选中了 value=2
    assert chosen.get_attribute("value") == "2"

finally:
    driver.quit()