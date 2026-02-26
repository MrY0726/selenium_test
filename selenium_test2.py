from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
 """
 打开页面后，找到页面里所有 <select>，打印数量（应该不止 1 个）。

第 1 个下拉（Fruit）：用 Select(...).select_by_visible_text(...) 选择 Apple，然后打印当前选中的文本。

第 2 个下拉（Super hero，多选）：

先 is_multiple() 判断它是多选（True）

再选择 The Avengers 和 Batman（两项都选上）

打印所有已选项（用 all_selected_options）

第 3 个下拉（Programming language）：

选择“最后一个选项”（用 index）

打印这个下拉的所有 options 文本列表，以及“最后一个选项”的文本

第 4 个下拉（Country）：

用 select_by_value(...) 选择 India（value 你自己在页面里确认一下是啥）

打印：get_attribute("value")（当前 value）+ 当前选中项的文本
 """
URL = "https://www.qaplayground.com/practice/select"

def main():
    driver = webdriver.Edge()  # 如果你用 Chrome：webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(URL)

        # 等至少一个 select 出现（满足“必须用 WebDriverWait”）
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))

        # 页面上有 4 个下拉框：Fruit / Super hero(多选) / Programming language / Country
        selects = driver.find_elements(By.TAG_NAME, "select")
        if len(selects) < 4:
            raise RuntimeError(f"预期至少 4 个 <select>，但实际找到 {len(selects)} 个")

        fruit_sel = Select(selects[0])
        hero_sel  = Select(selects[1])
        lang_sel  = Select(selects[2])
        country_sel = Select(selects[3])

        # 1) Fruit：按可见文本选 Apple
        fruit_sel.select_by_visible_text("Apple")
        print("Fruit selected:", fruit_sel.first_selected_option.text)

        # 2) Super hero：多选，选 The Avengers + Batman
        print("Hero is_multiple:", hero_sel.is_multiple)
        if not hero_sel.is_multiple:
            raise RuntimeError("第二个下拉框预期是多选，但 is_multiple=False")

        # 可选：先清空已选（有些页面默认选中一项）
        try:
            hero_sel.deselect_all()
        except Exception:
            pass

        hero_sel.select_by_visible_text("The Avengers")
        hero_sel.select_by_visible_text("Batman")
        print("Heroes selected:", [o.text for o in hero_sel.all_selected_options])

        # 3) Programming language：选最后一个，并打印所有选项
        all_lang = [o.text.strip() for o in lang_sel.options]
        last_idx = len(all_lang) - 1
        lang_sel.select_by_index(last_idx)
        print("All languages:", all_lang)
        print("Last language selected:", lang_sel.first_selected_option.text)

        # 4) Country：要求用 value 选 India
        # 先从 options 里找出 India 对应的 value，再 select_by_value（这样不怕你不知道 value 是啥）
        india_value = None
        for opt in country_sel.options:
            if opt.text.strip() == "India":
                india_value = opt.get_attribute("value")
                break
        if india_value is None:
            raise RuntimeError("找不到 Country 下拉里的 India 选项")

        country_sel.select_by_value(india_value)
        print("Country selected text:", country_sel.first_selected_option.text)
        print("Country selected value:", country_sel.first_selected_option.get_attribute("value"))

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

 
 
 
 
 


    