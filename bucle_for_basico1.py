# bucle_for_basico1.py

# 1. Básico: imprime todos los números enteros del 0 al 100.
print("1. Básico: números del 0 al 100")
for i in range(0, 101):
    print(i)
print("\n")

# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("2. Múltiples de 2 entre 2 y 500")
for i in range(2, 501):
    if i % 2 == 0:
        print(i)
print("\n")

# 3. Contando Vanilla Ice: números del 1 al 100, 
# si divisible por 5 imprime "ice ice", si divisible por 10 imprime "baby"
print("3. Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
print("\n")

# 4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total.
print("4. Suma de números pares del 0 al 500,000")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print(suma)
print("\n")

# 5. Regrésame al 3: imprime números positivos desde 2024 en cuenta regresiva de 3 en 3
print("5. Cuenta regresiva de 3 en 3 desde 2024")
for i in range(2024, 0, -3):
    print(i)
print("\n")

# 6. Contador dinámico: 
# variables numInicial, numFinal, multiplo
# imprime los múltiplos de multiplo entre numInicial y numFinal
print("6. Contador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
