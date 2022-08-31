quantidadeAnos = 5
horasTrabalhadas = 40
valorHora = 50
salario = 0

if quantidadeAnos <= 1:
    salario = 1500 + (valorHora * horasTrabalhadas)

elif quantidadeAnos > 1 and quantidadeAnos < 3:
        salario = 2000 + (valorHora * horasTrabalhadas)

else:
    salario = 3000 + (valorHora * horasTrabalhadas)


from tkinter import messagebox
messagebox.showinfo('Exemplos', 'salario' + str(salario))
print('salario' + str(salario))
