import logging
import sys


class Logger(object):
    r"""A class that creates a logger using the package logging_functions with the levels INFO, DEBUG and ERROR and which outputs
    any returned messages on the system's standard output. The format of the logger is as follows\:
        %(asctime)s - %(name)s - %(levelname)s - %(message)s
    """
    def __init__(self, name: str):
        """
        Initialises the logger using the name value that was passed.
        Args:
            name: The name you want to set as your logger's output name.
        """
        self.logger = self._set_logger(name)

    @staticmethod
    def _set_logger(name: str) -> logging.getLogger:
        """
        Initialize logger_tool with appropriate Level and Formatting
        Args:
            name: The name that the logger will report as. Used in the logger's formated output.
        Returns:
            The constructed logger.
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
