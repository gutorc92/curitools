#!/usr/local/bin/python3.5
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os


class BaseView(object):
    
    def __init__(self, page):
        self.page = page

    def content(self, main_content_type, id_content):
        soup = BeautifulSoup(self.page, 'html.parser')
        self.content_html = soup.find(main_content_type, {"id": id_content})
        return self.content_html
        

    def extract_html_table(self):
        lines = []
        for line in self.table.findAll('tr'):
            line_list = []
            for l in line.findAll('td'):
                if l.find('sup'):
                    l.find('sup').extract()
                line_list.append(l.getText().replace("\n", "").strip())
            lines.append(line_list)
        self.data = lines
    def extract_table(self):
        pass

    def get_max_length(self):
        max_column = []
        for lines in self.data:
            for i in range(0, len(lines)):
                try:
                    if max_column[i] < len(lines[i]):
                        max_column[i] = len(lines[i])
                except IndexError:
                    max_column.insert(i, len(lines[i]))
        self.max_column = max_column

    def print_table(self):
        self.extract_table()
        self.get_max_length()
        for lines in self.data:
            for i in range(0, len(lines)):
                text = "{0:{width}}".format(lines[i], width = self.max_column[i])
                print(text,'|', end=" ", flush=True)
            print("")


  



