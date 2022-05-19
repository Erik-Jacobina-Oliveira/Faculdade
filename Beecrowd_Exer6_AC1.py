sem = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

diasSema = input()
diasEntre = int(input())

entre = diasEntre + sem.index(diasSema)

if diasEntre == 0:
    print('chega hoje!')
elif entre <= 6:
    print(f'sera entregue {sem[entre]}')
else:
    entre1 = entre - 7
    print(f'sera entregue {sem[entre1]}')
