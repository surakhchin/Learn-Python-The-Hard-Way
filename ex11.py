print "How old are you?",
age = raw_input()
print "How tall are you?", #note: we put a , at the end of each print line so it doesnt end the line with a newline character and go to the next line
height = raw_input()
print "How much do you weight",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)

name = raw_input("What is your name? ")
print "Hello, %r" % name

nationality = raw_input("What country where you born?")
school = raw_input("What college did you graduate?")
job = raw_input("What job do you possess")

print "%s was born in %s went to %s and works as %s" % (name, nationality, school, job)