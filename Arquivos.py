import os

#printa a pasta que voce esta
print(os.getcwd())
# anda pelos diretorios
os.chdir('ArquivosApoio/chapter3')
#printa novamente a nova pasta
print(os.getcwd())

data = open('sketch.txt')

for each_line in data:
    print(each_line,end='')

