import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket(browser):
    browser.get(link)
    time.sleep(20)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, 'Кнопка не найдена!'

