'''=>____<

Bom dia

'''

try:
    lista = []
    
    lista.append(int('lucas'))
    
except(ValueError, IndexError) as excecao:
    excecao
    print('Erro')
except:
    print('Erro desconhecido')
    
finally:
    lista.append(3)
    print(lista)
    
    
#Excecao dentro de excecao

try:
    #DivisionByZeroError
    num = 1/0
    int(num)
    #ValueError
except Exception as E:
    raise ValueError from E

#Encadeia as exceções

 
    
    