#!/usr/local/bin/python3.5

import os
import time
import codecs
import sys
import re
import requests
from bs4 import BeautifulSoup
import requests as req
from curitools.settings import Settings
from curitools.status import SubmissionStatusOutput

class BasePage(object):
    
    def __init__(self, session = None, url = None):
        self.session = session if session is not None else req.Session()
        self.url = url

    def get_page(self):
        response = self.session.get(self.url)
        page = BeautifulSoup(response.content, "html.parser")
        return page

    def get_session(self):
        return self.session

    def run(self):
        pass

    def find_forms_fields(page):
        form_html = page.find("form")
        inputs = form_html.findAll("input", {"type":"hidden"})
        form = {}
        for inp in inputs:
            name = inp["name"] 
            value = inp["value"]
            print(inp["name"], inp["value"])
            form[name] = value
        print(form)
        return(form)

class SubmissionPage(BasePage):
    
    def __init__(self, session = None, problem, file_path=None, language = None):
        super(SubPage, self).__init__(session, "https://www.urionlinejudge.com.br/judge/pt/runs/add")
        self.problem = problem
        self.file_path = file_path if file_path is not None else self.get_file_path()
        self.language = 2 if language is None else language
        print(self.file_path)
    
    def read_file(self):
        text = ""
        with open(self.file_path, "r") as handle:
            text = handle.readlines()
        #text = [line.replace("\n","\\n") for line in text ]
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
  
    def print_submissions(self):
    

    def run(self):
        text = self.read_file()
        page = self.get_page()
        form = self.find_forms_field(page)
        form["problem_id"] = self.problem
        form["language_id"] = self.language
        form["source_code"] = text 
        print(form)
        response = self.session.post(self.url, data=form)
        print(response)
        
 

class LoginPage(BasePage):
    
    def __init__(self,session = None, user = None,  password=None):
        super(LoginPage, self).__init__(session, "https://www.urionlinejudge.com.br/judge/en/login")
        if user is None and password is None:
            settings = Settings()
            user, password = settings.get_settings()
    
        self.user = user
        self.password = password 

    def run(self):
        page = self.get_page()
        form = self.find_forms_field(page)
        form["email"] = self.user
        form["password"] = self.password
        print(form)
        response = self.session.post(self.url, data=form)
        print(response)
        
class TabelaSubmissionPage(BasePage):
    
    def __init__(self,session = None):
        super(TabelaSubmissionPage, self).__init__(session, "https://www.urionlinejudge.com.br/judge/pt/runs")

    def run(self):
        response_final = self.session.get(self.url) 
        status = SubmissionStatusOutput(response.content)
        status.print_table()
        
