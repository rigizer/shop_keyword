import os
import json

import db.DBHandler as baseDbHandler
import util.Logger as BaseLogger

from util.DataWithCollectsite import DataWithCollectsite

from taskJob.keywordmaster.Keywordmaster import Keywordmaster
from taskJob.elevenst.ElevenstKeyword import ElevenstKeyword
from taskJob.naverstore.NaverstoreKeyword import NaverstoreKeyword

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

    keywordmaster = Keywordmaster.make(db_handler)

    #elevenstKeyword = ElevenstKeyword.make(db_handler)
    #elevenstDataWithCollectSite = elevenstKeyword.run()
    #keywordmaster.run(elevenstDataWithCollectSite)

    naverstoreKeyword = NaverstoreKeyword.make(db_handler)
    naverstoreDataWithCollectSite = naverstoreKeyword.run()
    keywordmaster.run(naverstoreDataWithCollectSite)

if __name__ == '__main__':
    main()