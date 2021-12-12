class commodity:
    def __init__(self, com_code, com_name, com_price, com_stock):
        self.com_code = com_code
        self.com_name = com_name
        self.com_price = com_price
        self.com_stock = com_stock

    def get_commodity(self):
        com_dict = {
            'com_code': self.com_code,
            'com_name': self.com_name,
            'com_price': self.com_price,
            'com_stock': self.com_stock,
        }
        return com_dict