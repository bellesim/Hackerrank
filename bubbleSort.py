def countSwaps(a):
    # Write your code here
    #sort array in ascending order 
    swaps = 0
    for i in range (0, len(a)-1):
        for j in range (0,len(a)-1):
            if (a[j]> a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swaps +=1
    return swaps     
 

    
    #print number of sorts 
    #print first element 
    #print last element

if __name__ == '__main__':
    list1 = [5, 3, 8, 6, 7, 2]  
    print 'Array is sorted in',countSwaps(list1) , 'swaps.'
    print 'First Element:', list1[0]
    print 'Last Element:', list1[-1] 

