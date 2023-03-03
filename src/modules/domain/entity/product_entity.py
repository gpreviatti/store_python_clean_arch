class ProductEntity:

    id: int = None
    name: str = None
    description: str = None
    price: float = None
    quantity: int = None


    def __init__(self, id, name, description, price, quantity):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity