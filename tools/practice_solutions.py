"""SPOILERS: reference answers for practice/tasks.json, used only by tools/check-practice.py.
The app never shows these.

SOLUTIONS: a good answer for each task; it must pass every test and be fast.
SLOW:      a plausible but slow answer (usually O(n²)); the speed check must catch it.
"""

SOLUTIONS = {
    "t3-reverse-words": '''
def reverse_words(s):
    return " ".join(s.split()[::-1])
''',
    "t3-palindrome": '''
def is_palindrome(s):
    t = s.replace(" ", "").lower()
    return t == t[::-1]
''',
    "t3-anagram": '''
def is_anagram(a, b):
    return sorted(a) == sorted(b)
''',
    "t3-first-unique": '''
from collections import Counter
def first_unique(s):
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None
''',
    "t3-count-vowels": '''
def count_vowels(s):
    return sum(1 for ch in s if ch in "aeiouAEIOU")
''',
    "t3-compress": '''
def compress(s):
    if not s:
        return ""
    parts, run = [], 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            run += 1
        else:
            parts.append(s[i - 1] + str(run))
            run = 1
    parts.append(s[-1] + str(run))
    return "".join(parts)
''',
}

SLOW = {
    "t3-reverse-words": '''
def reverse_words(s):
    words = s.split()
    out = []
    while words:
        out.append(words.pop(0))   # pop(0) shifts the whole list each time: O(n²)
    return " ".join(out[::-1])
''',
    "t3-palindrome": '''
def is_palindrome(s):
    t = s.replace(" ", "").lower()
    while len(t) > 1:              # slicing copies the string each time: O(n²)
        if t[0] != t[-1]:
            return False
        t = t[1:-1]
    return True
''',
    "t3-anagram": '''
def is_anagram(a, b):
    rest = list(b)
    for ch in a:
        if ch not in rest:
            return False
        rest.remove(ch)            # remove scans the list each time: O(n²)
    return not rest
''',
    "t3-first-unique": '''
def first_unique(s):
    for ch in s:
        if s.count(ch) == 1:       # count scans the whole string each time: O(n²)
            return ch
    return None
''',
    "t3-count-vowels": '''
def count_vowels(s):
    vowels = [ch for ch in "aeiouAEIOU" * 20000]   # a huge list searched for every letter
    return sum(1 for ch in s if ch in vowels)
''',
    "t3-compress": '''
def compress(s):
    out = ""
    while s:
        ch = s[0]
        n = len(s) - len(s.lstrip(ch))
        out += ch + str(n)
        s = s[n:]                  # copies the rest of the string each time: O(n²)
    return out
''',
}
