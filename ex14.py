from sys import argv

script, user_name, user_age = argv
prompt = '> '

print "Hi, %s I'm the %s script and you are %s" % (user_name, script, user_age)
print "I'd like to ask you a few questioins."
print "Do you like me %r?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(10)

print """
Alrightt, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have %s computer. Nice
""" % (likes, lives, computer)
