from dataclasses import dataclass

@dataclass
class Product:
    link: str
    old_price: int
    new_price: int
    description: str
