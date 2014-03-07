
import string

def pat_1009(input):
    words = string.split(input)
    words.reverse()
    output = ' '.join(words)

    return output
            
if __name__== '__main__':
    input = raw_input()
    output = pat_1009(input)
    print output
