from __future__ import annotations
from inventory.pedido import Pedido
from cliente import Cliente
from inventory.item import Item
from typing import List


class Pizzeria:
    def __init__(self, nombre: str)-> None:
        self.__nombre = nombre
        self.__clientes= List["Cliente"] = []
        self.__items= List["Item"] = []
        self.__pedidos= List["Pedido"] = []
    
    def __repr__(self):
       return f"Pizzeria({self.__nombre})"


    def add_item(self, item: "Item") -> bool:
        if item not in self.__items:
            self.__items.append(item)
            return True
        return False
    
    def add_cliente(self, cliente: "Cliente") -> bool:
        if cliente not in self.__clientes:
            self.__clientes.append(cliente)
            return True
        return False
    
    def add_pedido(self, pedido: "Pedido") -> bool:
        if pedido not in self.__pedidos:
            self.__pedidos.append(pedido)
            return True
        return False
    
    def get_cliente(index: int) -> "Cliente":
        return self.__clientes[index]
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_item(index: int) -> "Item":
        return self.__items[index]
    
    def get_items(self) -> List["Item"]:
        return self.__items
    
    
    
    def calc_prod_mas_vendido_cliente(self, num_cliente: int) -> int:
        if num_cliente < len(self.__clientes):
            cliente_pedidos = self.__pedidos[num_cliente]
            cantidades = {}
            for pedido in cliente_pedidos:
                for item in pedido:
                    if item not in cantidades:
                        cantidades[item] = 1
                    else:
                        cantidades[item] += 1
            if cantidades:
                prod_mas_vendido = max(cantidades, key=cantidades.get)
                return prod_mas_vendido
        return -1
