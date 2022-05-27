# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if len(word) != len(anagram):
        return false

    first_word = sorted(word)

    second_word = sorted(anagram)

    if first_word == second_word:
        return True
    else:
        return False


result = find_anagram("save", "raid")
print(result)
