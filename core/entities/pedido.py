from dataclasses import dataclass

@dataclass
class Pedido:
    id: int
    item: str
    status: str = "Pendente"
    