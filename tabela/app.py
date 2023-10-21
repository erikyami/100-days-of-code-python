import pandas as pd 
#T = [[2, 8, 4, 5], [0,1, 7, 4 ],[1,2,3,4]]

T = [[2,1,3,9,7,3,8],
     [6,0,7,7,7,9,1],
     [4,2,8,3,5,0,6],
     [7,0,1,6,4,4,4],
     [2,2,0,6,1,1,1],
     [1,3,6,5,6,1,99]
     ]
#T = [[1,2],[3,4]]
numeros = []
print(str(len(T)))

def verifica(valor):
    if valor <= 60 and valor > 0:
        if valor < 10:
            #print('0'+str(valor))
            numeros.append('0'+str(valor))
        else:
            #print(valor)
            numeros.append(str(valor))

print('Tabela:')
for r in T:
   for c in r:
      print(c,end = " ")
   print()
        
print('Numeros:')

## num1 e num2 = horizontal
## num3 e num4 = vertical
## num5 e num6 = diagonal baixo
## num7 e num8 = diagonal cima

tamanho_tabela = len(T) - 1
for r in T:
    indice_linha = T.index(r)
    for c in r:
        indice_coluna = r.index(c)
        
        if indice_coluna == len(r)-1 and indice_linha < tamanho_tabela:
            num3 = str(c) + str(T[indice_linha+1][indice_coluna])
            num4 = str(T[indice_linha+1][indice_coluna]) + str(c)
            verifica(int(num3))
            if num3 != num4:
                verifica(int(num4))
        
        if r.index(c) < len(r) - 1:
            num1 = str(c) + str(r[r.index(c)+1])
            num2 = str(r[r.index(c)+1]) + str(c)
            verifica(int(num1))
            if num1 != num2:
                verifica(int(num2))

                
            if indice_linha < tamanho_tabela:
                num3 = str(c) + str(T[indice_linha+1][indice_coluna])
                num4 = str(T[indice_linha+1][indice_coluna]) + str(c)
                num5 = str(c) + str(T[indice_linha+1][indice_coluna+1])
                num6 = str(T[indice_linha+1][indice_coluna+1]) + str(c)
                verifica(int(num3))
                if num3 != num4:
                    verifica(int(num4))
                verifica(int(num5))
                if num5 != num6:
                    verifica(int(num6))    
            if indice_linha > 0:
                num7 = str(c) + str(T[indice_linha-1][indice_coluna+1])
                num8 = str(T[indice_linha-1][indice_coluna+1]) + str(c)
                verifica(int(num7))
                if num7 != num8:
                    verifica(int(num8))
numeros.sort()

count = pd.Series(numeros).value_counts()

print(numeros)
print("Num   Qtd")
print(count)