from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestSecretAgentShopHomePage(TestSecretAgentShopBase):
    
    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_home_page(self):
        self.logger.info("Verifying Home Page!")
        # Verify Home Page
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        assert self.home_page.is_explore_button_displayed(), "Explore Button NOT found!"

        # Verify Links are Present
        link_text = "View Gadget Repository"
        assert self.home_page.does_link_exist(link_text), f"Link: {link_text} NOT Found!"
        link_text = "Explore"
        assert self.home_page.does_link_exist(link_text), f"Link: {link_text} NOT Found!"

        # Verify Section Title are Present
        assert self.home_page.does_header_exist("Mission Critical Gear"), "Header: 'Mission Critical Gear' NOT Found!"

        # Verify Products are displayed!
        product_name = "Aqua Ace GT"
        assert self.home_page.is_product_displayed(product_name), f"Product Name: {product_name} NOT found / visible!"
        product_name = "Audio-Illusion Spinner"
        assert self.home_page.is_product_displayed(product_name), f"Product Name: {product_name} NOT found / visible!"
        product_name = "Facechanger Formal Wear"
        assert self.home_page.is_product_displayed(product_name), f"Product Name: {product_name} NOT found / visible!"

        appTitle = "The most public Secret Shop"
        assert self.home_page.does_header_exist(appTitle), "App Title: {appTitle} NOT found!"

        sub_section_title = "Why Choose Us"
        assert self.home_page.does_header_exist(sub_section_title), "Sub Section Title: {sub_section_title} NOT found!"

        reason_texts = self.home_page.get_reason_to_choose_us()
        assert len(reason_texts) == 3, "Incorrect number of reasons to choose us!"
        reason = "Covert Shipping"
        assert reason_texts[0].startswith(reason), f"Reason to choose us: {reason} NOT found!"
        reason = "Mission Guarantee"
        assert reason_texts[1].startswith(reason), f"Reason to choose us: {reason} NOT found!"
        reason = "Support"
        assert reason_texts[2].startswith(reason), f"Reason to choose us: {reason} NOT found!"

        self.logger.info("Verified Home Page!")

    # def get_current_page(self):
    #     return self.home_page

    @classmethod
    def teardown_class(cls):
        super().teardown_class()
