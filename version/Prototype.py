import sys
import os
import subprocess
import platform


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
        subprocess.run(['cp', src, dst], check=True)
        print(f"File {src} copied to {dst}.")
    except subprocess.CalledProcessError:
        print(f"Failed to copy {src} to {dst}.")
def move_file(src, dst):
    try:
        subprocess.run(['mv', src, dst], check=True)
        print(f"File {src} moved to {dst}.")
    except subprocess.CalledProcessError:
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
def system_info():
    print(f"Platform: {sys.platform}")
    print(f"Python version: {sys.version}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"User: {os.getlogin()}")
    print(f"Os: {platform.system()} {platform.release()}")

print("Enter a shell command: ")
while True:
    command = input()
    command = command.lower()
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
    elif command == 'sysinfo' or command == 'system info':
        system_info()
    elif command == 'programs' or command == 'list programs' or command == 'list all programs' or command == 'available programs' or command == 'installed programs':
        list_programs()
    elif command == 'yes' or command == 'repeat' or command == 'echo' or command == 'print':
        yes()
    else:
        print("Command not recognized. Please try again.")
