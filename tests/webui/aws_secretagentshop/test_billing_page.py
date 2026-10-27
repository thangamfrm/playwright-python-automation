from libs.webui.pages.aws_secretagentshop.billing_page import BillingPage
from libs.webui.pages.aws_secretagentshop.shipping_address_page import ShippingAddressPage
from libs.webui.pages.aws_secretagentshop.shipping_method_page import ShippingMethodPage
from libs.webui.pages.aws_secretagentshop.shopping_cart_review_page import ShoppingCartReviewPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestBillingPage(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_billing_page(self):
        self.logger.info("Verifying Billing Page!")
        # Verify Home Page
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        # Add Product to Cart
        product_name = "Aqua Ace GT"
        self.home_page.add_product_to_loadout(product_name)

        # Navigate to Shipping Address Page
        shopping_card_review_page = ShoppingCartReviewPage(self.app.current_page)
        shopping_card_review_page.click_checkout()

        # Shipping Address Page
        shipping_address_page = ShippingAddressPage(self.app.current_page)
        fsbd = self.generate_fake_shipping_and_billing_details()
        shipping_address_page.fill_shipping_details(fsbd)
        shipping_address_page.click_continue_button()

        # Shipping Method Page
        shipping_method_page = ShippingMethodPage(self.app.current_page)
        assert shipping_method_page.is_shipping_method_page(), f"Shipping Methods is NOT the current page: {shipping_method_page.get_page_title()}"
        self.verify_shipping_method_page(shipping_method_page)
        shipping_method_page.click_continue_button()

        # Billing Page
        billing_page = BillingPage(self.app.current_page)
        self.verify_billing_page(billing_page)
        billing_page.fill_billing_details(fsbd)

        # Click Back Button - Verify Shopping Cart Review Page
        billing_page.click_back_to_cart_button()
        self.verify_shopping_cart_review_page(shopping_card_review_page)

        self.logger.info("Verified Billing Page")
