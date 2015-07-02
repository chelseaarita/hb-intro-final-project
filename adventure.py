# You and your friends are walking through the Presido during dusk. 
# The atmosphere is quiet as you hear the ocean waves break onto shore.
# As you walk more into the Presido, you all come across an abandoned building. 

# It looks like the abandoned hopsital that was built in 1931 and closed in 1981.
# Do you walk closer to the building as nightfall is coming or keep walking?

# You and your friends walk closer to the building as leaves and sticks crunch beneath your shoes.
# There's a sudden chill in the air. 
# You get to the entrance of the hospital. You all look up at its grand glory. You all are awestrucked. 
# Do you walk in the hospital or leave? 
# You walk into the hospital and none of you have flashlights but remembered you have your phones that have the 
# flashlight app. You all turn it on.
# Once you turn on the flashlight, you see scurrying and movement. You flinch. Do you run out of the hospital or stay?

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
# mylist = [("You and your friends are walking through the Presido during dusk.", 0), 
#  ("The atmosphere is quiet as you hear the ocean waves break onto shore.", 0),
#  ("As you walk more into the Presido, you all come across an abandoned building.", 0),
#  ("Do you walk closer to the building as nightfall is coming or keep walking? ",1)]

# current = 0
# while current<len(mylist):
# 	if mylist[current][1] == 0:
# 		myinput = raw_input(mylist[current][0])
# 		print myinput
# 		current += 1
# 	else:
# 		myinput = raw_input(mylist[current][0])
# 		if myinput == 'keep walking':
# 			print "You keep walking."
# 		elif myinput == 'walk closer':
# 			print "You and your friends walk closer to the building as leaves and sticks crunch beneath your shoes."
# 		current += 1
	


#for curr_list in mylist:
#	myinput = raw_input(curr_list)#
#	print myinput


# def choosePath(numberOfPaths):
#     choice = 0
#     while choice < 1 or choice > numberOfPaths:
#         print('1 to ' + str(numberOfPaths) + '> ', end='')
#         choice = input()
#         if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
#             choice = 0
#         if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
#             choice = int(choice)
#     print()
#     return choice

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
	print("The atmosphere is quiet as you hear the ocean waves break onto shore.")
	print("You all come across an abandoned hospital.")
	print(" ")
	print("What will you do?")
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
	print("There is a repulsive stench of mildew, mold, and sulpher.")
	print("There is also movement and errie cries coming from unrecgonizable animals.")
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
	print("You're standing in long endless hallway and there are a dozen closed doors that see. What door do you go into?")
	print(" ")

	walk = choosePath(12)

	if walk == 7:
		zombie()
	else:
		stuck_door()

def zombie():
	print(" ")
	print("The door is hard to open from being stagnant for so long. You give the door a bigger push. After struggling for a moment, you finally get it open. But wait. What was that noise?")
	print("It's now silent but you chills just ran down your spine")
	print("You hear the same weird noise. You cower.")
	print("You shine the flashlight onto the movement.")
	print("It's a zombie coming right at you!")
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
	print("You take a swing, the zombie jumps back and you miss")
	print("The zombie lunges at you. You die.")
	print(" ")

def shocked():
	print(" ")
	print("You're so scared and still in shocked. You are not believing what you are seeing.")
	print("The zombie lunges at you. You die.")
	print(" ")

def run():
	print(" ")
	print("You run out of the room and down the hallway.")
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
	print("Walking through the park and hearing the waves crash onto shore is peaceful and comforting.")
	print("You enjoy their random stories and company and would have not thought twice about walking into an abandoned building.")
	print("	")

def scared():
	print(" ")
	print("You're so scared. You run so fast, you end up tripping on debris, and falling. You quickly get up and bump your head. You were never very graceful when you were scared.")
	print("You manage to limp away while holding your head, and you see the opening of the hopstial doors. You're so relieved.")
	print("You leave the hospital and run off, never returning.")
	print(" ")


#start the game
intro()
