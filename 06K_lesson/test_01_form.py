from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.service import Service

def test_01_form():
    driver = webdriver.Edge()
    driver.maximize_window()

# Открыть страницу 
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        )

#Заполните форму значениями
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
        }
    for field_name, value in form_data.items():
            field = driver.find_element(By.NAME, field_name)
            field.clear()
            field.send_keys(value)

#Нажмите кнопку Submit
    submit_button = driver.find_element(
         By.CSS_SELECTOR, "button[type='submit']"
         )
    driver.execute_script(
         "arguments[0].scrollIntoView({block: 'center'});", submit_button
         )
    driver.execute_script("arguments[0].click();", submit_button)

#Проверьте (assert), что поле Zip code подсвечено красным

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

# Проверяем, что zip-code подсвечен красным
    zip_element = driver.find_element(By.ID, "zip-code")
    assert zip_element.text == "N/A",(
          f"Ожидалось 'N/A', получено '{zip_element.text}'"
    )
    assert "alert-danger" in zip_element.get_attribute("class"), \
        f"Zip-code не подсвечен красным. Классы: {zip_element.get_attribute(
              'class'
              )}"

#Проверьте (assert), что остальные поля подсвечены зеленым

    green_fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
        }
    for field_id, expected_value in green_fields.items():
        element = driver.find_element(By.ID, field_id)
        
    assert element.text == expected_value, (
        f"Поле '{field_id}': ожидалось '{expected_value}', "
        f"получено '{element.text}'"
        )
    
    assert "alert-success" in element.get_attribute("class"), (
        f"Поле '{field_id}' НЕ подсвечено зелёным. "
        f"Классы: {element.get_attribute('class')}"
        )

    driver.save_screenshot("test_01_form.png")

    driver.quit()
