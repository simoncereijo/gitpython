from git import  *
from tkinter import messagebox
import os as os

class My_git:

    def __init__(self,path,user,email):
        global repo

        try:#Comprobamos is existe un repositorio creado
            repo = Repo(path)
            comand1 = ("git config --global user.name \"{}\"".format(user))
            comand2 = ("git config --global user.email \"{}\"").format(email)
            os.system(comand1)
            os.system(comand2)
        except:#Si no existe preguntamos si lo inicializamos, si responde si lo hacemos si responde no no hacemos nada
            valor = messagebox.askquestion("New Repo", "No existe repositorio en esta ruta, desea crear uno nuevo?")
            if valor == "yes":
                Repo.init(path)
                repo = Repo(path)

    def commit_add(self,comentario):

        try:#intentamos hacer el commit, es necesario avisar al usuario en caso de que se dejase la entrada del comentario vacia
            repo.git.add(all=True)
            repo.git.commit('-m', comentario)
        except:
            messagebox.showwarning("warning", "Ningun cambio a comitear\n Vuelve a seleccionar la carpeta.")

    def checkout_commit(self,commit_id):#volver a un commit seleccionamos
        repo.git.checkout(commit_id)
    def push_github(self,remote):

            try:
                repo.git.push("--set-upstream", remote, repo.head.ref)
            except:
                repo.remotes.remote.push()

    def list_remotes(self):
            return repo.remotes

    def crear_remote(self,name,url):
        try:
            return repo.create_remote(name, url)
        except:
            messagebox.showwarning("warning", "Fallo al crear remote")

    def borrar_remote(self,name):
        try:
            repo.delete_remote(name)
        except:
            messagebox.showwarning("warning", "Fallo al borrar remote")

    def show_commits(self):
        commits = ["--MASTER--"]+list(repo.iter_commits('master'))+["--HEAD--"]+list(repo.iter_commits('HEAD'))
        return commits
        lista_commits = [""for x in range(len(commits))]
