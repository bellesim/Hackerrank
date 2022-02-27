#https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def alternatingCharacters(s):
    # Write your code here
    #iterate each letter 
    #compare letter side by side, if it matches, remove 
    #increase count
    count = 0
    for i in range(1,len(s)):
        if(s[i] == s[i-1]):
            count +=1
    print count

if __name__ == '__main__':
    alternatingCharacters('AAAA')