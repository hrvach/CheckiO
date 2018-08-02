# migrated from python 2.7
import re

def translate(phrase):
    return re.sub(r'([aeiouy]){3}', r'\1', re.sub(r'((?![aeiouy])[a-z])([aeiouy])', r'\1',phrase))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate(u) == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"