def is_pangram(sentence):
    
    # first we do not know what we are comparing against, so lets set up a reference:
    alphabet = {'a': 'A',
                'b': 'B',
                'c': 'C',
                'd': 'D',
                'e': 'E',
                'f': 'F',
                'g': 'G',
                'h': 'H',
                'i': 'I',
                'l': 'J',
                'k': 'K',
                'l': 'L',
                'm': 'M',
                'n': 'N',
                'o': 'O',
                'p': 'P',
                'q': 'Q',
                'r': 'R',
                's': 'S',
                't': 'T',
                'u': 'U',
                'v': 'V',
                'w': 'W',
                'x': 'X',
                'y': 'Y',
                'z': 'Z'
                }
    # Now lets set up a default return value
    # UI am not sure this is a good idea but do not know why
    # I think default should return undefined
    answer = True
    # Now we can do the logic
    for key, value in alphabet.items():
      if key not in sentence:
        # I have not fidured out how to join 2 conditionals with AND in an if yet, 
        # so I am goin to nest them instead
        if value not in sentence:
            answer = False
    # if the sentence contains every letter then 'answer' should still be true
    return answer