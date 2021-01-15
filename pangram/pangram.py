import string
def is_pangram(sentence):
    new_sentence = list(sentence.lower().replace(" ", ""))
    a_z = list(string.ascii_lowercase)
    for letter in a_z:
      if letter not in new_sentence:
        return False 
    return True