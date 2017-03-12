import os
import pickle

#printa a pasta que voce esta
print(os.getcwd())
# anda pelos diretorios
os.chdir('ArquivosApoio/chapter3')
#printa novamente a nova pasta
print(os.getcwd())
man = []
other = []

# verifica se o arquivo foi encontrado
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if (role == 'Man'):
                man.append(line_spoken)

            elif (role == 'Other Man'):
                other.append(line_spoken)

        except ValueError:
            # ignora o erro e continua o programa
            pass
    data.close()
except IOError:
    print('the data file is missing!')

try:
    with open('OutMan.txt', 'wb') as out_man:
        pickle.dump(man, out_man)
    with open('OtherMan.txt', 'wb') as out_other_man:
        pickle.dump(other, out_other_man)
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
