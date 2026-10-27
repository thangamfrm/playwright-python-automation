import logging

from playwright.sync_api import Page
from libs.webui.core.base_page import BasePage

logger = logging.getLogger(__name__)

class SecretAgentShopBasePage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_briefcase_icon_locator(self):
        return self.current_page.locator("i.fa-briefcase")

    def is_briefcase_icon_displayed(self):
        logger.info("Checking briefcase icon displayed")
        try:
            briefcase_element = self.get_briefcase_icon_locator()
            logger.info(f"Briefcase Icon Count: {briefcase_element.count()} , Visible: {briefcase_element.is_visible()}")
            return briefcase_element.count() == 1 and briefcase_element.first.is_visible()
        except Exception as e:
            logger.error(f"Error occurred while checking briefcase icon displayed! Msg: {e}")
            raise e

    def click_briefcase_icon(self):
        self.get_briefcase_icon_locator().click()

    def is_home_link_displayed(self):
        logger.info("Checking Home Link displayed in page header")
        try:
            locator = self.current_page.locator("a[id='menu-home']")
            return locator.count() == 1 and locator.is_visible()
        except Exception as e:
            raise e

    def is_gadget_repository_link_displayed(self):
        logger.info("Checking Gadget Repository Link displayed in page header")
        try:
            locator = self.current_page.locator("a[id='menu-home']")
            return locator.count() == 1 and locator.is_visible()
        except Exception as e:
            raise e

    def get_shopping_cart_locator(self):
        return self.current_page.locator("a[id='go-cart']")

    def is_shopping_cart_displayed(self):
        logger.info("Checking Shopping Cart Icon displayed in page header")
        try:
            locator = self.get_shopping_cart_locator()
            return locator.count() == 1 and locator.is_visible()
        except Exception as e:
            raise e

    def click_shopping_cart(self):
        logger.info("Clicking Shopping Cart Icon in page header")
        try:
            self.get_shopping_cart_locator().click()
        except Exception as e:
            raise e

    def get_shopping_cart_size(self):
        return self.get_shopping_cart_locator().text_content().strip()

    def is_product_displayed(self, product_name):
        logger.info(f"Checking Product exist with name: {product_name}")
        try:
            product_element = self.current_page.locator(".product-name").filter(has_text=product_name)
            logger.info(f"Product Count: {product_element.count()} , Visible: {product_element.is_visible()}")
            return product_element.count() == 1 and product_element.is_visible()
        except Exception as e:
            raise e

    def get_product_card_locator(self, product_name):
        return self.current_page.locator(".product-card").filter(has_text=product_name)

    def is_product_card_exist(self, product_name):
        logger.info(f"Checking Product Card Exist: {product_name}")
        try:
            product_card = self.get_product_card_locator(product_name)
            logger.info(f"Product Card Count: {product_card.count()} , Visible: {product_card.is_visible()}")
            return product_card.count() and product_card.is_visible()
        except Exception as e:
            raise e

    def get_product_card_details(self, product_name):
        logger.info(f"Getting Product Card Details: {product_name}")
        try:
            product_card = self.get_product_card_locator(product_name)
            logger.info(f"Product Card: {product_card.text_content().strip()}")
            return product_card.text_content().strip()
        except Exception as e:
            raise e

    def add_product_to_loadout(self, product_name):
        logger.info(f"Add the Product name: {product_name} to Loadout")
        try:
            product_card = self.get_product_card_locator(product_name)
            logger.info(f"Product Card Count: {product_card.count()} , Visible: {product_card.is_visible()}")
            product_card.locator("button", has_text="Add to Loadout").click()
        except Exception as e:
            raise e

    def is_checkout_button_exist(self):
        logger.info("Checking Checkout Button present on this page!")
        try:
            element = self.current_page.locator("#checkout")
            logger.info(f"Checkout Button Count: {element.count()} , Visible: {element.is_visible()}")
            return element.count() == 1 and element.is_visible()
        except Exception as e:
            raise e

    def get_button_locator_by_text(self, text):
        return self.current_page.locator("#checkout-submit", has_text=text)

    def get_continue_button_locator(self):
        return self.get_button_locator_by_text("Continue")

    def click_continue_button(self):
        logger.info("Click Continue Button on this page!")
        try:
            element = self.get_continue_button_locator()
            logger.info(f"Continue Button Count: {element.count()} , Visible: {element.is_visible()}")
            element.click()
        except Exception as e:
            raise e

    def is_continue_button_exist(self):
        logger.info("Checking Continue Button present on this page!")
        try:
            element = self.get_continue_button_locator()
            logger.info(f"Continue Button Count: {element.count()} , Visible: {element.is_visible()}")
            return element.count() == 1 and element.is_visible()
        except Exception as e:
            raise e

    def get_breadcrumb_trail_step_locators(self):
        return self.current_page.locator("div.step-item").all()

    def get_breadcrumb_trail_step_texts(self):
        logger.info("Get BreadcrumbTrail Step Texts")
        breadcrumb_trail_step_locators = self.get_breadcrumb_trail_step_locators()
        step_texts = []
        for locator in breadcrumb_trail_step_locators:
            step_text = locator.text_content().strip()
            logger.info(f"Breadcrumb Trail Step Text: {step_text}")
            step_texts.append(step_text)
        logger.info(f"Count of Breadcrumb Trail Step Texts: {len(step_texts)}")
        return step_texts

    def is_breadcrumb_step_highlighted(self, step):
        logger.info(f"Checking BreadcrumbTrail Step Highlighted! Step: {step}")
        try:
            locators = self.current_page.locator("div.text-primary-500").all()
            for locator in locators:
                if locator.text_content().strip() == step:
                    return True
            logger.info(f"BreadcrumbTrail Step: {step} NOT Highlighted!")
            return False
        except Exception as e:
            raise e

    def get_back_to_cart_button_locator(self):
        return self.current_page.locator(f"xpath=//button[normalize-space()='Back to Cart']")

    def is_back_to_cart_button_present(self):
        logger.info("Checking Back to Cart Button present!")
        try:
            return self.get_back_to_cart_button_locator().is_visible()
        except Exception as e:
            raise e

    def click_back_to_cart_button(self):
        logger.info("Clicking Back to Cart Button!")
        self.get_back_to_cart_button_locator().click()

    def get_warning_message_locator(self):
        return self.current_page.locator("div[role='alert']")

    def is_warning_message_displayed(self):
        logger.info("Checking warning message displayed!")
        warning_msg_locators = self.get_warning_message_locator()
        return warning_msg_locators.count() == 1 and warning_msg_locators.first.is_visible()

    def get_warning_message(self):
        logger.info("Getting warning message!")
        try:
            warning_text = self.get_warning_message_locator().text_content().strip()
            clean_list = [line.strip() for line in warning_text.splitlines() if line.strip()]
            clean_list = [x for x in clean_list if x]
            return f"{clean_list[0]} {clean_list[1]} {clean_list[2]}"
        except Exception as e:
            raise e

    def get_links_under_section_in_page_footer(self, section_title):
        return self.current_page.locator(f"//h3[contains(text(), '{section_title}')]/..//a").all()

    def get_link_texts_under_section_in_page_footer(self, section_title):
        logger.info(f"Getting list of link texts under section: {section_title} in page footer!")
        link_texts = []
        try:
            locators = self.get_links_under_section_in_page_footer(section_title)
            for locator in locators:
                link_text = locator.text_content().strip()
                link_texts.append(link_text)
            logger.info(f"Link texts: {link_texts} under section: {section_title}")
            return link_texts
        except Exception as e:
            raise e

    def click_link_under_section_in_page_footer(self, section_title, link_text):
        logger.info(f"Clicking link: {link_text} , under section: {section_title} in page footer!")
        try:
            locators = self.get_links_under_section_in_page_footer(section_title)
            for locator in locators:
                if locator.text_content().strip() == link_text:
                    locator.click()
                    logger.info(f"Clicked Link: {link_text} under section: {section_title}")
                    return
            raise f"Unable to find link: {link_text} , under section: {section_title}"
        except Exception as e:
            raise e

    def get_contact_methods_in_page_footer(self):
        logger.info("Getting list of contact methods in page footer!")
        contact_methods = []
        locators = self.current_page.locator(f"//h3[contains(text(), 'Contact')]/..//li").all()
        for locator in locators:
            contact_methods.append(locator.text_content().strip())
        logger.info(f"Contact Methods: {contact_methods}")
        return contact_methods
