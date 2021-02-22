import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www)*\.?[a-zA-Z]+\.(com|gov)') # One way
pattern = re.compile(r'https?://(www\.)?\w+\.\w+') # Better way

matches = pattern.finditer(urls)

for match in matches:
    print(match)






# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))