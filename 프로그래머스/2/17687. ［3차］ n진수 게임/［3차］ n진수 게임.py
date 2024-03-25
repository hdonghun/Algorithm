def convert(num,n) :
    numOver = {10:"A", 11:"B", 12:"C",13:"D",14:"E",15:"F"}
    s = ""
    if ( num == 0) :
        return "0"
    
    while ( num ) :
        if (num % n >= 10 ) :
            s = s + numOver[num%n]
        else :
            s = s +  str(num%n)
        num //= n
    return s[::-1]
    

def solution(n, t, m, p):
    answer = ''
    s = ""
    for i in range(t * m):
        s += convert(i,n)

    i = p-1
    while (i < len(s) ) :
        if (len(answer) == t):
            break
        
        answer += s[i]
        i += m
    
    return answer