
from typing import List
from pedido import Pedido

class Cliente:
    def __init__(self, nombre: str)-> None:
        self.__nombre = nombre
        self.__pedidos = List["Pedido"] = []
    
    def __repr__(self) -> str:
        return f"Cliente(nombre={self.__nombre}, pedidos={self.__pedidos})" 

    def add_pedido(self, pedido: Pedido) -> bool:
        if pedido not in self.__pedidos:
            self.__pedidos.append(pedido)
            pedido.set_cliente(self)
            return True
        return False

    def get_nombre(self) -> str:
        return self.__nombre

    def get_pedidos(self) -> List[Pedido]:
        return self.__pedidos
