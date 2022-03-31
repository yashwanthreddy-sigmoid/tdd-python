import os.path
from unittest.mock import MagicMock
from AreaFinder import *
import pytest


class TestClass:
    @pytest.fixture()
    def area(self):
        area = AreaFinder()
        return area

    @classmethod
    def setup_class(cls):
        print("\n\nAreaFinder class prints area of square\n")

    @classmethod
    def teardown_class(cls):
        print("\n\nEnd of AreaFinder Class\n\n")

    def test_check_if_input_file_exists(self):
        assert os.path.exists("/Users/somalayashwanthreddy/Documents/python/testimg/yash.txt") == 1

    @pytest.mark.parametrize("test_input, expected", [(2, 4), (3, 9), (6, 36), (100, 10000)])
    def test_eval(self, area, test_input, expected):
        assert area.find(test_input) == expected

    def test_exception_with_bad_input(self, area):
        with pytest.raises(Exception):
            area.find(0)
            area.find(-1)

    def test_returns_correct_output(self, area, monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value=100)
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        mock_exists = MagicMock(return_value=True)
        monkeypatch.setattr("os.path.exists", mock_exists)
        result = area.fromfile("/Users/somalayashwanthreddy/Documents/python/testimg/yash.txt")
        mock_open.assert_called_once_with("/Users/somalayashwanthreddy/Documents/python/testimg/yash.txt", "r")
        assert result == 100
