dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos Km rodados ? '))
total = dias * 60
print(' O Valor total a pagar é de R$ {:.2f}'.format((km * 0.15) + total))
