from selene import browser, have, by, be


def test_for_adding_and_removing_items_from_the_cart():
    browser.open('/')
    browser.element('.search-widget-field').type('Бэтмен').press_enter()
    browser.element('.product-card-wrapper').click()
    browser.element('.button-buy').click()
    browser.element('.main-menu-wrapper .shopcart-widget-amount').click()
    browser.driver.refresh()
    browser.element('.cart-item-inner').should(have.text('Бэтмен'))







