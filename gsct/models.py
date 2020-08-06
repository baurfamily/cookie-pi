from datetime import datetime

class Box:

    def __init__(self, cost, flavor):
        self.cost = cost
        self.flavor = flavor
        

class Sale:
    def __init__(self):
        self.boxes = []
        self.timestamp = datetime.now()

    def box_count(self):
        return len(self.boxes)

    def total(self):
        return sum(box.cost for box in self.boxes)
    
    def add_box(self, box):
        self.boxes.append(box)

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

    def add_sale(self, sale):
        self.sales.append(sale)


