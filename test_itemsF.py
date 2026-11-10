import time


def test_product_page_has_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    button = browser.find_element("css selector", ".btn-add-to-basket")

    assert button is not None, "Add to cart button not found on product page"
