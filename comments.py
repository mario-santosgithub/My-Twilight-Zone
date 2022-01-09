# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:42:36 2021

@author: Madalena Custódio - 63128, Mariana Pereira - 62968, Rafaela Reis - 63040
"""

class Comment:
    def __init__(self, user, stance, message):
        self.user = user
        self.stance = stance
        self.message = message

    def getUser(self):
        return self.user

    def getStance(self):
        return self.stance

    def getMessage(self):
        return self.message