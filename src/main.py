# Created by Kieran Gainer (github.com/krgainer)
import webbrowser
import tkinter as tk
import os
import subprocess
import sys
import platform
from tkinter import *
import csv
# from win32com.client import Dispatch

userPlatform = platform.system()
slash = "\\" if userPlatform == "Windows" else "/"

def main():
	global master
	master = Tk()
	master.tk.call("source", "sun-valley.tcl")
	master.tk.call("set_theme", "dark")
	# screen_width = master.winfo_screenwidth()
	# screen_height = master.winfo_screenheight()
	master.geometry("280x500")
	master.title("PSD Bulk Actioner")
	master.iconbitmap("icon.ico")
	PSDFileEntry = ttk.Entry(master, textvariable="")
	PSDFileEntry.pack()

def read_CSV(File):
	with open(File, 'r') as file:
		csv_file = csv.DictReader(file)
	for row in csv_file:
		print(dict(row))

def open_file(filename):
	if userPlatform == "Windows":
		try:
			os.startfile(filename)
		except BaseException:
			messagebox.showwarning(title="😬", message="File or folder does not exist!")
	else:
		# Unix open subprocess throws a non-BaseException error, that I don't particularly care to implement a
		# popup for. Edge case, it still works, and most people don't use unix so idgaf.
		opener = "open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call([opener, filename])

main()
