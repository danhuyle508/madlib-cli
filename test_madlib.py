from madlib import replace_word, find_all_instances

def test_replace_word_pass():
    actual = replace_word('The dog ran.', 'dog', 'cat' )
    expected ='The cat ran.'
    assert expected == actual

def test_find_all_instances_pass():
    actual = find_all_instances('The {animal} {verb}')
    expected = ['{animal}', '{verb}']
    assert expected == actual

def test_replace_word_fail():
    actual = replace_word('The dog ran', 'dog', 'cat')
    expected ='The dog ran.'
    assert expected != actual

