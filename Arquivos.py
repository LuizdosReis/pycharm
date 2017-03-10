import os

#printa a pasta que voce esta
print(os.getcwd())
# anda pelos diretorios
os.chdir('ArquivosApoio/chapter3')
#printa novamente a nova pasta
print(os.getcwd())

# verifica se o arquivo foi encontrado
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')
        except ValueError:
            # ignora o erro e continua o programa
            pass
    data.close()
except IOError:
    print('the data file is missing!')
