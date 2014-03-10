
import string

def pat_1016(input1,i1,input2,i2):
    num1 = input1.count(i1)
    num2 = input2.count(i2)
 #   print num1,num2
    
    if num1 | num2:
        out1 = 0
        out2 = 0
        for num in range(num1):
            out1 = out1*10+string.atoi(i1)
        for num in range(num2):
            out2 = out2*10+string.atoi(i2)
    
        return out1+out2
    
    return 0
        
            
if __name__== '__main__':
    input = raw_input()
    input1,i1,input2,i2 = input.split()
    output = pat_1016(input1,i1,input2,i2)
    print output
