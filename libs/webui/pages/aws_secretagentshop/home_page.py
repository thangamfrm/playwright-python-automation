import logging

from playwright.sync_api import Page

from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class HomePage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def get_explore_button_locator(self):
        return self.current_page.locator("a[id='shop-now']")

    def click_explore_button(self):
        logger.info("Clicking explore button")
        try:
            self.get_explore_button_locator().click()
        except Exception as e:
            raise e

    def is_explore_button_displayed(self):
        logger.info("Checking explore button displayed")
        try:
            explore_button_locator = self.get_explore_button_locator()
            logger.info(f"Explore Button Count: {explore_button_locator.count()} , Visible: {explore_button_locator.is_visible()}")
            return explore_button_locator.count() == 1 and explore_button_locator.is_visible()
        except Exception as e:
            raise e

    def get_reason_to_choose_us(self):
        logger.info("Getting Reason to Choose Us!")
        try:
            reason_texts = []
            locator = self.current_page.locator(f"div.grid-cols-1:has-text('Covert Shipping') > *")
            for i in range(locator.count()):
                child_element = locator.nth(i)
                reason_texts.append(child_element.text_content().strip())
            logger.info(f"Reason Texts: {reason_texts}")
            return reason_texts
        except Exception as e:
            raise e


