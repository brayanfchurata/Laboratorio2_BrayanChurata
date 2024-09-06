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

# Lista dada
lista = [5, 2, 9, 1, 5, 6]
ordenada, iteraciones = bubble_sort(lista)
print(f'Lista ordenada: {ordenada}')
print(f'Número de iteraciones: {iteraciones}')
