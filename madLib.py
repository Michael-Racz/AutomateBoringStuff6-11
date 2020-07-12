'''
Mad Libs

Ex. User would be prompted to insert a certain adjective,
    noun, adverb or verb, depending on what is written in the text
    file. 
    Example. The ADJECTIVE panda walked down to the NOUN and then VERB.A
    nearby NOUN was unaffected by these events.
Then the program would write these inputs to the file and saved. Also output
to the screen.

'''
from pathlib import Path
import re

#Path of the file you want to scan
##TODO: REPLACE #FILENAME WITH YOUR OWN FILE PATH
madLibs = open(#FILENAME#)
text = madLibs.read()
madLibs.close()

#Finding the certain strings to replace, in this case Adj, noun, verb, adverb in all caps
finder = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

while True:
    #storing the results of a regex search
    result = finder.search(text)
    #if the search of the text results in no matches(i.e. None) end the loop
    if result == None:
        break
    
    #Get user input to replace the string
    if result.group() == 'ADJECTIVE' or result.group() == 'ADVERB':
        print('Enter an %s:' % (result.group().lower()))
    elif result.group() == 'NOUN' or result.group() == 'VERB':
        print('Enter a %s:' % (result.group().lower()))
    i = input()
    text = finder.sub(i,text,1)
print(text)
print('\n')

#Get user input for the name of the new file
print('Name your file: ')
name = input()
#TODO: REPLACE YOUR FILE NAME BELOW
newFile = open(##FILENAME## %s.txt# ' % (name), 'w')
newFile.write(text)
