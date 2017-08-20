#!/usr/local/bin/python3.5

import os
import time
import codecs
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re

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
        files = os.listdir(os.getcwd())
        files = [ x for x in files if x.startswith(str(self.problem))]
        #r = re.compile("^" + str(self.problem))
        #files = filter(r.match, files)
        print(files)
        print(type(files))
        if len(files) == 1:
            return os.path.join(os.getcwd(),files[0] ) 
   
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

        

