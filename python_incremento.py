numero = 5

from tkinter import messagebox

messagebox.showinfo('Operadores Incremento' , 'numero = ' + str(numero))
print('numero = ' + str(numero))

#incremento
numero+=1
messagebox.showinfo('Operadores Incremento' , 'numero = ' + str(numero))
print('numero = ' + str(numero))

#decremento
numero-=1
messagebox.showinfo('Operadores Decremento', 'numero = ' + str(numero))
print('numero = ' + str(numero))


##desafioUm
desafioUm = 5
desafioUm += 6
messagebox.showinfo('Desafio Um' , desafioUm)
print(desafioUm)

##desafioDois
desafioDois = 5
desafioDois += 5
messagebox.showinfo('Desafio Dois', desafioDois)
print(desafioDois)




