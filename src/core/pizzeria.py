from __future__ import annotations
from typing import List
from inventory.pedido import Pedido
from person.cliente import Cliente
from inventory.item import Item


class Pizzeria:
    def __init__(self, nombre: str)-> None:
        self.__nombre = nombre
        self.__clientes: List[Cliente] = []
        self.__items: List[Item] = []
        self.__pedidos: List[Pedido] = []
    
    def __repr__(self):
       return f"Pizzeria({self.__nombre})"

    def add_cliente(self, cliente: "Cliente") -> bool:
        self.__clientes.append(cliente)
        return True
    
    def add_item(self, item: "Item") -> bool:
        self.__items.append(item)
        return True
    
    def add_pedido(self, pedido: "Pedido") -> bool:
        self.__pedidos.append(pedido)
        return True
    
    def get_cliente(self, index: int) -> "Cliente":
        return self.__clientes[index]

    def get_item(self, index: int) -> "Item":
        return self.__items[index]
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_items(self) -> List["Item"]:
        return self.__items
    
    
    
    def calc_prod_mas_vendido_cliente(self, num_cliente: int):

        items_in_pizzeria = [item.get_nombre() for item in self.__items]
        cliente = self.get_cliente(num_cliente)
        freq_items = cliente.frecuencia_items(items_in_pizzeria)

        # Imprimimos el número del cliente
        print(f"num_cliente = {self.__clientes.index(cliente)}")

        # Imprimimos la frecuencia con la que un producto fue adquirido
        for nombre, freq in freq_items.items():
            print(f'El producto {nombre} se vendió {freq}')

        ningun_item_comprado = sum(freq_items.values()) <= 0
        if ningun_item_comprado:
            return -1

        item_mas_comprado = max(freq_items, key=freq_items.get)
        for item in self.__items:
            if item.get_nombre() == item_mas_comprado:
                return self.__items.index(item)