from libs.webui.pages.aws_secretagentshop.home_page import HomePage
from libs.webui.pages.aws_secretagentshop.shopping_cart_review_page import ShoppingCartReviewPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestShoppingCardReviewPage(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_shopping_cart_review_page(self):
        self.logger.info("Verifying Home Page!")
        # Verify Header & Footer
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        # Add Product to Cart
        product_name = "Aqua Ace GT"
        self.home_page.add_product_to_loadout(product_name)

        shopping_card_review_page = ShoppingCartReviewPage(self.app.current_page)
        self.verify_shopping_cart_review_page(shopping_card_review_page)

        # Verify ShoppingCartReview Page
        assert shopping_card_review_page.is_remove_icon_present_for_product(product_name), f"Remove Icon NOT present for Product: {product_name}"
        assert shopping_card_review_page.get_count_of_products_in_cart() == 1, "The count of items in the card didn't match!"
        assert shopping_card_review_page.get_shopping_cart_size() == "1", "Shopping Cart size didn't match!"

        # Remove the Product from the Cart
        product_removed_from_cart = shopping_card_review_page.remove_product_from_cart(product_name)
        assert product_removed_from_cart, f"Remove Product from Cart Failed! Product Name: {product_name}"
        assert shopping_card_review_page.get_basket_text() == "You don't have any items!", "Basket message didn't match!"
        assert shopping_card_review_page.get_shopping_cart_size() == "0", "Shopping Cart size didn't match!"

        # Move back to Home Page
        shopping_card_review_page.click_briefcase_icon()

        # Add the Product Again & Verify
        self.home_page = HomePage(self.app.current_page)
        self.home_page.add_product_to_loadout(product_name)
        shopping_card_review_page = ShoppingCartReviewPage(self.app.current_page)
        self.verify_shopping_cart_review_page(shopping_card_review_page)
        assert shopping_card_review_page.get_shopping_cart_size() == "1", "Shopping Cart size didn't match!"
