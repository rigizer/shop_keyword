import os
import json

import db.DBHandler as baseDbHandler
import util.Logger as BaseLogger

from taskJob.elevenst.ElevenstKeyword import ElevenstKeyword

logger = BaseLogger.log

def get_db_info():
    db_info = None
    path = os.path.dirname(os.path.abspath(__file__))

    try:
        with open(path + '/db/db_info.json', encoding='UTF-8') as json_file:
            db_info_json = json.load(json_file)
            db_info = db_info_json.get('db_info')

    except AttributeError as attributeError:
        logger.error('[GET_DB_INFO] AttributeError: '.format(attributeError))

    except FileNotFoundError as fileNotFounderror:
        logger.error('[GET_DB_INFO] FileNotFoundError: '.format(fileNotFounderror))

    return db_info

def make_db_handler(db_info):
    return baseDbHandler.DBHandler(db_info)

def main():
    db_info = get_db_info()
    db_handler = make_db_handler(db_info)

    c = ElevenstKeyword.make(db_handler)
    c.run()

if __name__ == '__main__':
    main()