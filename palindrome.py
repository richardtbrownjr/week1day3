import re
phrase = []

def recursion(phrase):
    #print('String here', phrase
        if phrase[0] == phrase[-1]:
            print(phrase)
            del phrase[0]
            del phrase[-1]
            print(phrase)
            value=len(phrase)
            if value > 1:
                recursion(phrase)
            elif value == 0:
                print("Palindrome!")
        else:
            print("Not a palindrome")
            return

def is_palindrome(phrase):
    # TODO: return True or False if the sentence is or isn't a palindrome
        #print ('is pal',phrase)
        string_of_phrase = ''.join(phrase)
        #string additions not working yet
        #phrase = re.sub('[^A-Za-z0-9]','',phrase)
        phrase = list(string_of_phrase)
        #print(phrase[0])
        #print(phrase[-1])
        recursion(phrase)

def main():
    # TODO: put your input/output code here
    print(" Program to test for palindrome")
    sentence = input("Give me a sentence to test if it is a palindrome or not: ")
    phrase =[sentence]

    is_palindrome(phrase)


if __name__ == '__main__':
    main()
