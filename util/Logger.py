import logging
import logging.handlers

import os
import time
import util.Util as util

log = logging.getLogger('logger')
log.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')

my_path = util.get_dirpath('logs')
util.make_directory(my_path)

file_handler = logging.handlers.TimedRotatingFileHandler(
    filename = my_path + '/logs', 
    when = 'midnight', 
    interval = 1, 
    encoding = 'utf-8'
)

file_handler.setFormatter(formatter)
log.addHandler(file_handler)