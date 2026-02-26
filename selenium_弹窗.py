from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/javascript_alerts"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    # 1) JS Alert
    driver.find_element(By.XPATH, "//button[contains(., 'JS Alert')]").click()
    driver.switch_to.alert.accept()
    result = wait.until(EC.visibility_of_element_located((By.ID, "result"))).text
    print("alert:", result)
    assert "successfully clicked an alert" in result

    # 2) JS Confirm（取消）
    driver.find_element(By.XPATH, "//button[contains(., 'JS Confirm')]").click()
    driver.switch_to.alert.dismiss()
    result = driver.find_element(By.ID, "result").text
    print("confirm:", result)
    assert "Cancel" in result

    # 3) JS Prompt（输入 + 确认）
    driver.find_element(By.XPATH, "//button[contains(., 'JS Prompt')]").click()
    a = driver.switch_to.alert
    a.send_keys("hello")
    a.accept()
    result = driver.find_element(By.ID, "result").text
    print("prompt:", result)
    assert "hello" in result

finally:
    driver.quit()
