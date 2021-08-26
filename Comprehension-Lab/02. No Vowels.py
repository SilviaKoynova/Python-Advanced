def is_vowel(character):
    if character.lower() in 'aeouei':
        return True
    return False


word = input()
print(''.join([char for char in word if not is_vowel(char)]))