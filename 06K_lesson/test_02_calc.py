from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_slow_calculator():
  
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

# 2. Ввести значение 45 в поле задержки
    delay_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
    delay_input.clear()
    delay_input.send_keys("45")

# 3. Нажать кнопки: 7, +, 8, = 
    buttons = ["7", "+", "8", "="]
    for btn_text in buttons:
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                      By.XPATH, f"//span[text()='{btn_text}']"))
            )
# Прокручиваем к кнопке и кликаем через JS
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", button
            )
            driver.execute_script("arguments[0].click();", button)

# 4. Дождаться появления результата 15 в окне калькулятора
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

# 5. Проверить, что результат равен 15
    actual_result = driver.find_element(By.CLASS_NAME, "screen").text
    assert actual_result == "15", (
            f"Ожидался результат '15', получен '{actual_result}'"
        )

    driver.save_screenshot("test_02_calc.png")

    driver.quit()
