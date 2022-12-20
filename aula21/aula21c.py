def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    : Param i: inicio da contagem
    : Param f: fim da contagem
    : Param p: passo da contagem
    : return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)
