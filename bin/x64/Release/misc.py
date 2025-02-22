# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:01:09 2017

@author: Frank
"""
import os,sys

def remove_all_files_with_certain_extension(dirpath,extension=".docx"):
    for filename in [ filename for filename in os.listdir(dirpath) if filename.endswith(extension)]:
        os.remove(os.path.join(dirpath, filename))

import glob

def remove_all_files_with_certain_pattern(dirpath,pattern="*.*"):
    for filepath in glob.glob(os.path.join(dirpath, pattern)):
        os.remove(filepath)

#import shutil
        
def mkdir(dirpath):
    if os.path.exists(dirpath):
        remove_all_files_with_certain_pattern(dirpath)
        #shutil.rmtree(dirpath)
        #os.mkdir(dirpath)
    else:
        os.mkdir(dirpath)

import webbrowser
import platform

def open_chrome(filepath):
    for case in switch(platform.system()):
        if case('Windows'):
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"#'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            break
        if case('MacOS'):
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            break
        if case('Linux'):
            chrome_path = '/usr/bin/google-chrome %s'
            break
    print(chrome_path,filepath)
    webbrowser.get(chrome_path).open(filepath)#("http://bing.com")

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
    
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False