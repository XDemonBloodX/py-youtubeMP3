import os 

path = './convert'
path2 = './songs'
try: 
    os.mkdir(path) 
except OSError as error: 
    print(error)  

try: 
    os.mkdir(path2) 
except OSError as error: 
    print(error)  