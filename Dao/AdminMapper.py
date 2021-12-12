import os
import sqlite3

def login(username, password):
    pro_path = os.path.abspath(os.path.dirname(__file__)).split('shop_info_system')[0]
    connection = sqlite3.connect(pro_path+'\shop_info_system\sqlite\commodity_info.db')
    sql = 'select * from user where username=? and password=?'
    cursor = connection.cursor()
    cursor.execute(sql, (username, password))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(result) == 0:
        return False
    else:
        return True