class Recipe:
    __slots__ = ('id', 'recipe', 'products', 'products_id')

    def __init__(
        self,
        id,
        recipe,
        products,
        products_id
    ):
        self.id = id,
        self.recipe = recipe,
        self.products = products,
        self.products_id = products_id

    @classmethod
    def from_dict(cls, data):
        return Recipe(**data)