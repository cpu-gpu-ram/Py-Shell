#import all needed base packages. 


import sys
import os
import subprocess
import platform
import getpass
import pathlib
import shutil
import time
import datetime
import zipfile

#you like the assci art i used a text to art converter.
print(r"""
  ____             ____  _          _ _
 |  _ \ _   _     / ___|| |__   ___| | |
 | |_) | | | |____\___ \| '_ \ / _ \ | |
 |  __/| |_| |_____|__) | | | |  __/ | |
 |_|    \__, |    |____/|_| |_|\___|_|_|
        |____|
V2.0

""")
#greets the user
programs_list = []
print(f"Welcome to Py-Shell! , {getpass.getuser()}" \
"\nThis program will translate your commands into shell/bash." \
    "\nType 'exit' to quit the program.")

#list all files in the directory 
def list_files():
    files = os.listdir('.')
    for file in files:
        print(file)

#changes the directory (needs to be updated) for one line cmd with out losing compatablity for thee old way 

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {path}")
    except FileNotFoundError:
        print(f"Directory {path} not found.")

#makes new directory needs to be updated for one line cmd

def make_directory(path):
    try:
        os.mkdir(path)
        print(f"Directory {path} created.")
    except FileExistsError:
        print(f"Directory {path} already exists.")

#deletes an empty directory need to update so it can delete a full directory in one cmd

def remove_directory(path):
    try:
        os.rmdir(path)
        print(f"Directory {path} removed.")
    except FileNotFoundError:
        print(f"Directory {path} not found.")
    except OSError:
        print(f"Directory {path} is not empty.")

#copies file need to update for one cmd to copy

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"File {src} copied to {dst}.")
    except shutil.Error:
        print(f"Failed to copy {src} to {dst}.")

#moves file need to update for one cmd to copy

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        print(f"File {src} moved to {dst}.")
    except shutil.Error:
        print(f"Failed to move {src} to {dst}.")

#removes file need to update for one cmd to copy

def remove_file(path):
    try:
        os.remove(path)
        print(f"File {path} removed.")
    except FileNotFoundError:
        print(f"File {path} not found.")

#repeats the users input until crash

def yes():
    usr_input = input()
    while True:
        print(usr_input)

#output current users directory

def where_am_i():
    print(f"Current working directory: {os.getcwd()}")

#outputs uername

def who_am_i():
    print(f"User: {os.getlogin()}")

#clears terminal

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

#outputs current user directorys file tree

def show_file_tree():
    for root, dirs, files in os.walk('.'):
        level = root.replace(os.getcwd(), '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

#Shows disk space

def show_disk_usage():
   if shutil.disk_usage('.'):
        total, used, free = shutil.disk_usage('.')
        print(f"Total: {total // (2**30)} GB")
        print(f"Used: {used // (2**30)} GB")
        print(f"Free: {free // (2**30)} GB")

#search current directory for keyword

def search_files(keyword):
    found = False
    for root, dirs, files in os.walk('.'):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))
                found = True
    if not found:
        print(f"No files found matching '{keyword}'.")

#fetchs system info

def fakefastfetch():
    print("Fetching data...")
    time.sleep(2)
    print("Data fetched successfully!")
    print(platform.platform())
    print(f"Python version: {platform.python_version()}")
    print(f"User: {getpass.getuser()}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"System architecture: {platform.architecture()[0]}")
    print(f"Processor: {platform.processor()}")
    print(f"Machine: {platform.machine()}")
    print(f"Node: {platform.node()}")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(';)')

#command history

def log_history():
    print(history)

#reads out files

def peek(file_name):
    try: 
        print(open(file_name).read())
    except FileNotFoundError:
        print(f"File {file_name} not found.")

#get system date and time


def current_date_time():
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")

#Shows basic info about a file

def file_info(file_name):
    try:
        file_path = pathlib.Path(file_name)
        print(f"File name: {file_path.name}")
        sizeinbytes = file_path.stat().st_size
        if sizeinbytes < 2**10:
            print(f"File size: {sizeinbytes} bytes")
        elif sizeinbytes < 2**20:
            print(f"File size: {sizeinbytes // 2**10} KB")
        elif sizeinbytes < 2**30:
            print(f"File size: {sizeinbytes // 2**20} MB")
        else:
            print(f"File size: {sizeinbytes // 2**30} GB")  
        print(f"File created: {datetime.datetime.fromtimestamp(file_path.stat().st_ctime)}")
        print(f"File modified: {datetime.datetime.fromtimestamp(file_path.stat().st_mtime)}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

#Should print all commands

def help():
	print("""
	Listing all commands:
	ls
	mkdir
	cd
	rmdir
	cp
	mv
	rm
	programs
	check to wiki for more.""")

#checks if a site/ip is up

def Ping(ipdomain):
    print('-'*60)
    if not ipdomain or ' ' in ipdomain or '.' not in ipdomain:
        print ('INVALID INPUT TRY AGIAN.')
        print('-'*60)
        return1 = False
    else:
        return1 = True
        if not sys.platform.startswith('win'):
            flag = '-c'
        else:
            flag = '-n'
        pingcommand =  ['ping' , flag, '1', ipdomain]
        result = subprocess.run(pingcommand, capture_output=True, text=True)
        if return1 == True:
            print (result.stdout)
        else:
            print ('cant reach')

#my alternative to the up arrow on windows

def recall():
	last_item = history[-2]
	print (last_item)

#zips a file

def zipfunc():
    zip_name = input('Enter zip file name (include .zip): ')
    zip_dir = input('Enter folder to zip: ')
    with zipfile.ZipFile(zip_name, 'w') as z:
        for root, dirs, files in os.walk(zip_dir):
            for file in files:
                z.write(os.path.join(root, file))
    print(f"Zipped {zip_dir} into {zip_name}.")

#unzips a file

def unzipfunc():
    zip_name = input('Enter zip file name to extract: ')
    extract_dir = input('Enter folder to extract to: ')
    with zipfile.ZipFile(zip_name, 'r') as contents:
        contents.extractall(extract_dir)
    print(f"Extracted {zip_name} to {extract_dir}.")

#List every exe found in usr/bin and for windows The program folder

def list_programs():
    programs = []

    paths = os.environ['PATH'].split(os.pathsep)
    for path in paths:
        try:
            for file in os.listdir(path):
                programs.append(file)
        except PermissionError:
            pass
        except FileNotFoundError:
            pass
    programs = sorted(set(programs))
    for i, program in enumerate(programs, 1):
        print(f"{i}. {program}")
        if i % 10 == 0:
            input("--- press enter for more ---")
    return programs

#run anyone of the previous noted files/programs


def run_program(programs):
    try:
        number = int(input("Enter program number: "))
        program = programs[number - 1]
        subprocess.run([program])
    except IndexError:
        print("Invalid number.")
    except FileNotFoundError:
        print(f"Could not run that program.")
    except ValueError:
        print("Enter a number.")

#My second project ever basic two digit calc

def calc():
	A = int(input('1st number = '))
	B = int(input('2nd number = '))
	op = input('operation + - * / = ')
	if op == '+':
		ans = (A + B)
		print (f'Answer is {ans}')
	elif op == '-':
		ans = (A - B)
		print (f'Answer is {ans}')
	elif op == '/': 
		ans = (A / B)
		print (f'Answer is {ans}')
	elif op == '*': 
		ans = (A * B)
		print (f'Answer is {ans}')
	else:
		print ('invalid input')
	


#defines all previous commands
history = []

#Main loop
while True:
    
    print (os.getcwd())
    command = input(f"{getpass.getuser()}@{platform.node()} - ")
    command = command.lower()
    history.append(command)

    if command == 'exit':
        print("Exiting the program. Goodbye!")
        break


    elif command == 'ls' or command == 'list files' or command == 'list all files' or command == 'files' or command == 'current files':
        list_files()


    elif command == 'cd' or command == 'change directory' or command == 'change dir' or command == 'cd to' or command == 'change to' or command == 'go to' or command == 'go to directory' or command == 'go to dir' or command == 'go to folder' or command == 'change folder' :
        path = input("Enter the directory path: ")
        change_directory(path)


    elif command == 'mkdir' or command == 'make directory' or command == 'create directory' or command == 'make dir' or command == 'create dir' or command == 'new directory' or command == 'new dir' or command == 'new folder' or command == 'create folder' or command == 'make folder':
        path = input("Enter the directory path: ")
        make_directory(path)


    elif command == 'rmdir' or command == 'remove directory' or command == 'delete directory' or command == 'remove dir' or command == 'delete dir' or command == 'delete folder' or command == 'remove folder':
        path = input("Enter the directory path: ")
        remove_directory(path)


    elif command == 'cp' or command == 'copy file' or command == 'copy' or command == 'duplicate file' or command == 'duplicate':
        src = input("Enter the source file path: ")
        dst = input("Enter the destination file path: ")
        copy_file(src, dst)


    elif command == 'mv' or command == 'move file' or command == 'move' or command == 'rename file' or command == 'rename' or command == 'move to' or command == 'move file to' or command == 'move to directory' or command == 'move to dir' or command == 'move to folder' or command == 'transfer file' or command == 'transfer':
        src = input("Enter the source file path: ")
        dst = input("Enter the destination file path: ")
        move_file(src, dst)


    elif command == 'rm' or command == 'remove file' or command == 'delete file' or command == 'delete':
        path = input("Enter the file path: ")
        remove_file(path)


    elif command == 'programs' or command == 'list programs' or command == 'list all programs' or command == 'available programs' or command == 'installed programs':
        list_programs()


    elif command == 'yes' or command == 'repeat' or command == 'echo' or command == 'print':
        yes()


    elif command == 'pwd' or command == 'where am i' or command == 'current directory' or command == 'current dir' or command == 'current folder':
        where_am_i()


    elif command == 'whoami' or command == 'who am i' or command == 'current user' or command == 'user':
        who_am_i()


    elif command == 'clear' or command == 'clear screen' or command == 'cls'or command == 'clear console' or command == 'clear terminal'or command == 'blank':
        clear_screen()


    elif command == 'tree' or command == 'show file tree' or command == 'file tree' or command == 'directory tree' or command == 'dir tree' or command == 'folder tree':
        show_file_tree()


    elif command == 'disk usage' or command == 'show disk usage' or command == 'disk space' or command == 'show disk space' or command == 'df':
        show_disk_usage()


    elif command == 'search' or command == 'search files' or command == 'find files' or command == 'find file' or command == 'search file':
        keyword = input("Enter the keyword to search for: ")
        search_files(keyword)


    elif command == 'fetch' or command == 'fakefetch' or command == 'fake fast fetch' or command == 'fastfetch' or command == 'sysinfo' or command == 'system info' or command == 'system information'or command == 'fff':
        fakefastfetch()


    elif command == 'history' or command == 'log history' or command == 'show history' or command == 'command history' or command == 'history log'or command == 'log':
        log_history()


    elif command == 'peek' or command == 'peek file' or command == 'show file' or command == 'cat' or command == 'type' or command == 'read' or command == 'read file' or command == 'show contents' or command == 'show file contents' or command == 'show contents of file':
        file_name = input("Enter the file name: ")
        peek(file_name)


    elif command == 'date' or command == 'time' or command == 'current date and time' or command == 'current time' or command == 'current date':
        current_date_time()


    elif command == 'file info' or command == 'file information' or command == 'show file info' or command == 'show file information' or command == 'file details' or command == 'show file details':
        file_name = input("Enter the file name: ")
        file_info(file_name)


    elif command == 'help' or command == 'save me please' or command == 'remind me':
        help()


    elif command == 'ping' or command == 'connect':
        ipdomain = input('enter ip/domain ')
        Ping(ipdomain)
        print('-'*60)


    elif command == 'disk' or command == 'space':
        show_disk_usage()



    elif command == '!!' or command == 'last command':
        recall()


    elif command == 'zip' or command == 'archive':
        zipfunc()


    elif command == 'unzip' or command == 'unarchive':
        unzipfunc()


    elif command == 'programs' or command == 'list programs':
        program_list = list_programs()


    elif command == 'run' or command == 'run program':
        run_program(program_list)
        program_list = list_programs()


    elif command == 'calc':
        calc()

    else:
        print("Command not recognized. Please try again.")
