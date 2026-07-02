from pages.login_page import LoginPage


def test_valid_login(driver):

        login_page = LoginPage(driver)

        inventory_page = login_page.login(
                "standard_user", "secret_sauce")

        
        assert inventory_page.is_inventory_loaded(), \
        "Something's wrong check again !"
        print("Page has loaded")
        
        assert inventory_page.get_product_count() == 6, \
        "Expected 6, wtf ! "
        print("Ooooh there those 6 products....la la")

        
        inventory_page.add_to_cart()

        assert inventory_page.get_cart_badge_count() == 1

        cart_page = inventory_page.click_cart()

        assert cart_page.is_item_present()



    
    


