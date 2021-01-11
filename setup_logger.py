import logging
import sys


'''
setup logger
if filename_log is not provide, the logger only output to stdout
logger_name is the name of the logger
default mode_ is overwrite the logger file, possible mode: 'a':append
'''
def setup_logger(logger_name=f'{__file__}', logLevel_=logging.DEBUG, filename_log=None,mode_='w'):
    logger_ = logging.getLogger(logger_name)
    logger_.setLevel(logLevel_)

    if filename_log:
        # Add a file handler
        f_handler = logging.FileHandler(filename=filename_log,mode=mode_)
        f_handler.setLevel(logLevel_) 
        f_formatter = logging.Formatter('%(asctime)s-%(name)s:%(levelname)s:%(message)s')
        f_handler.setFormatter(f_formatter) 
        logger_.addHandler(f_handler)

    # Add a stream handler
    s_handler = logging.StreamHandler(sys.stdout)
    s_handler.setLevel(logLevel_) 
    s_formatter = logging.Formatter('%(asctime)s-%(name)s:%(levelname)s:%(message)s')
    s_handler.setFormatter(s_formatter) 
    logger_.addHandler(s_handler)
    
    assert logger_ is not None
    return logger_
