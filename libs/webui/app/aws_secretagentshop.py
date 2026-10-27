from libs.webui.core.playwright_automation import PlaywrightAutomation
from libs.webui.pages.aws_secretagentshop.home_page import HomePage


class SecretAgentShop(PlaywrightAutomation):

    def __init__(self):
        super().__init__()
        aut_url = self.test_config.get_prop("aws_secretagentshop_url")
        self.current_page.goto(aut_url)
        self.home_page = HomePage(self.get_current_page())

    def get_home_page(self):
        return self.home_page