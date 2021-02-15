strs = ["flower","flow","flight"]

# First approach: 36 ms, 14.2 mb
common_word = ''

def LCP(strs):
    if strs == None or len(strs) == 0:
        return ''
    for letter in range(len(strs[0])): # For each letter in the first word (strs[0])
        current_letter = strs[0][letter] # First word, current letter
        
        for word in range(1, len(strs)):
            if letter == len(strs[word]) or strs[word][letter] != current_letter:
                common_word = strs[0][:letter]
                return common_word
    return strs[0] # If all words are equal or there is only 1 word, return it


# Second approach - Pythonic: 36 ms, 14.4 mb
def LCP2(strs):
    if strs == None or len(strs) == 0:
        return ''
    for letter in range(len(strs[0])+1):
        common_word = strs[0][0:letter+1]
        for word in strs[1:]:
            if not word.startswith(common_word):
                return strs[0][:letter]
                
    return strs[0][:letter]

print(LCP(strs))
print(LCP2(strs))
