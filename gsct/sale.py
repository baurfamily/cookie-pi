from datetime import datetime

class Sale:
    def __init__(self):
        self.boxes = []
        self.timestamp = datetime.now()

    def box_count(self):
        return len(self.boxes)

    def total(self):
        return sum(box.cost for box in self.boxes)
    
    def addBox(self, box):
        self.boxes.append(box)