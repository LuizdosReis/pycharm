import os


def importa_arquivos(nome_arquivo):
    try:
        with open(nome_arquivo) as file:
            return file.readline().strip().split(',')
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


def printing(name, list, list_order, list_unique, list_three_best):
    print(name)
    print('Data')
    print(list)
    print('Order')
    print(list_order)
    print('Unique')
    print(list_unique)
    print('three best times')
    print(list_three_best)

os.chdir('ArquivosApoio/chapter5')

james = [];
julie = [];
mikey = [];
sarah = [];

nome_arquivo = 'james.txt'
james = importa_arquivos('james.txt')
julie = importa_arquivos('julie.txt')
mikey = importa_arquivos('mikey.txt')
sarah = importa_arquivos('sarah.txt')

james_order = ordena_lista(iterableList(james))
julie_order = ordena_lista(iterableList(julie))
mikey_order = ordena_lista(iterableList(mikey))
sarah_order = ordena_lista(iterableList(sarah))

james_unique = unique(james_order)
julie_unique = unique(julie_order)
mikey_unique = unique(mikey_order)
sarah_unique = unique(sarah_order)

printing('james', james, james_order, james_unique, james_unique[0:3])

printing('julie', julie, julie_order, julie_unique, julie_unique[0:3])

printing('mikey', mikey, mikey_order, mikey_unique, mikey_unique[0:3])

printing('sarah', sarah, sarah_order, sarah_unique, sarah_order[0:3])
