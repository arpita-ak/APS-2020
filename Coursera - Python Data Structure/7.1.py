
"""
7.1 Write a program that prompts for a file name, 
then opens that file and reads through the file, 
and print the contents of the file in upper case. 
Use the file 'words.txt' to produce the output below.

"""

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File Not Found : ",fname)
    quit()
    
for i in fh:
    i=i.strip()
    print(i.upper())