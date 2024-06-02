# Creating python file 

file_names = [ str(i).zfill(3) + '.py' for i in range(0,102)]

for file in file_names:
    temp = open('src/'+file, 'w')
    temp.close()