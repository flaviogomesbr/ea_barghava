def findSmallest(arr):
    smallest = arr[0] # armazena o menor valor
    smallest_index = 0 # armazena o índice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): # ordenações em um array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # encontra o menor elemento do array e adiciona ao novo array
        newArr.append(arr.pop(smallest))
    return newArr
print(selectionSort([5, 3, 6, 2, 10]))


""" 
# OBS.: O código indicado abaixo está no livro da versão PT, mas dá erro. Precisei refatorar para o inglês para dar certo!

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return NovoArr
print(ordenacaoporSelecao([5, 3, 6, 2, 10]))

"""
























