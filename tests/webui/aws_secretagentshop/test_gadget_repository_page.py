import csv
import os

import pytest

from libs.webui.pages.aws_secretagentshop.gadget_repository_page import GadgetRepositoryPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestGadgetRepositoryPage(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()
        cls.expected_categories = [item.strip() for item in "All Products, Accessories, Clothing, Food, Vehicles".split(',')]

    def test_gadget_repository_page(self):
        self.logger.info("Verifying Gadget Repository Page!")
        # Verify Home Page
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        self.home_page.click_explore_button()


        gadget_repository_page = GadgetRepositoryPage(self.app.current_page)
        actual_categories = gadget_repository_page.get_product_categories()

        for actual_category in actual_categories:
            assert actual_category in self.expected_categories, f"Category: {actual_category} is NOT recognized! Known Categories: {self.expected_categories}"
            gadget_repository_page.click_product_category(actual_category)

    @staticmethod
    def _get_static_product_catalog():
        return [
            ("Accessories", "The Forgetter MK-II", "$225"),
            ("Clothing", "Up & Away Parasol", "$125"),
            ("Vehicles", "SkyCycle X-1000", "$9000"),
            ("All Products", "The Morning Teleporter", "$40"),
        ]

    @staticmethod
    def _get_external_product_catalog():
        product_catalog = []
        curr_dir = os.path.dirname(os.path.dirname(__file__))
        csv_file = f"{curr_dir}/../data/product_catalog.csv"
        with open(csv_file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                product_catalog.append((row["category"], row["product_name"], row["price"]))
        return product_catalog

    @pytest.mark.parametrize("category, product_name, price", _get_static_product_catalog())
    def test_static_product_catalog(self, category, product_name, price):
        self._verify_product_catalog(category, product_name, price)

    @pytest.mark.parametrize("category, product_name, price", _get_external_product_catalog())
    def test_external_product_catalog(self, category, product_name, price):
        self._verify_product_catalog(category, product_name, price)

    def _verify_product_catalog(self, category, product_name, price):
        self.logger.info(f"Verifying Product Exist in Catalog! Category: {category} , Product Name: {product_name} , Price: {price}")

        self.home_page.click_briefcase_icon()
        self.home_page.click_explore_button()

        gadget_repository_page = GadgetRepositoryPage(self.app.current_page)

        assert gadget_repository_page.is_product_card_exist_in_category(category, product_name), f"Unable to find Product: {product_name} in Category: {category}"

        product_details = gadget_repository_page.get_product_card_details(product_name)
        assert price in product_details, f"Product's Price NOT matched for Product: {product_name} , Price: {price} in Product Details: {product_details}"

        self.logger.info(f"Verified Category: {category} , Product: {product_name} , Price: {price}")
