from ..entities.pedido import Pedido
from ..repositories.pedido_repository import PedidoRepository

class CriarPedidoUseCase:
    def __init__(self, repositorio: PedidoRepository):
        self.repositorio = repositorio
    
    def executar(self, id_pedido: int, nome_item: str):
        novo_pedido = Pedido(id=id_pedido, item=nome_item)
        self.repositorio.salvar(novo_pedido)
        return f"Sucesso! {nome_item} (ID: {id_pedido}) foi registrado!"
