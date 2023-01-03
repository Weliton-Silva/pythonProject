nome = input('Qual nome do funcionario ? ')
sal = float(input('Qual salario ? '))
print('Novo Salario do {} com aumento de 15% é de R${:.2f}'.format(nome, (15 * sal) /100 + sal))



