from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

# Установите cookie пользователя 1.
    driver.add_cookie({
   "name": "SESSION",
   "value": "NDJkNGViN2QtZDEzYy00MWVhLTliMmQtOTk2YTczMTcwMGE0",
   "domain": "gitflic.ru"
})
 # Обновите страницу
    driver.refresh()

# Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/abbiecoffee")

# Сохраните текущий URL.
    url_user1 = driver.current_url

# Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()   

# Установите cookie пользователя 2.
    driver.add_cookie({
   "name": "SESSION",
   "value": "OTUzNjYyYjctNDFhNi00OGJmLWIzYjctMzQ0Zjk5ODExMTFk",
   "domain": "gitflic.ru"
})
# Обновите страницу
    driver.refresh()

# Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/isobelmoccasin")

# Сохраните текущий URL.
    url_user2 = driver.current_url

# Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2, (
        f"URL должны различаться!\n"
        f"URL1: {url_user1}\n"
        f"URL2: {url_user2}"
        )

    driver.quit()
