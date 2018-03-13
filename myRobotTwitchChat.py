import myTwitchChat
import Tiny4WD
import operator
import time

myRobot = Tiny4WD.Tiny4WD()
myTwitch = myTwitchChat.myTwitchChat()


def mainLoop():
    while True:
	command = getOftenCommand()
	print("Perform Command: "+str(command))
	performCommand(command)
	myTwitch.sendMessage("Action: Performing: "+command)
	time.sleep(15)


def performCommand(command):
    print("Perform Command: "+str(command))
    if command == "F":
        myRobot.forward()
    if command == "B":
        myRobot.backward()
    if command == "L":
        myRobot.left()
    if command == "R":
        myRobot.right()
    if command == "S":
        myRobot.stop()

allowedCommands = {"Forward":"F","F":"F",
		   "Backward":"B","B":"B",
		   "L":"L",
		   "R":"R",
		   "S":"S"}

def getOftenCommand():
    messages = myTwitch.getMessages()
    commands = {'F':0,'B':0,'L':0,'R':0,'S':0}
    for message in messages:
        command = getCommandInMessage(message)
        if command:
            commands[command] = commands[command]+1
    
    oftenEntry = getOftenEntry(commands)
    return oftenEntry
    
def getOftenEntry(commands):
    return max(commands.iteritems(), key=operator.itemgetter(1))[0]

def getCommandInMessage(dictMessage):
    username = dictMessage['username']
    content = dictMessage['message']
    #print(username+': '+content)
    if content in allowedCommands:
        return allowedCommands[content]
    

