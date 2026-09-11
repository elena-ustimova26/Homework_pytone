from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    # Локаторы элементов
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")
    # Базовый шаблон для кнопок – будет подставляться текст
    BUTTON_TEMPLATE = "//span[text()='{text}']"

    def __init__(self, driver, url="https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        # Открыть страницу калькулятора
        self.driver.get(self.url)
        self.driver.maximize_window()

    def set_delay(self, seconds: int):
        # Установить задержку в поле #delay
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, text: str):
        # Нажать кнопку калькулятора по её тексту.

        xpath = self.BUTTON_TEMPLATE.format(text=text)
        button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        # Прокрутка к элементу и клик через JS
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def get_result(self) -> str:
        # Получить текст из поля результата (экрана)
        screen = self.driver.find_element(*self.SCREEN)
        return screen.text

    def wait_for_result(self, expected: str, timeout: int = 50):
        # Ожидать появления указанного текста в поле результата
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )

    def save_screenshot(self, filename: str):
        # Сделать скриншот страницы
        self.driver.save_screenshot(filename)
