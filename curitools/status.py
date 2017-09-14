#!/usr/local/bin/python3.5
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os
import subprocess
from clint.textui import colored


class SubmissionStatusOutput(object):
    
    def __init__(self, page):
        self.page = page

    def separar_quadro(self):
        soup = BeautifulSoup(self.page, 'html.parser')
        r = soup.find("div", {"id": "element"})
        self.table = r.find("table")
        

    def format_result(self, text):
        if "Accepted" in text:
            text = colored.green(text)
        elif "Wrong" in text:
            text = colored.red(text)
        elif "Compilation" in text:
            text = colored.yellow(text)
        return text
       
    def format_table(self):
        for lines in self.table:
            if len(lines) == 7:
                lines.pop(0)
        
    def get_max_length(self):
        max_column = []
        for lines in self.table:
            for i in range(0, len(lines)):
                try:
                    if max_column[i] < len(lines[i]):
                        max_column[i] = len(lines[i])
                except IndexError:
                    max_column.insert(i,len(lines[i]))
        self.max_column = max_column

    def print_table(self):
        self.extract_table()
        self.format_table()
        self.get_max_length()
        for lines in self.table:
            for i in range(0, len(lines)):
                text = "{0:{width}}".format(lines[i], width = self.max_column[i])
                print(self.format_result(text),'|', end=" ", flush=True)
            print("")

    def extract_table(self):
        self.separar_quadro()
        lines = []
        for line in self.table.findAll('tr'):
            line_list = []
            for l in line.findAll('td'):
                if l.find('sup'):
                    l.find('sup').extract()
                line_list.append(l.getText().replace("\n","").strip())
            lines.append(line_list)
        self.table = lines
        
  
if __name__ == "__main__":
    main()           



