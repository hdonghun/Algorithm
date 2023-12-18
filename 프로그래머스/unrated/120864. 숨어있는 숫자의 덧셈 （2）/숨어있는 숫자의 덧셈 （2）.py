def solution(myString):
    answer=0
    # my_string='1a2b3c4d123Z'
    for i in myString:
        if i.isdigit():
            pass
        else:
            myString=myString.replace(i,' ')
        
        
    return sum(list(map(int,myString.split())))
