import os
import errno
import time

curr_dir = os.path.dirname(os.path.abspath(__file__)) + '/../logs'

def make_directory(directory):
    try:
        if not (os.path.isdir(directory)):
            os.makedirs(os.path.join(directory))

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

        pass

def get_dirpath(param):
    year = time.strftime('%Y', time.localtime(time.time()))
    month = time.strftime('%m', time.localtime(time.time()))
    day = time.strftime('%d', time.localtime(time.time()))
    dirpath = curr_dir + '/' + param + '/' + year + '/' + month + '/' + day + '/'
    return dirpath