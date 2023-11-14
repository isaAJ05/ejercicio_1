from __future__ import annotations
from typing import List
#from inventory.pedido import Pedido

class Cliente:
    def __init__(self, nombre: str)-> None:
        self.__nombre = nombre
        self.__pedidos : List["Pedido"] = []
    
    def __repr__(self) -> str:
        return f"Cliente(nombre={self.__nombre}, pedidos={self.__pedidos})" 

    def add_pedido(self, pedido: "Pedido") -> bool:
        self.__pedidos.append(pedido)
        return True

    def get_nombre(self) -> str:
        return self.__nombre

    def get_pedidos(self) -> List["Pedido"]:
        return self.__pedidos
    
    def frecuencia_items(self, items: List["Item"]) -> dict:
        # En este diccionario se va a guardar qué tanto aparece un producto
        freq = self.__create_freq_dict(items)

        for pedido in self.__pedidos:
            # Acá verificamos que el pedido es de PedidoOnLine
            if pedido.__class__.__name__ == 'PedidoOnLine':
                for item in pedido.get_items():
                    freq[item.get_nombre()] += 1
        return freq

    def __create_freq_dict(self, items: List["Items"]) -> dict:
        item_dict = {}
        for item in items:
            item_dict[item] = 0  # Creamos una key para cada item
        return item_dict


