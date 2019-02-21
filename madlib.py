import re

welcome_message = """
Welcome to the Mad Libs game! YOu will be prompted to enter certain types of words. These words will be used in a mad lib and printed out for you.
"""
def fill_mad_lib(file):
    new_mad_lib = ''
    #import pdb; pdb.set_trace()
    with open('text.txt', 'r+') as f:
        try: 
            for line in f:
                # use regex to find all instances of{ something }
                array_of_word_types = find_all_instances(line)
                for i, val in enumerate(array_of_word_types):
                    user_answer = input('Enter a ' + val + ': ')
                    line = replace_word(line, array_of_word_types[i], user_answer)   
                new_mad_lib += line
            print(new_mad_lib)   
        except FileNotFoundError:
            print('The file was not found')    

def replace_word(line, old_word, new_word):
    return line.replace(old_word, new_word, 1)   

def find_all_instances(line):
    regex = r"{[^{]+}"
    return re.findall(regex, line)