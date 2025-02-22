import unittest
from unittest.mock import patch
import pytest
from function_mocking_python.main_2 import enough_files

@pytest.fixture(scope="session", autouse=True)
def get_number_of_files_fixture() -> None:
  with patch("function_mocking_python.main_2.get_number_of_files", lambda s: 3):
    yield


class TestFunctions(unittest.TestCase):
  def test_enough_files(self):
    self.assertEqual(enough_files("some_storage_path", 7), False)
