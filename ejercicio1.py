numero_inicial = int(input("Introduce un número inicial: "))
numero_final = int(input("Introduce número final: "))
numeros_impares = []

while numero_inicial >= numero_final:
    print("Numero final tiene que ser mayor al número inicial")
    numero_inicial = int(input("Introduce un número inicial: "))
    numero_final = int(input("Introduce número final: "))

for impares in range(numero_inicial, numero_final+1):
    if(impares % 2 != 0):
        print(impares)

