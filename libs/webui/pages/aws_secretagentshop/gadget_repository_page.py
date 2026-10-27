import logging
from playwright.sync_api import Page
from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class GadgetRepositoryPage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def get_product_categories_locator(self):
        return self.current_page.locator("ul.category-menu li")

    def get_product_categories(self):
        logger.info("Getting product categories!")
        try:
            locator = self.get_product_categories_locator()
            categories = []
            for i in range(locator.count()):
                category = locator.nth(i).text_content().strip()
                #logger.info(f"Product Category: {category}")
                categories.append(category)

            logger.info(f"Count of product categories: {len(categories)}")
            return categories
        except Exception as e:
            raise e

    def click_product_category(self, category):
        logger.info(f"Clicking product category: {category}")
        try:
            locator = self.get_product_categories_locator()
            for i in range(locator.count()):
                curr_category = locator.nth(i).text_content().strip()
                if curr_category == category:
                    locator.nth(i).click()
                    return
            raise Exception(f"Unable to find Product Category: {category}")
        except Exception as e:
            raise e

    def get_pagination_links_locator(self):
        return self.current_page.locator("nav[aria-label=\"Pagination\"] a")

    def click_page_number_link_in_pagination(self, page_number):
        logger.info(f"In Pagination, clicking link with page number: {page_number}")
        try:
            locator = self.get_pagination_links_locator()
            for i in range(locator.count()):
                curr_page_number = locator.nth(i).text_content().strip()
                logger.info(f"Current Page Number: {curr_page_number}")
                if curr_page_number == page_number:
                    locator.nth(i).click()
                    return True
            raise Exception(f"In Pagination, unable to find page number link: {page_number}")
        except Exception as e:
            raise e

    def is_product_card_exist_in_category(self,category, product_name):
        logger.info(f"Checking Product: {product_name} exist in Category: {category}")
        self.click_product_category(category)
        try:
            # Check Product Exist
            next_page_number = 1
            while True:
                if self.is_product_card_exist(product_name):
                    break
                next_page_number += 1

                self.click_page_number_link_in_pagination(f"{next_page_number}")
            logger.info(f"Found Product: {product_name} in Category: {category} in Page: {next_page_number}")
            return True
        except Exception as e:
            return False
