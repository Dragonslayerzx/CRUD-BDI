from tkinter import Tk, Label, Button, Entry, messagebox, Toplevel
from db.connection import dbConnect

class mainWindow:
    #Constructor se ejecuta al instanciar un objeto
    def __init__(self):
        #creando ventana principal
        self.root = Tk()
        self.root.title("CRUD DBI")
        self.root.geometry("600x400")
        self.index()
        # self.root.config(bg="gray")

    def index(self):
        #Self para que las variables sean accesibles fuera del metodo
        self.lbl = Label(self.root, text="Operaciones Crud DB", font ="Helvetica 20")
        self.lbl.pack(pady=20)

        self.lbl2 = Label(self.root, text="Ingrese las credenciales de usuario de la DB", font ="Helvetica 12")
        self.lbl2.pack()

        self.lblUser = Label(self.root, text = "User: ", font="Helvetica 10") #Se ocupa el self, ya que se hace referencia abajo
        self.lblUser.place(x=100, y=140, width=100, height=30)
        self.userEntry = Entry(self.root)
        self.userEntry.place(x=300, y=140, width=200, height=25)

        self.lblPass = Label(self.root, text = "Password: ", font="Helvetica 10")
        self.lblPass.place(x=100, y=190, width=100, height=30)
        self.passEntry = Entry(self.root, show="*")
        self.passEntry.place(x=300, y=190, width=200, height=25)

        self.lblServer = Label(self.root, text = "Server: ", font="Helvetica 10")
        self.lblServer.place(x=100, y=240, width=100, height=30)
        self.serverEntry = Entry(self.root)
        self.serverEntry.place(x=300, y=240, width=200, height=25)

        self.lblDb = Label(self.root, text = "Database: ", font="Helvetica 10")
        self.lblDb.place(x=100, y=290, width=100, height=30)
        self.dbEntry = Entry(self.root)
        self.dbEntry.place(x=300, y=290, width=200, height=25)

        self.btn = Button(self.root, text="Ingresar", width=15, height=2, command=self.connectDb)
        self.btn.place(x=250, y=340)

    def connectDb(self):
        user = self.userEntry.get()
        password = self.passEntry.get()
        server = self.serverEntry.get()
        dbname = self.dbEntry.get()

        self.connection = dbConnect(user, password, server, dbname)

        if self.connection:
            print("Conexion exitosa")
            #messagebox.showinfo("Conexion exitosa")
            self.openAdminWindow()
        else:
            print("Failed connection")
            messagebox.showerror("Failure", "Hubo un error al conectarse la DB")
    
    def openAdminWindow(self):
        self.adminWindow = adminWindow(self.root, self.connection)
        self.adminWindow.run()

    def run(self):
        self.root.mainloop()

#Clase para la administracion de la DB
class adminWindow:
    #Constructor de la clase
    def __init__(self, parent, connection):
        self.connection = connection 
        self.window = Toplevel(parent)   #Ventana a partir de vantana padre
        self.window.title("DB Admin")
        self.admin_ui()
    
    def admin_ui(self):
        self.window.geometry("600x400")

        title = Label(self.window, text="Administracion de la Database", font = "Helvetica 20")
        title.pack(pady=20)


        create_btn = Button(self.window, text = "Create table")
        create_btn.pack(pady=15)

        select_btn = Button(self.window, text = "Select")
        select_btn.pack(pady=15)

        insert_btn = Button(self.window, text = "Insert")
        insert_btn.pack(pady=15)

        delete_btn = Button(self.window, text = "Delete")
        delete_btn.pack(pady=15)

    def run(self):
        self.window.mainloop()