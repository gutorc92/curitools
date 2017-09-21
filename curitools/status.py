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
        self.content  = soup.find("body")

    def get_title(self):
        if not hasattr(self, "content"):
            self.separar_quadro()
        title = self.content.find("div", {"class", "header"})
        if title:
            self.title = title.find("h1").getText()
            l.debug("Title of the problem %s", str(title))
        else:
            l.debug("Title not found")
        return self.title

    def get_problem_div(self):
        if not hasattr(self, "content"):
            self.separar_quadro()
        problem_div = self.content.find("div", {"class" : "problem"})
        return problem_div

    def get_description(self):
        self.description = self.get_text_div("description")
        return self.description

    def get_text_div(self, class_name):
        problem = self.get_problem_div()
        div = problem.find("div", {"class": class_name})
        div = div.find("p")
        if div:
            text = div.getText()
            text = text.replace("\n", "")
            text = text.replace("\t","")
            return text
        else:
            l.debug("Input not found for class: %s", class_name)
        return None

    def get_output(self):
        self.output_text = self.get_text_div("output")
        return self.output_text

    def get_input(self):
        self.input_text = self.get_text_div("input")
        return self.input_text

    def print_table(self):
        self.separar_quadro()
        print("Titulo", self.get_title())
        print("Description", self.get_description())
        print("Input", self.get_input())
        print("Output", self.get_output())

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



