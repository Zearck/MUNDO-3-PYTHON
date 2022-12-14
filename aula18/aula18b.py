# -> Cria uma lista composta "galera" com 4 listas
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# -> Exibe [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])  # -> Exibe ['João', 19]
print(galera[0][0])  # -> Exibe João
print(galera[2][1])  # ->  Exibe 13
print('')
for pessoa in galera:  # -> Para cada "pessoa" na lista composta "galera"...
    print(pessoa)  # -> Exibe todos os dados (nome e idade) da "pessoa" atual
