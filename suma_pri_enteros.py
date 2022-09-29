# Ejercicio con while No.25: Suma de los primeros números enteros positivos.

#input
N = int(input("Digita hasta que numero entero positivo quieres sumar: "))

#process
i = 1
sum = 0

while i <= N:
    sum = sum + i
    i = i + 1

#output

print("La suma de los primeros números enteros hasta",N,"es:",sum)