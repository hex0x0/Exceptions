"""
    try:
    pass

except:
    pass

finally:
    pass
    
    
"""

try:
    
    file = open('algumacoisa.txt', 'r')
    
    line = file.readline()
    
    line.split('!')
    
    line = line[0]
    
    file.close()
    
    file = open('algumacoisa.txt', 'a')
    
    file.write(line)

except:
    print('Deu erro!!!')
    #Indica o tipo de erro ocasionado por exemplo
    #FileNotFoundError
    
    file = open('algumacoisa.txt', 'w')
    
    file.write('Erro!!!')
    
    
finally:
    file.close()    
      
    