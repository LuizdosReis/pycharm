import os
from athlete import Athlete

def importa_arquivos(nome_arquivo):
    try:
        with open(nome_arquivo) as file:
            list = file.readline().strip().split(',')
            athlete = Athlete(list.pop(0), list.pop(0), unique(ordena_lista(iterableList(list))))
            return athlete
    except IOError as err:
        print('Erro: ' + str(err))
        return None


def ordena_lista(lista):
    return sorted(lista)


def sanitize(time_string):
    if '-' in time_string:
        (mins, secs) = time_string.split('-')
    elif ':' in time_string:
        (mins, secs) = time_string.split(':')
    else:
        return time_string
    return mins + '.' + secs


def iterableList(list):
    list_aux = [sanitize(time) for time in list]
    return list_aux


def unique(list):
    list_unique = []
    for time in list:
        if time not in list_unique:
            list_unique.append(time)
    return list_unique


def printing(athlete):
    print('name')
    print(athlete.name)
    print('dob')
    print(athlete.dob)
    print('times')
    print(athlete.top3())


os.chdir('ArquivosApoio/chapter6')

sarah2 = importa_arquivos('sarah2.txt')
james2 = importa_arquivos('james2.txt')
julie2 = importa_arquivos('julie2.txt')
mikey2 = importa_arquivos('mikey2.txt')

printing(sarah2)
printing(james2)
printing(julie2)
printing(mikey2)

