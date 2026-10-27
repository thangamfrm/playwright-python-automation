import logging
from playwright.sync_api import Page
from libs.webui.pages.aws_secretagentshop.base_page import SecretAgentShopBasePage

logger = logging.getLogger(__name__)

class TopologyPage(SecretAgentShopBasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def get_section_title(self):
        logger.info("Getting Section Title!")
        return self.get_current_page().locator("div", has=self.current_page.locator("i.fa-cubes")).text_content().strip()

    def _get_app_service_locators(self):
        return self.current_page.locator("div.rounded-lg").all()

    def get_app_service_details(self):
        logger.info("Getting App Service Details")
        service_details = {}
        try:
            locators = self._get_app_service_locators()
            for locator in locators:
                filtered_list = [stripped for line in locator.text_content().strip().splitlines() if (stripped := line.strip())]
                service_name = filtered_list[0]
                logger.info(f"Service Name: {service_name} , Status: {filtered_list[1]}")
                service_details[service_name] = filtered_list
            return service_details
        except Exception as e:
            raise e