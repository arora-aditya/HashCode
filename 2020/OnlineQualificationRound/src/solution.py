import os
import pickle
from typing import List, Dict

class Solution:
    def __init__(self, directory_name: str = 'oof', filename: str = '', libraries: List = []):
        self.directory_name = directory_name
        self.filename = filename
        self.libraries = libraries
    
    def to_file(self):
        # print(file.global_tags)
        try:
            os.mkdir(self.directory_name)
        except OSError:
            # Dir already exists
            pass
        
        # with open(f'{self.directory_name}/{self.filename}.pickle', 'w+') as file: 
        #     pickle.dump(self, file)
        le = len(self.libraries)
        ret_val = ""
        for lib in self.libraries:
            st = lib.to_file()
            if st == "":
                le -= 1
            ret_val += st
        
        with open(f'{self.directory_name}/{self.filename}.txt', 'w+') as file:
            file.write(f"{le}\n{ret_val}")
        
        
        
    
    