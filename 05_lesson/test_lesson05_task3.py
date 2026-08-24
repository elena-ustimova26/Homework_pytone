from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()

    #Найдите все ссылки на странице (тег <a>)
    all_links = driver.find_elements(By.TAG_NAME, "a")
    
    #Проверьте, что количество ссылок равно 9
    expected_count = 9
    actual_count = len(all_links)
    assert actual_count == expected_count, \
        f"Ожидалось {expected_count} ссылок, найдено {actual_count}"
    
    #Проверьте, что все ссылки отображаются на странице
    for i, link in enumerate(all_links):
        assert link.is_displayed(
        ), f"Ссылка с индексом {i} не отображается на странице"
    
    #Проверьте, что текст первой ссылки содержит "1"
    first_link_text = all_links[0].text
    assert "1" in first_link_text, \
        f"Текст первой ссылки '{first_link_text}' не содержит '1'"
    
    print(f"Все проверки пройдены! Найдено {actual_count} ссылок")
    print(f"Текст первой ссылки: '{first_link_text}'")
    
    driver.quit()