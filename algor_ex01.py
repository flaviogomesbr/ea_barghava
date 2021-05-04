def binary_search(list, item):
    # baixo e alto acompanham a parte da lista que estamos procurando
    low = 0
    high = len(list)-1
    # enquanto ainda não conseguiu chegar a um único elemento...
    while low <= high:
        # verifica o elemento central
        mid = (low + high) // 2
        guess = list[mid]
        # acha o item
        if guess == item:
            return mid
        # se o chute for muito alto (> item), subtrair 1
        if guess > item:
            high = mid - 1
        # ou se o chute for muito baixo, somar 1
        else:
            low = mid + 1
    # se não encontrar, é porque não existe
    return None
# vamos testar em uma lista que nós mesmos criamos
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => imprime 1, pois estamos procurando o número 3 da lista, logo, encontramos no índice 1 (arrays começam no índice 0)
print(binary_search(my_list, -1)) # => imprime None, pois não existe o número -1 indicado em nenhum índice de my_list


