import os
import subprocess
import win32api
from win32com.client import Dispatch

# Different ways to open/launch/start things in Windows without having to type 'open'

def cmd_test1(ensoapi):
    subprocess.call(["notepad", "\\dev\\enso-portable\\enso\\docs\\enso-docs.txt"])

def cmd_test2(ensoapi):
    subprocess.call(["notepad", r"\dev\enso-portable\enso\docs\enso-docs.txt"])

def cmd_test3(ensoapi):
    os.startfile("\dev\enso-portable\enso\docs\enso-docs.txt")

def cmd_test4(ensoapi):
    win32api.WinExec("notepad \dev\enso-portable\enso\docs\enso-docs.txt")

def cmd_test5(ensoapi):
    xl = Dispatch('Excel.Application')
    wb = xl.Workbooks.Open('\dev\enso-portable\enso\docs\enso-docs.txt')
    xl.Visible = True

