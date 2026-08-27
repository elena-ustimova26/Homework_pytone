from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    driver.maximize_window()
# Найдите и кликните на ссылку HTML Form.
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
# Проверьте, что URL изменился на /forms/post.
    sleep(2)
    assert "/forms/post" in driver.current_url, "URL не содержит /forms/post"
# Вернитесь назад на главную страницу.
    driver.back()
# Проверьте, что вернулись на исходный URL. 
    sleep(2)      
    assert driver.current_url == "https://httpbin.qa-territory.online/", "Не вернулись на главную"

    driver.quit()
