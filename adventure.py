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
mylist = [("You and your friends are walking through the Presido during dusk.", 0), 
 ("The atmosphere is quiet as you hear the ocean waves break onto shore.", 0),
 ("As you walk more into the Presido, you all come across an abandoned building.", 0),
 ("Do you walk closer to the building as nightfall is coming or keep walking? ",1)]

current = 0
while current<len(mylist):
	if mylist[current][1] == 0:
		myinput = raw_input(mylist[current][0])
		print myinput
		current += 1
	else:
		myinput = raw_input(mylist[current][0])
		if myinput == 'keep walking':
			print "You keep walking."
		elif myinput == 'walk closer':
			print "You and your friends walk closer to the building as leaves and sticks crunch beneath your shoes."
		current += 1
	


#for curr_list in mylist:
#	myinput = raw_input(curr_list)#
#	print myinput


def choosePath(numberOfPaths):
    choice = 0
    while choice < 1 or choice > numberOfPaths:
        # print('1 to ' + str(numberOfPaths) + '> ', end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':
            choice = int(choice)
    print()
    return choice

def choosePath():


def intro():
	print("You and your friends are walking through the Presido during dusk.")
	print("The atmosphere is quiet as you hear the ocean waves break onto shore.")
	print("You all come across an abandoned hospital.")
	print("")
	print("What will you do?")
	print(" 1 Go inside of the abandoned hopsital.")
	print(" 2 Keep walking on the path.")


def front():
	print("You are standing in front of the hospital. It's dark and uninviting.")
	print("There is a repulsive stench of mildew, mold, and sulpher.")
	print("There is also movement and errie cries coming from unrecgonizable animals.")
	print("")
	print("What do you do?")
	print(" 1 Walk through the hallways.")
	print(" 2 Not going to take any chances and leave.")

def path():
	print("You and your friends continue walking the path in the Presidio.")
	print("You enjoy their random stories and company and would have not thought twice about walking into an abandoned building.")
	print("	")

#start the game
intro()



