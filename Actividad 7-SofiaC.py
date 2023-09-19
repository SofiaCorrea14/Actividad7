

from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def igualdad (self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre): 
        self.elementos = [] 
        self.nombre = nombre  
        Conjunto.contador += 1
        self.__id = Conjunto.contador
 

    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto: 'Conjunto'):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto: 'Conjunto'):
        resultado = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado
    
    @classmethod
    def intersectar(cls, conjunto1, conjunto2): 
        elementos_comunes = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre_resultado)
        resultado.elementos = elementos_comunes
        return resultado

    def __str__(self): 

        elementos_str = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"

#Ejemplo

conjunto_A = Conjunto("A")
conjunto_B = Conjunto("B")

elemento_x = Elemento("X")
elemento_y = Elemento("Y")
elemento_z = Elemento("Z")

# Intersección de los conjuntos A y B
interseccion = Conjunto.intersectar(conjunto_A, conjunto_B)
print("Intersección:", interseccion)

# Agregar elementos a los conjuntos
conjunto_A.agregar_elemento(elemento_x)
conjunto_A.agregar_elemento(elemento_y)
conjunto_B.agregar_elemento(elemento_z)

# Unión de los conjuntos A y B
union = conjunto_A + conjunto_B
print("Unión:", union)


