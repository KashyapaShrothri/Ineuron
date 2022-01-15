'''1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass. '''

class Area:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area_of_trianlge(self):
        s = self.a + self.b + self.c
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return area

tria = Area(3, 4, 5)
print(tria.area_of_trianlge())

#--------------------------------------------------------------------------------------------------

'''1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.'''

def filter_long_words(words_list, n):
    long_words = []
    for word in words_list:
        if len(word) > n:
            long_words.append(word)
    return long_words

wordsList = ['abs', 'engine', 'chasis', 'body', 'radiator', 'lubrication', 'transmission']
print(filter_long_words(wordsList, 5))

#--------------------------------------------------------------------------------------------------

'''2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.'''

def word_len_map(words_list):
    word_len = []
    for word in words_list:
        word_len.append(len(word))
    return word_len

wordsList = ['abs', 'engine', 'chasis', 'body', 'radiator', 'lubrication', 'transmission']
print(word_len_map(wordsList))

#------------------------------------------------------------------------------------------------

'''2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.'''

def idetify_vowel(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if character.lower() in vowels:
        return True
    else:
        return False

print(idetify_vowel('U'))

#-----------------------------------------------------------------------------------------------