print "You have 3 doors in front of you.. door #1, #2, #3, choose wisely or you shall face the wrath of this code:"

def doors():

    door = raw_input("> ")
    if door == "1":
        print "you walk in the room with a sleeping bear. Do you:"
        print "1. Turn around and walk the way you came from."
        print "2. Wake the bear up (lol)."
        print "3. Wet your pants and prepare for Seppuku"
        door1 = raw_input("> ")
        if door1 == "1":
            print "Sry m8 the door is locked. Do you:"
            print "1. Turn around and walk the way you came from."
            print "2. Wake the bear up (lol)."
            print "3. Wet your pants and prepare for Seppuku"
            door1 = raw_input("> ")
            if door1 == "1":
                print "You turn around and stumble into the bear, waking him up, he gets mad and eats you."
                print "Game over!"
        elif door1 == "2":
            print "you wake up the bear, who is mad, and he eats you."
            print "Game over!"
        elif door1 == "3":
            print "you pull out your blade, but then realize oh snap I have a blade. Do you:"
            print "1. Still kill yourself because you don't wanna get eaten."
            print "2. Perform a flying downward sword thrust of doom."
            door1 = raw_input("> ")
            if door1 == "1":
                print "Good try, but Game over!"
            elif door1 == "2":
                print "Congratulations! You defeated the bear and completed level 6."
            else:
                print "You didnt pick a valid option, so the bear wakes up and eats you."
                print "Game over!"
        else:
            print "You did not follow the directions, the bear wakes up and eats you."
            print "Game over!"
    elif door == "2":
        print "Door 2 is locked. Try another door."
        doors()
    elif door == "3":
        print "Door 3 is locked. Try another door."
        doors()
    else:
        print "Uhh you did not pick a door option, please try again."
        doors()

doors()