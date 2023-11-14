
contador_item=0
class Item:
    def __init__(self, nombre: str, valor: float) -> None:
        self.__nombre = nombre
        self.__valor = valor
        contador_item += 1
        self.__id = contador_item
        
    def __repr__(self) -> str:
        return f"Item(nombre={self.__nombre}, valor={self.__valor}, id={self.__id})"
