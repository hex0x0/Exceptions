import os
import random



class Jogo(object):
    def __init__(self):
        self.__capitais = {
            
            'Brasil':'Brasilia', 'China':'Pequim', 'Colombia':'Bogotá', 'Canadá':'Otawa',
            'Peru':'Lima', 'Argentina':'Buenos aires', 'Chile':'Santiago', 'Inglaterra':'Londres',
            'Estados Unidos':'Washington', 'Mexico':'Mexico', 'Angola':'Luanda', 'Portugal': 'Lisboa',
            'Argélia':'Argel', 'Filipinas':'Manila', 'Grécia':'Atenas', 'Índia':'Nova Délhi',
            'Itália':'Roma', 'Taiwan':'Taipei', 'Rússia':'Moscou'               
        }
        
        self.__score = 0
        
        self.main()
        
    def correct_answer(self):
        resp = list(self.__capitais.values())
        
        return resp
    
    def wrong_answer(self):
        resp = list()
        
    def pause(self):
        pause = input('Press <Enter> key to continue')
        
    
        
    def showInfo(self):
        print(' '*50 + 'Quiz')
        print('-'*100)
        print('Made by @Lucas')
       
        print('''
                Esse jogo é um quiz das capitais de alguns países do mundo
                
                O jogador é perguntado qual a capital de um país e deve escolher uma das
                4 opções (1, 2, 3, ou 4)
                
              
              ''')  
        
        
    def show_score(self, score, sizeDict): 
        print(sizeDict)
        if score == sizeDict:
            print('*'*50)
            print('Seu score: %i'%score)
            print('Eba... Você é um gigachad!')
            print('*'*50) 
        else:
            print('*'*50)
            print('Seu score: %i'%score)
            print('*'*50)
        
    def main(self):
        self.showInfo()
        states = list(self.__capitais.keys())
        self.__score = 0
        for i in range(len(self.__capitais)):
            #gera uma lista de estados
            corret_answer = self.__capitais[states[i]]
            wrong_answers = list(self.__capitais.values())
            del wrong_answers[wrong_answers.index(corret_answer)]
            
            wrong_answers = random.sample(wrong_answers, 3)
            
            answer_options = wrong_answers + [corret_answer]
            
            random.shuffle(answer_options)
        
            while True:
                
                for j in range(4):
                    print('%d - %s'%(j+1, answer_options[j]))
                
                resp = int(input('Qual a capital do/da %s: '%states[i]))
                
                if corret_answer == answer_options[resp-1]:
                    print('Parabéns, a reposta correta é %s'%answer_options[resp-1])
                    self.__score += 1
                    self.pause()
                    os.system('cls')
                    break
                else:
                    print('Você errou! Próxima questão!')
                    print('Você é muito burro, tá ok?!"')
                    #os.system('cls')
                    self.pause()
                    os.system('cls')
                    break
                

            
            
            self.show_score(self.__score, len(self.__capitais))
            
            
            
            
            
    
  


if __name__ == '__main__':
    x = Jogo()