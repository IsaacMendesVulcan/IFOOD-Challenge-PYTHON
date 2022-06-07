lista = [['O minero', [4.2, 1.7]],
         ['Amor aos pedaços', [4.3, 1.2]],
         ['We Coffe', [4.5, 0.8]],
         ['Lamen Kazu', [4.8, 0.7]],
         ['Brigaderia', [4.7, 1.2]],
         ['Mr. Pretzels', [4.7, 1.1]]]

def avaliacao(elem):
    return elem[1][0]

def distancia(elem):
    return elem[1][1]

lista.sort(key=distancia)

lista.sort(key=avaliacao, reverse= True)

print( "\n\n\n•|ENTREGAR EM: Próximo de Bela Vista|•  \n\n\n")

rank = 0
for restaurante in lista:
    rank = rank + 1
    temp = 0
    for item in restaurante:
        temp = temp + 1
        if temp == 1:
            print(f'-------  RANK: {rank}° -------\n')
            print(f'Nome: {item}')
        else:
            temp = 0
            for numero in item:
                temp = temp + 1
                if temp == 1:
                    print(f'Avaliação: {numero}')
                else:
                    print(f'Distância: {numero}\n')
