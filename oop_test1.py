from urllib import urlopen


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []


# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


print "*" * 134
print urlopen(WORD_URL).readlines()

print "*" * 134
print WORDS

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print len(fruits)
print range(80)
print range(len(fruits))
print "Good bye!"