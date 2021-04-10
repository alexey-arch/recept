class Products:
    __slots__ = ('id', 'products', 'quantity', 'weight')

    def __init__(
        self,
        id,
        products,
        quantity,
        weight
    ):
        self.id = id,
        self.products = products,
        self.quantity = quantity
        self.weight = weight

    @classmethod
    def from_dict(cls, data):
        return Products(**data)
