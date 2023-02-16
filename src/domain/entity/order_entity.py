class OrderEntity:

    id : int = 0
    date : str = None
    status : str = None
    total : float = None
    items : list = []

    def __init__(self, id, date, status, total):
        self.validate(id, date, status, total)

        self.id = id
        self.date = date
        self.status = status
        self.total = total
    
    def validate(self, id, date, status, total):
        if id == None:
            raise ValueError("Order id does not match")
        
        if date == None:
            raise ValueError("Order date does not match")
        
        if status == None:
            raise ValueError("Order status does not match")

        if total == None:
            raise ValueError("Order total does not match")
    
    def create(self) -> bool:
        return True
    
    def delete(self) -> bool:
        return True

