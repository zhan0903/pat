
import string

table1 = {0:'',1:'1',2:'12',3:'123',4:'1234',\
          5:'12345',6:'123456',7:'1234567',\
          8:'12345678',9:'123456789'}
table3 = {0:'',1:'B',2:'BB',3:'BBB',4:'BBBB',\
          5:'BBBBB',6:'BBBBBB',7:'BBBBBBB',\
          8:'BBBBBBBB',9:'BBBBBBBBB'}
table2 = {0:'',1:'S',2:'SS',3:'SSS',4:'SSSS',\
          5:'SSSSS',6:'SSSSSS',7:'SSSSSSS',\
          8:'SSSSSSSS',9:'SSSSSSSSS'}
def pat_1006(input):
    num = string.atoi(input)
    output = table1[num%10]
    num = num/10
    if num > 0:
        output = table2[num%10]+output
        num = num/10
        if num > 0:
            output = table3[num%10]+output
    return output
            
if __name__== '__main__':
    input = raw_input()
    output = pat_1006(input)
    print output
