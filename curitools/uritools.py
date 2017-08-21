#!/usr/local/bin/python3.5
import os
import time
import codecs
import sys
import re
import click
from selenium import webdriver
from curitools.status import SubStatus
from curitools.settings import Settings
from curitools.pages import LoginPage, SubPage

@click.command()
@click.option('-s', default=1, help='Submeter um problema')
@click.option('-r', is_flag=True, help='Imprimir tabela de submissoes')
@click.option('--driver', default="phantom",type=click.Choice(['phantom', 'chrome']) , help='driver to use')
def uri(s, r, driver):
    """Simple program that greets NAME for a total of COUNT times."""
    
    settings = Settings() 
    user, password = settings.get_settings()
    print(user)
    print(password)
    print(s)
    if r:
        status(user, password, driver)
    elif s:
        submit_problem(user,password, s, driver)

        
def submit_problem(user, password, problem, driver):
    driver = create_driver(driver)
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

def create_driver(type_driver="phantom"):
    uritools_dir = os.path.dirname(os.path.realpath(__file__))
    if "phantom" in type_driver:
        drive_path = os.path.join(uritools_dir,"phantomjs")
        driver = webdriver.PhantomJS(drive_path)
    else:
        chrome_path = os.path.join(uritools_dir, "chromedriver")
        driver = webdriver.Chrome(chrome_path)
    #print(chrome_path,chrome_dir, os.path.realpath(__file__))
    driver.maximize_window()
    return driver

def status(user, password, driver):
    driver = create_driver(driver)
    l = LoginPage(driver, user, password)
    if l.login():
        driver.get("https://www.urionlinejudge.com.br/judge/pt/runs")
        sub = SubStatus(driver.page_source)
        sub.print_table()
    else:
        print("Deu errado")
    driver.quit()

if __name__ == "__main__":
    uri()
