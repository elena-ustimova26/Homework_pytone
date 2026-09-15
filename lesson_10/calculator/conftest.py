import pytest
import allure
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

    # Если тест упал — прикрепляем скриншот в Allure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
