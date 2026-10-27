from libs.webui.pages.aws_secretagentshop.shipping_address_page import ShippingAddressPage
from libs.webui.pages.aws_secretagentshop.shopping_cart_review_page import ShoppingCartReviewPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestShippingAddressPage(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_shipping_address_page(self):
        self.logger.info("Verifying Home Page!")
        # Verify Home Page
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        # Add Product to Cart
        product_name = "Aqua Ace GT"
        self.home_page.add_product_to_loadout(product_name)

        # Navigate to Shipping Address Page
        shopping_card_review_page = ShoppingCartReviewPage(self.app.current_page)
        shopping_card_review_page.click_checkout()

        shipping_address_page = ShippingAddressPage(self.app.current_page)
        assert shipping_address_page.is_warning_message_displayed(), "Warning Message NOT displayed in Shipping Address Page!"
        assert shipping_address_page.get_warning_message() == "Warning This site is for demonstration/educational purposes only, do not enter personal details", "Warning message NOT matching in Shipping Address Page!"

        self.verify_breadcrumb(shipping_address_page)

        assert shipping_address_page.is_continue_button_exist(), "Continue Button NOT found!"

        shipping_address_page.click_continue_button()

        step = "Covert Delivery"
        assert shopping_card_review_page.does_header_exist(step), f"Header: {step} NOT found!"