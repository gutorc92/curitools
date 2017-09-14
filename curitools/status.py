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
       
    def print_table(self):
        for lines in self.table:
            for column in lines:
                print(column,'|', end=" ", flush=True)
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
                #print(self.format_result(l.getText().replace("\n","").strip()),'|', end=" ", flush=True)
            #print("")
            lines.append(line_list)
        self.table = lines
        
  
if __name__ == "__main__":
    main()           



