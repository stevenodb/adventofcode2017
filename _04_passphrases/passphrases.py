"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input.

How many passphrases are valid?
"""

from itertools import permutations


def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
        else:
            return True
    return False


"""
--- Part Two ---

For added security, yet another system policy has been put in place. 
Now, a valid passphrase must contain no two words that are anagrams of 
each other - that is, a passphrase is invalid if any word's letters can 
be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be 
rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to 
be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
"""


def anagrams_in(words):

    def anagrams_of(word):
        return {''.join(p) for p in permutations(word)}

    all_anagrams = set()
    for i in range(len(words)):
        selected_word = words[i]
        other_words = set(words[:i]).union(set(words[i + 1:]))
        anagrams_for_word = other_words.intersection(anagrams_of(selected_word))
        all_anagrams = all_anagrams.union(anagrams_for_word)
    return all_anagrams


def has_anagrams(words):
    return len(anagrams_in(words)) > 0


if __name__ == '__main__':
    with open('input') as file:
        valid_count = 0
        for line in file:
            line = line.strip()
            words = line.split()
            if not (has_duplicates(words) or has_anagrams(words)):
                valid_count = valid_count + 1

    print('Valid passphrases: {:d}'.format(valid_count))


