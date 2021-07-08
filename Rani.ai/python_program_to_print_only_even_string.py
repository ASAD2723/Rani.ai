def printWords(s): 
    s = s.split(' ')  
    for words in s:
        if len(words)%2==0:
            print(words) 

s = "Hello Everyone how are you hope you doing good" 
printWords(s) 