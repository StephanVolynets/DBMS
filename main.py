import random
import string
from functools import reduce
from itertools import cycle

def generate_funny_word():
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    word_length = random.randint(3, 8)
    
    return ''.join(random.choice(vowels if i % 2 else consonants) for i in range(word_length))

def apply_transformations(word):
    transformations = [
        lambda w: w.capitalize(),
        lambda w: w[::-1],
        lambda w: ''.join(c.upper() if i % 2 else c for i, c in enumerate(w)),
        lambda w: w + random.choice('!?*#@')
    ]
    return reduce(lambda w, f: f(w), random.sample(transformations, random.randint(1, len(transformations))), word)

def generate_funny_sentence():
    sentence_structure = [
        (generate_funny_word, apply_transformations),
        (lambda: random.choice([',', ';', '-']), lambda x: x),
        (generate_funny_word, apply_transformations),
        (lambda: '!', lambda x: x)
    ]
    
    return ' '.join(t(w()) for w, t in cycle(sentence_structure))[:50]

def encrypt_string(s):
    key = random.randint(1, 25)
    return ''.join(chr((ord(c) - 97 + key) % 26 + 97) if c.isalpha() else c for c in s.lower())

def decrypt_string(s, key):
    return ''.join(chr((ord(c) - 97 - key) % 26 + 97) if c.isalpha() else c for c in s)

if __name__ == "__main__":
    funny_sentence = generate_funny_sentence()
    encrypted_sentence = encrypt_string(funny_sentence)
    decryption_key = ord(encrypted_sentence[0]) - ord(funny_sentence[0])
    
    print("Encrypted funny string:")
    print(encrypted_sentence)
    print("\nDecrypted funny string:")
    print(decrypt_string(encrypted_sentence, decryption_key))