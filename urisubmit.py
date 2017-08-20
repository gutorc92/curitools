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

class BasePage(object):
    
    def __init__(self, driver, url = None):
        self.driver = driver
        self.url = url

class SubPage(BasePage):
    
    def __init__(self, driver, problem, file_path=None, language = None):
        super(SubPage, self).__init__(driver, "https://www.urionlinejudge.com.br/judge/pt/runs/add")
        self.problem = problem
        self.file_path = file_path if file_path is not None else self.get_file_path()
        self.language = 1 if language is None else language
        print(self.file_path)
    
    def read_file(self):
        text = ""
        with open(self.file_path, "r") as handle:
            text = handle.readlines()
        text = [line.replace("\n","\\n") for line in text ]
        text = [line.replace("\"","\\\"") for line in text ]
        return text

    def get_file_path(self):
       return os.path.join(os.getcwd(), self.problem+".cpp") 
   
    def submit(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('problem-id').send_keys(self.problem)
        text = self.read_file()
        try:
            myElem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'editor')))
        except TimeoutException:
            print("Nao achou o editor")
        self.driver.execute_script("editor.setValue('')");
        for i in range(0,len(text)):
            script = "editor.session.insert({row:%s , column: 0}, \"%s\")" % (str(i), text[i]) 
            print(script)
            self.driver.execute_script(script);
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");
        self.driver.find_element_by_css_selector("input.send-green").click()     
        try:
            myElem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.flash-success')))
            return True
        except TimeoutException:
            return False

         
 

class LoginPage(BasePage):
    
    def __init__(self, driver, user, password):
        super(LoginPage, self).__init__(driver, "https://www.urionlinejudge.com.br")
        self.user = user;
        self.password = password
       

    def login(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('email').send_keys(self.user)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_css_selector("input.send-green").click()     
        try:
            self.driver.find_element_by_id("menu")
            return True
        except NoSuchElementException:
            return False

        
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


def main():
    user, password = read_settings()
    print(user)
    print(password)
    webdriver_download(user,password, sys.argv[1])

if __name__ == "__main__":
    uri()
