import logging

from playwright.sync_api import Page

logger = logging.getLogger(__name__)

class BasePage():

    def __init__(self, page: Page):
        logger.info("Base Page!")
        self.current_page = page

    def get_current_page(self):
        return self.current_page

    def get_page_title(self):
        return self.current_page.title().strip()

    def click_link(self, link_text):
        self.current_page.get_by_text(link_text)

    def does_link_exist(self, link_text):
        logger.info(f"Checking link exist with text: {link_text}")
        try:
            link = self.current_page.get_by_role("link", name=link_text)
            return link.count() == 1
        except Exception as e:
            logger.error(f"Error occurred while checking link: {link_text} , Msg: {e}")
            return False

    def does_header_exist(self, header_text):
        logger.info(f"Checking header exist with text: {header_text}")
        try:
            heading = self.current_page.get_by_role("heading", name=header_text)
            return heading.count() == 1
        except Exception as e:
            logger.error(f"Error occurred while checking heading: {header_text} , Msg: {e}")
            return False

    def enter_text_in_field(self, label, text):
        logger.info(f"In Field: {label} , entering text: {text}")
        try:
            self.current_page.get_by_label(label, exact=True).fill(text)
        except Exception as e:
            logger.error(f"Error occurred while entering field in label: {label} with Text: {text} , Msg: {e}")
            raise e

    def get_button_locator_by_label(self, button_text):
        return self.current_page.get_by_role("button", name=button_text)

    def enter_text_in_field_using_name_attr(self, field_name_attr, text):
        logger.info(f"In Field with name attribute: {field_name_attr} , Entering text: {text}")
        try:
            self.current_page.locator(f"input[name='{field_name_attr}']").fill(text)
        except Exception as e:
            logger.error(f"Error occurred while entering text in field with name attribute: {field_name_attr} . Text: {text} , Msg: {e}")
            raise e
