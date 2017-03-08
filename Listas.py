'Exercicio 1 pagina 13'
movies = ['the holy grail', 'the life of brian', 'the meanin of life']
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)
print(movies)

'exercicio 2 pagina 13'
movies1 = ['the holy grail', 1975, 'the life of brian', 1979, 'the meanin of life', 1983]
print(movies1)

'exercico pagina 21'
movies3 = ['the holy grail', 1975, 'terry jones & terry gillian', 91,
           ['graham chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam','Eric Idle','Terry Jones']]]

for movie in movies3:
    if(isinstance(movie,list)):
        for m in movie:
            if (isinstance(m, list)):
                for n in m:
                    print(n)
            else:
                print(m)
    else:
        print(movie)

'exercicio pagina 29'
def print_lol(the_list):
    for item in the_list:
        if(isinstance(item,list)):
            print_lol(item)
        else:
            print(item);





print_lol(movies3)