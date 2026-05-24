import sys
import src.logger as logger

def log_exception(error, error_details):
    if isinstance(error_details, tuple) and len(error_details) == 3:
        _, _, exc_tb = error_details
    else:
        _, _, exc_tb = sys.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = '<unknown>'
        line_number = 0

    error_message = (
        f"Error occurred in file: {file_name} at line: {line_number} "
        f"with error message: {str(error)}"
    )
    logger.logging.error(error_message)
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_details):
        super().__init__(error)
        self.error_message = log_exception(error, error_details)

    def __str__(self):
        return self.error_message
