import logging
from playwright.sync_api import Page
from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class ShippingAddressPage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def is_shipping_address_page(self):
        step = "Rendezvous Location"
        return self.does_header_exist(step)

    def enter_street_address(self, street_address):
        logger.info(f"Entering Street Address: {street_address}")
        self.enter_text_in_field_using_name_attr("address1", street_address)

    def fill_shipping_details(self, shipping_details):
        self.enter_text_in_field("First Name", shipping_details["first_name"])
        self.enter_text_in_field("Last Name", shipping_details["last_name"])
        self.enter_street_address(shipping_details["street_address"])
        self.enter_text_in_field("City", shipping_details["city"])
        self.enter_text_in_field("State/Province", shipping_details["state"])
        self.enter_text_in_field("ZIP", shipping_details["zip"])
        self.enter_text_in_field("E-mail", shipping_details["email_address"])

