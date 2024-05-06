# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# find anagrams
# ----------------------------------------------------------------------------

import collections

def find_anagrams(dictionary):

    sorted_string_to_anagrams = collections.defaultdict(list)

    for s in dictionary:
        # sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]


# ----------
dictionary = {'debitcard', 'elevis', 'silent', 'badcredit', 'lives', 'freedom', 'listen',
              'levis', 'money'}

find_anagrams(dictionary=dictionary)


# ----------
s = 'debitcard'

print(''.join(sorted(s)))

sorted_string_to_anagrams = collections.defaultdict(list)
sorted_string_to_anagrams[''.join(sorted(s))].append(s)
print(sorted_string_to_anagrams)

