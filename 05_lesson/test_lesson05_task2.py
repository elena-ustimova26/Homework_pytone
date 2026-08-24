from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Откройте страницу https://httpbin.qa-territory.online/forms/post
def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    #найдите поле ввода с названием custname u Введите в него ваше имя

    driver.find_element(
        By.NAME, "custname").send_keys("Елена")
    
    #Найдите кнопку Submit и нажмите на нее.
    old_url = driver.current_url
    driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]").click()
    sleep(2)

    WebDriverWait(driver, 5).until(
        EC.url_changes(old_url)
    )
    assert driver.current_url != old_url, f"URL не изменился. Текущий URL: {driver.current_url}"

    driver.quit()
