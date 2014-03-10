
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
    
def pat_1021(input):
 #   input = function(input1)
 #   print num1,num2
 #   num = 0
    for item in range(10):
        num = input.count(str(item))
        if input.count(str(item)) != 0:
            print str(item)+':'+str(num)
  #      num += 1
    
        
            
if __name__== '__main__':
    input = raw_input()
    output = pat_1021(input)
 #   print output
