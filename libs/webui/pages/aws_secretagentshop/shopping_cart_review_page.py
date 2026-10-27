import logging
from playwright.sync_api import Page
from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class ShoppingCartReviewPage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def is_shopping_card_review_page(self):
        return self.is_checkout_button_exist()

    def get_count_of_products_in_cart(self):
        logger.info("Getting Count of Products in the Cart!")
        try:
            h2_elements = self.current_page.locator("h2.item-name").all()
            logger.info(f"H2 Element Count: {len(h2_elements)}")
            return len(h2_elements)
        except Exception as e:
            raise e

    def _get_cart_locator_for_product(self, product_name):
        return self.current_page.locator(".cart-item", has_text=product_name)

    def _get_remove_icon_locator_for_product(self, product_name):
        cart_item = self._get_cart_locator_for_product(product_name)
        return cart_item.locator("button[aria-label=\"Remove item\"]")

    def get_cart_text_for_product(self, product_name):
        logger.info(f"Get cart text for product: {product_name}")
        try:
            return self._get_cart_locator_for_product(product_name)
        except Exception as e:
            raise e

    def is_remove_icon_present_for_product(self, product_name):
        logger.info(f"Checking remove icon present for product: {product_name}")
        try:
            locator = self._get_remove_icon_locator_for_product(product_name)
            return locator.is_visible()
        except Exception as e:
            raise e

    def remove_product_from_cart(self, product_name):
        logger.info(f"Remove product: {product_name} from cart!")
        try:
            locator = self._get_remove_icon_locator_for_product(product_name)
            locator.click()
            return True
        except Exception as e:
            raise e

    def get_basket_text(self):
        logger.info("Get basket text!")
        try:
            return self.current_page.locator("div[id=\"basket\"]").text_content().strip()
        except Exception as e:
            raise e

    def _get_checkout_locator(self):
        return self.current_page.locator("button[id=\"checkout\"]")

    def is_checkout_button_present(self):
        logger.info("Checking is checkout button present")
        try:
            checkout_button_present = self._get_checkout_locator().is_visible()
            logger.info(f"is Checkout Button Present: {checkout_button_present}")
            return checkout_button_present
        except Exception as e:
            raise e

    def get_checkout_button_text(self):
        logger.info("Getting checkout button text")
        try:
            button_text = self._get_checkout_locator().text_content().strip()
            logger.info("Get checkoutButton text: {button_text}")
            return button_text
        except Exception as e:
            raise e

    def click_checkout(self):
        logger.info("Click checkout")
        try:
            locator = self._get_checkout_locator()
            locator.click()
            return True
        except Exception as e:
            raise e

    def get_cart_sub_total(self):
        logger.info("Get Cart Sub Total!")
        try:
            locator = self.current_page.locator("p.cart-subtotal")
            sub_total = locator.text_content().strip()
            logger.info(f"Cart Sub Total: {sub_total}")
            return sub_total
        except Exception as e:
            raise e
