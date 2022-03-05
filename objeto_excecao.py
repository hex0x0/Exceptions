#As vezes queremos levantar uma exceção
#Em outras, queremos mostrar o estado da exceção


from with_and_object_ContextManager import NossoContextManager


with NossoContextManager() as nosso:
    raise ValueError('spam')

class DeuErro(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def __str__(self):
        return 'Putz, deu erro na linha %s do arquivo %s'%(self.line, self.file)


#Posso ter um custom print -> deu erro justo agora

try:
    raise DeuErro('meu', 'arquivo.txt')
except DeuErro:
    print(DeuErro('meu', 'arquivo.txt'))