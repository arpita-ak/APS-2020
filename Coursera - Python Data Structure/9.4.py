
"""
9.4 Write a program to read through the mbox-short.txt 
and figure out who has sent the greatest number of mail 
messages. The program looks for 'From ' lines and takes 
the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's 
mail address to a count of the number of times they appear in the 
file. After the dictionary is produced, the program reads 
through the dictionary using a maximum loop to find the most
 prolific committer.
 
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("No such file found!")
    quit()
sender=dict()
for line in handle:
    line=line.strip().split()
    if len(line)>0 and line[0]=='From':
        #print(line[1])
        u=line[1]
        sender[u]=sender.get(u,0)+1
#print(sender)
maxkey=None
maxval=None
for key,value in sender.items():
    if maxval==None or value>maxval:
        maxval=value
        maxkey=key
print(maxkey,maxval)

"""
Desired Output:cwen@iupui.edu 5
"""