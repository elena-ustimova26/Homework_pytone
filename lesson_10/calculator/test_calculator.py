import allure
from calculator_page import CalculatorPage


@allure.epic("Калькулятор")
@allure.feature("Медленный калькулятор")
@allure.story("Сложение")
@allure.title("Проверка сложения 7 + 8 с задержкой 45 секунд")
@allure.description(
    "Устанавливаем задержку 45 сек, нажимаем 7 + 8 =, ожидаем 15"
)
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)

    with allure.step("Нажать кнопки: 7, +, 8, ="):
        for btn in ["7", "+", "8", "="]:
            calc_page.click_button(btn)

    with allure.step("Ожидать результат 15"):
        calc_page.wait_for_result("15", timeout=50)

    with allure.step("Проверить результат"):
        actual = calc_page.get_result()
        assert actual == "15", f"Ожидался результат '15', получен '{actual}'"

    with allure.step("Сохранить скриншот"):
        calc_page.save_screenshot("screen/test_02_calc.png")
