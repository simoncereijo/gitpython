from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox

import os as os
from clase_git import My_git

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
    def open_directory(self):
        filepath = filedialog.askdirectory()
        return filepath
    def crear_label_directorio(self,frame,user,email):
        filepath = filedialog.askdirectory()
        label_directorio=Label(frame,text=filepath,width=40)
        label_directorio.grid(row=3,column=1)
        self.repo=My_git(filepath,user,email)
    def checkout_versio(self):
        elemento_selecciondo=self.listbox.curselection()
        elemento_selecciondo=elemento_selecciondo[0]
        try:
            self.repo.checkout_commit(self.commits[elemento_selecciondo])
        except:
            pass

    def frame_izquierdo(self):

        #declaramos Frames
        frame_left=Frame(self)
        frame_left.config(width=1200/2, height=710,relief="sunken",bd=1)
        frame_left.grid(row=0,column=0)
        frame_left.grid_propagate(0)

        #Encabezado
        cabecera="CONFIGURACION DEL REPOSITORIO"
        encabezado=Label(frame_left,text=cabecera,height=3,font=("Arial",15))
        f = font.Font(encabezado, encabezado.cget("font"))
        f.configure(underline=True)
        encabezado.configure(font=f)
        encabezado.grid(row=0,column=0,columnspan=2)
        #Usuario
        label_user=Label(frame_left,text="User:",width=10)
        label_user.grid(row=1,column=0)
        entry_user=Entry(frame_left,width=40)
        entry_user.grid(row=1,column=1)
        #Email
        label_email=Label(frame_left,text="Email:",width=10)
        label_email.grid(row=2,column=0)
        entry_email=Entry(frame_left,width=40)
        entry_email.grid(row=2,column=1)
        #ruta de la carpeta donde crear el repositorio
        boton_busqueda_cd=Button(frame_left,text="Archivo...",width=10,command=lambda :self.crear_label_directorio(frame_left,entry_user.get(),entry_email.get()))
        boton_busqueda_cd.grid(row=3,column=0)
        #separador
        separador=Label(frame_left,text="------------------------------------------------------------------------------------------------------------")
        separador.grid(row=5,column=0,columnspan=20)
        #comit repo
        entrada_commit=Entry(frame_left,width=48)
        entrada_commit.grid(row=6,column=0)
        boton_commit=Button(frame_left,text="Validar nuevo Commit",width=40,command=lambda :self.repo.commit_add(entrada_commit.get()))
        boton_commit.grid(row=7,column=0)
        #separador
        separador=Label(frame_left,text="------------------------------------------------------------------------------------------------------------")
        separador.grid(row=8,column=0,columnspan=20)
        ##checkout repo

        boton_commit_checkout=Button(frame_left,text="Recuperar version",width=40,command=lambda :self.checkout_versio())
        boton_commit_checkout.grid(row=10,column=0)
        #separador
        separador=Label(frame_left,text="------------------------------------------------------------------------------------------------------------")
        separador.grid(row=11,column=0,columnspan=20)
        #push a github
        entrada_repo_github=Entry(frame_left,width=48)
        entrada_repo_github.grid(row=12,column=0)
        boton_push=Button(frame_left,text="Push a Github",width=40,command=lambda :self.repo.push_github(entrada_repo_github.get()))
        boton_push.grid(row=13,column=0)



    def lista_comits(self,frame):
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

    def frame_derecho(self):


        frame_rigth=Frame(self)
        frame_rigth.config(width=1200 / 2, height=710, relief="sunken", bd=1)
        frame_rigth.grid(row=0,column=1)
        frame_rigth.grid_propagate(0)

        #Creo botones


        boton_reflog=Button(frame_rigth,text="Reflog",width=90,command=lambda :self.lista_comits(frame_rigth))
        boton_reflog.grid(row=0, column=0)





