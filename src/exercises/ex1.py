import re

def encrypt(text: chr, size: int = 5):
    '''
    The Atbash cipher is a simple substitution cipher that relies on transposing 
    all the letters in the alphabet such that the resulting alphabet is 
    backwards. The first letter is replaced with the last letter, the second 
    with the second-last, and so on.
    '''
    cipher = [chr(i) for i in range(ord("z"), ord("a") - 1, -1)]
    alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    cipherMap = {ch: cipher[i] for i, ch in enumerate(alphabet)}

    text = re.sub(r'[^\w]', '', text.lower())
    coded = "".join(cipherMap.get(chr, chr) for chr in text)
                     
    return " ".join([coded[i:i+size] for i in range(0, len(coded), size)])
