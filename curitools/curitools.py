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
import logging

@click.command()
@click.option('-s', default=0, help='Submeter um problema')
@click.option('-c', default=0, help='Criar arquivos para desenvolver o problema')
@click.option('-r', is_flag=True, help='Imprimir tabela de submissoes')
@click.option('-d', is_flag=True, help='Debug output')
def uri(s, c, r, d):
    """Simple program that greets NAME for a total of COUNT times."""
    if(d): 
        log_file = os.path.join(os.getcwd(), "curitools.log")
        print("log_file")
        print(log_file)
        logging.basicConfig(filename=log_file, format='%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.debug("The value of s: %s, c: %s, r: %s, d: %s", str(s), str(c), str(r), str(d)) 
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)

    

    settings = Settings() 
    try:
        user, password = settings.get_settings()
    except MissingFileSettings:
        logging.debug("Settings' file was not found")
        sys.exit()
    #options that do not need login 
    if c:
       logging.debug("C option was executed")
       cwd = os.getcwd()
       template_dir = os.path.dirname(os.path.realpath(__file__))
       template_dir = os.path.join(template_dir, "templates")
       setup = SetupProblem(str(c), cwd, template_dir, "c++")
       setup.create_files()
       return 1
    try:
        login = rp.LoginPage(user=user, password=password)
        login.run()
    except HTTPError:
        logging.debug("HTTP error")
        sys.exit()
    

    if r:
       logging.debug("R option was executed")
       sub = rp.TabelaSubmissionPage(session=login.get_session())
       sub.run() 
    elif s:
       logging.debug("S option was executed")
       sub = rp.SubmissionPage(login.get_session(), s)
       sub.run() 


if __name__ == "__main__":
    uri()
