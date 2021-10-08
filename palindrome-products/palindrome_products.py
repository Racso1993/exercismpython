import itertools
def iter_palindromes(max_factor, min_factor):
    for a, b in itertools.combinations_with_replacement(range(min_factor, max_factor + 1), 2):
        p = a * b
        s = str(p)
        if s == s[::-1]:
            yield p, (a, b)
def smallest_palindrome(max_factor, min_factor=0):
    return min(iter_palindromes(max_factor, min_factor))
def largest_palindrome(max_factor, min_factor=0):
    return max(iter_palindromes(max_factor, min_factor))
