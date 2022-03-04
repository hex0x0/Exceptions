import os
from pathlib import Path
import os.path


#This will create 
"""

*Delicious
    *Walrus
     *Ucranom   
"""


try:
    os.makedirs('C:\\Delicious\\Wlarus\\Ucranom')

except:
    print('Folders already created')
    
    
finally:
       
    try:
        Path(r'C:\\Users\\Delta\\Desktop\\eggs').mkdir()
        
    except:
        print('Um try dentro de outro try')


#Retorna o mesmo que os.getcwd()

print(Path.cwd().is_absolute())

#Para obter um caminho absoluto a partir de um caminho relativo
print(Path.cwd() / Path('my/path/is/relative'))


print(Path.home() / Path('my/path'))


print(os.path.abspath('C:\\Users'))

print(os.path.abspath('.'))
#scripts é filho de excecoes
print(os.path.abspath('.\\scripts'))
"""
ANCHOR
|
C:\\Users\\Al\text.txt
    ?????????  Stem | suffix
    Parent
    


"""
#Instancia uma classe do tipo Path

pt = Path('C:\\Users\\Delta\\Desktop\\800px-ASCII-Table-wide.svg')

print(pt.anchor)
print(pt.parent)
print(pt.name)


#e assim por diante

#Avalia para os diretórios pais de um objeto Path com indíce inteiro
print(pt.cwd().parents[0])

#Chamando os.path.dirname retornará uma string de tudo que vier antes da barra invertida
#Chamando os.path.basename retornará uma string de tudo que vier depois da barra


print(os.path.dirname(pt))
print(os.path.basename(pt))

#Se você quiser pode guarda os valores de dirname e basename numa tupla


path_tuple = os.path.split(pt)

print(path_tuple)

#Retorna todas as partes de um path como strings
print(path_tuple[0].split(os.sep))


#Retorna o tamanho do arquivo em bytes
print(os.path.getsize('C:\\Reflect_Install.log'))

#Pega o nome dos arquivos e diretórios no meu diretório atual
print(os.listdir())


total_size = 0

for filename in os.listdir('C:\\Windows\\System32'):
    total_size += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
    
print(total_size)



