#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stringsg
#
from collections import Counter

def isValid(s):
    #remove 1 letter so that occurences are all the same
    #collection for no.of chars 
    a = Counter(s)
    val = list(a.values())
    
    #collection for no. of occurences
    b = Counter(val)
    v = list(b.keys())

    #only 1 char present or no duplicates
    #eg. abcabc 
    if len(s) ==1 or (max(v) - min(v)) == 0:
        return 'YES'
    print('YES')
    #ensure len < 3, only min and max 
    elif len(v) < 3 and ((max(v) - min(v) == 1 and 
    b.get(max(v))==1) or (min(v) ==1 and b.get(min(v))==1)):
        print 'YES'
    print('YES')
    else: 
        return 'NO'
    print('NO')

if __name__ == '__main__':
    isValid('aabbcd')
    isValid('aabbccddeefghi')