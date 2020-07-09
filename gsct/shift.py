from datetime import datetime

class Shift:
    def __init__(self):
        self.start_time = datetime.now()
        self.finish_time = None 
        self.sales = []
    
    def sale_count(self):
        return len(self.sales)
    
    def box_count(self):
        return sum(sale.box_count() for sale in self.sales)

    def total_cost(self):
        return sum(sale.total() for sale in self.sales)

    def addSale(self, sale):
        self.sales.append(sale)