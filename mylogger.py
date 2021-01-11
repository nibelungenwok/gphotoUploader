import logging
import sys
import time
'''
logging.basicConfig(filename=f'{__file__}.log',filemode='a', format='%(asctime)s-%(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('test')
'''

"""
setup logger
"""
#ToDo create logger to file and stdout
logger = logging.getLogger(f'test')
logger.setLevel(logging.DEBUG)
# Add a file handler
f_handler = logging.FileHandler(f'{__file__}.log')
f_handler.setLevel(logging.DEBUG) 
f_formatter = logging.Formatter('%(asctime)s-%(name)s:%(levelname)s:%(message)s')
f_handler.setFormatter(f_formatter) 
logger.addHandler(f_handler)

'''
# Add a stream handler
s_handler = logging.StreamHandler(sys.stdout)
s_handler.setLevel(logging.DEBUG) 
s_formatter = logging.Formatter('%(asctime)s-%(name)s:%(levelname)s:%(message)s')
s_handler.setFormatter(s_formatter) 
logger.addHandler(s_handler)

'''
logger.debug('done setup logger')
time.sleep(10)
