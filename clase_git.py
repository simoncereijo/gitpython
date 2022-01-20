from git import  *
from tkinter import messagebox
import os as os

class My_git:

    def __init__(self,path,user,email):
        global repo

        try:
            repo = Repo(path)
            comand1 = ("git config --global user.name \"{}\"".format(user))
            comand2 = ("git config --global user.email \"{}\"").format(email)
            os.system(comand1)
            os.system(comand2)
        except:
            valor = messagebox.askquestion("New Repo", "No existe repositorio en esta ruta, desea crear uno nuevo?")
            if valor == "yes":
                Repo.init(path)

    def commit_add(self,comentario):

        try:
            repo.git.add(all=True)
            repo.git.commit('-m', comentario)
        except:
            messagebox.showwarning("warning", "Ningun cambio a comitear\n o error en la ruta")

    def checkout_commit(self,commit_id):
        repo.git.checkout(commit_id)
    def push_github(self,origen):
        origin = repo.remote(name=origen)
        origin.push()
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
