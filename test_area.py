import os.path
import pytest
from area import area
from unittest.mock import MagicMock

class Testclass:
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
        assert Area.areaofsquare(test_input) == expected


    def test_exception_with_bad_input(self, Area):
        with pytest.raises(Exception):
            Area.areaofsquare(0)
            Area.areaofsquare(-1)

