from operator import index
from pathlib import Path
from shlex import shlex
import random
pt = Path('C:\\Users\\Delta\\Desktop')


"""

Objetos Path tem um método glob() para listar os conteúdos de um diretório de acordo
com um padrão 'glob'

Padrões globs são formas simplificadas de expressões regulares


O objeto glob retorna um objeto do tipo Generator



"""

lista = list(pt.glob('*'))

print(lista[0])


#Voce pode querer fazer uma pesquisa dos arquivos que .txt, por exemplo 


lista = list(pt.glob('*.txt'))

#Ou qualquer caracter com um marcador especial ?

lista = list(pt.glob('project?.docx'))

# project2.docx
#project4.docx
#

#p.exists() _ verifica se um path existe

#p.is_file() _ verifica se um path existe e se é um arquivo

#p_is_directory() _ verifica se path existe e se é um diretório


import shelve

shelfFile = shelve.open('mydata')

cats = ['zophie', 'pooka', 'simon']

shelfFile['cats'] = cats

shelfFile.close()


shelfFile = shelve.open('mydata')

print(shelfFile['cats'])

import pprint

cats = [{'name':'zophie', 'desc':'chubby'}, {'name':'mike', 'desc':'skinny'}]

pprint.pformat(cats)

fileObj=open('mycats.py', 'w')

fileObj.write('cats = ' + pprint.pformat(cats)  + '\n')

fileObj.close()

#import mycats

#print(mycats.cats)


capitals = {
    'brasil':'brasilia', 'argentina':'buenos aires', 'china':'pequim', 'canada':'otawa',
     'colombia':'bogota', 'peru':'lima', 'japao':'tokyo','tailandia':'bangkok', 'india':'delhi'}

states = list(capitals.keys())
#print(states)
for i in range(len(capitals)):
    correctAnswer = capitals[states[i]]
    wrong_answers = list(capitals.values())
    
    del states[wrong_answers.index(correctAnswer)]
    
    wrong_answers = random.sample(wrong_answers, 3)
    
    
    
    answer_options = wrong_answers + [correctAnswer]
    
    print(answer_options)
    
    
    
    
    #print(wrong_answers)
   #WE print(correctAnswer)
#pag 224