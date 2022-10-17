import tkinter
from bd_utils import crear_usuario
import cryptocode

class EntryWithPlaceholder(tkinter.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


class Login:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Ingreso")

        f1 = tkinter.Frame(self.ventana)
        f1.grid(column=0, row=0)
        f2 = tkinter.Frame(self.ventana)
        f2.grid(column=0, row=1)

        etiqueta = tkinter.Label(f1, text = "¡Welcome to Roluby Clash!", font = "Arial 30", bg = "pink")
        etiqueta.pack()

        self.cajaNombre = EntryWithPlaceholder(f1,"Ingrese su nombre")
        self.cajaNombre.pack()
        
        self.cajaUsuario = EntryWithPlaceholder(f1,"Ingrese nombre de usuario")
        self.cajaUsuario.pack()
        
        self.cajaPassw = EntryWithPlaceholder(f1,"Ingrese su contraseña")
        self.cajaPassw.pack()
        self.cajaPassw['show'] = "*"

        boton1 = tkinter.Button(f2, text = "Let's go ;)", bg = "pink", command=self.ejecutar)
        boton1.pack()

        self.ventana.mainloop()
    
    def ejecutar(self):
        nombre = self.cajaNombre.get()
        usuario = self.cajaUsuario.get()
        passw = self.cajaPassw.get()
        passw_encrip = cryptocode.encrypt(passw,"wow")
        crear_usuario(nombre, usuario, passw_encrip)
        self.ventana.destroy()

    '''def chechPas(password, hashed):
        check = password.encode('utf-8')
        if bcrypt.checkpw(check, hashed):
            return True
        else:
            return False'''
    
if __name__ == "__main__":
    l = Login()
    
