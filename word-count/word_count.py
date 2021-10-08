#
# Count-words
#
def word_count(input_str):
    '''idea for strin_clean copied ovr'''
    string_clean = ''.join(s.lower() if s.isalnum() else ' ' for s in input_str)
    result = {}
    for word in string_clean.split():
        result[word] = result.get(word, 0) + 1
    return result
