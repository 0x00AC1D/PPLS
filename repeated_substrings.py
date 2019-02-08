# generator approach
def repeating_substrings(sentence, min_len=10, max_len=20, repeat_threshold=5):
    """ 
    Generates and counts substrings of length inbetween min_len and max_len (both included),
    which occur in the sentence at least repeat_threshold times.
    sentence: str
    min_len, max_len, repeat_threshold: int
    return: sub: str, sub_count, total: int
    """
    total = 0
    observed = set() # substrings of various length already taken account for
    for position in range(len(sentence) + 1 - min_len):
        for sub_len in range(max_len, min_len-1, -1):
            sub = sentence[position:position + sub_len]
            sub_count = sentence[position:].count(sub)
            if sub not in observed and sub_count >= repeat_threshold:
                observed.add(sub)
                total += sub_count
                yield sub, sub_count, total

for sub, sub_count, total in repeating_substrings("abababadcdc", min_len=2, max_len=3, repeat_threshold=2):
    print(f"substring: '{sub}'\ncount: {sub_count}\ntotal count: {total}\n")

""" output
substring: 'aba'
count: 2
total count: 2

substring: 'ab'
count: 3
total count: 5

substring: 'ba'
count: 3
total count: 8

substring: 'dc'
count: 2
total count: 10
"""