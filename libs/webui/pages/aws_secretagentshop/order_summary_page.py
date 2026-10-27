import logging
import uuid
from playwright.sync_api import Page
from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class OrderSummaryPage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def is_order_id_a_valid_uuid(self):
        logger.info(f"Checking generated Order ID is a valid UUID!")
        order_id = ""
        try:
            locators = self.current_page.locator("div.grid-cols-1").filter(has_text="Order ID").all()
            order_text = locators[1].text_content().strip()
            order_id = order_text.replace("Order ID", "").strip()
            logger.info(f"Extracted Order ID: {order_id}")
            return order_id
        except Exception as e:
            raise e

        try:
            uuid.UUID(str(order_id))
        except ValueError:
            return False

    def get_progress_bar_stage_locator(self):
        return self.current_page.locator("div[aria-hidden=\"true\"]")

    def get_progress_bar_stages(self):
        logger.info("Getting progress bar stages!")
        try:
            stages_text = self.get_progress_bar_stage_locator().text_content().strip()
            logger.info(f"Stages Text: {stages_text}")
            stages = [line.strip() for line in stages_text.splitlines()]
            logger.info(f"Count of Stages: {len(stages)}")
            return stages
        except Exception as e:
            raise e

    def is_progress_bar_stage_highlighted(self, stage):
        logger.info(f"Checking progress bar stage highlighted: {stage}")
        try:
            locators = self.current_page.locator("div.text-primary-500").filter(has_text=stage).all()
            for locator in locators:
                logger.info(f"Stage Highlighted: {locator.text_content().strip()}")
                return True
            return False
        except Exception as e:
            raise e

    def get_order_sub_total(self):
        return self.current_page.locator("span[id=\"order-subtotal\"]").text_content().strip()

    def get_order_shipping(self):
        return self.current_page.locator("span[id=\"order-shipping\"]").text_content().strip()

    def get_order_tax(self):
        return self.current_page.locator("span[id=\"order-tax\"]").text_content().strip()

    def get_order_total(self):
        return self.current_page.locator("span[id=\"order-total\"]").text_content().strip()

    def get_product_details_in_order_summary(self):
        logger.info("Getting product details in order summary!")
        try:
            locators = self.current_page.locator("[alt='Product']").locator("xpath=..").all()
            product_details = {}
            for locator in locators:
                product_text = locator.text_content().strip()
                logger.info(f"Product Text: {product_text}")
                filtered_list = [stripped for line in product_text.splitlines() if (stripped := line.strip())]
                product_name = filtered_list[0]
                quantity = filtered_list[1]
                product_total_price = filtered_list[2]
                price_per_product = filtered_list[3]
                logger.info(f"Order Details Product Name: {product_name} , Quantity : {quantity} , Total Price: {product_total_price} , Price Per Quantity: {price_per_product}")
                product_details[product_name] = filtered_list
            return product_details
        except Exception as e:
            raise e




