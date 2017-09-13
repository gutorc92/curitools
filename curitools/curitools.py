#!/usr/local/bin/python3.5
import os
import time
import codecs
import sys
import re
import click
from curitools.settings import Settings, MissingFileSettings
import curitools.requestpages.pages as rp
from requests.exceptions import HTTPError


@click.command()
@click.option('-s', default=1, help='Submeter um problema')
@click.option('-r', is_flag=True, help='Imprimir tabela de submissoes')
def uri(s, r):
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
    elif s:
       sub = rp.SubmissionPage(login.get_session(), s)
       sub.run() 


if __name__ == "__main__":
    uri()
