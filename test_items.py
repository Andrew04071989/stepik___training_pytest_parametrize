import time


link = "http://selenium1py.pythonanywhere.com/" \
       "catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    result = browser.find_element_by_css_selector(
        'button.btn.btn-lg.btn-primary.btn-add-to-basket'
    )
    time.sleep(3)
    print(f"Button is presented as: {result.text}")
    assert result,  "We have no add to basket button"
