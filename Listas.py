import nester

'Exercicio 1 pagina 13'
movies = ['the holy grail', 'the life of brian', 'the meanin of life']
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)
#print(movies)

'exercicio 2 pagina 13'
movies1 = ['the holy grail', 1975, 'the life of brian', 1979, 'the meanin of life', 1983]
#print(movies1)

'exercico pagina 21'
movies3 = ['the holy grail', 1975, 'terry jones & terry gillian', 91,
           ['graham chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam','Eric Idle','Terry Jones']]]

#exercicio pagina 43
nester.print_lol(movies3)

#exercicio pagian
nester.print_lol(movies3,True)

nester.print_lol(movies3,True,1)
