salario = float(input('qual o seu salario?: '))
percentual = float(input('informe o digito para percentual: '))

percentual = percentual / 100

ajuste = salario * percentual
novo_salario = salario + ajuste

print(f'salario anterior: R$ {salario:.2f}')
print(f'Valor de ajuste: R$ {ajuste:.2f}')
print(f'Novo salario: R$ {novo_salario:.2f}')

