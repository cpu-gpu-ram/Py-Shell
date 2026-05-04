import sys
import os
import subprocess
import platform
import getpass
import pathlib
import shutil
import datetime
import time

print("Welcome to my python based shell translator!" \
"\nThis program will translate your shell commands into python code." \
    "\nType 'exit' to quit the program.")
def list_files():
    files = os.listdir('.')
    for file in files:
        print(file)
def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {path}")
    except FileNotFoundError:
        print(f"Directory {path} not found.")
def make_directory(path):
    try:
        os.mkdir(path)
        print(f"Directory {path} created.")
    except FileExistsError:
        print(f"Directory {path} already exists.")
def remove_directory(path):
    try:
        os.rmdir(path)
        print(f"Directory {path} removed.")
    except FileNotFoundError:
        print(f"Directory {path} not found.")
    except OSError:
        print(f"Directory {path} is not empty.")
def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"File {src} copied to {dst}.")
    except shutil.Error:
        print(f"Failed to copy {src} to {dst}.")
def move_file(src, dst):
    try:
        shutil.move(src, dst)
        print(f"File {src} moved to {dst}.")
    except shutil.Error:
        print(f"Failed to move {src} to {dst}.")
def remove_file(path):
    try:
        os.remove(path)
        print(f"File {path} removed.")
    except FileNotFoundError:
        print(f"File {path} not found.")
def list_programs():
    programs = os.listdir('/usr/bin')
    for program in programs:
        print(program)
def yes():
    usr_input = input()
    while True:
        print(usr_input)
def where_am_i():
    print(f"Current working directory: {os.getcwd()}")
def who_am_i():
    print(f"User: {os.getlogin()}")
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
def show_file_tree():
    for root, dirs, files in os.walk('.'):
        level = root.replace(os.getcwd(), '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")
def show_disk_usage():
    total, used, free = shutil.disk_usage('.')
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")
def search_files(keyword):
    found = False
    for root, dirs, files in os.walk('.'):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))
                found = True
    if not found:
        print(f"No files found matching '{keyword}'.")
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
def log_history():
    print(history)
def peek(file_name):
    try:
        print(open(file_name).read())
    except FileNotFoundError:
        print(f"File {file_name} not found.")
def current_date_time():
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
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

history = []

print("Enter a shell command: ")
while True:
    command = input()
    command = command.lower()
    history.append(command)
    if command == 'exit':
        print("Exiting the program. Goodbye!")
        break
    elif command == 'ls' or command == 'list files' or command == 'list all files' or command == 'files' or command == 'current files':
        list_files()
    elif command == 'cd' or command == 'change directory' or command == 'change dir' or command == 'cd to' or command == 'change to' or command == 'go to' or command == 'go to directory' or command == 'go to dir' or command == 'go to folder' or command == 'change folder':
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
    elif command == 'clear' or command == 'clear screen' or command == 'cls' or command == 'clear console' or command == 'clear terminal' or command == 'blank':
        clear_screen()
    elif command == 'tree' or command == 'show file tree' or command == 'file tree' or command == 'directory tree' or command == 'dir tree' or command == 'folder tree':
        show_file_tree()
    elif command == 'disk usage' or command == 'show disk usage' or command == 'disk space' or command == 'show disk space' or command == 'df':
        show_disk_usage()
    elif command == 'search' or command == 'search files' or command == 'find files' or command == 'find file' or command == 'search file':
        keyword = input("Enter the keyword to search for: ")
        search_files(keyword)
    elif command == 'fetch' or command == 'fakefetch' or command == 'fake fast fetch' or command == 'fastfetch' or command == 'sysinfo' or command == 'system info' or command == 'system information' or command == 'fff':
        fakefastfetch()
    elif command == 'history' or command == 'log history' or command == 'show history' or command == 'command history' or command == 'history log' or command == 'log':
        log_history()
    elif command == 'peek' or command == 'peek file' or command == 'show file' or command == 'cat' or command == 'type' or command == 'read' or command == 'read file' or command == 'show contents' or command == 'show file contents' or command == 'show contents of file':
        file_name = input("Enter the file name: ")
        peek(file_name)
    elif command == 'date' or command == 'time' or command == 'current date and time' or command == 'current time' or command == 'current date':
        current_date_time()
    elif command == 'file info' or command == 'file information' or command == 'show file info' or command == 'show file information' or command == 'file details' or command == 'show file details':
        file_name = input("Enter the file name: ")
        file_info(file_name)
    else:
        print("Command not recognized. Please try again.")
