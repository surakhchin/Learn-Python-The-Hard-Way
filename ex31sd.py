print "You have 3 doors in front of you.... door #1, #2, and #3... choose wisely or you shall face the wrath of this code:"

def doors():
    door = raw_input("> ")
    if door == "1":
        print "You walk in the room with a sleeping bear. Do you:"
        print "1. Turn around and walk the way you came from."
        print "2. Wake the bear up (lol)."
        print "3. Piss your pants and perform a Seppuku"
        door1 = raw_input("> ")
        if door1 == "1":
            print "Sry m8 the door is locked. Do you:"
            print "1. Turn around and walk the way you came from."
            print "2. Wake the bear up (lol)."
            print "3. Piss your pants and perform a Seppuku"
            door1 = raw_input("> ")
            if door1 == "1":
                print "You turn around and stumble into the bear, waking him up, he gets pissed and eats you."
                print "GAME OVER BRO"
        elif door1 == "2":
            print "You wake up the bear, who is pissed, and he eats you."
            print "GAME OVER BRO"
        elif door1 == "3":
            print "You pull out your blade, but then realize oh snap I have a blade. Do you:"
            print "1. Still kill yourself cause you are a faggot."
            print "2. Perform a flying downward sword thrust of doom."
            door1 = raw_input("> ")
            if door1 == "1":
                print "Good job you played yo self"
                print "GAME OVER BRO"
            elif door1 == "2":
                print "Congratulations! You defeated the bear and completed level 6. You are not a Faggot."
            else:
                print "You are Fag and can't follow directions. Bear wakes up and eats you."
                print "GAME OVER BRO"
        else:
            print "You are fag and can't follow directions. Bear wakes up and eats you."
            print "GAME OVER BRO"
    elif door == "2":
        print "Door 2 is locked. Try another door."
        doors()
    elif door == "3":
        print "Door 3 is locked. Try another door."
        doors()
    else:
        print "Uhh you did nothing, try again."
        doors()
doors()