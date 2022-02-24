import os.path
import pytest
from AreaFinder import AreaFinder
from unittest.mock import MagicMock

class AreaFinderTest:
    @pytest.fixture()
    def Area(self):
        Area = area()
        return Area

    @classmethod
    def setup_class(cls):
        print("\n\narea class prints area of square\n")

    @classmethod
    def teardown_class(cls):
        print("\n\nEnd of area Class\n\n")



    def test_check_if_input_file_exists(self):
        assert os.path.exists("/Users/somalayashwanthreddy/Documents/python/yash.txt") == 1


    @pytest.mark.parametrize("test_input, expected", [(2, 4), (3, 9), (6, 36), (10,100)])
    def test_eval(self, Area, test_input, expected):
        assert Area.find(test_input) == expected


    def test_exception_with_bad_input(self, Area):
        with pytest.raises(Exception):
            Area.find(0)
            Area.find(-1)
            
     

    def test_returns_correct_output(self, Area, monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value=100)
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        mock_exists = MagicMock(return_value =True)
        monkeypatch.setattr("os.path.exists", mock_exists)
        result = Area.fromfile("/Users/somalayashwanthreddy/Documents/python/yash.txt")
        mock_open.assert_called_once_with("/Users/somalayashwanthreddy/Documents/python/yash.txt", "r")
        assert result == 100


