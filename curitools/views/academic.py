#!/usr/local/bin/python3.5
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import re
import sys
import os
from curitools.views.base_view import BaseView

class AcademicView(BaseView):
    
    def __init__(self, page):
        super(AcademicView, self).__init__(page)

    def get_name(self, element):
        name_element = element.find("h3")
        return name_element.getText() if name_element is not None else None

    def get_professor(self, element):
        prof_element = element.find("p", {"class": "discipline-professor"})
        return prof_element.getText() if prof_element is not None else None

    def extract_table(self):
        cont = self.content("ul", "groups")
        list_html = cont.findAll("li")
        self.data = []
        for e in list_html:
            name = self.get_name(e)
            prof = self.get_professor(e)
            if name is not None and prof is not None:
                self.data.append([name, prof])


class ListView(BaseView):
    def __init__(self, page):
        super(ListView, self).__init__(page)


    def extract_table(self):
        cont = self.content("div", "element")
        self.table  = cont.find("table")
        self.extract_html_table()


  



