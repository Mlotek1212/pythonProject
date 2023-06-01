''' might see a simplified version of this mission already First Word (simplified). This mission is a little bit more complex as not only English letters can be in the given string.

You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, one/multiple dot(s) or space(s).
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.'''

# def first_word(text: str) -> str:
#     text = text.split(' ')
#     if text[0] == '':
#         word = text[1]
#     else:
#         word = text[0]
#     if word.isalpha():
#         return word
#     else:
#         if word[-2] == "'":
#             return word
#         elif word.endswith(','):
#             word1 = word.replace(word[-1] ,'')
#             return word1
#         else:
#             return text[1]
def get_validate_word(word: str) -> str:
    result = ''
    for char in word:
        if char == "'":
            result += char
        elif char.isalpha():
            result += char
        else:
            return result
    return result


def first_word(text: str) -> str:
    text = text.lstrip('.').lstrip(' ')
    for word in text.split(' '):
        for alowed_word in word.split('.'):
            return get_validate_word(alowed_word)


#
# get_validate_word("Hello")
# get_validate_word("ala123")
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("hello.world") == "hello"
