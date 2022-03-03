class LevantaExcecao(Exception):
    def __str__(self):
        return 'Número já foi digitado!'

try:
    v = int(input())
    
    if 1 <= v <= 20:
        raise ValueError

except ValueError:
    print('A exceção foi levantada')
    
def main():
    lista = []
    
    
    for i in range(3):
        while True:
            try:
                num = int(input()) 
                break
            except ValueError:
                print('Digite só numeros')
        
        
              
        if num not in lista:
            lista.append(num)
        else:
            raise LevantaExcecao
            
            
            

if __name__ == '__main__':
    main()
    