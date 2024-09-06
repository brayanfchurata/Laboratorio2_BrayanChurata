def bubble_sort(arr):
    n = len(arr)
    iterations = 0  # Contador de iteraciones
    for i in range(n):
        swapped = False  # Para detectar el mejor caso
        for j in range(0, n-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # Si no hubo intercambio, el arreglo ya está ordenado (mejor caso)
            break
    return arr, iterations

# Pruebas con otras listas
listas = [
    [10, 8, 7, 3, 2, 1],  # Peor caso
    [1, 3, 2, 4, 6, 5],   # Parcialmente ordenada
    [4, 4, 2, 2, 9, 1],   # Elementos repetidos
    [1],                  # Un solo elemento
    [5, 5, 5, 5, 5]       # Todos los elementos iguales
]

for idx, lista in enumerate(listas):
    ordenada, iteraciones = bubble_sort(lista)
    print(f'\nPrueba {idx + 1}:')
    print(f'Lista original: {lista}')
    print(f'Lista ordenada: {ordenada}')
    print(f'Número de iteraciones: {iteraciones}')
