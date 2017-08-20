#!/usr/local/bin/python3.5

import os
import time
import codecs
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"selenium"))
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
from status import SubStatus
import click
from settings import Settings
from pages import LoginPage, SubPage

@click.command()
@click.option('-s', default=1, help='Submeter um problema')
@click.option('-r', is_flag=True, help='Imprimir tabela de submissoes')
def uri(s, r):
    """Simple program that greets NAME for a total of COUNT times."""
    
    settings = Settings() 
    user, password = settings.get_settings()
    print(user)
    print(password)
    if r:
        print("Aqui")
        status(user, password)
    elif s:
        webdriver_download(user,password, s)

        
def webdriver_download(user, password, problem):
    chrome_dir = os.path.dirname(os.path.realpath(__file__))
    chrome_path = os.path.join(chrome_dir, "chromedriver", "chromedriver")
    print(chrome_path,chrome_dir, os.path.realpath(__file__))
    driver = webdriver.Chrome(chrome_path)
    driver.maximize_window()
    l = LoginPage(driver, user, password)
    if l.login():
        sub = SubPage(driver, problem)
        if sub.submit():
            print("Deu certo")
        else:
            print("Deu errado")
    else:
        print("Deu errado")
    time.sleep(5)
    driver.quit()

def status(user, password):
    chrome_dir = os.path.dirname(os.path.realpath(__file__))
    #chrome_path = os.path.join(chrome_dir, "chromedriver", "chromedriver")
    chrome_path = os.path.join(chrome_dir, "phantomjs", "bin", "phantomjs")
    print(os.path.isfile(chrome_path))
    print(os.path.isdir(chrome_path))
    print(chrome_path,chrome_dir, os.path.realpath(__file__))
    #driver = webdriver.Chrome(chrome_path)
    driver = webdriver.PhantomJS(chrome_path)
    driver.maximize_window()
    l = LoginPage(driver, user, password)
    if l.login():
        driver.get("https://www.urionlinejudge.com.br/judge/pt/runs")
        sub = SubStatus(driver.page_source)
        sub.print_table()
    else:
        print("Deu errado")
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    uri()
