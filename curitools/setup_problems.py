#!/usr/local/bin/python3.5
import re
import sys
import os
from shutil import copy

class SetupProblem(object):
    
    def __init__(self, problem, workdir, dir_template, language):
        self.problem = problem
        self.workdir = workdir
        self.dir_template = dir_template
        self.language = language
        self.list_files =  { 'c++' : { 'base' : 'base.cpp', 'makefile' : 'Makefile.c++'},
                             'python' : {'base' : "base.py" }}

    def has_makefile(self):
        if self.language in self.list_files and "makefile" in self.list_files[self.language]:
            return True
        return False

    def get_base_template(self):
        return os.path.join(self.dir_template, self.list_files[self.language]["base"]) 

    def get_makefile_template(self):
        return os.path.join(self.dir_template, self.list_files[self.language]["makefile"]) 
         
    def create_files(self):
        print(self.workdir)
        if os.path.isdir(self.workdir):
            problem_dir = os.path.join(self.workdir, self.problem)
            print("Aqui")
            if not os.path.isdir(problem_dir):
                os.makedirs(problem_dir)
                self.create_base_files(problem_dir)
            else:
                raise FileExistsError("Pasta com o nome do problema ja existe no diretorio")
        else:
            raise NotADirectoryError("Tentando criar arquivos para resolver o problema em um lugar que nao e um diretorio") 

    def create_base_files(self, problem_dir):
        base_file = self.get_base_template()
        if not os.path.exists(base_file):
            raise FileExistsError("O arquivo de template nao existe.")
        filename, file_extension = os.path.splitext(base_file)
        problem_file = "".join([self.problem, file_extension])
        problem_file =  os.path.join(problem_dir, problem_file)  
        copy(base_file, problem_file)
        if self.has_makefile():
            self.create_makefile(problem_dir)

    def create_makefile(self, problem_dir):
        make_file = self.get_makefile_template()
        make_file_dst = os.path.join(problem_dir, "Makefile")
        copy(make_file, make_file_dst)  



