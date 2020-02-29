'''
Imagine there is a file full of Facebook comments by various users and you are provided a set of words that signify 
profanity(a swear word/ Profanity is an act that shows disrespect for a religion). 
Write a program which can indicate the degree of profanity for each sentence in the file? Write in any programming language of 
your choice - mention any assumptions, but remember to state them.
'''

import re
import pandas as pd
import numpy as np

list_of_profanity = ['Fuck','Fuck you','bitch','Son of a bitch','Shit','Piss off','Dick head','Asshole','Bastard','damn']
comments = ['sam go fuck your self you fucking asshole bitch son of a bitch','sam go fuck your self you fucking Bastard','what a lovely day']#,'what a lovely day'
number_of_profanity_words = len(list_of_profanity)


df= pd.DataFrame({'comments':comments,'degree of profanity':0})

'''
---------------
Variables Used:
---------------
        list_of_profanity:  set words that signify profanity
        comments :three sample comments
        number_of_profanity_words:  total number of profinity words
        df : dataframe having result as 'degree of profanity' column, also with comments column.
        
'''
        



def pro(comment):
    '''
    Variable 'count' will count the number of profanity words persent in a comment , including repetative profanity words
        
    '''
    count=0
    for i in range(len(list_of_profanity)):
        count = count+len(re.findall(list_of_profanity[i].lower(),comment.lower())) # counting all profanity words
    
    '''
     profanity words 'f*ck' and 'f*ck you' both have 'f*ck' hence count will count it as 3 profanity words, 2 for 'f*ck' 1 for 'f*ck you' 
     so we will will substract extra 'f*ck' count which is equal to number of 'f*ck you'.
    '''
        
    count = count - len(re.findall(list_of_profanity[1].lower(),comment.lower())) 

    # same goes with 'bitch' and 'Son of a bitch'
    count = count - len(re.findall(list_of_profanity[3].lower(),comment.lower()))
    
    return count/number_of_profanity_words 
'''
degree of profanity = (number of profanity words in a comment)/(total number of profanity words)
'''



#df['degree of profanity'] = df.comments.apply(pro) # pandas apply function takes much lesser time than usual for loop 

print(df) # solution





 