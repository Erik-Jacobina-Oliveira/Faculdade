nt = float(input())
np = float(input())
med = (nt + np) / 2

if med < 0 and med > 10:
    print('ERRO!')

if med >= 6:
    print('aprovado')
elif nt < 2 or med < 6:
    print('reprovado')
else:
    print('talvez com a sub')
