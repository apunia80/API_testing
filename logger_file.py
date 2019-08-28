import logging
import constant
logger=logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatt=logging.Formatter(constant.logger_format)
file_handler=logging.FileHandler(constant.loggerpath)
file_handler.setFormatter(formatt)
logger.addHandler(file_handler)