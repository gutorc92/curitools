#!/usr/local/bin/python3.5
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os
import subprocess
from clint.textui import colored

def read_input(file_name):
    fn = open(file_name, 'r')
    text = fn.read()
    fn.close()
    return text

class SubStatus(object):
    
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
        self.separar_quadro()
        for line in self.table.findAll('tr'):
            for l in line.findAll('td'):
                if l.find('sup'):
                    l.find('sup').extract()
                print(self.format_result(l.getText().replace("\n","").strip()),'|', end=" ", flush=True)
            print("")
        
def main():
    text = read_input("/home/gustavo/Documents/uritools/test/tabelasubmissoes.html")
    s = SubStatus(text)
    s.print_table()
    
if __name__ == "__main__":
    main()           



