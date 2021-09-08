""" Test suite for functions in utils.py
"""
from rename_seq import utils as rs_utils


class TestRenameSeqUtils(object):
    """ Test suite for functions in rename_seq utils
    """
    def setup_method(self, method):
        self.input = ["img.11.jpg", "img.27.jpg", "img.3.jpg", "img.05.jpg"]

    def test_get_rename_map_empty(self):
        """ Test get_rename_map with empty list
        """
        result = rs_utils.get_rename_map([])
        assert len(result) == 0

    def test_get_rename_map(self):
        """ Test get_rename_map function
        """
        expected = [("img.3.jpg", "img.1.jpg"),
                    ("img.05.jpg", "img.2.jpg"),
                    ("img.11.jpg", "img.3.jpg"),
                    ("img.27.jpg", "img.4.jpg")]

        result = rs_utils.get_rename_map(self.input)
        assert result == expected

    def test_get_rename_map_with_start_number(self):
        """ Test get_rename_map function with start argument
        """
        expected = [("img.3.jpg", "img.1001.jpg"),
                    ("img.05.jpg", "img.1002.jpg"),
                    ("img.11.jpg", "img.1003.jpg"),
                    ("img.27.jpg", "img.1004.jpg")]

        result = rs_utils.get_rename_map(self.input, start=1001)
        assert result == expected

    def test_get_rename_map_with_padding(self):
        """ Test get_rename_map function with padding argument
        """
        expected = [("img.3.jpg", "img.0001.jpg"),
                    ("img.05.jpg", "img.0002.jpg"),
                    ("img.11.jpg", "img.0003.jpg"),
                    ("img.27.jpg", "img.0004.jpg")]

        result = rs_utils.get_rename_map(self.input, padding=4)
        assert result == expected

    def test_group_source_files(self):
        """ Test group_source_files
        """
        self.input = ["img.11.jpg", "img.b.11.png", "img.27.jpg", "img.32.jpg"]
        expected = {"imgjpg": ["img.11.jpg", "img.27.jpg", "img.32.jpg"],
                    "img.bpng": ["img.b.11.png"]}

        result = rs_utils.group_files_in_seq(self.input)
        assert result == expected
