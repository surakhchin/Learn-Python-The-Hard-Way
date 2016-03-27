print "\n\n\n\n"
print "This is a simple example of a list:"
things = ['a', 'b','c','d']
print things[1]
things[1] = 'z'
print things
print "\n"
print "Now lets look at dicts:"
stuff = {'name': 'Zed', 'age': 39, 'height': 6*12 +2}
print stuff['name']
print stuff['age']
print stuff['height']
stuff['city'] = "San Francisco"
print stuff['city']
print stuff
print "\n\n\n"
stuff[1] = 'wow'
stuff[2] = 'Neato'
print stuff
print '\n\n\n'
print "no delete stuff use del:"
del stuff['city']
del stuff[1]
del stuff[2]
print stuff
print "\n\n\n"
