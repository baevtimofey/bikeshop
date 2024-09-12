import dataclasses


@dataclasses.dataclass
class Product:
    id: int
    title: str
    price: int
    description: str
    category_id: int
