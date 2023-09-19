mystr = input()
maxWord = ''
word = ''
for i in range(len(mystr)):
    if (mystr[i]== ' '):
        if (len(word) > len(maxWord)):
            maxWord = word
        word = ''    
    else:
        word += mystr[i]
if (len(word) > len(maxWord)):
    maxWord = word        
print(maxWord)        
