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
            messagebox.showwarning("warning", "Ningun cambio a comitear\n Vuelve a seleccionar la carpeta")

    def checkout_commit(self,commit_id):#volver a un commit seleccionamos
        repo.git.checkout(commit_id)
    def push_github(self,destino):

        if destino!="URL Repositorio remoto":
            try:  # Creamos un repositio remoto, hay que darle la opcion de seleccionarlo de la lista o crear uno nuevo, por ahora solo trabaja en mi repositorio
                origin = repo.create_remote('origin', destino)
                repo.git.push("--set-upstream", origin, repo.head.ref)
            except:
                repo.remotes.origin.push()

                # En un futuro mostrar los remotes creados para poder seleccionarlos
                # print('Remotes:')
                # for remote in repo.remotes:
                #    print(f'- {remote.name} {remote.url}')



    def show_commits(self):
        commits = list(repo.iter_commits('master'))
        return commits
        lista_commits = [""for x in range(len(commits))]
        j=0
        for commit in commits:
            item = ("{}---{}---by---{}---({})".format(commit.hexsha, commit.summary,
                                                                           commit.author.name, commit.author.email))

            lista_commits[j]=item
            j+=1
        return lista_commits
