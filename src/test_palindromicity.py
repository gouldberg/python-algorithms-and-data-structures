# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# is palindromic
# ----------------------------------------------------------------------------

def is_palindromic(s):

    # Note that s[~i] for i in [0,len(s)-1] is s[-(i+1)].
    return all(s[i] == s[~i] for i in range(len(s) // 2))


is_palindromic2 = lambda phrase: phrase == phrase[::-1]


# ----------
s1 = 'amanznama'

is_palindromic(s1)

is_palindromic2(s1)


s1[~3]

s1[-4]


# ----------------------------------------------------------------------------
# is palindromic
# ----------------------------------------------------------------------------

def is_palindromic3(s):

    return all(a == b for a, b in zip(map(str.lower, filter(str.isalnum, s)),
                                      map(str.lower, filter(str.isalnum, reversed(s)))))


# ----------
s1 = 'A man, a plan, a canal, Panama'

s2 = 'Able was I, ere I saw Elba'

s3 = 'Ray a Ray'

is_palindromic(s1)

is_palindromic3(s1)
