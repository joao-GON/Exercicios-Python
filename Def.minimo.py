## encontrar minimo 

lista =[2,10,3,1,4,5]

def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo): 
            minimo = elem
    return minimo

print(encontrar_minimo(lista)) 