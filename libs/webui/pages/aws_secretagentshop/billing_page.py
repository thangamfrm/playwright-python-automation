import logging
from playwright.sync_api import Page
from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class BillingPage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def is_billing_page(self):
        step = "Mission Funding"
        return self.does_header_exist(step)

    def set_card_holder_name(self, full_name):
        logger.info(f"Entering Card Holder Name: {full_name}")
        self.enter_text_in_field_using_name_attr("cardHolder", full_name)

    def set_card_number(self, card_number):
        logger.info(f"Entering Card Number: {card_number}")
        self.enter_text_in_field_using_name_attr("cardNumber", card_number)

    def set_expiry_date(self, expiry_date):
        logger.info(f"Entering Expiry Date: {expiry_date}")
        self.enter_text_in_field_using_name_attr("expiryDate", expiry_date)

    def fill_billing_details(self, billing_details):
        self.set_card_holder_name(billing_details["full_name"])
        self.set_card_number(billing_details["card_number"])
        self.set_expiry_date(billing_details["expiry_date"])
        self.enter_text_in_field("CVC/CVV", billing_details["cvv"])

    def is_purchase_button_present(self):
        logger.info("Is Purchase Button present on this page!")
        try:
            element = self.get_button_locator_by_text("Purchase")
            logger.info(f"Continue Button Count: {element.count()} , Visible: {element.is_visible()}")
            return element.is_visible()
        except Exception as e:
            raise e

    def click_purchase_button(self):
        logger.info("Click Purchase Button!")
        try:
            element = self.get_button_locator_by_text("Purchase")
            logger.info(f"Continue Button Count: {element.count()} , Visible: {element.is_visible()}")
            element.click()
        except Exception as e:
            raise e
