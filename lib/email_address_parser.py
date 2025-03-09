# your code goes here!

import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string
        
    
    def parse(self):
        exp = re.compile(r'[\w\.-]+@[\w\.-]+')
        return sorted(exp.findall(self.string))