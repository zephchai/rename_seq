""" Test suite for functions in rs_logging.py
"""
import logging

from rename_seq import rs_logging


class TestRsLogging(object):
    """ Test suite for functions in rs_logging
    """
    def test_get_logger(self):
        """ Test get_logger
        """
        logger = rs_logging.Logger.get_logger("panda")
        assert isinstance(logger, logging.Logger)
