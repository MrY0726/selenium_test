from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://the-internet.herokuapp.com/drag_and_drop"

JS_DND = """
function triggerDragAndDrop(selectorDrag, selectorDrop) {
  const drag = document.querySelector(selectorDrag);
  const drop = document.querySelector(selectorDrop);
  const dataTransfer = new DataTransfer();

  drag.dispatchEvent(new DragEvent('dragstart', { dataTransfer }));
  drop.dispatchEvent(new DragEvent('drop', { dataTransfer }));
  drag.dispatchEvent(new DragEvent('dragend', { dataTransfer }));
}
triggerDragAndDrop(arguments[0], arguments[1]);
"""

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)

    driver.execute_script(JS_DND, "#column-a", "#column-b")   

    a_text = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "#column-a header").text)
    b_text = driver.find_element(By.CSS_SELECTOR, "#column-b header").text
    print("A:", a_text, "B:", b_text)

finally:
    driver.quit()
