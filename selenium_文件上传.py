from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/upload"

# 1) 创建一个临时文件（放在脚本同目录），默认当前的工作目录
tmp_file = Path("upload_demo.txt")
tmp_file.write_text("hello selenium upload\n", encoding="utf-8")

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    # 2) 找到 <input type="file">，把本地文件绝对路径传进去
    file_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
    file_input.send_keys(str(tmp_file.resolve()))

    # 3) 点击上传按钮
    wait.until(EC.element_to_be_clickable((By.ID, "file-submit"))).click()

    # 4) 验证上传结果页面
    header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
    uploaded_name = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files"))).text

    print("header:", header)
    print("uploaded:", uploaded_name)

    assert "File Uploaded!" in header
    assert uploaded_name.strip() == tmp_file.name

finally:
    driver.quit()
    # 清理临时文件（可选）
    try:
        tmp_file.unlink()
    except Exception:
        pass
