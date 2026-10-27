import logging

import playwright
from playwright.sync_api import sync_playwright
from libs.utils.automation_config import TestConfig

logger = logging.getLogger(__name__)

class PlaywrightAutomation():

    def __init__(self):
        logger.info("Initializing Browser!")
        self.test_config = TestConfig()
        browser_headless_mode = self.test_config.get_prop_as_boolean("browser_headless_mode")
        logger.info(f"Browser Headless Mode: {browser_headless_mode}")
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=bool(browser_headless_mode))
        self.current_page = self.browser.new_page()
        self.current_page.goto(self.test_config.get_prop("aws_secretagentshop_url"))
        logger.info("Initialized Browser!")

    def get_current_page(self):
        return self.current_page

    def close_browser(self):
        logger.info("Closing Browser!")
        self.browser.close()
        self.playwright.stop()
        logger.info("Closed the Browser!")