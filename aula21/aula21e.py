def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
# -> Por ter dado print em um escopo global, o x não conseguiu ser chamado por ser de escopo local
# print(f'No programa principal, x vale {x}')
