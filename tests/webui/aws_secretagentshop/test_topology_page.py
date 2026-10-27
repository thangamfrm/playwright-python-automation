from libs.webui.pages.aws_secretagentshop.topology_page import TopologyPage
from tests.webui.aws_secretagentshop.test_base import TestSecretAgentShopBase


class TestTopologyPage(TestSecretAgentShopBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = cls.app.get_home_page()

    def test_topology_page(self):
        self.logger.info("Verifying Topology Page!")

        # Verify Header & Footer
        self.verify_page_header(self.home_page)
        self.verify_page_footer(self.home_page)

        self.home_page.click_link_under_section_in_page_footer("Tools", "Topology")
        topology_page = TopologyPage(self.app.current_page)

        section_title = topology_page.get_section_title()
        self.logger.info(f"Topology Page - Section Title: {section_title}")
        assert section_title, "Application Services" "Topology Page Section Title didn't match!"

        expected_services = [item.strip() for item in "Catalog, Carts, Checkout, Recommendations, Orders".split(",")]
        service_details = topology_page.get_app_service_details()
        for service in expected_services:
            self.logger.info(f"Verifying Service: {service}")
            assert service in service_details, f"Service: {service} NOT found!"

        assert service_details["Catalog"][1], "HEALTHY" "Catalog Service Status is NOT HEALTHY!"
        assert service_details["Carts"][1], "HEALTHY" "Carts Service Status is NOT HEALTHY!"
        assert service_details["Checkout"][1], "HEALTHY" "Checkout Service Status is NOT HEALTHY!"
        assert service_details["Recommendations"][1], "NONE" "Recommendations Service Status is NOT NONE!"
        assert service_details["Orders"][1], "HEALTHY" "Orders Service Status is NOT HEALTHY!"

        self.logger.info("Verify Topology Page Complete!")
