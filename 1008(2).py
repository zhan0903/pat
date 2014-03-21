
import string


        
def function(input,n,m):
    start = n-m%n
    for i in range(start,n):
        print input[i],
    for i in range(start):
        print input[i],
    #    if i != (start-1):print ' ',
    
def pat_1008(input,n,m):
    function(input,n,m)

        
            
if __name__== '__main__':
    input1 = raw_input()
    input2 = raw_input()
    n = input1.split()[0]
    m = input1.split()[1]
    
    pat_1008(input2.split(),int(n),int(m))
