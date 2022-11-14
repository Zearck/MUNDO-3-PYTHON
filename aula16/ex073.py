times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
         'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Botafogo', 'América-MG',
         'Fortaleza', 'São Paulo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Atlético-GO', 'Ceará SC', 'Avaí', 'Juventude')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em odem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense está na {times.index("Capecoense")+1}ª posição')
