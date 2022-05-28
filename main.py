# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word)==sorted(anagram):
        return True
    else:
        return False
print('A program that checks if two words are anagram. Enter any two words of your choice')

word = input("Enter the first word: \n")

anagram = input("Enter the second word: \n")

print(find_anagram(word, anagram))





