"""
The initial code is taken from https://www.guyrutenberg.com/2008/12/15/damerau-levenshtein-distance-in-python/
"""


def my_damerau_levenshtein_distance(s1, s2):
    """Compute the Damerau-Levenshtein distance between two given strings (lists of elements)"""
    d = {}
    str_len1 = len(s1)
    str_len2 = len(s2)
    for i in range(-1, str_len1+1):
        d[(i, -1)] = i+1
    for j in range(-1, str_len2+1):
        d[(-1, j)] = j+1

    for i in range(str_len1):
        for j in range(str_len2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                           d[(i-1, j)] + 1,  # deletion
                           d[(i, j-1)] + 1,  # insertion
                           d[(i-1, j-1)] + cost,  # substitution
                          )
            if i and j and s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i-2, j-2] + cost)  # transposition
    return d[str_len1-1, str_len2-1]
