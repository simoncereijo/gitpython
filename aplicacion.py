from tkinter import *
from tkinter import filedialog
from tkinter import font
from clase_git import My_git

#Aplicacion para el uso de Git sin tener que utilizar la consola.
#En las entradas de "User" y "Email" configuras la pesrona que ha hecho las modificaciones en el repositorio
#Puedes validar un comit metiendo el comentario y pulsado validar
#puedes recuperar un commit seleccionandolo de la lista de commits y pulsando checkout
#Para generar la lista de commit debes estar dentro de una ruta con un repositorio creado y pulsar reflog
#si quieres sibir el repositio a github puedes introducir la url y pulsar subir a github

#Errores:
#-Cuando creo un repositio nuevo, tengo que volver a seleccionar la ruta para poder hacer commit
#-a la hora de subir a github, esta pendiente mostrar la lista de repositioros remotos creados para poder Seleccionar/borrar/crear


class Aplicacion(Tk):

    def __init__(self,*args,**kwargs):
        super(Aplicacion,self).__init__(*args,**kwargs)
        #configuracion root principal
        self.title("My Git")
        self.config(bg="ivory2",relief="sunken",bd=1)
        self.geometry("1200x710")
        self.resizable(0,0)
        self.frame_izquierdo()
        self.frame_derecho()
    def open_directory(self):#Seleccion de la ruta de nuestro repositorio local
        filepath = filedialog.askdirectory()
        return filepath
    def crear_label_directorio(self,frame,user,email):#Creamos un texto mostrando la ruta seleccionado y creamos o seleccionamos el repositorio
        filepath = filedialog.askdirectory()
        label_directorio=Label(frame,text=filepath,width=40)
        label_directorio.grid(row=3,column=1)
        self.repo=My_git(filepath,user,email)
    def checkout_versio(self):#recumeramos el comit seleccionado de la lista
        elemento_selecciondo=self.listbox.curselection()
        elemento_selecciondo=elemento_selecciondo[0]
        try:
            self.repo.checkout_commit(self.commits[elemento_selecciondo])
        except:
            pass
    def validar_commit(self,comentario):

        try:
            self.repo.commit_add(str(comentario))
            self.lista_comits(self.frame_rigth)
            
        except:
            pass



    def frame_izquierdo(self):#botones/textos dentro del frame del lado izquierdo

        #declaramos Frames
        self.frame_left=Frame(self)
        self.frame_left.config(width=1200/2, height=710,relief="sunken",bd=1)
        self.frame_left.grid(row=0,column=0)
        self.frame_left.grid_propagate(0)

        #Encabezado
        cabecera="CONFIGURACION DEL REPOSITORIO"
        encabezado=Label(self.frame_left,text=cabecera,height=3,font=("Arial",15))
        f = font.Font(encabezado, encabezado.cget("font"))
        f.configure(underline=True)
        encabezado.configure(font=f)
        encabezado.grid(row=0,column=0,columnspan=2)
        #Usuario
        label_user=Label(self.frame_left,text="User:",width=10)
        label_user.grid(row=1,column=0)
        entry_user=Entry(self.frame_left,width=40)
        entry_user.grid(row=1,column=1)
        #Email
        label_email=Label(self.frame_left,text="Email:",width=10)
        label_email.grid(row=2,column=0)
        entry_email=Entry(self.frame_left,width=40)
        entry_email.grid(row=2,column=1)
        #ruta de la carpeta donde crear el repositorio
        boton_busqueda_cd=Button(self.frame_left,text="Archivo...",width=10,command=lambda :self.crear_label_directorio(self.frame_left,entry_user.get(),entry_email.get()))
        boton_busqueda_cd.grid(row=3,column=0)
        #separador
        separador=Label(self.frame_left,text="------------------------------------------------------------------------------------------------------------")
        separador.grid(row=5,column=0,columnspan=20)
        #comit repo
        entrada_commit=Entry(self.frame_left,width=48)
        entrada_commit.grid(row=6,column=0)
        boton_commit=Button(self.frame_left,text="Validar nuevo Commit",width=40,command=lambda :self.validar_commit(entrada_commit.get()))
        boton_commit.grid(row=7,column=0)
        #separador
        separador=Label(self.frame_left,text="------------------------------------------------------------------------------------------------------------")
        separador.grid(row=8,column=0,columnspan=20)
        ##checkout repo

        boton_commit_checkout=Button(self.frame_left,text="Recuperar version",width=40,command=lambda :self.checkout_versio())
        boton_commit_checkout.grid(row=10,column=0)
        #separador
        separador=Label(self.frame_left,text="------------------------------------------------------------------------------------------------------------")
        separador.grid(row=11,column=0,columnspan=20)
        #push a github
        entrada_repo_github=Entry(self.frame_left,width=48)
        entrada_repo_github.grid(row=12,column=0)
        boton_push=Button(self.frame_left,text="Push a Github",width=40,command=lambda :self.repo.push_github(entrada_repo_github.get()))
        boton_push.grid(row=13,column=0)



    def lista_comits(self,frame):#Generamos la lista de los comits del repositorio seleccionado
        try:
            self.listbox = Listbox(frame, width=106, height=600)
            self.listbox.grid(row=1, column=0)
            self.listbox.grid_propagate(0)
            self.commits = self.repo.show_commits()
            j = 0
            lista_commits = ["" for x in range(len(self.commits))]
            for commit in self.commits:
                item = ("{}---{}---by---{}---({})".format(commit.hexsha, commit.summary,
                                                          commit.author.name, commit.author.email))

                lista_commits[j] = item
                j += 1
            if lista_commits != None:

                j = 0
                for i in lista_commits:
                    self.listbox.insert(j, i)
                    j += 1

        except:
            pass

    def frame_derecho(self):#Botones/textos dentro del frame del lado derecho


        self.frame_rigth=Frame(self)
        self.frame_rigth.config(width=1200 / 2, height=710, relief="sunken", bd=1)
        self.frame_rigth.grid(row=0,column=1)
        self.frame_rigth.grid_propagate(0)

        #Creo botones


        boton_reflog=Button(self.frame_rigth,text="Reflog",width=90,command=lambda :self.lista_comits(self.frame_rigth))
        boton_reflog.grid(row=0, column=0)





