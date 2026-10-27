from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestPageFooterLinks(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_page_footer_links(self):
        self.logger.info("Verifying Page Footer links!")
        # Verify Home Page
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        section_title = "Quick Links"
        links_under_section = self.home_page.get_links_under_section_in_page_footer(section_title)
        links_under_section[0].click()
        assert self.home_page.is_gadget_repository_link_displayed(), f"Invalid first link: {links_under_section[0].text_content().strip()} under 'Quick Links'"