#!/usr/bin/python3
#menuadv.py
import os, fnmatch, re, sys
from subprocess import call
            
# call("find .  | egrep -i 'pdf$' | egrep -i nginx > /tmp/jjj.txt", shell=True)

# line = subprocess.check_call(["/Users/pmeharg/bin/book-search", "GIT"])
# print ("line =",line)
# SCRIPT_DIR="." #Use current directory
# SCRIPT_NAME=os.path.basename(__file__)
#relevant_path = "/Users/pmeharg/Dropbox/books"
#included_extentions = ['pdf', 'PDF']
#file_names = [ fn for fn in os.listdir(relevant_path)
#               if any(fn.endswith(ext) for ext in included_extentions) ]

# todo: take an argument from the command line for the pattern
# Define expected arguments.
PATTERN=1
ARG_LENGTH=2

pattern = sys.argv[PATTERN]
print("pattern = %s"%(pattern))

# todo: 
topdir = "/Users/pmeharg/Dropbox/books"
books=[]
exten = '.pdf'
item_num=1

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            if name.lower().count(pattern):
                file=(os.path.join(dirpath,name))
                # print("file = %s"%(file))
                print("%s:%s"%(item_num,file))
                item_num+=1
                books.append(file)

running = True
while (running):
    print("Enter book number to open: 1-%d (x to exit)" % (len(books)))
    
    book_item = input()
    try:
        book_number = int(book_item)
        if len(books) >= book_number > 0:
            print("Opening book number:" + book_item)
            commands = ["open", books[book_number-1]]
            print (commands)
            call(commands)
            running = False
    except ValueError:
            # Otherwise, ignore invalid input
            if run_item == "x":
                running = False
                print("Exit")
#End
# print(books)            
# print ("path=",path)
# print ("file names = ", file_names)
