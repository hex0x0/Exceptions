""" 

from pathlib import Path
import os



p = Path(Path.home().joinpath('Desktop/eggs/spam'))

for filename in p.glob('*.txt'):
    #os.unlink(filename)
    #os.rmdir(p)
    #alternatively, we can delete files using send2trash
    #send2trash.send2trash(filename)
    print(filename.name)
    
    
#Walking a directory tree, ou melhor dizendo, caminhando por um diretório

for folderName, SubFolders, filenames in os.walk(p):
    print('The current folder is: ' + folderName)
    
    for dir in SubFolders:
        print(dir)
        
    for file in filenames:
        print(file)
    

with open('arquivo.txt', 'r') as arq:
    for line in arq:
        print(line)

#É similar a fazer

arq = open('arquivo.txt','r')
try:
    for line in arq:
        print(line)
except:
    print('Error')
finally:
    arq.close()
    
    
    


"""

from multiprocessing.sharedctypes import Value


class NossoContextManager:
    def imprime_msg(self, msg):
        print(msg)
    def __enter__(self):
        print('Entrando no nosso bloco with')
        return self

    def __exit__(self, tipo, valor, traceback):
        print(tipo)
        print(valor)
        print(traceback)
        
        
        
with NossoContextManager() as teste:
    teste.imprime_msg('ola mundo')
    raise ValueError