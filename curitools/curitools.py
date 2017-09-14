#!/usr/local/bin/python3.5
import os
import time
import codecs
import sys
import re
import click
from curitools.settings import Settings, MissingFileSettings
from curitools.setup_problems import SetupProblem
import curitools.requestpages.pages as rp
from requests.exceptions import HTTPError


@click.command()
@click.option('-s', default=1, help='Submeter um problema')
@click.option('-c', default=1, help='Criar arquivos para desenvolver o problema')
@click.option('-r', is_flag=True, help='Imprimir tabela de submissoes')
def uri(s, c, r):
    """Simple program that greets NAME for a total of COUNT times."""
    
    settings = Settings() 
    try:
        user, password = settings.get_settings()
    except MissingFileSettings:
        print(e.message)
        sys.exit()
    
    try:
        login = rp.LoginPage(user=user, password=password)
        login.run()
    except HTTPError:
        sys.exit()
    

    if r:
       sub = rp.TabelaSubmissionPage(session=login.get_session())
       sub.run() 
    elif c:
        cwd = os.getcwd()
        template_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(template_dir, "templates")
        setup = SetupProblem(str(c), cwd, template_dir, "c++")
        setup.create_files()
    elif s:
       sub = rp.SubmissionPage(login.get_session(), s)
       sub.run() 


if __name__ == "__main__":
    uri()
