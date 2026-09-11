from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_saucedemo_checkout_total(driver):
    # Тест-сценарий:
    # 1. Открыть сайт
    # 2. Авторизоваться как standard_user
    # 3. Добавить три товара
    # 4. Перейти в корзину → Checkout
    # 5. Заполнить форму (данные можно подставить)
    # 6. Проверить, что итоговая сумма = $58.29

    # 1. Страница логина
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Главная страница – добавляем товары
    inventory_page = InventoryPage(driver)
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items_to_add:
        inventory_page.add_item_to_cart(item)

    # 3. Переход в корзину
    inventory_page.go_to_cart()

    # 4. Страница корзины – Checkout
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    # 5. Страница оформления – заполняем форму (свои данные)
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form(
        first_name="Иван", last_name="Иванов", postal_code="123456"
    )

    # 6. Получаем итоговую сумму
    total = checkout_page.get_total()

    # 7. Проверка
    expected_total = 58.29
    assert (
        total == expected_total
    ), f"Ожидалось {expected_total}, получено {total}"

    # Скриншот
    driver.save_screenshot("screen/saucedemo_checkout.png")
