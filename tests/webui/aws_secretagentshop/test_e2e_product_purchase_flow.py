from libs.webui.pages.aws_secretagentshop.billing_page import BillingPage
from libs.webui.pages.aws_secretagentshop.order_summary_page import OrderSummaryPage
from libs.webui.pages.aws_secretagentshop.shipping_address_page import ShippingAddressPage
from libs.webui.pages.aws_secretagentshop.shipping_method_page import ShippingMethodPage
from libs.webui.pages.aws_secretagentshop.shopping_cart_review_page import ShoppingCartReviewPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestE2EProductPurchaseFlow(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_e2e_product_purchase_purchase_flow(self):
        self.logger.info("Verifying E2E Product Purchase Flow!")
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

        # Update Product Details
        fsbd["product_name_one"] = product_name
        fsbd[f"{product_name}_quantity"] = "Quantity: 1"
        fsbd[f"{product_name}_product_total_price"] = "$10000"
        fsbd[f"{product_name}_price_per_product"] = "$10000 each"

        step = "Covert Delivery"
        assert shopping_card_review_page.does_header_exist(step) == False, f"Header: {step} should NOT be present in this page!"
        shipping_address_page.click_continue_button()
        assert shopping_card_review_page.does_header_exist(step), f"Header: {step} NOT found!"

        # Shipping Method Page
        shipping_method_page = ShippingMethodPage(self.app.current_page)
        assert shipping_method_page.is_shipping_method_page(), f"Shipping Methods is NOT the current page: {shipping_method_page.get_page_title()}"
        self.verify_shipping_method_page(shipping_method_page)
        shipping_method_page.click_continue_button()

        # Billing Page
        billing_page = BillingPage(self.app.current_page)
        self.verify_billing_page(billing_page)
        billing_page.fill_billing_details(fsbd)

        step = "Mission Authorized!"
        assert billing_page.does_header_exist(step) == False, f"Header: {step} should NOT be found!"
        billing_page.click_purchase_button()
        assert billing_page.does_header_exist(step), f"Header: {step} NOT found!"

        order_summary_page = OrderSummaryPage(self.app.current_page)
        self.verify_order_summary_page(order_summary_page)

        assert order_summary_page.get_shopping_cart_size() == "1", "Shopping Cart size didn't match!"
        assert order_summary_page.is_order_id_a_valid_uuid(), "Generated Order ID is NOT a valid UUID!"

        fsbd["order_subtotal"] = "$10000"
        fsbd["order_shipping_charges"] = "$10"
        fsbd["order_taxes"] = "$5"
        fsbd["order_total"] = "$10015"

        self.verify_product_in_order_details(order_summary_page, product_name, fsbd)
        self.verify_order_details(order_summary_page, fsbd)
        self.logger.info("Verified E2E Product Purchase Flow")
