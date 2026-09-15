import allure
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.epic("SauceDemo")
@allure.feature("Оформление заказа")
@allure.story("Расчет итоговой суммы")
@allure.title("Проверка итоговой суммы при покупке трёх товаров")
@allure.description("Авторизация standard_user, добавление трёх товаров, оформление, проверка суммы 58.29")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout_total(driver):
    with allure.step("Открыть сайт и авторизоваться"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory_page = InventoryPage(driver)
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Нажать Checkout"):
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

    with allure.step("Заполнить форму оформления"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form(
            first_name="Иван", last_name="Иванов", 
            postal_code="123456"
        )

    with allure.step("Получить итоговую сумму"):
        total = checkout_page.get_total()

    with allure.step("Проверить сумму"):
        expected_total = 58.29
        assert total == expected_total, (
            f"Ожидалось {expected_total}, получено {total}"
        )

    with allure.step("Сохранить скриншот"):
        driver.save_screenshot("screen/saucedemo_checkout.png")
