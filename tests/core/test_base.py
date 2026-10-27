import logging
import abc

from libs.utils.automation_config import TestConfig

logging.basicConfig(
            level=logging.DEBUG,  # Sets the threshold to INFO (DEBUG logs will be ignored)
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

class TestBase(abc.ABC):
    """ This servers as Base Test for all Tests """

    @classmethod
    def setup_class(cls):
        # Initialize basic configuration
        cls.logger = logging.getLogger(cls.__name__)
        cls.logger.info("Logging initialized successfully!")
        cls.test_config = TestConfig()
        cls.logger.info("Config loaded successfully!")

    def get_prop(self, prop_name):
        return self.test_config.get_prop(prop_name)

    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to setup_class."""
        cls.logger.info("teardown_class")
