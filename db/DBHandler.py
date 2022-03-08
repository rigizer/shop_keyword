import os
import json
import pymysql

import db.DBConnect as DBConnect
import util.Logger as BaseLogger

logger = BaseLogger.log

class DBHandler():
    def __init__(self, db_info):
        path = os.path.dirname(os.path.abspath(__file__))

        try:
            with open(path + "/query.json") as json_file:
                self.query = json.load(json_file)

            self.connector = DBConnect.DBConnect(db_info)

        except AttributeError as attribute_error:
            logger.error('[DBHANDLER_INIT] AttributeError: {}'.format(attribute_error))

        except FileNotFoundError as file_not_found_error:
            logger.error('[DBHANDLER_INIT] FileNotFoundError: '.format(file_not_found_error))

    def insert_mws_keyword(self, param):
        conn = None

        try:
            conn = self.get_connect()

            self.execute_query(conn, self.query.get('INSERT_MWS_KEYWORD'), param)
            conn.commit()

        except Exception as e:
            logger.error('[INSERT_MWS_KEYWORD] Exception: {}'.format(e))
            pass

        finally:
            if conn != None:
                conn.close()
    
    def insert_mws_keyword_rate(self, param):
        conn = None

        try:
            conn = self.get_connect()

            self.execute_query(conn, self.query.get('INSERT_MWS_KEYWORD_RATE'), param)
            conn.commit()

        except Exception as e:
            logger.error('[INSERT_MWS_KEYWORD_RATE] Exception: {}'.format(e))
            pass

        finally:
            if conn != None:
                conn.close()

    def insert_mws_service_log(self, param):
        conn = None

        try:
            conn = self.get_connect()

            self.execute_query(conn, self.query.get('INSERT_MWS_SERVICE_LOG'), param)
            conn.commit()

        except Exception as e:
            logger.error('[INSERT_MWS_SERVICE_LOG] Exception: {}'.format(e))
            pass

        finally:
            if conn != None:
                conn.close()

    def execute_query(self, conn, query, param):
        cur = None

        try:
            cur = self.get_cursor(conn)
            cur.execute(query, param)
            rows = cur.fetchall()

            return rows

        except Exception as e:
            logger.error('[EXECUTE_QUERY] Exception: {}'.format(e))
            pass

        finally:
            if cur != None:
                cur.close()

    def get_connect(self):
        return self.connector.get_connect()

    def get_cursor(self, conn):
        return conn.cursor(pymysql.cursors.DictCursor)