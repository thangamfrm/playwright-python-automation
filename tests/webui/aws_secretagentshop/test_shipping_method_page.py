from libs.webui.pages.aws_secretagentshop.shipping_address_page import ShippingAddressPage
from libs.webui.pages.aws_secretagentshop.shipping_method_page import ShippingMethodPage
from libs.webui.pages.aws_secretagentshop.shopping_cart_review_page import ShoppingCartReviewPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestShippingMethodPage(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_home_page(self):
        self.logger.info("Verifying Home Page!")
        # Verify Header & Footer
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        # Add Product to Cart
        product_name = "Aqua Ace GT"
        self.home_page.add_product_to_loadout(product_name)

        # Navigate to Shipping Address Page
        shopping_card_review_page = ShoppingCartReviewPage(self.app.current_page)
        shopping_card_review_page.click_checkout()

        shipping_address_page = ShippingAddressPage(self.app.current_page)
        shipping_address_page.click_continue_button()

        shipping_method_page = ShippingMethodPage(self.app.current_page)
        assert shipping_method_page.is_shipping_method_page(), "Shipping Methods is NOT the current page!"
        self.verify_shipping_method_page(shipping_method_page)

        # Verify Back Button - Navigate back to Shopping Cart Review Page
        shipping_method_page.click_back_to_cart_button()
        self.verify_shopping_cart_review_page(shopping_card_review_page)
        shipping_address_page.click_shopping_cart()

        self.logger.info("Shipping Method Page Test Complete!")