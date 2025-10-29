#Set(listas)
    #simliar a listas
    #Evita itens duplicados
    #Não utiliza index


list1= [10,20,30,40,50]
list2= [10,20,30,40,70,80,60]


num1= set(list1)
num2= set(list2)

print(num1| num2)  #essa barra significa union(uniao)
print(num1 - num2) #Difference
print(num1 ^ num2 ) #Symetric
print(num1 & num2) #And  (duplicado)
print(len(num1))