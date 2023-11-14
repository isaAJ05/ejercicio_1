from __future__ import annotations
from cliente import Cliente
from abc import ABC

class Pedido(ABC):
    def __init__(self, cliente:"Cliente" , items,**kwargs: Any)-> None:
        super().__init__(**kwargs)
        self._cliente = cliente
        self._items = items

    def __repr__(self):
        return f'{self.__class__.__name__}({self.cliente!r}, {self.items!r})'
    

class PedidoOnLine(Pedido):
    def __init__(self, email: str,**kwargs: Any)-> None:
        super().__init__(**kwargs)
        self.__email = email

    
class PedidoTelefono(Pedido):
    def __init__(self, telefono: str, **kwargs: Any)-> None:
        super().__init__(**kwargs)
        self.__telefono = telefono

    
