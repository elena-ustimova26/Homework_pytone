from pages.calculator_page import CalculatorPage


def test_slow_calculator(driver):
    # 1. Создаём объект страницы
    calc_page = CalculatorPage(driver)

    # 2. Открываем страницу
    calc_page.open()

    # 3. Устанавливаем задержку 45 секунд
    calc_page.set_delay(45)

    # 4. Последовательно нажимаем кнопки: 7, +, 8, =
    for btn in ["7", "+", "8", "="]:
        calc_page.click_button(btn)

    # 5. Ожидаем появления результата "15" (таймаут 50 сек)
    calc_page.wait_for_result("15", timeout=50)

    # 6. Проверяем результат
    actual = calc_page.get_result()
    assert actual == "15", f"Ожидался результат '15', получен '{actual}'"

    # 7. Сохраняем скриншот (опционально)
    calc_page.save_screenshot("screen/test_02_calc.png")
