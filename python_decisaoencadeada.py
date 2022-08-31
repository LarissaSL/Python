texto = 'NAO TESTE'


if texto == 'TESTE':
    from tkinter import messagebox
    messagebox.showinfo('Decisão Encadeada' , str(texto) + ' igual')

elif texto == 'NAO TESTE':
    from tkinter import messagebox
    messagebox.showinfo('Decisão Encadeada' , str(texto) + ' NÃO TESTE')

else:
    from tkinter import messagebox
    messagebox.showinfo('Decisão Encadeada' , str(texto) + ' diferente')