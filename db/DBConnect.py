import pymysql
from sqlalchemy import pool

class DBConnect:
    def __init__(self, db_info):
        self.connect_info = db_info
        self.set_connection_pool()

    def set_connection_pool(self):
        self.mypool = pool.QueuePool(lambda: pymysql.connect(**self.connect_info), pool_size=15, max_overflow=5)

    def get_connect(self):
        return self.mypool.connect()