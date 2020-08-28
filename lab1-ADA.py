import random
num = random.randint(1, 25)
intento = 0
print("PROBLEMA #1")
#print(num) print para revisar cual era el numero al momento de probar el codigo
while intento < 3:
    try:
        guess = int(input("Ingresa un numero entre el 1 y el 25: "))
        if guess >= 26:
            print("SOLO VALORES ENTRE 1 Y 25 BRO, INTENTA DE NUEVO")
        elif guess > num:
            print(f"El numero es menor a {guess}")
            intento = intento + 1
            print("Intentos restantes: ", 3 - intento)
        elif guess < num:
            print(f"el numero es mayor a {guess}")
            intento = intento + 1
            print("Intentos restantes: ", 3 - intento)
        elif guess == num: 
            print("Numero correcto!!")
            break       
    except ValueError:
        print("Solo se aceptan valores numericos dentro del rango, por favor ingresa un numero")
        intento = intento + 1
print(f"El numero era: {num}")

print("----------------------------------------------------------------")

print("PROBLEMA #2")
arr = []
for x in range(0, 5):
    col = []
    for y in range(0,3):
        num = int(input("Ingrese un numero entero: "))
        col.append(num)
    arr.append(col)


for col in arr:
    print(*col)

su=[sum(i) for i in arr]
print(f"la suma de cada fila, respectivamente, es: {su}")