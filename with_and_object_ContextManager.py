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
    


