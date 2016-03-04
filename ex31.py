print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake! What do you do?!"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Pretend you are dead."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear proceeds to eat your legs off. Good job faggot!"
    elif bear == "3":
        print "He saw you fall to the ground and begins to eat you..."
        print "Do you want to: \n1. Accept your fate and die like a man.\n2. Punch the bear in the nostrils."
        fate = raw_input("> ")
        if fate == "1":
            print "The bear thinks you are either a pussy and feels bad for you or you are dead, so he walks away in disgust"
        elif fate == "2":
            print "The bear gets really pissed and bites off your hand, then spits it out and shoves it in your ass. You die of constipation."
        else:
            print "You hesitated and pissed your pants, and the bear wants nothing to deal with a pants pisser."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of much. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
