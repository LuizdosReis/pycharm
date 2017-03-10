import os

#printa a pasta que voce esta
print(os.getcwd())
# anda pelos diretorios
os.chdir('ArquivosApoio/chapter3')
#printa novamente a nova pasta
print(os.getcwd())

data = open('sketch.txt')

for each_line in data:
    if each_line.find(':') != -1:
        (role,line_spoken) = each_line.split(':',1)
        print(role, end='')
        print(' said:', end='')
        print(line_spoken, end='')
    else:
        print(each_line,end='')

data.close()



