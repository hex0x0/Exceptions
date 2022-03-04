from pathlib import Path
import os, shutil

p = Path('C:\\Users\\delta\\Desktop\\eggs')
#shutil.copy(p / 'boobs.txt', p / 'new_folder')


#or

#shutil.copy(p / 'boobs.txt', p / 'new_folder/mega_boobs.txt')

#or
#Copia tudo que tem na pasta spam para a pasta spamzinho
#shutil.copytree(p / 'spam', p / 'spamzinho')

shutil.move(p / 'droga.txt', p / 'spamzinho')

