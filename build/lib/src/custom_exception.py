import sys
import logging
import src.logger as logger

def log_exception(error, error_details:sys.exc_info()):
    _, _, exc_tb = error_details
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file: {file_name} at line: {line_number} with error message: {str(error)}"
    logger.logging.error(error_message)
