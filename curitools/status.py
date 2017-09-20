#!/usr/local/bin/python3.5
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os
import subprocess
import logging as l
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


class ProblemOutput(object):
    def __init__(self, page):
        self.page = page

    def separar_quadro(self):
        soup = BeautifulSoup(self.page, 'html.parser')
        self.content  = soup.find("iframe", {"id": "description-html"})

    def get_title(self):
        title = self.content.find("div", {"class", "header"})
        if title:
            self.title = title.find("h1").getText()
            l.debug("Title of the problem %s", str(title))
        else:
            l.debug("Title not found")

    def get_problem_div(self):
        problem_div = self.content.find("div", {"class" : "problem"})
        return problem_div

    def get_description(self):
        problem = self.get_problem_div()
        description_div = problem.find("div", {"class":"description"})
        description = description_div.find("p")
        if description:
            self.description = description.getText()
        else:
            l.debug("Description not found.")
        return description

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
                    max_column.insert(i, len(lines[i]))
        self.max_column = max_column

    def print_table(self):
        print(self.get_title())
        print(self.get_description())
    def extract_table(self):
        self.separar_quadro()
        lines = []
        for line in self.table.findAll('tr'):
            line_list = []
            for l in line.findAll('td'):
                if l.find('sup'):
                    l.find('sup').extract()
                line_list.append(l.getText().replace("\n", "").strip())
            lines.append(line_list)
        self.table = lines


if __name__ == "__main__":
    main()           



