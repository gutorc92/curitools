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
        #print(response.status_code)
        if response.status_code == req.codes.ok:
            page = BeautifulSoup(response.content, "html.parser")
            return page
        else:
            response.raise_for_status()

    def get_session(self):
        return self.session

    def run(self):
        pass

    def find_forms_fields(self, page):
        #print("Forming")
        form_html = page.find("form")
        inputs = form_html.findAll("input", {"type":"hidden"})
        form = {}
        for inp in inputs:
            name = inp["name"] 
            value = inp["value"]
            #print(inp["name"], inp["value"])
            form[name] = value
        #print(form)
        return(form)

class SubmissionPage(BasePage):
    
    def __init__(self, session = None, problem = None, file_path=None, language = None):
        super(SubmissionPage, self).__init__(session, "https://www.urionlinejudge.com.br/judge/pt/runs/add")
        self.problem = problem 
        self.file_path = file_path if file_path is not None else self.get_file_path()
        self.language = 2 if language is None else language
        #print(self.file_path)
    
    def read_file(self):
        text = ""
        with open(self.file_path, "r") as handle:
            text = handle.read()
        #text = [line.replace("\n","\\n") for line in text ]
        #text = [line.replace("\"","\\\"") for line in text ]
        return text

    def get_file_path(self):
        files = os.listdir(os.getcwd())
        files = [ x for x in files if x.startswith(str(self.problem))]
        #r = re.compile("^" + str(self.problem))
        #files = filter(r.match, files)
        #print(files)
        #print(type(files))
        if len(files) == 1:
            return os.path.join(os.getcwd(),files[0] ) 

    def run(self):
        text = self.read_file()
        #print(text)
        page = self.get_page()
        form = self.find_forms_fields(page)
        form["problem_id"] = self.problem
        form["language_id"] = self.language
        form["source_code"] = text 
        #print("form final: ")
        #print(form)
        response = self.session.post(self.url, data=form)
        #print(response)
        if response.status_code == req.codes.ok:
            return True
        else:
            return False
        
 

class LoginPage(BasePage):
    
    def __init__(self,session = None, user = None,  password=None):
        super(LoginPage, self).__init__(session, "https://www.urionlinejudge.com.br/judge/en/login")
        if user is None and password is None:
            settings = Settings()
            user, password = settings.get_settings()
    
        self.user = user
        self.password = password 

    def run(self):
        #print("Running login")
        page = self.get_page()
        #print("Getting page")
        form = self.find_forms_fields(page)
        #print("Getting form")
        form["email"] = self.user
        form["password"] = self.password
        #print(form)
        response = self.session.post(self.url, data=form)
        #print(response)
        
class TabelaSubmissionPage(BasePage):
    
    def __init__(self,session = None):
        #print(session)
        super(TabelaSubmissionPage, self).__init__(session, "https://www.urionlinejudge.com.br/judge/pt/runs")

    def run(self):
        try:
            response_final = self.session.get(self.url) 
        except:
            return 1
        if response_final.status_code == req.codes.ok:
            status = SubmissionStatusOutput(response_final.content)
            status.print_table()
        else:
            return 1
        
