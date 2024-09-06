def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar el índice del mínimo elemento en la sublista arr[i:n]
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el elemento mínimo con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Imprimir la lista después de cada iteración
        print(f'Lista después de la iteración {i + 1}: {arr}')
    return arr

# Lista dada
lista = [64, 25, 12, 22, 11]
ordenada = selection_sort(lista)
print(f'\nLista final ordenada: {ordenada}')
