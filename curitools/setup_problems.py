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

    def has_makefile(self):
        if "c++" in self.language:
            return True
        return False

    def get_base_template(self):
        if "c++" in self.language:
            base_file = os.path.join(self.dir_template, "base.cpp") 
        else:
            base_file = os.path.join(self.dir_template, "base.cpp") 

        return base_file

    def get_makefile_template(self):
        if "c++" in self.language:
            make_file =  os.path.join(self.dir_template, "Makefile.c++")      
        else:
            make_file =  os.path.join(self.dir_template, "Makefile.c++")      

        return  make_file
         
    def create_files(self):
        if os.path.isdir(self.workdir):
            problem_dir = os.path.join(self.workdir, self.problem)
            if not os.path.isdir(problem_dir):
                os.makedirs(problem_dir)
                base_file = self.get_base_template()
                filename, file_extension = os.path.splitext(base_file)
                problem_file = ".".join([self.problem, file_extension])
                problem_file =  os.path.join(self.workdir, self.problem, problem_file)  
                copy(base_file, problem_file)
                if self.has_makefile():
                    self.create_makefile(problem_dir)

    def create_makefile(self, problem_dir):
        make_file = self.get_makefile_template()
        make_file_dst = os.path.join(problem_dir, "Makefile")
        copy(make_file, make_file_dst)  



