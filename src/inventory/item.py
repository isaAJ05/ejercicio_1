
class Item:
    contador_item=0
    def __init__(self, nombre: str, valor: float) -> None:
        self.__nombre = nombre
        self.__valor = valor
        Item.contador_item += 1
        self.__id = Item.contador_item
        
    def __repr__(self) -> str:
        return f"Item(nombre={self.__nombre}, valor={self.__valor}, id={self.__id})"
    def get_nombre(self) -> str:
        return self.__nombre
