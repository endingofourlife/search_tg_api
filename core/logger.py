import logging


class LoggerConfig:
    """
    A base class to configure and provide a reusable logger.
    """
    @staticmethod
    def get_logger(name="app", level=logging.INFO):
        """
        Configures and returns a logger instance.
        :param name: Name of the logger.
        :param level: Logging level.
        :return: Configured logger instance.
        """
        logger = logging.getLogger(name)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(level)
        return logger
