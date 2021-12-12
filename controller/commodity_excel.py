import pandas as pd
from entry.commodity import commodity
class com_excel:
    def __init__(self, path):
        self.filepath = path
        self.result = None
        self.dow_com()

    def dow_com(self):
        com = commodity('请删除本行','商品编号不允许重复','1','1')
        dict_com = com.get_commodity()
        list_com = [dict_com]
        com_code = []
        com_name = []
        com_price = []
        com_stock = []

        for li_com in list_com:
            com_code.append(li_com['com_code'])
            com_name.append(li_com['com_name'])
            com_price.append(li_com['com_price'])
            com_stock.append(li_com['com_stock'])
        testData = [com_code, com_name, com_price, com_stock]
        name = '/商品批量导入模板.xlsx'
        filepath = self.filepath + name
        self.result = self.pd_toexcel(testData, filepath)

    def pd_toexcel(self, data, filename):  # pandas库储存数据到excel

        dfData = {
            '商品编码': data[0],
            '商品名称': data[1],
            '商品价格': data[2],
            '商品库存': data[3],
        }
        df = pd.DataFrame(dfData)  # 创建DataFrame
        df.to_excel(filename, index=False)
        if len(df) != 0:
            return True
        else:
            return False