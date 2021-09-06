""" Simple logging module to setup the logger
"""
import logging


class Logger(object):
    _loggers = {}

    @classmethod
    def get_logger(cls, name):
        """ Return the named logger or create a new one if it does not exist

        Args:
            name (str): Name of the logger

        Returns:
            logging.Logger: the named logger
        """
        if name in cls._loggers:
            return cls._loggers.get(name)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        log_format = "[%(asctime)s] %(pathname)s:%(lineno)d %(levelname)s: " \
                     "%(message)s"
        formatter = logging.Formatter(log_format, "%m-%d %H:%M:%S")
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        cls._loggers[name] = logger
        return logger
