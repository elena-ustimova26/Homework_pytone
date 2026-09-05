from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # 3. Дождитесь появления текста "Hello World!"
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "finish"))
    )
    actual_text = element.text

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("06_lesson/screen/hello.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert actual_text == "Hello World!", (
        f"Ожидалось 'Hello World!', получено '{actual_text}'")


    driver.quit()
