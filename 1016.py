
import string

def pat_1016(input1,i1,input2,i2):
    num1 = input1.count(i1)
    num2 = input2.count(i2)
    
    if num1 | num2:
        for num in range(num1):
            out1 += i1*num*10
        for num in range(num2):
            out2 += i2*num*10
        
    
    winput1 = string.
    words.reverse()
    output = ' '.join(words)

    return output
            
if __name__== '__main__':
    input = raw_input()
    output = pat_1016(input1,i1,input2,i2)
    print output
