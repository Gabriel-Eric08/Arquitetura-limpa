from core.entities.pedido import Pedido
from core.repositories.pedido_repository import PedidoRepository

class MemoriaPedidoRepository(PedidoRepository):
    def __init__(self):
        self.dados = {}
    
    def salvar(self, pedido: Pedido):
        self.dados[pedido.id] = pedido
        print("[Log infra] Persiste em mémoria: {pedido}")