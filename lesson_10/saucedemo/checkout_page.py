import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Step One (форма)
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Step Two (обзор)
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Заполнить форму на первом шаге checkout")
    def fill_checkout_form(
        self, first_name: str, last_name: str, postal_code: str
    ):
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(
            postal_code
        )
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Получить итоговую сумму со страницы обзора")
    def get_total(self) -> float:
        total_text = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        ).text
        # total_text выглядит как "Total: $58.29" – извлекаем число
        amount_str = total_text.replace("Total: $", "").strip()
        return float(amount_str)
