from libs.webui.pages.aws_secretagentshop.billing_page import BillingPage
from libs.webui.pages.aws_secretagentshop.home_page import HomePage
from libs.webui.pages.aws_secretagentshop.order_summary_page import OrderSummaryPage
from libs.webui.pages.aws_secretagentshop.shipping_address_page import ShippingAddressPage
from libs.webui.pages.aws_secretagentshop.shipping_method_page import ShippingMethodPage
from libs.webui.pages.aws_secretagentshop.shopping_cart_review_page import ShoppingCartReviewPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestOrderSummaryPage(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_order_summary_page(self):
        self.logger.info("Verifying Order Summary Page!")
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

        # Update Product One Details
        fsbd["product_name_one"] = product_name
        fsbd[f"{product_name}_quantity"] = "Quantity: 1"
        fsbd[f"{product_name}_product_total_price"] = "$10000"
        fsbd[f"{product_name}_price_per_product"] = "$10000 each"

        # Step 4: Shipping Method Page
        shipping_method_page = ShippingMethodPage(self.app.current_page)
        assert shipping_method_page.is_shipping_method_page(), "Shipping Methods is NOT the current page!"
        self.verify_shipping_method_page(shipping_method_page)

        # Add Second Product to Cart
        shipping_method_page.click_briefcase_icon()
        product_name_two = "Audio-Illusion Spinner"
        self.home_page = HomePage(self.app.current_page)
        self.home_page.add_product_to_loadout(product_name_two)

        # Proceed to Shipping & Billing
        shopping_card_review_page = ShoppingCartReviewPage(self.app.current_page)
        shopping_card_review_page.click_checkout()

        shipping_address_page = ShippingAddressPage(self.app.current_page)
        shipping_address_page.click_continue_button()

        shipping_method_page = ShippingMethodPage(self.app.current_page)
        shipping_method_page.click_continue_button()

        # Verify Back Button - Navigate back to Shopping Cart Review Page
        shipping_method_page.click_back_to_cart_button()
        self.verify_shopping_cart_review_page(shopping_card_review_page)
        shopping_card_review_page.click_checkout()

        shipping_address_page = ShippingAddressPage(self.app.current_page)
        shipping_address_page.click_continue_button()

        shipping_method_page = ShippingMethodPage(self.app.current_page)
        shipping_method_page.click_continue_button()

        # Update Product Two Details
        fsbd["product_name_two"] = product_name_two
        fsbd[f"{product_name_two}_quantity"] = "Quantity: 1"
        fsbd[f"{product_name_two}_product_total_price"] = "$190"
        fsbd[f"{product_name_two}_price_per_product"] = "$190 each"

        # Step 5: Billing Page
        billing_page = BillingPage(self.app.current_page)
        self.verify_billing_page(billing_page)
        billing_page.fill_billing_details(fsbd)

        # Purchase
        billing_page.click_purchase_button()

        # Order Summary Page
        order_summary_page = OrderSummaryPage(self.app.current_page)
        self.verify_order_summary_page(order_summary_page)

        assert order_summary_page.get_shopping_cart_size() == "2", "Shopping Cart size didn't match!"
        assert order_summary_page.is_order_id_a_valid_uuid(), "Generated Order ID is NOT a valid UUID!"

        fsbd["order_subtotal"] = "$10190"
        fsbd["order_shipping_charges"] = "$10"
        fsbd["order_taxes"] = "$5"
        fsbd["order_total"] = "$10205"

        # Verify First Product
        self.verify_product_in_order_details(order_summary_page, product_name, fsbd)
        # Verify Second Product
        self.verify_product_in_order_details(order_summary_page, product_name_two, fsbd)

        order_summary_page.click_shopping_cart()
        assert order_summary_page.get_shopping_cart_size() == "0", "Shopping Cart size didn't match!"
        assert shopping_card_review_page.get_basket_text() == "You don't have any items!", "Shopping Cart Basket Empty Message didn't match!"

        self.logger.info("Order Summary Page Test Complete!")