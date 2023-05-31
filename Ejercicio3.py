CANT_VALORES_A_PEDIR = 10

cant_pares = 0
cant_impares = 0
for x in range(CANT_VALORES_A_PEDIR):
    valor = int(input("Ingrese un valor: "))
    if valor % 2 == 0:
        cant_pares += 1
    else:
        cant_impares += 1
print("\n\nCantidad de números pares:", cant_pares)
print("Cantidad de números impares:", cant_impares)