from typing import TypeVar, Generic, Type
from controls.tda.linked.linkedList import Linked_List
import json
import os

T = TypeVar("T")
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/data/"

    def _list(self) -> T:
        if os.path.isfile(self.URL + self.file):
            f = open(self.URL + self.file, "r")
            datos = json.load(f)
            self.lista.clear
            for data in datos:
                print(type(data))
                a = self.atype.deserializar(data)
                self.lista.add(a, self.lista._lenght)
            f.close()
        return self.lista
    
    def __transform__(self):
        aux = "["
        for i in range(0, self.lista._lenght):
            if i < self.lista._lenght - 1:
                aux += str(json.dumps(self.lista.get(i).serializable)) + ","
            else:
                aux += str(json.dumps(self.lista.get(i).serializable))
        aux += "]"
        return aux
    
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._lenght):
            aux.append(self.lista.get(i).serializable)
        return aux
    
    def _save(self, data: T) -> T:
        self._list()
        self.lista.add(data, self.lista._lenght)
        a = open(self.URL + self.file, "w")
        a.write(self.__transform__())
        a.close()
        
        
    def _merge(self, data: T, pos) -> T:
        print("Guardando")
        self._list()
        self.lista.edit(data, pos)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self.__transform__())
        f.close()
      
    def _delete(self, pos) -> T:
        self._list()
        self.lista.delete(pos)
        with open(self.URL + self.file, "w") as a:
            a.write(self.__transform__())