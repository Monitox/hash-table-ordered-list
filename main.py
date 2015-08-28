'''
Created on 2 Jun 2015

@author: sl0
'''
from repository.repository import Repository
from controller.controller import Controller
from ui.console import UI
import traceback

try:
    repo = Repository("songs.txt")
    ctrl = Controller(repo)
    cons = UI(ctrl)
    
    cons.startUI()
except Exception as err:
    print(traceback.print_exc())
x=input()