# Creating python file 

file_names = [ str(i).zfill(3) + '.py' for i in range(1,102)]

for file in file_names:
    temp = open('src/'+file, 'w')
    temp.write('import numpy as np')
    temp.close()