print('spam eggs')
print('doesn\t')
print('"Yes," They said')
print("\"Yes,\" they said")
print('"Isnt\'t," they said.')

print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'
print(s)

print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(3 * 'un' + 'ium')

print('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

prefix = 'Py'
prefix = 'thon'
print(prefix + 'thon')

word = 'Python'
print(word[0])
print(word[5])

print(word[-1])
print(word[-2])
print(word[-6])

print(word[0:2])
print(word[2:5])

print(word[:2])
print(word[4:])
print(word[-2:])

print(word[:2]+word[2:])
print(word[:4]+word[4:])

print(word[4:42])
print(word[42:])

print('J'+word[1:])
print(word[:2]+'py')

s = 'supercalifragilisticexpialidocious'
print(len(s))