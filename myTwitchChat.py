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

class myTwitchChat:
    def __init__(self):
        self.myToken = 'oauth:'+TwitchToken
        self.myUsername = TwitchUsername

    # Launch a verbose (!) twitch stream
        with TwitchChatStream(username=self.myUsername,
                          oauth=self.myToken,
                          verbose=True) as chatstream:

  	    self.chat = chatstream
            self.sendMessage("I'm ready to explore!")

    def sendMessage(self,message):
        self.chat.send_chat_message(message)

    def getMessages(self):
        self.received = self.chat.twitch_receive_messages()
	return self.received

        # Continuously check if messages are received (every ~10s)
        # This is necessary, if not, the chat stream will close itself
        # after a couple of minutes (due to ping messages from twitch
