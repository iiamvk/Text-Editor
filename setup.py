import cx_Freeze
import sys
import os 
base = None


"""
    Creator =  vinod kumar
    Email = iiamvinod@gmail.com
    Date = 29/07/2019 10:35

"""

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\vk\AppData\Local\Programs\Python\Python36\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\vk\AppData\Local\Programs\Python\Python36\tcl\tk8.6"

executables = [cx_Freeze.Executable("Text Editor.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Hello This Is My First Tkinter Application, This is a simple Text Editor.",
    executables = executables
    )
