import os
import sqlite3
from entry.commodity import commodity

def inquire(com_code):
    pro_path = os.path.abspath(os.path.dirname(__file__)).split('shop_info_system')[0]
    connection = sqlite3.connect(pro_path+'\shop_info_system\sqlite\commodity_info.db')
    sql = """select * from commodity where com_code=?"""
    cursor = connection.cursor()
    cursor.execute(sql,(com_code,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(result) == 0:
        return False
    else:
        com = commodity(result[0][0], result[0][1], result[0][2], result[0][3])
        return com

def modify(com_code, com_name, com_price, com_stock):
    pro_path = os.path.abspath(os.path.dirname(__file__)).split('shop_info_system')[0]
    connection = sqlite3.connect(pro_path + '\shop_info_system\sqlite\commodity_info.db')

    sql = """update commodity set com_name = ? , com_price = ? , com_stock = ? where com_code = ?"""
    cursor = connection.cursor()
    cursor.execute(sql, (com_name, com_price, com_stock, com_code,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(result) == 0:
        return True
    else:
        return False



def add(com_code, com_name, com_price, com_stock):
    pro_path = os.path.abspath(os.path.dirname(__file__)).split('shop_info_system')[0]
    connection = sqlite3.connect(pro_path + '\shop_info_system\sqlite\commodity_info.db')

    sql = """insert into commodity(com_code, com_name, com_price, com_stock) values (?,?,?,?)"""
    cursor = connection.cursor()
    cursor.execute(sql, (com_code, com_name, com_price, com_stock,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(result) == 0:
        return True
    else:
        return False


def adds_com(list_com):
    result = []
    list_com = list_com
    for com in list_com:
        com_code = com['com_code'][0]
        com_name = com['com_name'][0]
        com_price = com['com_price'][0]
        com_stock = com['com_stock'][0]
        resu = add(com_code, com_name, com_price, com_stock)
        result.append(resu)
    return result

def info_com():
    pro_path = os.path.abspath(os.path.dirname(__file__)).split('shop_info_system')[0]
    connection = sqlite3.connect(pro_path + '\shop_info_system\sqlite\commodity_info.db')

    sql = """select * from commodity"""
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    com_list = []
    for result in results:
        com_li = commodity(result[0], result[1], result[2], result[3])
        com_list.append(com_li)
    return com_list

def delete(com_code):
    pro_path = os.path.abspath(os.path.dirname(__file__)).split('shop_info_system')[0]
    connection = sqlite3.connect(pro_path + '\shop_info_system\sqlite\commodity_info.db')
    sql = """delete from commodity where com_code=?"""
    cursor = connection.cursor()
    cursor.execute(sql, (com_code,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    if len(result) == 0:
        return True
    else:
        return False