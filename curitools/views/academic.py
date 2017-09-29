#!/usr/local/bin/python3.5
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os


class AcademicView(object):
    
    def __init__(self, page):
        self.page = page

    def content(self):
        soup = BeautifulSoup(self.page, 'html.parser')
        self.content_html = soup.find("ul", {"id": "groups"})
        return self.content_html
        
    def get_name(self, element):
        name_element = element.find("h3")
        return name_element.getText() if name_element is not None else None

    def get_professor(self, element):
        prof_element = element.find("p", {"class": "discipline-professor"})
        return prof_element.getText() if prof_element is not None else None

    def extract_table(self):
        cont = self.content()
        list_html = cont.findAll("li")
        self.data = []
        for e in list_html:
            name = self.get_name(e)
            prof = self.get_professor(e)
            if name is not None and prof is not None:
                self.data.append([name, prof])

    def get_max_length(self):
        max_column = []
        for lines in self.data:
            for i in range(0, len(lines)):
                try:
                    if max_column[i] < len(lines[i]):
                        max_column[i] = len(lines[i])
                except IndexError:
                    max_column.insert(i,len(lines[i]))
        self.max_column = max_column

    def print_table(self):
        self.extract_table()
        self.get_max_length()
        for lines in self.data:
            for i in range(0, len(lines)):
                text = "{0:{width}}".format(lines[i], width = self.max_column[i])
                print(text,'|', end=" ", flush=True)
            print("")


  



