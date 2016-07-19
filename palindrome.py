phrase = []

def recursion(phrase):
    print('String here', phrase)
    if phrase[0] == phrase[-1]:
        del phrase[0]
        del phrase[-1]
        print(phrase)
        return
                #print('   ')
    else:
                #return False
        print("Not a palindrome")

def is_palindrome(phrase):
    # TODO: return True or False if the sentence is or isn't a palindrome
        #print ('is pal',phrase)
        string_of_phrase = ''.join(phrase)
        phrase = list(string_of_phrase)
        #print(phrase[0])
        #print(phrase[-1])
        count = len(phrase)
        #print(' is pal', count)
        length_of_word(count)

def length_of_word(count):
    #print(count)
    if count > 1:
        recursion(phrase)
        count-=1

def main():
    # TODO: put your input/output code here
    print(" Program to test for palindrome")
    sentence = input("Give me a sentence to test if it is a palindrome or not: ")
    phrase =[sentence]

    is_palindrome(phrase)

if __name__ == '__main__':
    main()
