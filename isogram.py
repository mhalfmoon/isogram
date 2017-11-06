def is_isogram(string):
    strList = list(string.replace('-', '').replace(' ', '').lower())
    strSetList = list(set(strList))
    
    return(sorted(strSetList) == sorted(strList)) 
