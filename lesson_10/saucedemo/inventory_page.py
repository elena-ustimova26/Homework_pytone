import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//div[text()='{}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']",
    )
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Добавить товар по имени в корзину")
    def add_item_to_cart(self, item_name: str):
        xpath = self.ADD_TO_CART_BUTTON[1].format(item_name)
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    @allure.step("Перейти в корзину (клик по иконке)")
    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
