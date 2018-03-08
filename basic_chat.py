#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This is a small example which connects to a user's chat channel to
send and receive the messages posted there
"""
from __future__ import print_function
from credentials import *
from twitchstream.outputvideo import TwitchOutputStreamRepeater
from twitchstream.chat import TwitchChatStream
import argparse
import time
import numpy as np

import myScrollPhatHD
display = myScrollPhatHD.MyScrollPhat()


def check_if_cmd(dictMessage):
    #received: [{'username': u'jack5496', 'message': u'Hallo', 'channel': u'#jack5496'}]
    username = dictMessage['username']
    message = dictMessage['message']
    print(username+': '+message)
    
    print('Command: '+message)
    if message == 'reset':
        display.reset_grid()
        print('resetted')
    else:
	print('Light it up')
        splits = message.split()
        state = float(splits[0])
        x = int(splits[1])
        y = int(splits[2])
        print('intense: '+str(state)+' at: '+str(x)+' '+str(y))
        display.update_pos(state,x,y)
        display.show_grid()
        chatstream.send_chat_message("Okay!")
        
    

if __name__ == "__main__":
    myToken = 'oauth:'+TwitchToken
    myUsername = TwitchUsername

    # Launch a verbose (!) twitch stream
    with TwitchChatStream(username=myUsername,
                          oauth=myToken,
                          verbose=True) as chatstream:

        # Send a message to this twitch stream
        chatstream.send_chat_message("I'm reading this!")

        # Continuously check if messages are received (every ~10s)
        # This is necessary, if not, the chat stream will close itself
        # after a couple of minutes (due to ping messages from twitch)
        while True:
            received = chatstream.twitch_receive_messages()
            if received:
                #print("received:", received)
		for dictMessage in received:
			check_if_cmd(dictMessage)
            time.sleep(1)
