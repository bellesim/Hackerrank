#https://www.hackerrank.com/challenges/mark-and-toys
def maximumToys(prices, k):
    # Write your code here
    #find different combinations of items 
    maxToys = 0
    prices.sort()
    for i in prices:
        if i<=k:
            maxToys+=1
            k-=i
        else: 
            break
    print maxToys

if __name__ == '__main__':
    maximumToys([1,12,5,111,200,1000,10],50)