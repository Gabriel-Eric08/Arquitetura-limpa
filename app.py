from infra.persistence.memoria_repository import MemoriaPedidoRepository
from core.use_cases.criar_pedido import CriarPedidoUseCase

repo = MemoriaPedidoRepository()

service = CriarPedidoUseCase(repo)

print(service.executar(55,"pizza"))