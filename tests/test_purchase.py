from pages.login_page import LoginPage

def test_purchase_flow(driver):

    login_page = LoginPage(driver)

    inventory_page = login_page.login("standard_user",
                                       "secret_sauce")

    inventory_page.add_to_cart()

    print(inventory_page.get_cart_badge_count())

    assert inventory_page.get_cart_badge_count() == 2

    cart_page = inventory_page.click_cart()

    assert cart_page.is_item_present()

    checkout_info_page = cart_page.click_checkout()

    checkout_info_page.enter_checkout_information("Vash",
                                                   "Stampede",
                                                     "666")

    checkout_overview_page = checkout_info_page.click_continue()

    complete_checkout_page = checkout_overview_page.click_finish()

    assert complete_checkout_page.is_order_completed()

    inventory_page = complete_checkout_page.click_back_home()

    assert inventory_page.is_inventory_loaded()

