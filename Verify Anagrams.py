def verify_anagrams(first_word, second_word):  
    fw = list(first_word.lower().replace(' ', ''))
    sw = list(second_word.lower().replace(' ', ''))
    return {x: fw.count(x) for x in set(fw)} == {x: sw.count(x) for x in set(sw)}

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"