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

# Lista dada
lista = [4, 3, 2, 10, 12, 1, 5]
ordenada, operaciones_10 = insertion_sort(lista)
print(f'Lista ordenada: {ordenada}')
print(f'Número de operaciones para que el 10 alcance su posición: {operaciones_10}')
print(f'Posición final del 10: {ordenada.index(10)}')
