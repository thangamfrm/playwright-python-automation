import configparser
import logging
import os
import os.path

logger = logging.getLogger(__name__)

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # This triggers __new__ and __init__ only once
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class TestConfig(metaclass=SingletonMeta):
    """ Class used to configure Test Automation. Test Classes use this class to get properties """
    config_file = 'testautomation.cfg'
    environment_config_file = '{0}_environment.cfg'
    overrides_environment_config_file = '{0}_overrides.cfg'
    overrides_config_file = 'overrides.cfg'

    default_header = 'settings'
    default_test_environment = 'dev'

    def __init__(self):

        logger.info("Starting TestConfig")
        self.config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        curr_dir = os.path.dirname(os.path.dirname(__file__))
        config_dir = "{}/../config".format(curr_dir)
        logger.info(f"Config Dir: {config_dir}")
        test_env = self._get_curr_env()
        logger.info(f"Test Environment: {test_env}")
        self.config.read([
            f"{config_dir}/{TestConfig.config_file}",
            f"{config_dir}/{TestConfig.environment_config_file.format(test_env)}",
            f"{config_dir}/{TestConfig.overrides_environment_config_file.format(test_env)}",
            f"{config_dir}/{TestConfig.overrides_config_file}"
        ])
        self.config[TestConfig.default_header]['environment'] = test_env
        logger.info("Complete TestConfig")

    def _get_curr_env(self):
        test_env = os.getenv("TEST_ENVIRONMENT")
        if test_env:
            return test_env
        else:
            return TestConfig.default_test_environment

    def get_prop(self, prop_name):
        return (self.config[TestConfig.default_header][prop_name]).strip()

    def get_prop_as_boolean(self, prop_name):
        prop_value = (self.config[TestConfig.default_header][prop_name]).strip().lower()
        if prop_value == "true":
            return True
        else:
            return False
