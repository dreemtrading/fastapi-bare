import logging
logging.basicConfig(level=logging.INFO, filename='dreemlogs.log', filemode='a+',
                    format="%(asctime)s - %(levelname)s - %(message)s")


class Log:
    def warn(message: str, extra: dict = None):
        message += f' - extra info - {extra}'
        logging.warning(message)

    def error(message: str, extra: dict = None):
        message += f' - extra info - {extra}'
        logging.error(message)

    def debug(message: str, extra: dict = None):
        message += f' - extra info - {extra}'
        logging.debug(message)

    def info(message: str, extra: dict = None):
        message += f' - extra info - {extra}'
        logging.info(message)
