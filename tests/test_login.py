from pages.login_page import LoginPage


def test_valid_login(driver):

        login_page = LoginPage(driver)

        inventory_page = login_page.login(
                "standard_user", "secret_sauce")

        
        assert inventory_page.is_inventory_loaded(), \
        "Page has loaded"
        


        assert inventory_page.get_product_count() == 6, \
        "Ooooh there those 6 products....la la"



    
    


