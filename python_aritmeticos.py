#Variaveis

n1 = 5.8
n2 = 3.2


#Caixa de Mensagem
from tkinter import messagebox

#adicao
resultado = n1 + n2
messagebox.showinfo('Operadores Aritméticos', 'Soma = ' + str(resultado))
print('Soma = ' + str(resultado))

#subtracao
resultado = n1 - n2
messagebox.showinfo('Operadores Aritméticos' , 'Sub = ' + str(resultado))
print('Sub = ' + str(resultado))

#multiplicao
resultado = n1 * n2
messagebox.showinfo('Operadores Aritméticos', 'Mul = ' + str(resultado))
print('Mul = ' + str(resultado))

#div
resultado = n1 / n2
messagebox.showinfo('Operadores Aritméticos' , 'Div = ' + str(resultado))
print('Div = ' + str(resultado))




