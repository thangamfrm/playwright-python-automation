import logging
from playwright.sync_api import Page
from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class ShippingMethodPage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.shipping_methods = {"Priority Mail": "priority-mail", "Priority Mail Express": "priority-mail-express"}

    def is_shipping_method_page(self):
        return self.does_header_exist("Covert Delivery")

    def get_shipping_method_locator(self):
        return self.current_page.locator("input[name=\"token\"]")

    def get_shipping_methods(self):
        logger.info("Getting shipping methods!")
        try:
            locators = self.get_shipping_method_locator().all()
            actual_shipping_methods = []
            for locator in locators:
                shipping_methods_reverse = {v: k for k, v in self.shipping_methods.items()}
                shipping_method = shipping_methods_reverse[locator.get_attribute("value")]
                actual_shipping_methods.append(shipping_method)
                logger.info(f"Shipping Method: {shipping_method}")
            return actual_shipping_methods
        except Exception as e:
            raise e

    def is_shipping_method_selected(self, shipping_method):
        logger.info(f"Checking is shipping method selected: {shipping_method}")
        try:
            locators = self.get_shipping_method_locator().all()
            shipping_method_code = self.shipping_methods[shipping_method]
            is_selected = False
            for locator in locators:
                if locator.get_attribute("value") == shipping_method_code:
                    is_selected = locator.is_checked()
                    logger.info(f"Shipping Method: {shipping_method} , Selected: {is_selected}")
                    break
            return is_selected
        except Exception as e:
            raise e

    def select_shipping_method(self, shipping_method):
        logger.info(f"Set shipping method: {shipping_method}")
        try:
            shipping_method_locators = self.current_page.locator("label.flex").all()
            shipping_method_selected = False
            for locator in shipping_method_locators:
                if shipping_method in locator.text_content().strip():
                    locator.click()
                    logger.info(f"Selected Shipping Method: {shipping_method}")
                    shipping_method_selected = True
                    break
            return shipping_method_selected
        except Exception as e:
            raise e