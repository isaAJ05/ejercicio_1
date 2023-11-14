from __future__ import annotations
class Item:
    contador_item=0
    def __init__(self, nombre: str, valor: float) -> None:
        self.__nombre = nombre
        self.__valor = valor
        Item.contador_item += 1
        self.__id = Item.contador_item
        
    def get_nombre(self) -> str:
        return self.__nombre
    def get_valor(self) -> float:
        return self.__valor
