
#Um ano é bissexto se ele for divisível por 400 ou se ele for divisível por 4 e não por 100.
# Assim:



def ano_bissexto(y):
    if y % 400 == 0:
        return 'Sim,bissexto'
    if y % 100 == 0:
        return 'não, não é bissexto'
    if y % 4 == 0:
        return 'sim, bissexto'
    else:
        return 'não, não é bissexto'
print(ano_bissexto(1900))
print(ano_bissexto(2004))
#
#
#

