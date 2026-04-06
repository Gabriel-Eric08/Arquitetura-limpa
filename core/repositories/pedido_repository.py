from abc import abstractmethod, ABC
from ..entities.pedido import Pedido

class PedidoRepository(ABC):
    @abstractmethod
    def salvar(pedido: Pedido)->None:
        pass