# funciones_intermedias_1.py

# 1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431


# 2. Función para iterar lista de diccionarios
def iterarDiccionario(lista):
    for dic in lista:
        salida = []
        for llave, valor in dic.items():
            salida.append(f"{llave} - {valor}")
        print(", ".join(salida))


# 3. Función para imprimir valores de una llave específica
def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])


# 4. Función para imprimir información de diccionario con listas
def imprimirInformacion(diccionario):
    for llave, valores in diccionario.items():
        print(f"{len(valores)} {llave.upper()}")
        for valor in valores:
            print(valor)
        print()


# Ejemplo de uso
if __name__ == "__main__":
    print("Matriz actualizada:", matriz)
    print("Cantantes actualizados:", cantantes)
    print("Ciudades actualizadas:", ciudades)
    print("Coordenadas actualizadas:", coordenadas)

    cantantes_extra = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"},
        {"nombre": "José José", "pais": "México"},
        {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
    ]

    print("\nIterar Diccionario:")
    iterarDiccionario(cantantes_extra)

    print("\nIterar Diccionario 2 - Nombres:")
    iterarDiccionario2("nombre", cantantes_extra)

    print("\nIterar Diccionario 2 - Países:")
    iterarDiccionario2("pais", cantantes_extra)

    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }

    print("\nImprimir Información Costa Rica:")
    imprimirInformacion(costa_rica)
