def letter_freq(word):
    letter_dict={}
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        letter_dict[i]=word.lower().count(i)
    return letter_dict
print(letter_freq('Face'))
