from faker import Faker
from pytest_check import check
from libs.webui.app.aws_secretagentshop import SecretAgentShop
from libs.webui.pages.aws_secretagentshop.billing_page import BillingPage
from libs.webui.pages.aws_secretagentshop.home_page import HomePage
from libs.webui.pages.aws_secretagentshop.order_summary_page import OrderSummaryPage
from libs.webui.pages.aws_secretagentshop.shipping_address_page import ShippingAddressPage
from libs.webui.pages.aws_secretagentshop.shipping_method_page import ShippingMethodPage
from libs.webui.pages.aws_secretagentshop.shopping_cart_review_page import ShoppingCartReviewPage
from tests.core.test_webui_base import TestBaseWebUI


class TestSecretAgentShopBase(TestBaseWebUI):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.app = SecretAgentShop()

    @staticmethod
    def verify_page_header(curr_page: HomePage):
        with check:
            assert curr_page.get_page_title() == "Demo Store", "Page title didn't match!"
            assert curr_page.is_briefcase_icon_displayed(), "Briefcase Icon NOT found!"
            assert curr_page.is_home_link_displayed(), "Home link NOT found in Page Header!"
            assert curr_page.is_gadget_repository_link_displayed(), "Gadget Repository link NOT found in Page Header!"
            assert curr_page.is_shopping_cart_displayed(), "Shopping Cart NOT found in Page Header!"

    @staticmethod
    def verify_breadcrumb(curr_page: ShippingAddressPage):
        with check:
            step_texts = curr_page.get_breadcrumb_trail_step_texts()
            assert len(step_texts) == 3, "Breadcrumb steps count didn't match!"
            assert step_texts[0] == "Rendezvous Location", "Breadcrumb step (Rendezvous Location) didn't match!"
            assert step_texts[1] == "Covert Delivery", "Breadcrumb step (Covert Delivery) didn't match!"
            assert step_texts[2] == "Mission Funding", "Breadcrumb step (Mission Funding) didn't match!"

            step = "Rendezvous Location"
            assert curr_page.is_breadcrumb_step_highlighted(step), f"Step: {step} NOT highlighted!"
            step = "Covert Delivery"
            assert curr_page.is_breadcrumb_step_highlighted(step) == False, f"Step: {step} should NOT be highlighted!"
            step = "Mission Funding"
            assert curr_page.is_breadcrumb_step_highlighted(step) == False, f"Step: {step} should NOT be highlighted!"

    @staticmethod
    def verify_shopping_cart_review_page(curr_page: ShoppingCartReviewPage):
        with check:
            assert curr_page.is_shopping_card_review_page(), "Shopping Cart Review is NOT the current page!"
            assert curr_page.is_checkout_button_present(), "Checkout Button NOT found!"
            assert curr_page.get_checkout_button_text() == "Start Equipment Requisition", "Checkout Button Text didn't match!"

    @staticmethod
    def verify_shipping_method_page(curr_page: ShippingMethodPage):
        with check:
            assert curr_page.is_warning_message_displayed(), "Warning Message NOT displayed in Shipping Method Page!"
            assert curr_page.get_warning_message() == "Warning This site is for demonstration/educational purposes only, do not enter personal details", "Warning message NOT matching in Shipping Method Page!"

            shipping_methods = curr_page.get_shipping_methods()
            assert len(shipping_methods) == 2, "Shipping Method Count didn't match!"

            shipping_method = "Priority Mail"
            assert shipping_methods[0] == shipping_method, f"Shipping Method: {shipping_method} NOT found!"

            shipping_method = "Priority Mail Express"
            assert shipping_methods[1] == shipping_method, f"Shipping Method: {shipping_method} NOT found!"

    @staticmethod
    def verify_billing_page(curr_page: BillingPage):
        with check:
            assert curr_page.is_purchase_button_present(), "Purchase Button NOT found!"
            assert curr_page.is_back_to_cart_button_present(), "Back to Cart Button NOT found!"
            assert curr_page.is_warning_message_displayed(), "Warning Message NOT displayed in Shipping Method Page!"
            assert curr_page.get_warning_message() == "Warning This site is for demonstration/educational purposes only, do not enter personal details", "Warning message NOT matching in Shipping Method Page!"

            step = "Rendezvous Location"
            assert curr_page.is_breadcrumb_step_highlighted(step), f"Step: {step} NOT highlighted!"
            step = "Covert Delivery"
            assert curr_page.is_breadcrumb_step_highlighted(step), f"Step: {step} NOT highlighted!"
            step = "Mission Funding"
            assert curr_page.is_breadcrumb_step_highlighted(step), f"Step: {step} NOT highlighted!"

    @staticmethod
    def verify_product_in_order_details(curr_page: OrderSummaryPage, product_name, fsbd):
        order_summary = curr_page.get_product_details_in_order_summary()
        product_details = order_summary[product_name]
        quantity = product_details[1]
        product_total_price = product_details[2]
        price_per_product = product_details[3]

        expected_quantity = fsbd[f"{product_name}_quantity"]
        expected_product_total_price = fsbd[f"{product_name}_product_total_price"]
        expected_price_per_product = fsbd[f"{product_name}_price_per_product"]

        with check:
            assert quantity == expected_quantity, "Product Quantity didn't match!"
            assert product_total_price == expected_product_total_price, "Product price didn't match!"
            assert price_per_product == expected_price_per_product, "Price per product didn't match!"


    @staticmethod
    def verify_order_details(curr_page: OrderSummaryPage, fsbd):
        sub_total = fsbd["order_subtotal"]
        shipping_charges = fsbd["order_shipping_charges"]
        taxes = fsbd["order_taxes"]
        order_total = fsbd["order_total"]
        with check:
            assert curr_page.get_order_sub_total() == sub_total, f"Sub Total: {sub_total} is NOT matching!"
            assert curr_page.get_order_shipping() == shipping_charges, f"Shipping Charges: {shipping_charges} is NOT matching!"
            assert curr_page.get_order_tax() == taxes, f"Taxes: {taxes} is NOT matching!"
            assert curr_page.get_order_total() == order_total, f"Order Total: {order_total} is NOT matching!"


    @staticmethod
    def verify_page_footer(curr_page: HomePage):
        with check:
            section_title = "Quick Links"
            link_texts = curr_page.get_link_texts_under_section_in_page_footer(section_title)
            assert link_texts[0] == "Gadget Repository", f"First link under section: {section_title} in page footer didn't match!"
            assert link_texts[1] == "About", f"Second link under section: {section_title} in page footer didn't match!"

            section_title = "Tools"
            link_texts = curr_page.get_link_texts_under_section_in_page_footer(section_title)
            assert link_texts[0] == "Information",  f"First link under section: {section_title} in page footer didn't match!"
            assert link_texts[1] == "Topology", f"Second link under section: {section_title} in page footer didn't match!"

            contact_methods = curr_page.get_contact_methods_in_page_footer()
            assert contact_methods[0] == "Email", "First contact method section: CONTACT in page footer didn't match!"
            assert contact_methods[1] == "Phone", "Second contact method under section: CONTACT in page footer didn't match!"

    @staticmethod
    def generate_fake_shipping_and_billing_details():
        fsbd = {}
        fake = Faker()
        fsbd["first_name"] = fake.first_name()
        fsbd["last_name"] = fake.last_name()
        fsbd["email_address"] = f"{fsbd['first_name']}_{fsbd['last_name']}@sdet.com"
        fsbd["street_address"] = fake.street_address()
        fsbd["city"] = fake.city()
        fsbd["state"] = fake.state_abbr()
        fsbd["zip"] = fake.zipcode()
        fsbd["full_name"] = f"{fsbd['first_name']}_{fsbd['last_name']}"
        fsbd["card_number"] = fake.credit_card_number(card_type='visa16')
        fsbd["expiry_date"] = fake.credit_card_expire()
        fsbd["cvv"] = fake.credit_card_security_code()
        return fsbd

    @staticmethod
    def verify_order_summary_page(curr_page: OrderSummaryPage):
        with check:
            assert curr_page.is_warning_message_displayed(),  "Warning Message NOT displayed in Order Summary Page!"
            assert curr_page.get_warning_message() == "Warning This site is for demonstration/educational purposes only, this order is not genuine", "Warning message NOT matching in Order Summary Page!"

            stages = curr_page.get_progress_bar_stages()
            assert len(stages) == 3, "Stages size count is NOT 3"
            stage = "Order placed"
            assert stages[0] == stage, f"First stage: {stage} is NOT matching!"
            assert curr_page.is_progress_bar_stage_highlighted(stage), f"Stage: {stage} is NOT Highlighted!"
            stage = "Processing"
            assert stages[1] == stage, f"Second stage: {stage} is NOT matching!"
            assert curr_page.is_progress_bar_stage_highlighted(stage) == False, f"Stage: {stage} should NOT be Highlighted!"
            stage = "Shipped"
            assert stages[2] == stage, f"Third stage: {stage} is NOT matching!"
            assert curr_page.is_progress_bar_stage_highlighted(stage) == False, f"Stage: {stage} should NOT be Highlighted!"


    @classmethod
    def teardown_class(cls):
        super().teardown_class()
        cls.app.close_browser()
