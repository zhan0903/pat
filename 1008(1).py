
import string

def function(input,start,end):
    count = 0
    end_m = 1+start+(end-start)/2
 #   print 'end_m',end_m
    for i in range(start,end_m):
        temp = input[i]
        input[i] = input[end-count]
        input[end-count] = temp
        count += 1
    
def pat_1008(input,n,m):
 #   input = function(input1)
 #   print num1,num2
 #   num = 0
    function(input,0,m-1)
 #   print '1',input
    function(input,m,n-1)
 #   print '2',input
    function(input,0,n-1)
 #   print '3',input

    print ' '.join(input)
        
            
if __name__== '__main__':
    input1 = raw_input()
    input2 = raw_input()
    n = input1.split()[0]
    m = input1.split()[1]
    
    pat_1008(input2.split(),int(n),int(n)-int(m))
