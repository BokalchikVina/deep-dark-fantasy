import sqlite3

import pymysql

class BotDB:

    def __init__(self, db_file):
        #Соеденение с БД
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exist(self, user_id):
        result = self.cursor.execute("SELECT 'id' FROM 'Users' WHERE 'user id' = ?", (user_id,))
        return bool(len(result.fetchall()))

    def