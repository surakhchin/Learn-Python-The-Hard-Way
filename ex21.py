def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVIDING %d * %d" % (a,b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d \nheight: %d \nweight: %d \niq: %d" % (age, height, weight, iq)


#puzzle for extra credit:
print "Here is the puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

x = 10
y = 30
z = 2
p = 10

w = add(x, subtract(y, multiply(z, divide(p,2))))

print w
