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
print "                Chelsea's final Project                  "
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
			print "You keep walking"
		elif myinput == 'get closer':
			print "you walk closer"
		current += 1
	


#for curr_list in mylist:
#	myinput = raw_input(curr_list)#
#	print myinput



