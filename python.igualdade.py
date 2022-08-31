valorA = 1
valorB = 2

textoA = 'TESTE'
textoB = 'TEXTO'


#Comparacao dos valores
if valorA == valorB:
    from tkinter import messagebox
    messagebox.showinfo('Igualdade' , 'Valores iguais')
    print('Valores iguais')

else:
    from tkinter import messagebox
    messagebox.showinfo('Igualdade' , 'Valores diferentes')
    print('Valores diferentes')

    if valorA != valorB:
        from tkinter import messagebox
        messagebox.showinfo('Igualdade','Valores diferentes')
        print('Valores diferentes')

    else:
        from tkinter import messagebox
        messagebox.showinfo('Igualdade','Valores iguais')
        print('Valores iguais')

#Comparacao dos textos
if textoA == textoB:
    from tkinter import messagebox
    messagebox.showinfo('Igualdade' , 'Valores iguais')
    print('Valores iguais')

else:
    from tkinter import messagebox
    messagebox.showinfo('Igualdade' , 'TEXTOS diferentes')
    print('TEXTOS diferentes')

    if textoA != textoB:
        from tkinter import messagebox
        messagebox.showinfo('Igualdade','TEXTOS diferentes')
        print('TEXTOS diferentes')

    else:
        from tkinter import messagebox
        messagebox.showinfo('Igualdade','TEXTOS iguais')
        print('TEXTOS iguais')
