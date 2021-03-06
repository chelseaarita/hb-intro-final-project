

print "                                                         "
print "                                                         "
print "                                                         "
print "========================================================="
print "                Chelsea's final project                  "
print "========================================================="
print "                                                         "
print "                                                         "
print "                                                         "

name = raw_input("What is your name? ")
print "Hello, %s. Welcome to my final project." % name
print "                                                         "
print "                                                         "
print "                                                         "
raw_input('Press enter to continue ')


def choosePath(numberOfPaths):
	# path = raw_input("1 to "+str(numberOfPaths)+">")
	# check whether the path is an integer between 1 and including the numberOfPaths
	while True: 
		path = raw_input("1 to "+str(numberOfPaths)+"> ")
		if path.isdigit() and int(path)>=1 and int(path)<=numberOfPaths: #when it's a raw input, it's always a string.
			break
	# print("Type Exit to exit")
		# item = raw_input("Add an item: ")
		# if(item == "exit"):

	return int(path)


def intro():
	print(" ")
	print("You and your friends are walking through the Presidio during dusk.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("The atmosphere is quiet as you hear the ocean waves break onto shore.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You all come across an abandoned hospital.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("What will you do?")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print(" 1 Walk inside the abandoned hopsital.")
	print(" 2 Keep walking on the path.")
	print(" ")

	walk = choosePath(2)

	if walk == 1:
		front()
	else:
		path()


def front():
	print(" ")
	print("You are standing in front of the hospital. It's dark and uninviting.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("There is a repulsive stench of mildew, mold, and sulpher.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("There is also movement and errie cries coming from unrecgonizable animals.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("What do you do?")
	print(" ")
	print(" 1 Walk through the hallways.")
	print(" 2 Not going to take any chances and leave.")
	print(" ")

	walk = choosePath(2)

	if walk == 1:
		hallways()
	else:
		scared()

def hallways():
	print(" ")
	print("You're standing in a long endless hallway and there are a dozen closed doors that you see. What door do you go into?")
	print(" ")

	walk = choosePath(12)

	if walk == 7:
		zombie()
	else:
		stuck_door()

def zombie():
	print(" ")
	print("The door is hard to open from being stagnant for so long. You give the door a bigger push. After struggling for a moment, you finally get it open.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You hear a strange noise off into the distance and chills just ran down your spine.")
	print(" ")
	raw_input('Press enter to continue ')
	print (" ")
	print("You start taking baby steps. You slowly walk forward, unable to see anything.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You start to feel a presence ahead of you but you think it's one of your friends so it's no big deal.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You keep walking forward until you hear an inaudible, monsterous noise. You immediately stop in your tracks.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You feel something slighty graze your shoulder and whatever touched you, felt inhumanly cold.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You fumble in the dark to get your phone. You want to turn on the flashlight app. The presence is hovering over you...")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You are trembling and bravely shine the light ahead of you...")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("It's a zombie!")
	print(" ")
	print("What do you do?")
	print(" ")
	print(" 1 Defend yourself")
	print(" 2 Stand there because you're in shock")
	print(" 3 Run for your life")
	print(" ")

	walk = choosePath(3)

	if walk == 1:
		defend()
	elif walk == 2:
		shocked()
	elif walk == 3:
		run()
	else:
		gohome()

def defend():
	print(" ")
	print("You don't have any weapons with you, so you take a swing at their chest, the zombie steps back and you miss.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("The zombie lunges at you and tries to bite you but it misses you by a mere half inch.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You try to jump on the zombie but you missed and fall to the ground.")
	raw_input('Press enter to continue ')
	print(" ")
	print("You're badly injured.")
	raw_input('Press enter to continue ')
	print(" ")
	print("The zombie is coming. You squirm and try to defend yourself, but it keeps coming closer to you.")
	raw_input('Press enter to continue ')
	print(" ")
	print("You are helpless and you shout and tell them to surrender, but they don't listen and keep coming closer. ")
	raw_input('Press enter to continue ')
	print("The zombie is inches away from you and takes a bite of your leg.")
	raw_input('Press enter to continue ')
	print("You scream in pain.")
	raw_input('Press enter to continue ')
	print(" ")
	print("You have died.")
	print(" ")

def shocked():
	print(" ")
	print("You're so scared and still in shocked. You are not believing what you are seeing.")
	raw_input('Press enter to continue ')
	print(" ")
	print("You don't have any weapons with you. The zombie lunges at you and bites you.")
	print(" ")
	print("You have died.")

def run():
	print(" ")
	print("You run out of the room and down the hallway.")
	raw_input('Press enter to continue ')
	print(" ")
	print("You're back to where you began.")
	print(" ")
	front()

def stuck_door():
	print(" ")
	print("Bummer, the door is stuck.")
	print(" ")
	hallways()

def gohome():
	print(" ")
	print("You decided to go home.")
	print(" ")

def path():
	print(" ")
	print("You and your friends continue walking the path in the Presidio.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("Walking through the park and hearing the waves crash onto shore is peaceful and comforting.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You enjoy their random stories and company and would have not thought twice about walking into an abandoned building.")
	print("	")

def scared():
	print(" ")
	print("You're so scared. You run so fast, you end up tripping on debris, and falling. You quickly get up and bump your head. You were never very graceful when you were scared.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ")
	print("You manage to limp away while holding your head, and you see the opening of the hopstial doors. You're so relieved.")
	print(" ")
	raw_input('Press enter to continue ')
	print(" ") 
	print("You leave the hospital and run off, never returning.")
	print(" ")

while True:
	intro()
	restart = raw_input("Do you want to play again? Y/N ")
	if restart != 'Y': 
		break
#start the game

