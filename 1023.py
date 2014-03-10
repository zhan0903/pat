
import string

def function(input):
    output = []
    num = 0
    for item1 in input:
        temp = item1
        for item2 in range(string.atoi(temp)):
            output.append(str(num))
        num += 1
    return output
    
def pat_1023(input1):
    input = function(input1)
 #   print num1,num2
    for item in input:
        temp = item
        if string.atoi(temp) != 0:
            if input.index(item) != 0:
                input[input.index(item)] = '0'
                input[0] = item
            break
    return ''.join(input)
    
        
            
if __name__== '__main__':
    input = raw_input().split()
    output = pat_1023(input)
    print output
