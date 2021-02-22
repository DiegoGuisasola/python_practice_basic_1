import re
# First source
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
3215554338
123.555.1234
123*555*1236
800-555-1235
900--555-1239
800-555-1239
900-555-1246
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

mat
bat
cat
pat
'''

# Second source
sentence = 'Start a sentence and then bring it to an end'

# Match Mr. and Mrs min 30: https://www.youtube.com/watch?reload=9&v=K8L6KVGG-7o&ab_channel=CoreySchafer
# pattern = re.compile(r'Mr.?\s[A-Z]\w*')
# .? -> Means dot is optional
# \s -> Space after the optional dot
# [A-Z] First letter of the word is any capital letter of the alphabet
# \w* -> Means that there are 0 or more alphanumeric values after the capital letter

# Match Mr, Ms, Mrs by using groups: ()
# pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*') # or: (r'(Mr|Ms|Mrs).?\s[A-Z]\w*') <- Both are valid.



# Establish the pattern we are looking for: Regex are case-sensitive!
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# Faster way: Using quantifiers
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# Match anytype of phone numbers
pattern = re.compile(r'\d{3}.?\d{3}.?\d{4}')

# To only match certain characters use a character set: [*.]
# pattern = re.compile(r'\d\d\d[-*]\d\d\d[*-]\d\d\d\d')

# Faster way: Using quantifiers
# pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')

# To only match numbers starting with 800 or 900
# pattern = re.compile(r'[89]00[*-]\d\d\d[*-]\d\d\d\d')

# All -at:
# pattern = re.compile(r'[^c]at') # Range is inclusive on both ends

# Find that pattern and return an iterable:
matches = pattern.finditer(text_to_search)

# The iterable gets consumed when getting the size or iterating through it: https://stackoverflow.com/questions/12351475/regular-expression-callable-iterator-get-length/12351496
for match in matches:
    print(match)
    
# =============================================================================
# # To count the elements, finditer-it again.
# matches = pattern.finditer(sentence)
# list_ = list(matches)
# print(f'The len is: {len(list_)}')
# =============================================================================

# Third source: Open a file
# =============================================================================
# with open('data.txt','r') as f: # If unicode error, use: open('data.txt','r', encoding='utf-8')
#     contents = f.read()
#     
#     # Find that pattern and return an iterable: We are using the same pattern as of numbers pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#     matches = pattern.finditer(contents)
# 
#     for match in matches:
#         print(match)
#     
#     # # Print the number of elements in matches. That is, the number of telephones in the file: 100
#     # matches = pattern.finditer(contents)
#     # print(len(list(matches)))
# =============================================================================


