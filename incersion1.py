def insertion_sort(arr):
    n = len(arr)
    operations_for_10 = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Contar operaciones para el número 10
        if key == 10:
            while j >= 0 and arr[j] > key:
                operations_for_10 += 1
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    
    # Devuelve la lista ordenada y las operaciones para el número 10
    return arr, operations_for_10

# Función de inserción se mantiene igual

# Pruebas con otras listas
listas = [
    [9, 7, 6, 3, 2, 1],   # Totalmente desordenada
    [1, 3, 5, 7, 6, 2],   # Parcialmente ordenada
    [5, 4, 4, 2, 2, 10],  # Elementos repetidos
    [1],                  # Un solo elemento
    [3, 3, 3, 3, 3]       # Todos los elementos iguales
]

for idx, lista in enumerate(listas):
    ordenada, operaciones_10 = insertion_sort(lista)
    print(f'\nPrueba {idx + 1}:')
    print(f'Lista original: {lista}')
    print(f'Lista ordenada: {ordenada}')
    if 10 in lista:
        print(f'Número de operaciones para que el 10 alcance su posición: {operaciones_10}')
        print(f'Posición final del 10: {ordenada.index(10)}')
