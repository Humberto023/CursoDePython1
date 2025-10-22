'''num1= 10
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)'''

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

novo_preco = preco - (preco * desconto/100)
print(f'O valor do preço com desconto será igual a R${novo_preco}:')

