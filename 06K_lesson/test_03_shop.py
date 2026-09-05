from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_checkout_total():

    driver = webdriver.Firefox()
    driver.maximize_window()

    # 1. Открыть сайт и авторизоваться
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ожидание загрузки страницы с товарами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # 2. Добавить товары в корзину
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    for item_id in items_to_add:
        driver.find_element(By.ID, item_id).click()

    # 3. Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )

    # Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # 4. Заполнить форму данными
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # Нажать Continue
    driver.find_element(By.ID, "continue").click()

    # Ожидание загрузки страницы с итогами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "checkout_summary_container")
        )
    )

    # 5. Прочитать итоговую стоимость
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text

    # Извлечение числа из текста (например, "Total: $58.29")
    total_value = total_text.replace("Total: ", "").strip()

    # 6. Проверка итоговой суммы
    expected_total = "$58.29"
    assert total_value == expected_total, (
        f"Итоговая сумма не совпадает. "
        f"Ожидалось: {expected_total}, получено: {total_value}"
    )

    driver.save_screenshot("test_03_shop.png")

    driver.quit()
