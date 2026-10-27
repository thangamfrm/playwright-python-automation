from abc import ABC, abstractmethod
from tests.core.test_base import TestBase


class TestBaseWebUI(TestBase):

    @classmethod
    def setup_class(cls):
        super().setup_class()

    @classmethod
    def teardown_class(cls):
        super().teardown_class()
