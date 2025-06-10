


""" the running time of bad_composing_strings is O(n^2) """
# Each time a character is added, Python copies all previous characters
# This leads to 1 + 2 + 3 + ... + n = O(n^2) 
def bad_composing_strings(document):
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    print(letters)

""" the running time of bad_composing_strings is O(n) """
def good_composing_strings(document):
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
        letters = ''.join(temp)
    print(letters)

""" the running time of bad_composing_strings is O(n) """
# avoid creating temp
def better_composing_strings(document):
    letters = ''.join([c for c in document if c.isalpha()])
    print(letters)

document = "Hello, my name is Hyunbin Yim thanks"
bad_composing_strings(document)

good_composing_strings(document)

better_composing_strings(document)