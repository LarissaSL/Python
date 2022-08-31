texto = 'TES'


if texto == 'TESTE':
    from tkinter import messagebox
    messagebox.showinfo('Decisão Composta' , str(texto) + ' igual')

else:
    from tkinter import messagebox
    messagebox.showinfo('Decisão Composta' , str(texto) + ' diferente')