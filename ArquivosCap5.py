import os


def importa_arquivos(nome_arquivo):
    with open(nome_arquivo) as file:
        return file.readline().strip().split(',')


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

james = iterableList(james)
julie = iterableList(julie)
mikey = iterableList(mikey)
sarah = iterableList(sarah)

james_order = ordena_lista(james)
julie_order = ordena_lista(julie)
mikey_order = ordena_lista(mikey)
sarah_order = ordena_lista(sarah)

print(james)
print(james_order)
print(julie)
print(julie_order)
print(mikey)
print(mikey_order)
print(sarah)
print(sarah_order)
