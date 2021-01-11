import datetime
import time
import logging
import sys
from demo_mediaItems import upload_image, upload_images
import yield_files
# step 1: Upload byte data to Google Server
# image_dir can be change by user
#image_dir = os.path.join(os.getcwd(),'test')
#image_dir = '/home/pi/projects/python_dev/scrapy/scrapy-tutorial-starter'
#image_dir = "/media/pi/62 GB Volume/taipowerScreenshots/2020/09" not working
image_dir = "/media/pi/FABB-1992/taipowerScreenshots/2020/09"

#image_dir = '/home/pi/projects/python_dev/google_api/test'
#ToDo: try-except block embrace getting the local_image_files?
print('get all files to be uploaded')
local_image_files = yield_files.yield_matched_files_to_be_upload(image_dir, 'png')
assert local_image_files != []
'''
for f in local_image_files:
    pass
'''
print(image_dir)

"""
setup logger
"""
#ToDo create logger to file and stdout
logger = logging.getLogger(f'{__file__}')

# Add a file handler
f_handler = logging.FileHandler(filename=f'{__file__}.log',mode='w')
f_handler.setLevel(logging.DEBUG) 
f_formatter = logging.Formatter('%(asctime)s-%(name)s:%(levelname)s:%(message)s')
f_handler.setFormatter(f_formatter) 
logger.addHandler(f_handler)

# Add a stream handler
s_handler = logging.StreamHandler(sys.stdout)
s_handler.setLevel(logging.DEBUG) 
s_formatter = logging.Formatter('%(asctime)s-%(name)s:%(levelname)s:%(message)s')
s_handler.setFormatter(s_formatter) 
logger.addHandler(s_handler)

logger.debug('done setup logger')

'''
ToDo parse the name of the image to be uploaded, cause we want to put images into monthly album
for example: 2020_10_xxTyy_ii_zzscreanshot.png all goes to album 2020_10
'''


logger.debug('start upload')     
for batch_files in yield_files.yield_every_n_minus_one_path(local_image_files, 50):
    assert len(batch_files) < 50
    print('got 49 files')
    response = upload_images(batch_files)
    '''
    ToDo: test if upload successful by inspect the response

    '''
    time.sleep(60)
    print('in main')
    print(response)
    #time.sleep(10)
# encounter error if 
