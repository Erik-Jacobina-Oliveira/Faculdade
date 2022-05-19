valor = float(input())
quant = int(input())

total = valor * quant

print(f'{total:.2f}')

desc = quant * 1 + 10
tf = (total * desc)/100
tf1 = total - tf
print(f'{tf1:.2f}')