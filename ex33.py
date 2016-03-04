number = []

def wyle(a,i):
    i
    while i < a:
        print "At the top i is %d" % i
        number.append(i)

        i = i + 1
        print "Numbers now: ", number
        print "At the bottom i is %d" % i
wyle(6,5)

print "The numbers"

for num in number:
    print num
